# used for preprocessing after getting the key phrases for actual printing in txt file
# importing various modules
import string

# taking the data
fp = open("results2.txt", "r")
line = fp.read()
fp.close()
line = line.split("},")
length = len(line)
temp = []
for i in range (0,length) :
	sentence = line[i]
	initialIndex = sentence.index("{")
	finalIndex = sentence.index("]")
	subString = sentence[initialIndex + 1: finalIndex]
	subString = subString.split("[")
	newList = subString[1]
	temp.append(newList)

# writing the result to the file
fp = open("finalDataSet2_result.txt", "w")
length2 = len(temp)
for i in range (0,length2) :
	fp.write(temp[i]+ "\n")
fp.close()
# end of file