# Author: Alberto Vázquez
# https://github.com/alb3rtov/
# https://informaticaenuno.wordpress.com/
# Version alfa-0.12.8

##############################
###    PACKAGES IMPORTED   ###
##############################

import subprocess
import time
import os, sys
import os.path as path
import signal
import re
from menus.management import bfunc


#####################
###   FUNCTIONS   ###
#####################


#Function to avoid Ctrl+C
def sigint_handler(signum, frame):
    print();
    print("Please, don't press Ctrl+C");
    print();
    time.sleep(1);

signal.signal(signal.SIGINT, sigint_handler)

#Exit program Function
def ExitProgram():
    print("");
    optionExit = input("Are you sure you want to exit? (y/n): ");
    if (optionExit == "y") or (optionExit == "Y"):
        sys.exit();
    elif (optionExit == "n") or (optionExit == "N"):
        time.sleep(2)
        bfunc.PressKey();();
    else:
        print("");
        print(" Use a right option (y/n)")
        ExitProgram();


#Operating System check Function
def CheckingOS():
    osName = "OS Name";
    osType1 = "Microsoft Windows Server 2016";
    osType2 = "Microsoft Windows Server 2012";
    cnt = 0

    os.system('systeminfo > systeminfo.txt');

    dirFile = 'systeminfo.txt'
    with open(dirFile, 'r') as reader:
      for line in reader:
         if (osName in line):
            print(f'  {line}');
            if (osType1 in line or osType2 in line):
               cnt = cnt+1;

    if (cnt == 1):
       FirstMenu();
    else:
       print("  Operting System must be Windows Server 2012/2016");
       time.sleep(3);
       sys.exit();

######################################################################################
##############################   MENU OPTIONS CHECK   ################################
######################################################################################

#Function for 6 options Menus
#def ChooseOption6():


############################# First Menu Options ##############################

#1- Active Directory check
def CheckAD1():
    print();
    print("  [*] Wait while it checks Active Directory  ",end="");
    bfunc.LoadAnimation();();
    print();
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\cup\\adcheck.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();

    lines = len(open('.\\scripts\\cup\\temp\\adcheck.txt').readlines());

    p = subprocess.Popen(["powershell.exe", "del .\\scripts\\cup\\temp\\adcheck.txt"],stdout=sys.stdout);

    #print(lines);

    if (lines != 0):
       os.system(f'type nul > menus\\security.txt')
       os.system('menus\\adconfig.py');
    else:
        print();
        print(" The Active Directory service is NOT installed");
        bfunc.PressKey();();


#2- Active Directory check
def CheckAD2():
    print();
    print("  [*] Wait while it checks Active Directory  ",end="");
    bfunc.LoadAnimation();();
    print();
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\cup\\adcheck.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();

    lines = len(open('.\\scripts\\cup\\temp\\adcheck.txt').readlines());

    p = subprocess.Popen(["powershell.exe", "del .\\scripts\\cup\\temp\\adcheck.txt"],stdout=sys.stdout);
    #print(lines);

    if (lines == 0):
       os.system(f'type nul > menus\\security.txt')
       os.system('menus\\adinstall.py');
    else:
        print();
        print(" The Active Directory service is ALREADY installed");
        bfunc.PressKey();();


#3- Active Directory check
def CheckAD3():
    print();
    print("  [*] Wait while it checks Active Directory  ",end="");
    bfunc.LoadAnimation();();
    print();
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\cup\\adcheck.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();

    lines = len(open('.\\scripts\\cup\\temp\\adcheck.txt').readlines());

    p1 = subprocess.Popen(["powershell.exe", "del .\\scripts\\comp\\temp\\adcheck.txt"],stdout=sys.stdout);

    #print(lines);


    if (lines != 0):
        print();
        print(" The Active Directory service is ALREADY installed");
        bfunc.PressKey();();
    else:
        print();
        print(" The Active Directory service is NOT installed");
        bfunc.PressKey();();





