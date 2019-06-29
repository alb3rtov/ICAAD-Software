
Write-Output "";
$objeto = read-host " Nombre del objeto a mover"
Write-Output "";
$nuevaUO = read-host " Nombre de la unidad organizativa donde mover el objeto"
Write-Output "";
$nombreDominio = read-host " Nombre dominio"
Write-Output "";
$extensionDominio = read-host " Sufijo de dominio"
Write-Output "";
#$nuevaUO = read-host " Nombre de la nueva unidad organizativa: "
#Write-Output "";

        try {

            Get-ADObject -Filter "Name -eq '$objeto'" > .\scripts\obj\docs\moverobjuo.txt
            
            $contador = (Get-Content .\scripts\obj\docs\moverobjuo.txt | where{$_-match"$objeto"}).Count
            
            #echo $contador

            if ($contador -ne 0) {

                $string = Get-Content .\scripts\obj\docs\moverobjuo.txt | where{$_-match"$objeto"}

                #echo $string

                $tag = $string.Split(" ",4)[0]
               

                #echo $tag

                Move-ADObject "$tag" -TargetPath "OU=$nuevaUO,DC=$nombreDominio,DC=$extensionDominio"

                Write-Host " El objeto $objeto se ha movido correctamente" -ForegroundColor DarkGreen
            }

            else {

                Write-Host " El objeto $objeto no existe" -ForegroundColor DarkRed

            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error") {
            }
            Write-Host " Error, algunos de los datos que ha introducido son incorrectos" -ForegroundColor DarkRed
        }

