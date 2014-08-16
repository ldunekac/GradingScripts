import GradeFramework.csvIndexes as csvIndexes

class Student:

    def __init__(self, row):
        self.studentInformation = row

    def makeString(self):
        """returns the csv string needed to upload the students information"""
        string = ""
        for info in self.studentInformation:
            string += '"' + info + '"' + ","
        return string[:-1]

    def isStudentID(self, directory):
        if self.studentInformation[2] == directory:
            return True

    def addScore(self, score):
        self.studentInformation[csvIndexes.SCORE] = str(score)

    def addComment(self, comment):
        self.studentInformation[csvIndexes.FEEDBACK_TO_USER] = comment

    def addZero(self):
        if self.studentInformation[csvIndexes.SCORE] == '':
            self.studentInformation[csvIndexes.SCORE] = "0.0"

