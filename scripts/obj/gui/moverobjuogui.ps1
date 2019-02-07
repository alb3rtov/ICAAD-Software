
#Write-Output "";
#$objeto = read-host " Nombre del objeto a mover"
#Write-Output "";
#$nuevaUO = read-host " Nombre de la unidad organizativa donde mover el objeto"
#Write-Output "";
#$nombreDominio = read-host " Nombre dominio"
#Write-Output "";
#$extensionDominio = read-host " Sufijo de dominio"
#Write-Output "";
#$nuevaUO = read-host " Nombre de la nueva unidad organizativa: "
#Write-Output "";


$datos1 = Get-Content ".\scripts\obj\gui\docs\moverobjuogui1.txt"

$datos2 = Get-Content ".\scripts\obj\gui\docs\moverobjuogui2.txt"

$datos3 = Get-Content ".\scripts\obj\gui\docs\moverobjuogui3.txt"

$datos4 = Get-Content ".\scripts\obj\gui\docs\moverobjuogui4.txt"


        try {

            Get-ADObject -Filter "Name -eq '$datos1'" > .\scripts\obj\gui\docs\moverobjuogui5.txt
            
            $contador = (Get-Content .\scripts\obj\gui\docs\moverobjuogui5.txt | where{$_-match"$datos1"}).Count
            
            #echo $contador

            if ($contador -ne 0) {

                $string = Get-Content .\scripts\obj\gui\docs\moverobjuogui5.txt | where{$_-match"$datos1"}

                #echo $string

                $tag = $string.Split(" ",4)[0]
               

                #echo $tag

                Move-ADObject "$tag" -TargetPath "OU=$datos2,DC=$datos3,DC=$datos4"

                #Write-Host " El objeto $objeto se ha movido correctamente" -ForegroundColor DarkGreen

                echo 0 > .\scripts\obj\gui\docs\compmouo.txt
            }

            else {

                #Write-Host " El objeto $objeto no existe" -ForegroundColor DarkRed

                echo 100 > .\scripts\obj\gui\docs\compmouo.txt
                

            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error") {
            }
            #Write-Host " Error, algunos de los datos que ha introducido son incorrectos" -ForegroundColor DarkRed
            
            echo 100 > .\scripts\obj\gui\docs\compmouo.txt
        }

