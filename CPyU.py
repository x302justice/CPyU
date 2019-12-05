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
    os.system("echo %PROCESSOR_LEVEL")
    os.system("pause>nul")
    print("h")
else:
    print("sorry, no os by", sys.playfirm, "exists in creators brain, try again in a later version")
