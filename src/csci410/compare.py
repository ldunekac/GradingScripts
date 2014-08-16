import subprocess
import sys
import re



def ignoreHeader(lines):
    i = 0
    while not '-' in text[i]:
        i += 1
    return i

def ingnoreSpace(index, lines):
    while lines[index].strip() == "":
        index += 1
    return index


def checkUserID(line, python=False):
    if python:
        return "# USERID:......... " in line
    else:
        return"// USERID:........ " in line

def checkProgrammer(line, python=False):
    if python:
        return "# PROGRAMMER:..... " in line
    else:
        return  "// PROGRAMMER:.... " in line

def checkCourse(line, python=False):
    if python:
        return "# COURSE:......... " in line
    else:
        return "// COURSE:........ " in line 

def checkTerm(line, python=False):
    if python:
        return "# TERM:........... " in line 
    else:
        return "// TERM:.......... " in line 

def checkProject(line, python=False):
    if python:
        return "# PROJECT:........ " in line
    else:
        return "// PROJECT:....... " in line

def checkFileName(line, python=False):
    if python:
        return "# FILENAME:....... " in line
    else:
        return "// FILENAME:...... " in line

def checkPythonVersion(line):
    return "# PYTHON VERSION:. " in line

def checkProjectHeaderOrFooter(line, python=False):
    if python:
        if line.strip() == "#" + "="*60:
            return True
    else:
        if line.strip() == "//" + "="*60:
            return True
    return False

def checkNulls(index, lines, typ):
    if not len(lines[index].strip()) == 15:
        print ("---- above hack is not correct length")
    index += 1
    if not typ in lines[index].strip():
        print("DID not find " + typ)
    index += 1
    if not len(lines[index].strip()) == 15:
        print( "---- below hack is not correct length")
        print(lines[index])
    index += 1
    return index

def checkPrintHeaders(index, lines, typ):
    index = checkNulls(index, lines, typ)
    if not checkProjectHeaderOrFooter(lines[index].strip(), False):
        print ("header for " + typ + " is wrong")
    index += 1
    if not checkUserID(lines[index].strip(), False):
        print("Failed UserID for " + typ)
    index += 1
    if not checkProgrammer(lines[index].strip(), False):
        print("Failed Programmer for " + typ)
    index += 1
    if not checkCourse(lines[index].strip(), False):
        print("Failed course for " + typ)
    index += 1
    if not checkTerm(lines[index].strip(), False):
        print("Failed term for " + typ)
    index += 1
    if not checkProject(lines[index].strip(), False):
        print("Failed Project for " + typ)
    index += 1
    if not checkFileName(lines[index].strip(), False):
        print("Faield File Name")
    index += 1
    if not checkProjectHeaderOrFooter(lines[index].strip(), False):
        print("Failed filename for " + typ)
    index += 1
    return index


def checkPrintHeadersPY(index, lines, typ):
    index = checkNulls(index, lines, typ)
    if not checkProjectHeaderOrFooter(lines[index].strip(), True):
        print ("header for " + typ + " is wrong")
    index += 1
    if not checkUserID(lines[index].strip(), True):
        print("Failed UserID for " + typ)
    index += 1
    if not checkProgrammer(lines[index].strip(), True):
        print("Failed Programmer for " + typ)
    index += 1
    if not checkCourse(lines[index].strip(), True):
        print("Failed course for " + typ)
    index += 1
    if not checkTerm(lines[index].strip(), True):
        print("Failed term for " + typ)
    index += 1
    if not checkProject(lines[index].strip(), True):
        print("Failed Project for " + typ)
    index += 1
    if not checkFileName(lines[index].strip(), True):
        print("Faield File Name")
    index += 1
    if not checkPythonVersion(lines[index].strip()):
        print("Failed python version")
    index += 1
    if not checkProjectHeaderOrFooter(lines[index].strip(), True):
        print("Failed filename for " + typ)
    index += 1
    return index

result = subprocess.Popen("python3 " + sys.argv[1],  shell=True,stdout=subprocess.PIPE)
types = ["HACK", "XML", "HDL", "ASM", "VM", "JACK", "PY"]
result = result.communicate()[0]

text = ""
for r in result:
    text += chr(r)

text = text.split('\n')
index = ignoreHeader(text)
index = checkNulls(index, text, "HACK")
index = ingnoreSpace(index, text)
index = checkNulls(index, text, "XML")
index = ingnoreSpace(index, text)
index = checkPrintHeaders(index, text,"HDL")
index = ingnoreSpace(index, text)
index = checkPrintHeaders(index, text,"ASM")
index = ingnoreSpace(index, text)
index = checkPrintHeaders(index, text,"VM")
index = ingnoreSpace(index, text)
index = checkPrintHeaders(index, text,"JACK")
index = ingnoreSpace(index, text)
index = checkPrintHeadersPY(index, text, "PY")
