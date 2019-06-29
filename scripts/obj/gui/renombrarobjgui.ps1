#Write-Output "";
#$nombre = read-host " Nombre del objeto a renombrar"
#Write-Output "";
#$nuevoNombre = read-host " Nuevo nombre del objeto"
#Write-Output "";
#$nuevaUO = read-host " Nombre de la nueva unidad organizativa: "
#Write-Output "";


$datos1 = Get-Content ".\scripts\obj\gui\docs\renombrarobj.txt"

$datos2 = Get-Content ".\scripts\obj\gui\docs\renombrarobj2.txt"

        try {

            Get-ADObject -Filter "Name -eq '$datos1'" > .\scripts\obj\gui\docs\renombrarobj3.txt

            
            $contador1 = (Get-Content .\scripts\obj\gui\docs\renombrarobj3.txt | where{$_-match"$datos1"}).Count
            
            #echo $contador
            
            if ($contador -ne 0) {

                $string = Get-Content .\scripts\obj\gui\docs\renombrarobj3.txt | where{$_-match"$datos1"}

                #echo $string
                
                $tag = $string.Split(" ",4)[0]
               
                #echo $tag

                Rename-ADObject -Identity "$tag" -NewName "$datos2"

                echo 0 > .\scripts\obj\gui\docs\comprobj.txt


               # Write-Host " El objeto $nombre se ha renombrado como $nuevoNombre" -ForegroundColor DarkGreen
            }

            else {

                # Write-Host " Error con los nombres de los objetos" -ForegroundColor DarkRed

                echo 100 > .\scripts\obj\gui\docs\comprobj.txt

            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error") {
            }
            #Write-Host " Error, algunos de los datos que ha introducido son incorrectos" -ForegroundColor DarkRed

            echo 100 > .\scripts\obj\gui\docs\comprobj.txt
        }

