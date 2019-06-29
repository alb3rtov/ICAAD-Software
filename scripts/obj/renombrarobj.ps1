Write-Output "";
$nombre = read-host " Nombre del objeto a renombrar"
Write-Output "";
$nuevoNombre = read-host " Nuevo nombre del objeto"
Write-Output "";
#$nuevaUO = read-host " Nombre de la nueva unidad organizativa: "
#Write-Output "";

        try {

            Get-ADObject -Filter "Name -eq '$nombre'" > .\scripts\obj\docs\renombrarobj.txt

            
            $contador1 = (Get-Content .\scripts\obj\docs\renombrarobj.txt | where{$_-match"$nombre"}).Count
            
            #echo $contador
            
            if ($contador -ne 0) {

                $string = Get-Content .\scripts\obj\docs\renombrarobj.txt | where{$_-match"$nombre"}

                #echo $string
                
                $tag = $string.Split(" ",4)[0]
               
                #echo $tag

                Rename-ADObject -Identity "$tag" -NewName "$nuevoNombre"


                Write-Host " El objeto $nombre se ha renombrado como $nuevoNombre" -ForegroundColor DarkGreen
            }

            else {

                Write-Host " Error con los nombres de los objetos" -ForegroundColor DarkRed

            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error") {
            }
            Write-Host " Error, algunos de los datos que ha introducido son incorrectos" -ForegroundColor DarkRed
        }

