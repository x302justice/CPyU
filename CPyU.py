import sys
import os
a = sys.platform
#the if else and elif goes here, not in some other file
if a == 'win32':
    print("architecture")
    os.system("echo %PROCESSOR_ARCHITECTURE%")
    print("CPU name:")
    os.system("echo %PROCESSOR_IDENTIFIER%")
    print("processor level:")
    os.system("echo %PROCESSOR_LEVEL%")
    os.system("pause>nul")
elif a == "linux":
    os.system("cat /proc/cpuinfo | grep 'vendor' | uniq")
    os.system("cat /proc/cpuinfo | grep 'model name' | uniq")
    print("number of cores:")
    os.system("cat /proc/cpuinfo | grep processor | wc -l")
    print("cores and ids:")
    os.system("cat /proc/cpuinfo | grep 'core id'")
else:
    print("sorry, no os by", sys.platform, "exists in creators brain, try again in a later version")