# ICAAD Software
ICAAD Software es un asistente de instalación, configuración y administración de Active Directory. 

Básicamente se crea una capa gráfica con diferentes menús y submenús con múltiples opciones para la administración de Active Directory
y mediante el backend se procesan los comandos de Powershell según las indicaciones establecidas en el frontend del administrador .

La principal utilidad de este proyecto es la de minimizar las tareas al administrador, creando una interfaz donde podremos encontrar
múltiples opciones en una misma consola de administración.

El desarrollo de este programa se orientó principalmente para versiones de Windows Server Core (sin experiencia de escritorio). 
Así el administrador no deberá de conocer todos los cmdlets de Powershell necesarios para la administración básica de un 
controlador de dominio.

Este proyecto se desarrolló los siguientes lenguajes:

- Python 3.6: Utilizado como base para la creación de menús y submenús.
- Powershell 5: Utilizado para la creación de scripts .ps1 que serán llamados desde el menú de Python.

Se han desarrollado dos versiones de ICAAD:

- Versión CMD: Se ejecuta en la consola de Windows donde se genera un menú numérico.
- Versión GUI: Se ejecuta en una interfaz independiente al CMD. Creado con la librería de Python, Tkinter.

Sistemas operativos aptos para ICAAD Software

- Windows Server 2016 (En todas sus versiones)
- Windows Server 2012 (Service Packs KB2919442 y KB2919335 necesarios)
 
ICAAD Software se encuentra actualmente en la versión alpha 0.12.8, con el tiempo se irán implementando 
nuevos menús y submenús con diferentes opciones.
