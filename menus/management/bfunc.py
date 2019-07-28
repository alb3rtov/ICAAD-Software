# Author: Alberto Vázquez
# https://github.com/alb3rtov/
# https://informaticaenuno.wordpress.com/
# Version alfa-0.12.8
# BASIC FUNTIONS OF ICAAD (use in all the .py scripts)


##############################
###    PACKAGES IMPORTED   ###
##############################

import subprocess
import time
import os, sys
import os.path as path
import signal
import re


###########################
###   BASIC FUNCTIONS   ###
###########################

#Charge animation Function (3.2s)
def LoadAnimation():
        y = 0;
        while y < 1:
                blah="\|/-\|/- "
                for l in blah:
                        sys.stdout.write(l)
                        sys.stdout.flush()
                        sys.stdout.write('\b')
                        time.sleep(0.2)
                        y = y + 1;


#Waiting function
def PressKey():
    print();
    key = input("Press ENTER to continue");


#System restart Function
def RestartComputer():
    print();
    optionRestart = input("Do you want to restart NOW? (y/n): ");
    if (optionRestart == "y") or (optionRestart == "Y"):
        p = subprocess.Popen(["powershell.exe", "Restart-Computer"],stdout=sys.stdout);
        p.communicate();
    else:
        PressKey();


###############################
## FUNTION OF MENU SELECTION ##
###############################

# The variable numOptions contains the number of options that the menu contains.
def ChooseOption(numOptions):
    correct = False;

    while (not correct):
       try:
            num = int(input("Choose a option: "));
            if (num < 1) or (num > numOptions):
                print("Error, not valid option");
            else:
                correct = True;

       except ValueError:
         time.sleep(1)
         print("Error, option must be a numerical value");
       except EOFError:
         time.sleep(1);
         print("If you want to exit the program choose the right option");
         print(" ");

    return num;


# THIS FUNCTIONS ARE USE IN THE SCRIPTS adinstall.py and adconfig.py

def PromoteDC():
    print();
    print("  [*] Checking if your system is Domain Controller  ",end="");
    LoadAnimation();
    print();

    p = subprocess.Popen(["powershell.exe", ".\\scripts\\cup\\dccheck.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();

    lines= len(open('.\\scripts\\cup\\temp\\checkdcdiag.txt').readlines());

    p1 = subprocess.Popen(["powershell.exe", "del .\\scripts\\cup\\temp\\checkdcdiag.txt"],stdout=sys.stdout);
    p1 = subprocess.Popen(["powershell.exe", "del .\\scripts\\cup\\temp\\dcdiag.txt"],stdout=sys.stdout);

    #print (lineas2);

    if (lines != 0):
        p = subprocess.Popen(["powershell.exe", ".\\scripts\\ad\\promote.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
        p.communicate();

        RestartComputer();
    else:
        print();
        print(" Your system is ALREADY Domain Controller");
        PressKey();

#Second Option, check DC
def CheckDC():
    print();
    print("  [*] Checking if your system is Domain Controller  ",end="");
    LoadAnimation();
    print();

    p = subprocess.Popen(["powershell.exe", ".\\scripts\\cup\\dccheck.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();

    lines = len(open('.\\scripts\\cup\\temp\\checkdcdiag.txt').readlines());

    p1 = subprocess.Popen(["powershell.exe", "del .\\scripts\\cup\\temp\\checkdcdiag.txt"],stdout=sys.stdout);
    p2 = subprocess.Popen(["powershell.exe", "del .\\scripts\\cup\\temp\\dcdiag.txt"],stdout=sys.stdout);

    #print (lineas2);

    if (lines != 0):
        print();
        print(" Your system is NOT Domain Controller, use option 1 to promote your system in a Domain Controller");
        PressKey();
    else:
        print();
        print(" Your system is ALREADY Domain Controller");
        PressKey();

#Third Option, delete ACTIVE DIRECTORY SERVICE
def DeleteAD():
    print();
    i = input(" Are you sure you want to delete the Active Directory Domain Services? (y/n): ");

    if (i == "y") or (i == "Y"):
        p = subprocess.Popen(["powershell.exe", "Remove-WindowsFeature -name AD-Domain-Services"],stdout=sys.stdout);
        p.communicate();
        RestartComputer(); #RESTART COMPUTER FOR SAVE SETTINGS AND CONFIGURATION
    else:
        PressKey();
