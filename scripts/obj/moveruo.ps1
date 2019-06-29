
Write-Output "";
Write-Host " [*] Asegúrese de que la unidad organizativa que va a mover se encuentre vacía" -ForegroundColor Yellow
Write-Output "";
$objeto = read-host " Nombre de unidad organizativa a mover"
Write-Output "";
$nuevaUO = read-host " Nombre de la unidad organizativa donde mover"
Write-Output "";
#$nuevaUO = read-host " Nombre de la nueva unidad organizativa: "
#Write-Output "";

        try {

            Get-ADObject -Filter "Name -eq '$objeto'" > .\scripts\obj\docs\moveruo1.txt

            Get-ADObject -Filter "Name -eq '$nuevaUO'" > .\scripts\obj\docs\moveruo2.txt
            
            $contador1 = (Get-Content .\scripts\obj\docs\moveruo1.txt | where{$_-match"$objeto"}).Count

            $contador2 = (Get-Content .\scripts\obj\docs\moveruo2.txt | where{$_-match"$nuevaUO"}).Count
            
            #echo $contador
            
            if ($contador1 -ne 0 -and $contador2 -ne 0) {

                $string1 = Get-Content .\scripts\obj\docs\moveruo1.txt | where{$_-match"$objeto"}

                $string2 = Get-Content .\scripts\obj\docs\moveruo2.txt | where{$_-match"$nuevaUO"}
                #echo $string
                
                $tag1 = $string1.Split(" ",4)[0]

                $tag2 = $string2.Split(" ",4)[0]
               

                #echo $tag1

                #echo $tag2

                Set-ADOrganizationalUnit -Identity "$tag1" -ProtectedFromAccidentalDeletion $false

                Move-ADObject "$tag1" -TargetPath "$tag2"

                Write-Host " La unidad organizativa $objeto se ha movido correctamente a $nuevaUO" -ForegroundColor DarkGreen
            }

            else {

                Write-Host " Error con los nombres de la unidad organizativa" -ForegroundColor DarkRed

            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error") {
            }
            Write-Host " Error, algunos de los datos que ha introducido son incorrectos" -ForegroundColor DarkRed
        }

