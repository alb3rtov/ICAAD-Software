# Author: Alberto Vázquez
# https://github.com/alb3rtov/
# https://informaticaenuno.wordpress.com/
# Version alfa-0.12.8
# ADMINISTRATION MENU ACTIVE DIRECTORY


##############################
###    PACKAGES IMPORTED   ###
##############################

import subprocess
import time
import os, sys
import os.path as path
import signal
from management import bfunc


#Function to avoid Ctrl+C
def sigint_handler(signum, frame):
    print();
    print("Please, don't press Ctrl+C");
    print();
    time.sleep(1);

signal.signal(signal.SIGINT, sigint_handler)

############################# Sixth Menu Options ######################################
# The first four options are directly called from the menu

# Fiveth Option
def SearchObj():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\searchObj.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system('del .\\scripts\\obj\\cmd\\temp\\searchObj.txt');
    bfunc.PressKey();

# Sixth Option
def RenameObj():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\renameObj.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system('del .\\scripts\\obj\\cmd\\temp\\renameObj.txt');
    bfunc.PressKey();

# Seventh Option
def ExportObj():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\exportObj.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system('del .\\scripts\\obj\\cmd\\temp\\exportObj.txt');
    bfunc.PressKey();

# Eighth Option
def SecCopy():
    print()
    source = input(" Source directory (i.e.: D:\Directory): ")
    print();
    destination = input(" Destination directory (i.e.: D:\Copy): ")


    if path.exists(source):


        print();
        option = input(f" Do you want to copy all the files, directories and subdirectories of {source}? (y/n): ")
        print();


        if (option == "y") or (option == "Y"):
           os.system(f'xcopy "{source}" "{destination}" /d/e/y/c/i/h')
           #print(" Archivos copiados")
           #print("0")
           bfunc.PressKey();

        elif (option == "n") or (option == "N"):

            option2 = input(f" Do you want to copy the directories and subdirectories of {source}? (y/n): ")
            print()
            #option3 = input(f" ¿Desea copiar archivos con una extensión específica? (s/n): ")
            #print();

            if (option2 == "y") or (option2 == "Y"):
               #os.system(f"xcopy '{source}' '{destination}' /d/e/y/c/i/h > log.txt 2>&1")

               option3 = input(f" Do you want to copy this files with especific extension (y/n): ")
               print();

               if (option3 == "N") or (option3 == "n"):
                  os.system(f'xcopy "{source}" "{destination}" /d/e/y/c/i/h')
                  #print("1")
                  bfunc.PressKey();


               elif (option2 == "y") or (option2 == "Y"):
                  extension = input(" Enter the extension of the files to copy (i.e.: pdf, doc, txt...): ")
                  print();
                  os.system(f'xcopy "{source}\*.{extension}" "{destination}" /d/e/y/c/i/h')
                  #print("2")
                  bfunc.PressKey();

               else:
                  print("")
                  print(" Choose a correct option (y/n)");
                  bfunc.PressKey();


            elif (option2 == "N") or (option2 == "n"):

                print(f" [*] Only the files of the directory {source} will be copied")
                print();

                option4 = input(f" Do you want to copy the files with a especific extension? (y/n): ")
                print();

                if (option4 == "N") or (option4 == "n"):
                   os.system(f'xcopy "{source}" "{destination}" /d/y/c/i/h')
                   #print("3")
                   bfunc.PressKey();


                elif (option4 == "Y") or (option4 == "y"):
                   extension = input(" Enter the extension of the files to copy (i.e.: pdf, doc, txt...): ")
                   print()
                   os.system(f'xcopy "{source}\*.{extension}" "{destination}" /d/y/c/i/h')
                   #print("4")
                   print()
                   bfunc.PressKey();


                else:
                   print("")
                   print(" Choose a correct option (y/n)");
                   bfunc.PressKey();


            else:
                print();
                print(" Choose a correct option (y/n))");
                bfunc.PressKey();

        else:
            print();
            print(" Choose a correct option (y/n)");
            bfunc.PressKey();


    else:
        print()
        print(f"Directory {source} doesn't exists")
        bfunc.PressKey();

# Nineth Option is to back to the previous menu



################################# SIXTH MENU ####################################
def SixthMenu():
    time.sleep(0.5)
    print("");
    print("  [*] Wait while it loads the menu  ",end="");
    bfunc.LoadAnimation();
    print();

    while True:
      print ("");
      print ("============ Menu of administration of Active Directory ============");
      print ("");
      print ("     1 ->    Organizational Unit                                  ");
      print ("     2 ->    Active Directory Users and Groups                    ");
      print ("     3 ->    Shared resources                                     ");
      print ("     4 ->    Group Policy Object (GPO)                            ");
      print ("     5 ->    Seach object Active Directory                        ");
      print ("     6 ->    Rename objects Active Directory                      ");
      print ("     7 ->    Export all the objects AD to a CSV file              ");
      print ("     8 ->    Create a secure copy                                 ");
      print ("     9 ->    Back (previous menu)                                 ");
      print ("");
      numOptions = 9;
      option = bfunc.ChooseOption(numOptions);
      if (option == 1):
         os.system(f'type nul > menus\\management\\security.txt')
         os.system('menus\\management\\ou.py') # call Organizational Unit menu
      elif (option == 2):
         os.system(f'type nul > menus\\management\\security.txt')
         os.system('menus\\management\\ug.py') # call AD Users and Groups menu
      elif (option == 3):
         os.system(f'type nul > menus\\management\\security.txt')
         os.system('menus\\management\\sr.py') # call Shared resources menu
      elif (option == 4):
         os.system(f'type nul > menus\\management\\security.txt')
         os.system('menus\\management\\gpo.py') # call GPOs menu
      elif (option == 5):
         SearchObj();
      elif (option == 6):
         RenameObj();
      elif (option == 7):
         ExportObj();
      elif (option == 8):
         SecCopy();
      elif (option== 9):
         print("");
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
   SixthMenu();
else:
   sys.exit();