#4 administrar ad
def ManageAD():
    print();
    print("  [*] Wait while it checks Active Directory  ",end="");
    bfunc.LoadAnimation();();
    print();
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\cup\\adcheck.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();

    lines = len(open('.\\scripts\\cup\\temp\\adcheck.txt').readlines());

    p = subprocess.Popen(["powershell.exe", "del .\\scripts\\cup\\temp\\adcheck.txt"],stdout=sys.stdout);
    #print(lines);

    if (lines == 0):
        print();
        print(" The Active Directory service is NOT installed");
        bfunc.PressKey();();
    else:
        print();
        print("  [*] Checking if your system is a Domain Controller  ",end="");
        bfunc.LoadAnimation();();
        print();

        p = subprocess.Popen(["powershell.exe", ".\\scripts\\cup\\dccheck.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
        p.communicate();

        lines2 = len(open('.\\scripts\\cup\\temp\\checkdcdiag.txt').readlines());

        p1 = subprocess.Popen(["powershell.exe", "del .\\scripts\\cup\\temp\\checkdcdiag.txt"],stdout=sys.stdout);
        p2 = subprocess.Popen(["powershell.exe", "del .\\scripts\\cup\\temp\\dcdiag.txt"],stdout=sys.stdout);
        #print (lines2);

        if (lines2 != 0):
            print();
            print(" This Server is NOT a Domain Controller");
            bfunc.PressKey();();
        else:
            os.system(f'type nul > menus\\security.txt')
            os.system('menus\\admanage.py')



#Configuration of DNS
def ConfigureDNS():
    print();
    print("  [*] Wait while it checks Active Directory  ",end="");
    bfunc.LoadAnimation();();
    print();
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\cup\\adcheck.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();

    lines = len(open('.\\scripts\\cup\\temp\\adcheck.txt').readlines());

    p = subprocess.Popen(["powershell.exe", "del .\\scripts\\cup\\temp\\adcheck.txt"],stdout=sys.stdout);
    #print(lines);

    if (lines == 0):
        print();
        print(" The Active Directory service is NOT installed");
        bfunc.PressKey();();
    else:
        print();
        print("  [*] Checking if your system is a Domain Controller  ",end="");
        bfunc.LoadAnimation();();
        print();

        p = subprocess.Popen(["powershell.exe", ".\\scripts\\cup\\dccheck.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
        p.communicate();

        lines2 = len(open('.\\scripts\\cup\\temp\\checkdcdiag.txt').readlines());

        p1 = subprocess.Popen(["powershell.exe", "del .\\scripts\\cup\\temp\\checkdcdiag.txt"],stdout=sys.stdout);
        p2 = subprocess.Popen(["powershell.exe", "del .\\scripts\\cup\\temp\\dcdiag.txt"],stdout=sys.stdout);

        #print (lines2);

        if (lines2 != 0):
            print();
            print(" Your system MUST be Domain Controller to configure DNS");
            bfunc.PressKey();();
        else:
            os.system(f'type nul > menus\\security.txt')
            os.system('menus\\dnsconfig.exe')


#6.- Exit to the program


############################################################################
##############################   MENUS   ###################################
############################################################################


#First menu, checking of Active Directory
def FirstMenu():
    while True:
      print ("");
      print ("==================== Main menu ICAAD Software ====================");
      print ("");
      print ("     1 ->    Active Directory Configuration           ");
      print ("     2 ->    Active Directory Installation            ");
      print ("     3 ->    Check installation of Active Directory   ");
      print ("     4 ->    Active Directory Management              ");
      print ("     5 ->    DNS Configuration                          ");
      print ("     6 ->    Exit                                      ");
      print ("");
      numOptions = 6;
      option = bfunc.ChooseOption(numOptions);
      if (option == 1):
         CheckAD1();
      elif (option == 2):
         CheckAD2();
      elif (option == 3):
         CheckAD3();
      elif (option == 4):
         ManageAD();
      elif (option == 5):
         ConfigureDNS();
      elif (option == 6):
         ExitProgram();
      else:
         break;



####################
###    START     ###
####################

# BANNER

#print();
#print("  ___       __   ________  ________  ________  ________  ________ _________   ");
#time.sleep(0.5);
#print(" |\  \     |\  \|\   __  \|\   ___ \|\   ____\|\   __  \|\  _____\\\___  ___\ ");
#time.sleep(0.5);
#print(" \ \  \    \ \  \ \  \|\  \ \  \_|\ \ \  \___|\ \  \|\  \ \  \__/\|___\  \_| ");
#time.sleep(0.5);
#print("  \ \  \  __\ \  \ \   __  \ \  \  \\ \ \_____  \ \  \\ \  \ \   __\   \ \  \  ");
#time.sleep(0.5);
#print("   \ \  \|\__\_\  \ \  \ \  \ \  \_ \\ \|____|\  \ \  \\ \  \ \  \_|    \ \  \ ");
#time.sleep(0.5);
#print("    \ \____________\ \__\ \__\ \_______\____\_\  \ \_______\ \__\      \ \__\ ");
#time.sleep(0.5);
#print("     \|____________|\|__|\|__|\|_______|\_________\|_______|\|__|       \|__| ");
#time.sleep(0.5);
#print("                                       \|_________|By Alberto Vázquez Martínez");
#print();

#print();
#print("                       _      _____   ___           _____");
#time.sleep(0.5);
#print("                      | | /| / / _ | / _ \___ ___  / _/ /_");
#time.sleep(0.5);
#print("                      | |/ |/ / __ |/ // (_-</ _ \/ _/ __/");
#time.sleep(0.5);
#print("                      |__/|__/_/ |_/____/___/\___/_/ \__/ ");
#time.sleep(0.5);
#print();
#print("                      Creado por Alberto Vázquez Martínez");


print();
print("          ____________   ___   ___    ____     _____     ");
time.sleep(0.5);
print("         /  _/ ___/ _ | / _ | / _ \  / __/__  / _/ /__    _____  _______ ");
time.sleep(0.5);
print("        _/ // /__/ __ |/ __ |/ // / _\ \/ _ \/ _/ __/ |/|/ / _ `/ __/ -_)");
time.sleep(0.5);
print("       /___/\___/_/ |_/_/ |_/____/ /___/\___/_/ \__/|__,__/\_,_/_/  \__/");
print();
print("                              By Alberto Vázquez");

#PROGRAM INFO
print();
print("[-*-]                      Welcome to ICAAD Software                      [-*-]");
print("[-*-]     Assitant of installation, configuration and management of AD    [-*-]")
print("[-*-]        Suitable OS: Windows Server 2012 y 2016 (All versions)       [-*-]");
print("[-*-]               Developed in Python 3.6 and Powershell 5              [-*-]");
print("[-*-]                         Version alpha-0.12.8                        [-*-]");

# LOAD
print();
print("  [*] Wait while the program loads  ",end="");
bfunc.LoadAnimation();();
print();
print();
print("  [*] Detecting your system components  ",end="");
bfunc.LoadAnimation();();
print();
print();

# Program Start
CheckingOS();
