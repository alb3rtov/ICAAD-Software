# ICAAD Software
ICAAD Software is a assitant of installation, configuration and management of Active Directory.

Basically, this software use a graphic layer with diferents menus with sereval options for the managament of Active Directory and through backend it process all the cmdlets according to the intructions set in frontend by the manager.

The main utility of this project is reduce the tasks of the manager, creating a interface where can find several options, all in one same console of management.

The development of this software was firstly set for versions of Windows Server Core (without desktop experience). In this way, the manager shouldn't know all the _cmdlets_ of `PowerShell` about the basic management of a **Domain Controller**. 
<br>
<hr/>


<img src="https://i.imgur.com/nsRCk6p.png" align="right" width="450"/>

This project was develop with the next programming language:

- `Python 3.6`: Use as base for the creation of menus.
- `PowerShell 5`: Use for the creation of scripts ps1 that will call from the Python menu.

Two ICAAD versions have been developed:

- **CMD version**: It runs in Windows console (cmd) where it generates a numerical menu.
- **GUI version**: It runs in a stand-alone interface to CMD. It uses Tkinter that is Python's de-facto standard GUI package.

Suitable Operating Systems for ICAAD Software:

- **Windows Server 2016** (All versions)
- **Windows Server 2012** (Service Packs KB2919442 and KB2919335 needed)


<hr/>

 
Nowadays, ICAAD Software is in development, as a alpha version 0.12.8 and there is only the Spanish version avaliable. Over time, I will adding new options and menus, and especially a English version.

_Visit the [Wiki](https://github.com/alb3rtov/ICAAD-Software/wiki) more information._

<hr/>

# License
This software is licensed under the GNU General Public License v3.0.


