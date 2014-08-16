import sys, os, re

# finds all directories
dirs = [f for f in os.listdir('.') if os.path.isdir(f)]
end = False
total = "Total:"

for d in dirs:
    if end:
        break
    # go into next directory
    os.chdir(d)
    if os.path.isfile("grade.txt"):
        isMatch = False
        f = open("grade.txt", "r")
        # check to see if the total has a number next to it
        for line in f:
            match = re.match(r"Total: \[.*/.*\]", line)
            if match:
                isMatch = True
        f.close()
        # if total does not have a number end
        if not isMatch:
            print (d)
            end = True
    os.chdir("..")

if not end:
    print ("Finished")