# Author: Alberto Vázquez
# https://github.com/alb3rtov/
# https://informaticaenuno.wordpress.com/
# Version alpha-0.12.8
# INSTALLATION MENU ACTIVE DIRECTORY


##############################
###    PACKAGES IMPORTED   ###
##############################

import time
import os, sys
import signal
import subprocess
import os.path as path
import re
from management import bfunc
#import glob


#Function that calls the Network Warning
def PressKey3():
    print();
    key = input("Press ENTER to continue");
    NetworkWarning();

#Function to exit the Network Warning
def PressKey2():
    print();
    key = input("Press ENTER to continue");
    ThirdMenu();


#Function to avoid Ctrl+C
def sigint_handler(signum, frame):
    print();
    print("Please, don't press Ctrl+C");
    print();
    time.sleep(1);

signal.signal(signal.SIGINT, sigint_handler)

######################### Second Menu Options ##############################
#First Option
def CheckComponents():
    osName = "OS Name";
    sistemaOperativo = "Nombre del sistema operativo";
    osType1 = "Microsoft Windows Server 2016";
    osType2 = "Microsoft Windows Server 2012";
    osType3 = "Microsoft Windows Server 2019";
    memory = "Total Physical Memory";
    memoria = "Cantidad total de memoria";
    quanMemory1 = "2,048 MB";
    quanMemory2 = "4,096 MB";
    quanMemory3 = "8,192 MB";
    quanMemory4 = "16,384 MB";
    cantMemoria1 = "2.048 MB";
    cantMemoria2 = "4.096 MB";
    cantMemoria3 = "8.192 MB";
    cantMemoria4 = "16.384 MB";
    networkCards = "Network Card(s)";
    tarjetasRed = "Tarjeta(s) de red";
    cnt = 0;

    #os.system('systeminfo > systeminfo.txt');
    print();

    dirFile = 'systeminfo.txt'
    with open(dirFile, 'r') as reader:
      for line in reader:
         if (osName in line or sistemaOperativo in line):
            print(f'  {line}');
            if (osType1 in line or osType2 in line or osType3 in line):
               cnt = cnt+1;
         elif (memory in line or memoria in line):
            print(f'  {line}');
            if (quanMemory1 in line or quanMemory2 in line or
               quanMemory3 in line or quanMemory4 in line or
               cantMemoria1 in line or cantMemoria2 in line or
               cantMemoria3 in line or cantMemoria4 in line):
               cnt = cnt+1;
            #for idx, i in enumerate(line):
            #for i in line:
               #if (i.isdigit() == True):
                  #number = int(i);
                  #first = i[0]

                  #print(memoryreal);
                  #print(number);
                  # FIX THIS FOR FUTURE PROBLEMS WITH NUMBERS STARTING IN 1 (16.384 RAM)
                  # Collect all the numbers and compare with 2048
                  # Use a variable to collect all the numbers
                  #if (number >= 2):
                  #   cnt+=1;
                  #   break
                  #else:
                  #   break

         elif (networkCards in line or tarjetasRed in line):
            print(f'  {line}');
            for i in line:
               if (i.isdigit() == True):
                  number = int(i);
                  if (number >= 2):
                     cnt=cnt+1;

    if (cnt == 3):
       print("  Your system is be able to Active Directory");
    else:
       print("  Your system is NOT be able to Active Directory");
    bfunc.PressKey();

#Second Option:
def CheckRequirements():
    print ("+-----------------------------------------------------------------------+");
    print ("|          Minimum requirements for install AD (ICAAD Software)         |");
    print ("+-----------------------------------------------------------------------+");
    print ("| Operating System: Windows Server 2012, 2016 & 2019                    |");
    print ("| RAM Memory: 2 GB                                                      |");
    print ("| Network: 2 network cards (internal y external)                        |");
    print ("| Storage: 2 Hard disks (Optional for the installation of AD)           |");
    print ("+-----------------------------------------------------------------------+");
    bfunc.PressKey();



