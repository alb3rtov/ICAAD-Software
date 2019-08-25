# Author: Alberto Vázquez
# https://github.com/alb3rtov/
# https://informaticaenuno.wordpress.com/
# Version alfa-0.12.8
# CONFIGURATION MENU ACTIVE DIRECTORY


##############################
###    PACKAGES IMPORTED   ###
##############################

import time
import os, sys
import signal
import subprocess
import os.path as path
from management import bfunc
#import glob


#Function to avoid Ctrl+C
def sigint_handler(signum, frame):
    print();
    print("Please, don't press Ctrl+C");
    print();
    time.sleep(1);

signal.signal(signal.SIGINT, sigint_handler)


############################### Fourth Menu Options ######################################
# The first three options are stored in bfunc.py script


#Fourth Option, check FSMO Roles
def FSMORoles():
    print();
    print("  [*] Checking if your system is Domain Controller  ",end="");
    bfunc.LoadAnimation();
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
        bfunc.PressKey();
    else:
        print();
        os.system('netdom query fsmo');
        bfunc.PressKey();

#Fiveth Option, check Global Catalog
def GlobalCatalog():
    print();
    print("  [*] Checking if your system is Domain Controller  ",end="");
    bfunc.LoadAnimation();
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
        bfunc.PressKey();
    else:
        print();
        p = subprocess.Popen(["powershell.exe", "Get-ADDomainController | ft Name,IsGlobalCatalog"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
        p.communicate();
        bfunc.PressKey();



#cuarto menu
def FourthMenu():
    time.sleep(0.5)
    print("");
    print("  [*] Wait while it loads the menu  ",end="");
    bfunc.LoadAnimation();
    print();

    while True:
      print ("");
      print ("============= Menu of system check as Domain Controller =============");
      print ("");
      print ("     1 ->    Promote this server to Domain Controller         ");
      print ("     2 ->    Check if this server is a Domain Controller      ");
      print ("     3 ->    Delete the Active Directory Domain Service       ");
      print ("     4 ->    Check FSMO Roles                                 ");
      print ("     5 ->    Check Global Catalog                             ");
      print ("     6 ->    Back (previous menu)                             ");
      print ("");
      numOptions = 6;
      opcion = bfunc.ChooseOption(numOptions);
      if (opcion == 1):
         bfunc.PromoteDC();
      elif (opcion == 2):
         bfunc.CheckDC();
      elif (opcion == 3):
         bfunc.DeleteAD();
      elif (opcion == 4):
         FSMORoles();
      elif (opcion == 5):
         GlobalCatalog();
      elif (opcion== 6):
         print();
         print("  [*] Wait while it loads the menu  ",end="");
         bfunc.LoadAnimation();
         print();
         sys.exit();
      else:
         break;


# This part of code of here is just a way of 'security' to avoid that the users
# execute the another scripts (.exe or .py) directly.
# This is because for a good working of this program, first, is necessary check
# Active Directory and Domain Controller parameters and this code is in the firsts scripts.

search = "security.txt"
directory = os.getcwd()
total = 0

if (len(sys.argv) > 1):
    if (not os.path.isdir(sys.argv[1])):
        #print(sys.argv[1]," no se reconoce como directorio")
        sys.exit(1)
    directory = sys.argv[1]

for root, dir, ficheros in os.walk(directory):
    for fichero in ficheros:
        if (search in fichero.lower()):
           #print(root+"\\"+fichero)
           total += 1

#print("En total hay", total, "archivos con", buscar)
if (total == 1):
   os.system('del menus\\security.txt');
   FourthMenu();
else:
   sys.exit();
