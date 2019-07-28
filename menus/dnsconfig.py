# Author: Alberto Vázquez
# https://github.com/alb3rtov/
# https://informaticaenuno.wordpress.com/
# Version alfa-0.12.8
# CONFIGURATION DNS - ACTIVE DIRECTORY


##############################
###    PACKAGES IMPORTED   ###
##############################


import time
import os, sys
#import glob
import signal
import subprocess
import os.path as path
import re
from management import bfunc



#Function to avoid Ctrl+C
def sigint_handler(signum, frame):
    print();
    print("Please, don't press Ctrl+C");
    print();
    time.sleep(1);

signal.signal(signal.SIGINT, sigint_handler)


########################## opciones quinto menu ######################################
#primera opción (crear zona inversa)
def ReverseZone():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\dns\\cmd\\reverseZone.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    bfunc.PressKey();

    p1 = subprocess.Popen(["powershell.exe", "del .\\scripts\\dns\\cmd\\temp\\reverseZone.txt"],stdout=sys.stdout);

#segunda opcion
def DeleteReverseZone():
    p = subprocess.Popen(["powershell.exe", ".\\scripts\\dns\\cmd\\deleteReverseZone.ps1"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    bfunc.PressKey();



#tercera opcion
def ShowDNSZones():
    p = subprocess.Popen(["powershell.exe", "Get-DnsServerZone"],stdout=sys.stdout); # se ponen dos barras para que no de problemas de codec
    p.communicate();
    bfunc.PressKey();


#cuarta opcion
def CheckDNSResolutionNames():
    print();
    print(" For check the resolution names, enter the domain name or IP address");
    print();
    print(" Use the command 'exit' to exit");
    print();
    os.system('nslookup');
    bfunc.PressKey();

# quinta opcion
def RefreshDNS():
    os.system('ipconfig -registerdns');
    bfunc.PressKey();

# sexta opcion es mostrar configurar de tarjetas de red
def ShowINConfig():
    os.system('netsh interface ipv4 show address "Internal Network"');
    os.system('netsh interface ipv4 show dns "Internal Network"');
    bfunc.PressKey();

# septima opción
def PreferredDNS():
    print();
    print(" Remember that for configure the network card is necessary the configuration of the adapter name ('Internal Network')");
    print();

    pdns = input("  Choose a address of Preferred DNS: ");

    flag4 = 0;
    pattern = "^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$";
    match4 = re.match(pattern, pdns);


    #dns preferido
    if (match4):
        field4 = pdns.split(".");
        for i in range(0, len(field4)):
            if (int(field4[i]) < 256):
                flag4 += 1
            else:
                flag4 = 0

    if (flag4 != 4):
        print();
        print("  Error, enter a correct DNS");
    else:
        os.system(f'netsh interface ip set dns "Internal Network" static {pdns}');
        print('  Correct Configuration for Internal Network adapter');
    bfunc.PressKey();

# octava opcion es menu anterior


# quinto menú
def FivethMenu():
   time.sleep(0.5)
   print("");
   print("  [*] Wait while it loads the menu  ",end="");
   bfunc.LoadAnimation();
   print();

   while True:
      print ("");
      print ("================ Menu of configuration and check of DNS ================");
      print ("");
      print ("     1 ->    Create a new primary reverse zone                           ");
      print ("     2 ->    Delete reverse zone                                         ");
      print ("     3 ->    Show DNS zones                                              ");
      print ("     4 ->    Check the resolution names (nslookup)                       ");
      print ("     5 ->    Refrest / register DNS names (ipconfig /registerdns)        ");
      print ("     6 ->    Check configuration of 'Internal Network'                   ");
      print ("     7 ->    Change preferred DNS of 'Internal Network'                  ");
      print ("     8 ->    Back (previous menu)                                        ");
      print ("");
      numOptions = 8;
      option = bfunc.ChooseOption(numOptions);
      if (option == 1):
         ReverseZone();
      elif (option == 2):
         DeleteReverseZone();
      elif (option == 3):
         ShowDNSZones();
      elif (option == 4):
         CheckDNSResolutionNames();
      elif (option == 5):
         RefreshDNS();
      elif (option == 6):
         ShowINConfig();
      elif (option == 7):
         PreferredDNS();
      elif (option == 8):
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
   FivethMenu();
else:
   sys.exit();
