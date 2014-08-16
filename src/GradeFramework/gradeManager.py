import csv
import GradeFramework.csvIndexes as csvIndexes
from GradeFramework.student import Student
import os, re

class GradeManager:

    def __init__(self, inputCSVFile):
        self.csvFile = inputCSVFile 
        self.studentList = []       

    def makeCSVFile(self):
        """Calls all the functions in order to make the csv file"""
        reader = csv.reader(open(self.csvFile, "r"), delimiter=",")
        first = True
        for row in reader:
            if first:
                self.header = row
                first = False
            else:
                self.makeStudent(row)
        self.header[0] = self.header[0][2:-1]
        self.getGradeInformation()
        self.makeCSV()

    def makeStudent(self, row):
        """Makes a list of students based on each line of the csv file
        """
        self.studentList.append(Student(row))

    def getGradeInformation(self):
        """calls the student class to get the grading information"""
        directories = [f for f in os.listdir(".") if os.path.isdir(f)]

        for directory in directories:
            score = self.getScore(directory)
            comment = self.getComment(directory)
            student = self.getStudent(directory)
            student.addScore(score)
            student.addComment(comment)

        for student in self.studentList:
            student.addZero()

    def makeString(self):
        """makes the stirng needed to upload the students information"""
        string = ""
        for h in self.header:
            string += '"' + h + '"' + ","
        string = string[:-1]
        return string

    def makeCSV(self):
        """Makes the csv needed to upload the assignment to blackboard"""
        with open("upload.csv", "w") as f:
            f.write(self.makeString() + "\n" )
            for student in self.studentList:
                f.write(student.makeString() + "\n")

    def getScore(self, directory):
        """gets the students grade"""
        totalRegex = r"Total:.*\[(.*)/(.*)\].*"
        with open(os.path.join(directory, "grade.txt")) as f:
            for line in f:
                if re.match(totalRegex, line):
                    return re.match(totalRegex, line).group(1)

    def getComment(self, directory):
        commentline = "----- Comments -----"
        atCommentLine = False
        returnString = ""
        with open(os.path.join(directory, "grade.txt")) as f:
            for line in f:
                if atCommentLine:
                    returnString += line.strip() + "\n"
                if commentline in line.strip():
                    atCommentLine = True
        return returnString.strip()

    def getStudent(self, directory):
        for student in self.studentList:
            if student.isStudentID(directory):
                return student

