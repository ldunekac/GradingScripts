GradingFramework
================
Note: This grading frame work still needs some improvements to it. 

This framework consists of three major scripts:
1: format.py
2: evulateGrade.py
3: nextToGrade.py
4: generateSubmissionFile.py


format.py:
With the  downloaded zip file from blackboard and a rubric, this script creats a workspace that organizes all the students into their own directory. Each student directory is names with ther username. In each student directory consists of their personal rubric file, and a folder named Assignment with all of their submitted files. 

To run the format.py script you need to first open format.py file. In that file you will find the line "NEED TO CHANGE FOR EVERY ASSIGNMENT". Here you will need to enter the due date of the assignment and the attempt type. There are two different attemp types.

1: grade attempt before submission:
	This will take all of the students submission and grade the last assignment before the due date. Otherwise the student will get a zero on the assignment. 
2: grede last attempt:
	This  will take the students last submission and apply a late penility per day the assignemnt is late. 

Note: when downloading files form blackboard you need to get all the students submissions.

If you want you can take thoes lines out and hard code the config file found in the AssignmentFormat directory. My goal was to have a config file for each class I was grading but I never got around to it. 

evulateGrade.py:
This script needs to be ran in the student directory with the grad.txt file. The grade.text file is the rubric file that is formated for that student. It will add up all the students points and make a "Total:" line for their total score. Then if you have any notes for the student put them belwo the notes line. Never touch the notes line. That needs to be just like that so I can parse the file later.

nextToGrade.py:
	This script needs to be ran in the assignment workspace. It goes into each student directory and checks to see if they have recevied a final score. It wil print out the first student that has not been graded.

generateSubmissionFile.py:
	This takes the csv file for the assignment that is downloaded from blackboard and fills in all the students grades and comments and will output the file "upload.csv". This file can be given to blackboad and all the studets and comments will be submitted. 
	WARNING: This will overwrite all information with that assignemnt. So if you modified a students grade inside of blackboard, DON'T resubmit the upload.txt file. 

	The rest of the .py files in the src directory are just some scripts to help me grade different assignemtns feel free to change them.