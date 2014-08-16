### This is for simple scripts that need to run for every student ###

import subprocess, sys

if subprocess.check_output(["python3 " + sys.argv[1] + " ./BasicLoop/BasicLoop.vm"], shell=True):
    subprocess.Popen("python " + sys.argv[1] + " ./BasicLoop/BasicLoop.vm", shell = True)

if subprocess.check_output(["python3 " + sys.argv[1] + " ./FibonacciSeries/FibonacciSeries.vm"], shell=True):
    subprocess.Popen("python " + sys.argv[1] + " ./FibonacciSeries/FibonacciSeries.vm", shell = True)

