
#Write-Output "";
#$confirmacion = read-host " ¿Desea habilitar o deshabilitar un usuario? (h/d)"
#Write-Output "";

    

$datos = Get-Content ".\scripts\obj\gui\docs\habilitarusu.txt"


        try {
            Get-ADUser -Filter "Name -eq '$datos'" > .\scripts\obj\gui\docs\habilitarusu.txt
            
            $contador = (Get-Content .\scripts\obj\gui\docs\habilitarusu.txt | where{$_-match"$datos"}).Count

            if ($contador -ne 0) {

                Enable-ADAccount -Identity $datos
                #Write-Host " El usuario $datos ha sido habilitado" -ForegroundColor DarkGreen
                echo 0 > .\scripts\obj\gui\docs\comphdusu.txt
            }

            else {
                #Write-Host " El usuario $datos no existe" -ForegroundColor DarkRed
                echo 100 > .\scripts\obj\gui\docs\comphdusu.txt

            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error"){
            }
            #Write-Host " Debe introducir algún dato" -ForegroundColor DarkRed
            echo 100 > .\scripts\obj\gui\docs\comphdusu.txt
        }



