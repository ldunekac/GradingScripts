import os, sys, subprocess

orgionalDirectory = os.getcwd()

def preformAction(directoryPath, action):
    os.chdir(directoryPath)
    subprocess.Popen(action, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    os.chdir(orgionalDirectory)


def main():
    if(len(sys.argv) != 2):
        print("Not enough arguments")
        exit(1)
    action = sys.argv[1]

    directories = [os.path.join(orgionalDirectory,o) for o in os.listdir(orgionalDirectory) if os.path.isdir(os.path.join(orgionalDirectory,o))]
    directories = [os.path.join(d, "Assignment") for d in directories]

    for d in directories:
        preformAction(d, action)



if __name__ == '__main__':
    main()