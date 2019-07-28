# Author: Alberto Vázquez
# https://github.com/alb3rtov/
# https://informaticaenuno.wordpress.com/
# Version alfa-0.12.8
# Submenu of Organizational Unit (Administration)


##############################
###    PACKAGES IMPORTED   ###
##############################

import subprocess
import time
import os, sys
import os.path as path
import signal
import bfunc


#Function to avoid Ctrl+C
def sigint_handler(signum, frame):
    print();
    print("Please, don't press Ctrl+C");
    print();
    time.sleep(1);

signal.signal(signal.SIGINT, sigint_handler)


############################## Seventh Menu Options #################################
#First Option
def CreateOU():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\createOU.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\createOU.txt");
    bfunc.PressKey();

#Second Option
def ShowOU():
    p = subprocess.Popen(["powershell.exe", "Get-ADOrganizationalUnit -Filter 'Name -like \"*\"' | Format-Table Name,DistinguishedName,Country,City -A"],stdout=sys.stdout);
    time.sleep(2);
    bfunc.PressKey();


#Third Option
def SearchOU():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\searchOU.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\searchOU.txt");
    bfunc.PressKey();


#Fourth Option
def DeleteOU():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\deleteOU.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\deleteOU.txt");
    bfunc.PressKey();


#Fiveth Option
def ShowObjOU():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\showObjOU.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\showObjOU.txt");
    bfunc.PressKey();


#Sixth Option
def MoveObjOU():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\moveObjOU.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\moveObjOU.txt");
    bfunc.PressKey();

#Seventh Option
def MoveOU():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\moveOU.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\moveOU1.txt");
    os.system("del .\\scripts\\obj\\cmd\\temp\\moveOU2.txt");
    bfunc.PressKey();



################################ SEVENTH MENU MENU ###################################
def SeventhMenu():
    time.sleep(0.5)
    print("");
    print("  [*] Wait while it loads the menu  ",end="");
    bfunc.LoadAnimation();
    print("");
    os.system('cd..');

    while True:
      print ("");
      print ("====================== Organizational Unit Menu ======================");
      print ("");
      print ("     1 ->    Create Organizational Unit                        ");
      print ("     2 ->    Show all Organizational Units                     ");
      print ("     3 ->    Search Organizational Units                       ");
      print ("     4 ->    Delete Organizational Unit                        ");
      print ("     5 ->    Show objects inside of Organizational Units       ");
      print ("     6 ->    Move objects inside of Organizational Units       ");
      print ("     7 ->    Move Organizational Units inside of another ones  ");
      print ("     8 ->    Back (previous menu)                              ");
      print ("");
      numOptions = 8;
      option = bfunc.ChooseOption(numOptions); # eigth options
      if (option == 1):
         CreateOU();
      elif (option == 2):
         ShowOU();
      elif (option == 3):
         SearchOU();
      elif (option == 4):
         DeleteOU();
      elif (option == 5):
         ShowObjOU();
      elif (option == 6):
         MoveObjOU();
      elif (option == 7):
         MoveOU();
      elif (option == 8):
         print("");
         print("  [*] Wait while it loads the menu  ",end="");
         bfunc.LoadAnimation();
         print("");
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
   os.system('del menus\\management\\security.txt');
   SeventhMenu();
else:
   sys.exit();
