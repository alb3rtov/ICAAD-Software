
#Write-Output "";
#$nombreUsuario = read-host " Buscar usuario"
#Write-Output "";



$datos = Get-Content ".\scripts\obj\gui\docs\buscarusugui.txt"

        try {
            Get-ADUser -Filter "Name -eq '$datos'" > .\scripts\obj\gui\docs\buscarusugui.txt
            
            $contador = (Get-Content .\scripts\obj\gui\docs\buscarusugui.txt | where{$_-match"$datos"}).Count

            if ($contador -ne 0) {
                #Get-ADUser -Filter "Name -eq '$datos'"

                echo 0 > .\scripts\obj\gui\docs\compbusu.txt
            }

            else {
               # Write-Host " El usuario $datos no existe" -ForegroundColor DarkRed

               echo 100 > .\scripts\obj\gui\docs\compbusu.txt
            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error"){
            }
           # Write-Host " Debe introducir algún dato" -ForegroundColor DarkRed

           echo 100 > .\scripts\obj\gui\docs\compbusu.txt
        }




