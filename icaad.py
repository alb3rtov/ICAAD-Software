# Author: Alberto Vázquez
# https://github.com/alb3rtov/
# https://informaticaenuno.wordpress.com/
# Version alfa-0.12.8

##############################
###    PACKAGES IMPORTED   ###
##############################

import sys, os, time

def startProgram():
    print();
    opcion = input(" Do you want execute this program with version GUI (g) or CMD (c)? (g/c/e): ")
    if (opcion == "g") or (opcion == "G"):
        if __name__ == "__main__":
            time.sleep(1)
            os.system('cls')
            os.system(".\\gui.py")
    elif (opcion == "c") or (opcion == "C"):
        os.system('cls')
        time.sleep(1)
        os.system(".\\cmd.py");
    elif (opcion == "e") or (opcion == "E"):
        sys.exit();
    else:
        print("");
        print("  [*] Error, use a correct option (g/c/e)")
        time.sleep(2)
        os.system('cls')
        startProgram();


startProgram();
