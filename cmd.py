# Author: Alberto Vázquez
# https://github.com/alb3rtov/
# https://informaticaenuno.wordpress.com/
# Version alpha-0.12.8

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
    sistemaOperativo = "Nombre del sistema operativo";
    osType1 = "Microsoft Windows Server 2016";
    osType2 = "Microsoft Windows Server 2012";
    osType3 = "Microsoft Windows Server 2019";

    cnt = 0

    os.system('systeminfo > systeminfo.txt');

    dirFile = 'systeminfo.txt'
    with open(dirFile, 'r') as reader:
      for line in reader:
         if (osName in line or sistemaOperativo in line):
            print(f'  {line}');
            if (osType1 in line or osType2 in line or osType3 in line):
               cnt = cnt+1;

    if (cnt == 1):
       FirstMenu();
    else:
       print("  Operating System must be Windows Server 2012, 2016 or 2019");
       bfunc.PressKey();
       sys.exit();

######################################################################################
##############################   MENU OPTIONS CHECK   ################################
######################################################################################

#Function for 6 options Menus


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
        bfunc.PressKey();


#2- Active Directory check
def CheckAD2():
    print();
    print("  [*] Wait while it checks Active Directory  ",end="");
    bfunc.LoadAnimation();
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
        bfunc.PressKey();


#3- Active Directory check
def CheckAD3():
    print();
    print("  [*] Wait while it checks Active Directory  ",end="");
    bfunc.LoadAnimation();
    print();
    
    p = subprocess.Popen(["powershell.exe", "-ExecutionPolicy", "Bypass", ".\\scripts\\adcheck.ps1"], stdout=subprocess.PIPE, stderr= subprocess.PIPE)

    for line in p.stdout:
        decoded_output = line.decode('utf-8', errors='strict').strip()

    if (decoded_output == "False"):
        print();
        print(" The Active Directory service is NOT installed");
        bfunc.PressKey();
    else:
        print();
        print(" The Active Directory service is ALREADY installed");
        bfunc.PressKey();






#4 administrar ad
def ManageAD():
    print();
    print("  [*] Wait while it checks Active Directory  ",end="");
    bfunc.LoadAnimation();
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

def Banner():

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
	print("[-*-]     Suitable OS: Windows Server 2012, 2016 & 2019 (All versions)    [-*-]");
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


if (len(sys.argv) == 1) :

	Banner();
	CheckingOS();



if (len(sys.argv) == 2) :

	if (sys.argv[1] == "/version" or sys.argv[1] == "-v") :

		print();
		print("ICAAD Software version alpha 0.12.8");
		print();
		print("You are executing the CMD version of ICAAD software.");
		print("Use /gui to execute the GUI version");
		print();

	elif (sys.argv[1] == "/help" or sys.argv[1] == "-h") :

		print();
		print("ICAAD Software version alpha 0.12.8");
		print("You can visit the project here --> www.github.com/alb3rtov/icaad-software");
		print("Also you can visit my wordpress to see more stuff --> www.informaticaenuno.wordpress.com");
		print();
		print("This software is licensed under the GNU General Public License v3.0");
		print();
		print("    cmd.py	Start the program");
		print();
		print("Parameters list:");
		print();
		print("    /version	Shows the current version of the software");
		print("    /help	Shows a complete help for users");
		print("    /gui 	Executes the GUI version of ICAAD");
		print("    /os  	Shows the suitable Operating Systems");
		print();

	elif (sys.argv[1] == "/gui" or sys.argv[1] == "-g") :

		os.system("gui.py");

	elif (sys.argv[1] == "/os" or sys.argv[1] == "-o") :

		print();
		print("Suitable Operating Systems");
		print();
		print("    - Windows Server 2012 R2");
		print("    - Windows Server 2016");
		print("    - Windows Server 2019");
		print();
		print("For Windows Server 2012 R2 you need to have installed the next Service Packs:");
		print();
		print("    - KB2919442 ->");
		print("    - KB2919335 ->");
		print();


	else:

		print();
		print("ICAAD Software version alpha 0.12.8");
		print("This software is licensed under the GNU General Public License v3.0");
		print();
		print("ERROR: Not valid syntax");
		print("Error with" , sys.argv[1]);
		print();
		print("Use the parameter /help to see all the options");
		print();

