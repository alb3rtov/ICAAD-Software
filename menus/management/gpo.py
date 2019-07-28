# Author: Alberto Vázquez
# https://github.com/alb3rtov/
# https://informaticaenuno.wordpress.com/
# Version alfa-0.12.8
# Submenu of Group Policy Object (Administration)


##############################
###    PACKAGES IMPORTED   ###
##############################

import subprocess
import time
import os, sys
import os.path as path
import signal
#import io
import bfunc


#Function to avoid Ctrl+C
def sigint_handler(signum, frame):
    print();
    print("Please, don't press Ctrl+C");
    print();
    time.sleep(1);

signal.signal(signal.SIGINT, sigint_handler)



############################## opciones septimo menu #################################
#primera opcion
def CreateGPO():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\createGPO.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();

    os.system("del .\\scripts\\obj\\cmd\\temp\\createGPO.txt")
    bfunc.PressKey();

#segunda opcion
def ShowGPO():
    p = subprocess.Popen(["powershell.exe", "Get-GPO -all"],stdout=sys.stdout);
    time.sleep(2);
    bfunc.PressKey();


#tercera opcion
def SearchGPO():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\searchGPO.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\searchGPO.txt")
    bfunc.PressKey();



#cuarta opcion
def LinkGPO():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\linkGPO.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\linkGPO1.txt")
    os.system("del .\\scripts\\obj\\cmd\\temp\\linkGPO2.txt")
    bfunc.PressKey();


#quinta opcion
def DeleteGPO():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\deleteGPO.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\deleteGPO.txt")
    bfunc.PressKey();


#sexta opcion
def DeleteLink():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\deleteLink.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\deleteLink1.txt")
    os.system("del .\\scripts\\obj\\cmd\\temp\\deleteLink2.txt")

    bfunc.PressKey();


# septima opcion
#menu de configuracion de gpos

# octava opcion
def ReportGPO():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\reportGPO.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\reportGPO.txt")
    bfunc.PressKey();




############################## opciones octavo menu #################################
#primera opcion
def UpdateGPO():
    os.system("gpupdate /force");
    bfunc.PressKey();


#segunda opcion
def ConfigureGPO():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\configureGPO.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\configureGPO.txt")
    bfunc.PressKey();



#septimo menu, unidades organizativas:
def NinethMenu():
    time.sleep(0.5)
    print("");
    print("  [*] Wait while it loads the menu  ",end="");
    bfunc.LoadAnimation();
    print("");
    os.system('cd..');

    while True:
      print ("");
      print ("================== Menu of Group Policy Object (GPO) ==================");
      print ("");
      print ("     1 ->    Create GPO                                               ");
      print ("     2 ->    Show all GPOs                                            ");
      print ("     3 ->    Search GPO                                               ");
      print ("     4 ->    Link GPOs                                                ");
      print ("     5 ->    Delete GPO                                               ");
      print ("     6 ->    Delete link of GPOs                                      ");
      print ("     7 ->    Menu of configuration GPOs                               ");
      print ("     8 ->    Generate a report with GPO configuration                 ");
      print ("     9 ->    Back (previous menu)                                     ");
      print ("");
      numOptions = 9;
      option = bfunc.ChooseOption(numOptions); # ocho opciones
      if (option == 1):
         CreateGPO();
      elif (option == 2):
         ShowGPO();
      elif (option == 3):
         SearchGPO();
      elif (option == 4):
         LinkGPO();
      elif (option == 5):
         DeleteGPO();
      elif (option == 6):
         DeleteLink();
      elif (option == 7):
         TenthMenu();
      elif (option == 8):
         ReportGPO();
      elif (option == 9):
         print("");
         print("  [*] Wait while it loads the menu  ",end="");
         bfunc.LoadAnimation();
         print("");
         sys.exit();
      else:
         break;




def TenthMenu():
    time.sleep(0.5)
    print("");
    print("  [*] Wait while it loads the menu  ",end="");
    bfunc.LoadAnimation();
    print("");
    os.system('cd..');

    while True:
      print ("");
      print ("==================== Menú de configuración de GPOs ====================");
      print ("");
      print ("     1 ->    Update GPO (gpudpate)                                    ");
      print ("     2 ->    Configure GPO (Register key and Value)                   ");
      print ("     3 ->    Back (previous menu)                                     ");
      print ("");
      numOptions = 3;
      option = bfunc.ChooseOption(numOptions); # ocho opciones
      if (option == 1):
         UpdateGPO();
      elif (option == 2):
         ConfigureGPO();
      elif (option == 3):
         NinethMenu();
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
   NinethMenu();
else:
   sys.exit();
