import sys
from GradeFramework.gradeManager import GradeManager

def main():
    """Assums that the directory you are in is the assignment directory"""
    if not len(sys.argv) == 2:
        print("Requires the csv file for this assignment")
        print(sys.argv)
        exit(0)

    gradeCSV = sys.argv[1]

    gradeManager = GradeManager(sys.argv[1])
    gradeManager.makeCSVFile()

if __name__ == '__main__':
    main()