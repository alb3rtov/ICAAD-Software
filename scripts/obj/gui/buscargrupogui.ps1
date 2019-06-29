
#Write-Output "";
#$nombreUsuario = read-host " Buscar usuario"
#Write-Output "";



$datos = Get-Content ".\scripts\obj\gui\docs\buscargrupogui.txt"

        try {
            Get-ADGroup -Filter "Name -eq '$datos'" > .\scripts\obj\gui\docs\buscargrupogui.txt
            
            $contador = (Get-Content .\scripts\obj\gui\docs\buscargrupogui.txt | where{$_-match"$datos"}).Count

            if ($contador -ne 0) {
                #Get-ADUser -Filter "Name -eq '$datos'"

                echo 0 > .\scripts\obj\gui\docs\compbgrupo.txt
            }

            else {
               # Write-Host " El usuario $datos no existe" -ForegroundColor DarkRed

               echo 100 > .\scripts\obj\gui\docs\compbgrupo.txt
            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error"){
            }
           # Write-Host " Debe introducir algún dato" -ForegroundColor DarkRed

           echo 100 > .\scripts\obj\gui\docs\compbgrupo.txt
        }




