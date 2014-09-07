# this will open the rubix file and sum up the total score and assign it
import re
import sys

regexString = r".*\[(.*?)/(.*?)\].*"
# finds the total number of points the rubric
# and wries the new total

pathToGrade = 'grade.txt'
comment = ''

if len(sys.argv) == 2:
    pathToGrade = sys.argv[1]

f = open(pathToGrade, 'r')
scoreTotal = 0
totalPoints = 0
for line in f:
    # don't add the total line 
    match = re.search(r"Total:.*", line)
    if match:
        break
    # add points
    match =  re.search(regexString, line)
    if match:
        scoreTotal += float(match.group(1))
        totalPoints += float(match.group(2))
        
        if float(match.group(1)) < float(match.group(2)):
            comment += line

if scoreTotal < 0:
    scoreTotal = 0

f.close()

# make the new file string
# replacing the total with the curent total
f = open(pathToGrade, 'r')
newFileString = ""
for line in f:
    match = re.search(r"Total:.*?", line)
    if match:
        newFileString += "Total: [" + str(scoreTotal) + "/" + str(totalPoints) + "]\r\n"
    else:
        newFileString += line
f.close()

f = open(pathToGrade, 'w')
f.write(newFileString)
f.write(comment)
f.close()

# print the total grade
print ("Score: " + str(scoreTotal) +  "/" + str(totalPoints)) 