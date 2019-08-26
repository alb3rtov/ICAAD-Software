# Author: Alberto Vázquez
# https://github.com/alb3rtov/
# https://informaticaenuno.wordpress.com/
# Version alfa-0.12.8
# Submenu of Shared Resources (Administration)


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

############################## opciones septimo menu #################################
# First Option
def CreateDir():
    print();
    directoryName = input(" Name of the directory/path (D:\Compartida): ");
    print();
    os.system(f'md "{directoryName}"');
    bfunc.PressKey();
    #p = subprocess.Popen(["powershell.exe", ".\\scripts\\cc\\crearc.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    #p.communicate();
    #bfunc.PressKey();

# Second Option
def SharedDir():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\sr\\cmd\\sharedDir.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\sr\\cmd\\temp\\resource.txt")
    os.system("del .\\scripts\\sr\\cmd\\temp\\users.txt")
    bfunc.PressKey();


# Third Option
def ModPermissions():
    print();
    sharedResource = input(" Name of the shared resource to modify the permissions: ");
    print();
    print( " [*] Users found");
    p = subprocess.Popen(["powershell.exe", "Get-ADUser -Filter * | Format-Table Name,DistinguishedName"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();


    accountName = input(" Name of the account (user/group) to add permissions: ");
    print();
    permissionType = input(f" Type of permission that you want to add to {accountName} (R/C/F): ");

    os.system(f'net share > .\\scripts\\sr\\cmd\\temp\\resource.txt ');

    os.system(f'net user > .\\scripts\\sr\\cmd\\temp\\users.txt ');

    cnt = 0

    dirFile = '.\\scripts\\sr\\cmd\\temp\\resource.txt';
    with open(dirFile, 'r') as reader:
        for line in reader:
            if (sharedResource in line):
                #print(line)
                cnt = cnt+1

    #no encuentra esto
    dirFile2 = '.\\scripts\\sr\\cmd\\temp\\users.txt'
    with open(dirFile2, 'r') as reader:
        for line in reader:
            #print(line)
            if (accountName in line):
                #print(line)
                cnt = cnt+1


    #print(cnt)

    os.system("del .\\scripts\\sr\\cmd\\temp\\resource.txt")
    os.system("del .\\scripts\\sr\\cmd\\temp\\users.txt")

    if (cnt == 2):

        if (permissionType == "R" or permissionType == "r"):

            p = subprocess.Popen(["powershell.exe", f"Grant-SmbShareAccess -Name {sharedResource} -AccountName {accountName} -AccessRight Read -Confirm:$false -Force"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
            p.communicate();
            bfunc.PressKey();

        elif (permissionType == "C" or permissionType == "c"):

            p = subprocess.Popen(["powershell.exe", f"Grant-SmbShareAccess -Name {sharedResource} -AccountName {accountName} -AccessRight Change -Confirm:$false -Force"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
            p.communicate();
            bfunc.PressKey();

        elif (permissionType == "F" or permissionType == "f"):

            p = subprocess.Popen(["powershell.exe", f"Grant-SmbShareAccess -Name {sharedResource} -AccountName {accountName} -AccessRight Full -Confirm:$false -Force"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
            p.communicate();
            bfunc.PressKey();

        else:
            print();
            print(" Choose a correct option (R/C/F)");
            bfunc.PressKey();
    else:
        print();
        #print(cnt)
        print(f" Enter correct data");


# Fourth Option
def SearchSR():
    print();
    SRName = input(" Name of the shared resource: ");
    print();

    if (len(SRName) != 0):
        os.system(f'net share "{SRName}"');
        bfunc.PressKey();
    else:
        print();
        print(" Introduce algún nombre de recurso compartido");

# Fiveth Option
def ShowSR():
    os.system('net share');
    bfunc.PressKey();


# Sixth Option
def DeleteSR():
    print();
    SRName = input(" Name of the shared resource you want delete: ");

    if (len(SRName) == 0):
        print();
        print(" Enter some name for the shared resource");
    else:
        print();
        confirmation = input(f" ¿Desea realmente eliminar el recurso {SRName}? (y/n): ")
        print();

        if (confirmation == "Y" or confirmation == "y"):
            os.system(f'net share "{SRName}" /delete');
            bfunc.PressKey();
        else:
            print();
            print(f" Could not deleted the shared resource {SRName}");
            bfunc.PressKey();


# Seventh Option
def DeleteDir():
    print();
    nameDir = input(" Name of the directory you want delete: ");
    print();
    os.system(f'rd /s /q {nameDir}');



############################## Seventh Menu ###################################
def SeventhMenu():
    time.sleep(0.5)
    print("");
    print("  [*] Wait while it loads the menu  ",end="");
    bfunc.LoadAnimation();
    print("");
    os.system('cd..');

    while True:
      print ("");
      print ("================== Menu of Shared Resources ==================");
      print ("");
      print ("     1 ->    Create directory                                     ");
      print ("     2 ->    Share a folder/directory                             ");
      print ("     3 ->    Modify permissions of shared resources               ");
      print ("     4 ->    Search a shared resource                             ");
      print ("     5 ->    Show all the shared resources                        ");
      print ("     6 ->    Delete shared resources                              ");
      print ("     7 ->    Delete directories and subdirectories                ");
      print ("     8 ->    Back (previous menu)                                 ");
      print ("");
      numOptions = 8;
      option = bfunc.ChooseOption(numOptions); # ocho opciones
      if (option == 1):
         CreateDir();
      elif (option == 2):
         SharedDir();
      elif (option == 3):
         ModPermissions();
      elif (option == 4):
         SearchSR();
      elif (option == 5):
         ShowSR();
      elif (option == 6):
         DeleteSR();
      elif (option == 7):
         DeleteDir();
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
