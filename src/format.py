import argparse
import AssignmentFormat.config as config
from AssignmentFormat.assignmentManager import AssignmentManager

def main():
    parser = argparse.ArgumentParser(description="Arguemtns for formating assignments")
    parser.add_argument("-z", "--zipFile", action="store", dest="submissionZipFile")
    parser.add_argument("-r", "--rubric", action="store", dest="rubricFile")
    results = parser.parse_args()

    if not results.submissionZipFile:
        print ("The submission zip file was not given")
        exit(1)
    if not results.rubricFile:
        print("A rubric needs to be given")
        exit(1)
    


    config.SUBMISSION_ZIP_LOCATION = results.submissionZipFile 
    config.RUBRIC_PATH = results.rubricFile
    ############# NEED TO CHANGE FOR EVERY ASSIGNMENT #########
    # GRADE_ATTEMPT_BEFORE_SUBMISSON
    # GRADE_LAST_ATTEMPT
    config.ATTEMPT_TYPE = config.GRADE_ATTEMPT_BEFORE_SUBMISSON
    config.DUE_DATE = "2014-05-03-23-59-59"
    ###########################################################

    assignmentManager = AssignmentManager()
    assignmentManager.format()

    
if __name__ == '__main__':
    main()