#Third Option
def CheckSystem():
    osName = "OS Name";
    sistemaOperativo = "Nombre del sistema operativo";
    osType1 = "Microsoft Windows Server 2012";
    osType2 = "Microsoft Windows Server 2016";
    osType3 = "Microsoft Windows Server 2019";
    memory = "Total Physical Memory";
    memoria = "Cantidad total de memoria";
    quanMemory1 = "2,048 MB";
    quanMemory2 = "4,096 MB";
    quanMemory3 = "8,192 MB";
    quanMemory4 = "16,384 MB";
    cantMemoria1 = "2.048 MB";
    cantMemoria2 = "4.096 MB";
    cantMemoria3 = "8.192 MB";
    cantMemoria4 = "16.384 MB";
    networkCards = "Network Card(s)";
    tarjetasRed = "Tarjeta(s) de red";
    cnt = 0;

    #os.system('systeminfo > systeminfo.txt') ;
    dirFile = 'systeminfo.txt'
    with open(dirFile, 'r') as reader:
      for line in reader:
         if (osName in line or sistemaOperativo in line):

            if (osType1 in line or osType2 in line or osType3 in line):
               cnt = cnt + 1;

         elif (memory in line or memoria in line):

            if (quanMemory1 in line or quanMemory2 in line or
               quanMemory3 in line or quanMemory4 in line or
               cantMemoria1 in line or cantMemoria2 in line or
               cantMemoria3 in line or cantMemoria4 in line):
               cnt = cnt+1;

         elif (networkCards in line or tarjetasRed in line):
            for i in line:
               if (i.isdigit() == True):
                  number = int(i);
                  if (number >= 2):
                     cnt=cnt+1;


    if (cnt == 3):
       print();
       print("  Your system is be able to Active Directory");
       PressKey3();
    else:
       print();
       print("  Your system is NOT be able to Active Directory");
       bfunc.PressKey();


#Fourth Option is for exit the program

########################### Third Menu Options #######################
# First Option for the Third Menu
def ChangeAdapter():
    print();
    adapter = input(" Current adapter name: ");
    print();
    newAdapter = input(" What of this names do you want for the adapter: Internal Network (i) or Internet (e): ");
    print();
    if (newAdapter == "i" or newAdapter == "I"):
       os.system(f'netsh interface set interface name="{adapter}" newname="Internal Network"');
    elif (newAdapter == "e" or newAdapter == "E"):
       os.system(f'netsh interface set interface name="{adapter}" newname="Internet"');
    else:
       print(" Choose a correct option (i/e)");

    bfunc.PressKey();


# Second Option for the Third Menu, configure internal network card
def ConfigureNetwork(networkCard):
    print();
    print(f'============= Configuration of Internal network card "{networkCard}"=============');
    print();
    print(f'****Remember that the name of your adapter MUST BE "{networkCard}"****');
    print();
    ipAddress = input("  Choose a IP address: ");
    print();
    mask = input("  Choose a mask: ");
    print();
    gateway = input("  Choose a default gateway: ");
    print();
    pdns = input("  Choose a Preferred DNS server: ");

    flag1 = 0;
    flag2 = 0;
    flag3 = 0;
    flag4 = 0;
    pattern = "^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$";
    match1 = re.match(pattern, ipAddress);
    match2 = re.match(pattern, mask);
    match3 = re.match(pattern, gateway);
    match4 = re.match(pattern, pdns);

    #IP Address
    if (match1):
        field1 = ipAddress.split(".");
        for i in range(0, len(field1)):
            if (int(field1[i]) < 256):
                flag1 += 1
            else:
                flag1 = 0
    #Mask
    if (match2):
        field2 = mask.split(".");
        for i in range(0, len(field2)):
            if (int(field2[i]) < 256):
                flag2 += 1
            else:
                flag2 = 0

    #default gateway
    if (match3):
        field3 = gateway.split(".");
        for i in range(0, len(field3)):
            if (int(field3[i]) < 256):
                flag3 += 1
            else:
                flag3 = 0

    #Preferred DNS
    if (match4):
        field4 = pdns.split(".");
        for i in range(0, len(field4)):
            if (int(field4[i]) < 256):
                flag4 += 1
            else:
                flag4 = 0


    if (flag1 != 4):
        print();
        print("  Error, enter a valid IP address (i.e.: 192.168.1.10)");
    elif (flag2 != 4):
        print();
        print("  Error, enter a correct mask (i.e.: 255.255.255.0)")
    elif (flag3 != 4):
        print();
        print("  Error, enter a correct puerta de enlace");
    elif (flag4 != 4):
        print();
        print("  Error, enter a correct DNS");
    else:
        os.system(f'netsh interface ip set address "{networkCard}" static {ipAddress} {mask} {gateway}');
        os.system(f'netsh interface ip set dns "{networkCard}" static {pdns}');
        print(f'  Correct Configuration for "{networkCard}" adapter');

    bfunc.PressKey();



#Fourth option of the Third Menu, check Network Configuration
def CheckNetworkConfig():
    os.system('ipconfig /all');
    bfunc.PressKey();

#Fiveth option of the Third Menu, change computer name
def ChangeComputerName():
    p = subprocess.Popen([f"powershell.exe", ".\\scripts\\oscripts\\renameComputer.ps1"],stdout=sys.stdout);
    p.communicate();
    bfunc.RestartComputer();

#Sixth option of the Third Menu, check computer name

def CheckComputerName():
    print("The current name of your computer is: ");
    os.system('hostname');
    bfunc.PressKey();


#Seventh option of the Third Menu, install Active Directory
def InstallAD():
    print();
    print("  [*] Installing Active Directory Domain Services, please wait  ",end="");
    bfunc.LoadAnimation();();
    print();
    p = subprocess.Popen([f"powershell.exe", "Install-WindowsFeature AD-Domain-Services -IncludeAllSubFeature -IncludeManagementTools"],stdout=sys.stdout);
    p.communicate();

    FourthMenu();
    #os.system(f'type nul > menus\\seguridad.txt')
    #os.system('menus\\configuracionad.py');

