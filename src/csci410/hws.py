import os
import subprocess
import shutil
import sys

pathToHardwareSimulator = "C:/School/Nand2Tetris/JackCompiler.bat"

# pathTo10 = "C:/School/Nand2Tetris/projects/11/grade"

# functionsToTest = ["grade/Average",
#                     "grade/ComplexArrays",
#                     "grade/ConvertToBin",
#                     "grade/Pong",
#                     "grade/Seven",
#                     "grade/Square"]

cwd = os.getcwd()
cwd = cwd.split("/cygdrive/c/")[1] #cygwin uses cygdrive and hws uses C:/
cwd = "C:/" + cwd

# if not os.path.isdir(cwd + "/grade"):
#     shutil.copytree(pathTo10, cwd + "/grade")

# if os.path.isfile( os.getcwd() + "/grade/FibonacciElement.asm"):
#     shutil.copy(os.getcwd() + "/grade/FibonacciElement.asm", cwd + "/grade/FibonacciElement/")
# if os.path.isfile( os.getcwd() + "/grade/SimpleFunction.asm"):
#     shutil.copy(os.getcwd() + "/grade/SimpleFunction.asm", cwd + "/grade/SimpleFunction/")
# if os.path.isfile( os.getcwd() + "/grade/StaticsTest.asm"):
#     shutil.copy(os.getcwd() + "/grade/StaticsTest.asm", cwd + "/grade/StaticsTest/")

if not len(sys.argv) == 2:
    print("no input")
    exit(1) 


# for test in functionsToTest:
#     print ("----- Testing " + test + " ------ ")
command = pathToHardwareSimulator + " " + cwd + "/" + sys.argv[1]
print (command)
result = subprocess.Popen(command , shell=True,stdout=subprocess.PIPE)


# #    result = str(result.communicate()[0])
   # if "Comparison ended successfully" in result:
#         print ("    " + "Passed")
#     else:
#         print ("    " + "Failed")
#         print (result)
#     print ("----------------------------------------------")
#     print("")
#     print("")

# """
# # enter grades in the rubric
# # rubric needs to be one folder back
# pathToGrade = "../../grade.txt"

# if not os.path.isfile(pathToGrade):
#     print ("rubric was not found in " + cwd)
# else:
#     contents = ""
#     once = True
#     with open(pathToGrade) as f:
#         contents = f.readline()
#         contents += "\r\n"
#         for function in sorted(functionsToTest.items()):
#             contents += "[" + str(functionsToTest[function[0]][0]) + "/" + str(functionsToTest[function[0]][1]) + "]" + " " + function[0] + "\r\n"
#         end = False
#         for line in f:
#             if "==" in line:
#                 end = True
#                 if once:
#                     contents += "\r\n"
#                     once = False
#             if end == True:
#                 contents += line
#     f = open(pathToGrade, "w")
#     f.write(contents)
#     f.close()
#     #print(os.listdir("C:/School/GradingFramework" ))
#     os.system("python3 C:/School/GradingFramework/GradingFramework/src/evulateGrade.py " +  pathToGrade)
# """