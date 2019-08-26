# Author: Alberto Vázquez
# https://github.com/alb3rtov/
# https://informaticaenuno.wordpress.com/
# Version alfa-0.12.8
# Submenu de Active Directory Users and Groups (Administración)


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


############################## Eigth Menu Options #################################
# First Option
def CreateUser():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\createUser.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\createUser1.txt")
    os.system("del .\\scripts\\obj\\cmd\\temp\\createUser2.txt")
    bfunc.PressKey();

# Second Option
def CreateMultipleUsers():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\createMultipleUsers.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    bfunc.PressKey();

# Third Option
def ShowUsers():
    p = subprocess.Popen(["powershell.exe", "Get-ADUser -Filter * | Format-Table Name,DistinguishedName,Enabled"],stdout=sys.stdout);
    time.sleep(2);
    bfunc.PressKey();

# Fourth Option
def SearchUsers():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\searchUsers.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\searchUsers.txt")
    bfunc.PressKey();

# Fiveth Option
def DeleteUsers():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\deleteUsers.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\deleteUsers.txt")
    bfunc.PressKey();

# Sixth Option
def EDUsers():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\edUsers.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\edUsers.txt")
    bfunc.PressKey();

# Seventh Option
def ResetPasswordUsers():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\resetPasswordUsers.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\resetPasswordUsers.txt")
    bfunc.PressKey();

# Eighth Option
def ExportUsers():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\exportUsers.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\exportUsers.txt")
    bfunc.PressKey();

# Nineth Option
def CreateGroup():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\createGroup.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\createGroup1.txt")
    os.system("del .\\scripts\\obj\\cmd\\temp\\createGroup2.txt")
    bfunc.PressKey();

# Tenth Option
def ShowGroups():
    p = subprocess.Popen(["powershell.exe", "Get-ADGroup -Filter * | Format-Table Name,DistinguishedName,Enabled"],stdout=sys.stdout);
    time.sleep(2);
    bfunc.PressKey();

# Eleventh Option
def SearchGroups():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\searchGroups.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\searchGroups.txt")
    bfunc.PressKey();

# Twelveth Option
def DeleteGroups():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\deleteGroups.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\deleteGroups.txt")
    bfunc.PressKey();

# Thirdteenth Option
def ShowUsersGroups():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\showUsersGroups.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\showUsersGroups.txt")
    bfunc.PressKey();

# Fourteenth Option
def AddUsersGroups():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\addUsersGroups.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\addUsersGroups1.txt")
    os.system("del .\\scripts\\obj\\cmd\\tmep\\addUsersGroups2.txt")
    bfunc.PressKey();

# Fiveteenth Option
def ExportGroups():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\obj\\cmd\\exportGroups.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    os.system("del .\\scripts\\obj\\cmd\\temp\\exportGroups.txt")
    bfunc.PressKey();


####################### EIGTH MENU / OU ADMINISTRATION #########################
def EigthMenu():
    time.sleep(0.5)
    print("");
    print("  [*] Wait while it loads the menu  ",end="");
    bfunc.LoadAnimation();
    print("");

    while True:
      print ("");
      print ("============= Menú de Usuarios de Active Directory =============");
      print ("");
      print ("=========================== USERS ==========================   ");
      print ("");
      print ("     1 ->    Create users                                      ");
      print ("     2 ->    Create multiple users (from CSV file)             ");
      print ("     3 ->    Show all the users                                ");
      print ("     4 ->    Search users                                      ");
      print ("     5 ->    Delete users                                      ");
      print ("     6 ->    Enable/Disable users                              ");
      print ("     7 ->    Reset password of a user                          ");
      print ("     8 ->    Export all the users to a CSV file                ");
      print ("");
      print ("========================== GROUPS ==========================  ");
      print ("");
      print ("     9 ->    Create groups                                     ");
      print ("    10 ->    Show all the groups                               ");
      print ("    11 ->    Search groups                                     ");
      print ("    12 ->    Delete groups                                     ");
      print ("    13 ->    Search users in groups                            ");
      print ("    14 ->    Add users in groups                               ");
      print ("    15 ->    Export all the groups to a CSV file               ");
      print ("    16 ->    Back (previous menu)                              ");
      print ("");
      numOptions = 16;
      option = bfunc.ChooseOption(numOptions); # thirteen options
      if (option == 1):
         CreateUser();
      elif (option == 2):
         CreateMultipleUsers();
      elif (option == 3):
         ShowUsers();
      elif (option == 4):
         SearchUsers();
      elif (option == 5):
         DeleteUsers();
      elif (option == 6):
         EDUsers();
      elif (option == 7):
         ResetPasswordUsers();
      elif (option == 8):
         ExportUsers();
      elif (option == 9):
         CreateGroup();
      elif (option == 10):
         ShowGroups();
      elif (option == 11):
         SearchGroups();
      elif (option == 12):
         DeleteGroups();
      elif (option == 13):
         ShowUsersGroups();
      elif (option == 14):
         AddUsersGroups();
      elif (option == 15):
         ExportGroups();
      elif (option == 16):
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
   EigthMenu();
else:
   sys.exit();
