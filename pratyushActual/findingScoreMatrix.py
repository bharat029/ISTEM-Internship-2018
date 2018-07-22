# modules to be used
import string

# reading data from the file
fp = open("KeyPhrasesOfDescriptions.txt", "r")
line = fp.readline()
sentences = []
while(line) :
	line = line.rstrip("\n")
	sentences.append(line)
	line = fp.readline()
fp.close()

# length of score matrix 
length = len(sentences)

# matrix containing the jacardian coefficient between any 2 sentences in the dataset 
scoreMatrix = []

# filling up of the initial scoreMatrix
for i in range(0, length) :
	scoreMatrix.append([])
	for j in range (0, length) :
		if(i==j) :
			scoreMatrix[i].append(1)
		else :
			scoreMatrix[i].append(0)

# dictionary to hold the common phrases between any two sentences
commonPhrases = {}

# processing the data for jecard coefficient and filling of the dictionary
for i in range (0, length) :
	outerList = sentences[i].split(",")
	for j in range (i+1, length) :
		innerList = sentences[j].split(",")
		temp = list(set(outerList).intersection(innerList))
		lengthOfIntersection = len(temp)
		lengthOfUnion = len(list(set().union(outerList,innerList)))
		result = float (lengthOfIntersection)/lengthOfUnion
		result = float("{0:.3f}".format(result))
		scoreMatrix[i][j] = result
		scoreMatrix[j][i] = result
		index = str(i) +" " +  str(j)
		commonPhrases[index] = temp

# writing the results to a file
fp = open("resultOfCoefficient.txt", "w")
fp.write("The coefficient matrix is:" + "\n")
fp.write(str(scoreMatrix) + "\n")
fp.write("The dictionary containing common sentences between any two sentences is:" + "\n")
fp.write(str(commonPhrases) + "\n")
fp.close()
# end of file 