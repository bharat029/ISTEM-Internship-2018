# modules to be used
import string

# reading data from the actual database
entireData = []
fp = open("finalDataSet_2.txt", "r")
line = fp.readline()
while(line) :
	line = line.rstrip("\n")
	entireData.append(line)
	line = fp.readline()
fp.close()

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
		testing = []
		innerList = sentences[j].split(",")
		temp = list(set(outerList).intersection(innerList))
		lengthOfIntersection = len(temp)
		lengthOfUnion = len(list(set().union(outerList,innerList)))
		result = float (lengthOfIntersection)/lengthOfUnion
		result = float("{0:.3f}".format(result))
		scoreMatrix[i][j] = result
		scoreMatrix[j][i] = result
		index = str(i) +" " +  str(j)
		testing.append(temp)
		testing.append(entireData[i])
		testing.append(entireData[j])
		commonPhrases[index] = testing

# writing the results to a file
fp = open("resultOfAnalysis.txt", "w")
for c in commonPhrases:
	if(len(commonPhrases[c][0]) != 1):
		fp.write(str(c) + "\n")
		fp.write(str(commonPhrases[c][0]) + "\n")
		fp.write(str(commonPhrases[c][1]) + "\n")
		fp.write(str(commonPhrases[c][2]) + "\n")
		fp.write("\n")
fp.close()
# end of file 