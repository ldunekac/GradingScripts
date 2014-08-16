import os
import re
import shutil
import zipfile
import time
import math
import AssignmentFormat.config as config

class Student:

    def __init__(self, studentID, dataFiles, pathToAssignmentDirectroy, studentTimeStamp):
        """ Initialize sutdent class"""
        self.studentID = studentID
        self.dataFiles = dataFiles
        self.assignmentDir = pathToAssignmentDirectroy
        self.timeStamp = studentTimeStamp
       

    def format(self):
        """ Calles all the functions that the student needs to 
            complete its setup 
        """
        self.makeStudentDirectory()
        self.insertDataFiles()
        self.unzipAssignmentDirectory(self.assignmentDir)
        self.insertGradingRubric()

    def makeStudentDirectory(self):
        """Make the directory for the student in the Assignmet directory
            and makes a directory called 'Assignment' for the assignments
            files
        """
        self.studentDir = os.path.join(self.assignmentDir, self.studentID)
        self.studentAssignmentDir = os.path.join(self.studentDir, 'Assignment')
        
        os.mkdir(self.studentDir)
        os.mkdir(self.studentAssignmentDir)



    def insertDataFiles(self):
        """Puts the assignment files in the Assignment directory
            and places all other files in the student directory.
            The files that are moved to the Assignment directory
            will be renamed to remove the prepended blackboard
            information
        """
        # get information text document
        informationRegex = ".*_\d\d\d\d-\d\d-\d\d-\d\d-\d\d-\d\d\.txt"
        informationFile = [f for f in self.dataFiles if re.match(informationRegex,f)][0]
        self.infoFile = informationFile
        self.dataFiles.remove(informationFile)
        shutil.copy(informationFile, self.studentDir)
        
        # get zip files
        zipRegex = ".*\.zip" 
        zipFiles = [f for f in self.dataFiles if re.match(zipRegex, f)]
        self.dataFiles = [f for f in self.dataFiles if f not in zipFiles] # remvoe zip files from list
        if(len(zipFiles) == 1):
            try:
                with zipfile.ZipFile(zipFiles[0]) as zf:
                    zf.extractall(self.studentAssignmentDir)
            except:
                print(self.studentID + " does not have a dot a real zip file")
        elif len(zipFiles) > 1: # multiple zip files each one needs its own directory
            print("MULTIPLE ZIP FILES OCCURED, IMPLEMENT TO CONTINUE")

        if len(self.dataFiles) > 0: # move the files into the assignments folder
            for dataFile in self.dataFiles:
                shutil.copy(dataFile, os.path.join(self.studentAssignmentDir, self.stripBlackboardFormat(dataFile)))


    def stripBlackboardFormat(slef, dataFile):
        blackboardRegex = "(.*)_(.*)_(.*)_(\d\d\d\d-\d\d-\d\d-\d\d-\d\d-\d\d)_(.*)"
        return re.match(blackboardRegex,dataFile).group(5)


    def unzipAssignmentDirectory(self, path):
        """Recursively unzips all ziped files in the students
            assignments directory.
        """
        zipRegex = ".*\.zip"
        zipFiles = [f for f in os.listdir(path) if re.match(zipRegex, f)]
        for zipFile in zipFiles:
            with zipfile.ZipFile(zipFiles) as zf:
                zf.extractall()
            shutil.remove(zipFile)

        directories = [f for f in os.listdir(path) if os.path.isdir(f)]
        for directory in directories:
            self.unzipAssignmentDirectory(os.path.join(path, directory))


    def insertGradingRubric(self):
        """Takes the template rubric adds in the students name found
            in the student text file and addes it to the top of the 
            rubirc. Then makes the footer of the rubric where the 
            late penility and total fields are.
        """
        gradeRubric = ""

        penility = self.calculateLatePenility()
        with open(self.infoFile) as f:
            gradeRubric = f.readline().split("Name: ")[1]
        with open(config.RUBRIC_PATH) as f:
            gradeRubric += f.read()

        gradeRubric += "\n"*2 + "="*20 + "\n"
        gradeRubric += "[{0}/0] Late\n".format(penility)
        gradeRubric += "="*20 + "\n"
        gradeRubric += "Total: \n"
        gradeRubric += "-"*5 + " Comments " + "-"*5 + "\n"
        if penility < 0:
            gradeRubric += "{0}: Late".format(str(penility))

        with open(os.path.join(self.studentDir, "grade.txt"), "w") as r:
            r.write(gradeRubric)

    def calculateLatePenility(self):
        """Calculates how many points need to be taken off for
            late submissions.
        """
        if config.ATTEMPT_TYPE == config.GRADE_ATTEMPT_BEFORE_SUBMISSON:
            if time.strptime(self.timeStamp, config.DATE_FORMAT) <= time.strptime(config.DUE_DATE, config.DATE_FORMAT):
                return 0
            else:
                return -1000
        elif config.ATTEMPT_TYPE == config.GRADE_LAST_ATTEMPT:
            daysLate = self.findDaysLate(self.timeStamp, config.DUE_DATE)
            return self.findPenalty(daysLate)


    def findDaysLate(self, summitDate, dueDate):
        summitDate = time.strptime(summitDate, config.DATE_FORMAT)
        dueDate = time.strptime(dueDate, config.DATE_FORMAT)
        daysLate = math.ceil((time.mktime(summitDate) - time.mktime(dueDate))/float(config.SECONDS_IN_DAY))
        return daysLate

    def findPenalty(self, daysLate):
        if daysLate <=0:
            return 0
        if daysLate > config.MAX_DAYS_LATE:
            return -1000
        else:
            return (-1) * daysLate * config.PENALTY_PER_DAY_LATE;