#Eighth option is back to the previous menu

#Nineth option is back to the main menu


########################## Fourth Menu Options ######################################
#First Option, promote DC



#Second Menu, installation AD and system check
def SecondMenu():
   time.sleep(0.5)
   print("");
   print("  [*] Wait while it loads the menu  ",end="");
   bfunc.LoadAnimation();();
   print("");


   while True:
      print ("");
      print ("========== Menu of system check and installation of AD ==========");
      print ("");
      print ("     1 ->    Show and check components of THIS system             ");
      print ("     2 ->    Show minimum components for AD (ICAAD Software)      ");
      print ("     3 ->    Start with installation of Active Directory          ");
      print ("     4 ->    Main Menu                                            ");
      print ("");
      numOptions = 4;
      option = bfunc.ChooseOption(numOptions);
      if (option == 1):
         CheckComponents();
      elif (option == 2):
         CheckRequirements();
      elif (option == 3):
         CheckSystem(); # This option calls the below Menu
      elif (option == 4):
         print("");
         print("  [*] Wait while it loads the menu  ",end="");
         bfunc.LoadAnimation();();
         print("");
         sys.exit();
      else:
         break;

# Third Menu
def ThirdMenu():
   time.sleep(0.5)
   print("");
   print("  [*] Wait while it loads the menu  ",end="");
   bfunc.LoadAnimation();();
   print();

   while True:
      print ("");
      print ("================ Menu of Configuration of Network Cards  ================");
      print ("");
      print ("     1 ->    Change name of network adapter                          ");
      print ("     2 ->    Configure internal network card (Internal Network)      ");
      print ("     3 ->    Configure external network card (Internet)              ");
      print ("     4 ->    Show network cards configuration                        ");
      print ("     5 ->    Change computer name                                    ");
      print ("     6 ->    Show computer name                                      ");
      print ("     7 ->    Install Domain Services of Active Directory             ");
      print ("     8 ->    Back (previous menu)                                    ");
      print ("     9 ->    Main menu                                               ");
      print ("");
      numOptions = 9;
      option = bfunc.ChooseOption(numOptions);
      if (option == 1):
         ChangeAdapter();
      elif (option== 2):
         internal = "Internal Network";
         ConfigureNetwork(internal);
      elif (option == 3):
         external = "Internet";
         ConfigureNetwork(external);
      elif (option == 4):
         CheckNetworkConfig();
      elif (option == 5):
         ChangeComputerName();
      elif (option == 6):
         CheckComputerName();
      elif (option == 7):
         InstallAD();
      elif (option == 8):
         SecondMenu();
      elif (option == 9):
         print("");
         print("  [*] Wait while it loads the menu  ",end="");
         bfunc.LoadAnimation();();
         print("");
         sys.exit();
      else:
         break;


#Fourth Menu
def FourthMenu():
    time.sleep(0.5)
    print("");
    print("  [*] Wait while it loads the menu  ",end="");
    bfunc.LoadAnimation();();
    print();

    while True:
      print ("");
      print ("============= Menu of system check as Domain Controller =============");
      print ("");
      print ("     1 ->    Promote this server to Domain Controller      ");
      print ("     2 ->    Check if this server is a Domain Controller   ");
      print ("     3 ->    Delete the Active Directory Service           ");
      print ("     4 ->    Main menu                                     ");
      print ("");
      numOptions = 4;
      option = bfunc.ChooseOption(numOptions);
      if (option == 1):
         bfunc.PromoteDC();
      elif (option == 2):
         bfunc.CheckDC();
      elif (option == 3):
         bfunc.DeleteAD();
      elif (option == 4):
         print("");
         print("  [*] Wait while it loads the menu  ",end="");
         bfunc.LoadAnimation();();
         print("");
         sys.exit();
      else:
         break;


#Network Warning
def NetworkWarning():
    time.sleep(0.5)
    print("");
    print("  [*] Wait while it loads the menu  ",end="");
    bfunc.LoadAnimation();();
    print();

    while True:
        print();
        print("***********************************************************************************");
        print("******************************* IMPORTANT WARNING *********************************");
        print("***********************************************************************************");
        print();
        print("The following menu contains some OPTIONALS choices.");
        print("This options can be change from the Windows GUI easily.");
        print("In the case of you want to configure with this program, make sure of:");
        print();
        print("  ->  Adapter name for the internal network: 'Internal Network' (without quotes)");
        print("  ->  Adapter name for the external network: 'Internet' (without quotes)");
        print();
        print("Please, for a correct Network configuration perfom this configuration.")
        PressKey2();
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
   SecondMenu();
else:
   sys.exit();
