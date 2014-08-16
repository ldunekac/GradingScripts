from AssignmentFormat.student import Student
import AssignmentFormat.config as config
import os
import shutil
import zipfile
import sys
import glob

class AssignmentManager:

    def __init__(self):
        """Initializeds the AssignmentManager class"""
        self.students = []

    def format(self):
        """ Calls the AssignmentManager functions in order"""
        self.makeTempDirectory()
        self.unZipFile()
        self.makeAssignmentDirectory()
        self.findAllStudents()
        self.getStudentAssignmetns()
        self.formatStudents()
        self.removeTempDirectory()

    def makeTempDirectory(self):
        """Makes a temp directory to hold the contents of the zip file"""
        self.tempDir = "AssignmentTemp"
        if(os.path.isdir(self.tempDir)):
            print("Need to delete AssignmentTemp to continue.")
            print("Delete AssignmentTemp (yes/no)?")
            if(sys.stdin.readline().strip() == "yes"):
                shutil.rmtree(self.tempDir)
            else:
                exit(1)
        os.mkdir(self.tempDir)


    def unZipFile(self):
        """Unzips the assignment zip file in the temp directory."""
        with zipfile.ZipFile(config.SUBMISSION_ZIP_LOCATION) as zf:
            zf.extractall(self.tempDir)


    def makeAssignmentDirectory(self):
        """Makes the assignment directory where all the student
            Assignments will be placed 
        """
        self.assignmentPath = config.SUBMISSION_ZIP_LOCATION.split('/')[-1].split('_')[2]
        os.mkdir(self.assignmentPath)

    def findAllStudents(self):
        """makes a list of all students found in the temp directory"""
        self.studentSet = set([f.split('_')[1] for f in os.listdir(self.tempDir)])

    def getStudentAssignmetns(self):
        """Finds all files needed for the student.These files include
            the zip/assignment files and the information file.
            Returns the files that will be graded.
        """
        for student in self.studentSet:
            (timeStamp, submissionFilesToGrade) = self.filterAssignmentsSubmissionType(glob.glob(self.tempDir+ "/*" + student + '*'))
            self.addStudent(student, submissionFilesToGrade, timeStamp)
            


    def filterAssignmentsSubmissionType(self, assignmentList):
        timeStamps = list(set([f.split('_')[3].split('.')[0] for f in assignmentList]))
        timeStamps = sorted(timeStamps)

        if config.ATTEMPT_TYPE == config.GRADE_LAST_ATTEMPT:
            return (timeStamps[-1], [f for f in assignmentList if timeStamps[-1] in f])
        elif config.ATTEMPT_TYPE == config.GRADE_ATTEMPT_BEFORE_SUBMISSON:
            timeStampBeforeSubmissionDate = timeStamps[0]
            for timeStamp in timeStamps:
                if timeStamp <= config.DUE_DATE:
                    timeStampBeforeSubmissionDate = timeStamp
                else:
                    break
            return (timeStamp, [f for f in assignmentList if timeStampBeforeSubmissionDate in f])
        else:
            print("ERROR the ATTEMPT_TYPE was not given")
            return None


    def addStudent(self, student, submissionFilesToGrade, timeStamp):
        """Adds a student to the list of student objects from the studentID,
            and the assignment files for that student
        """
        self.students.append(Student(student, submissionFilesToGrade,self.assignmentPath, timeStamp))


    def formatStudents(self):
        """Loops through all student objects and tells the students
            to setup their directory
        """
        for student in self.students:
            student.format()

    def removeTempDirectory(self):
        shutil.rmtree(self.tempDir)