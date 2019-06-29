
#Write-Output "";
#Write-Host " [*] Asegúrese de que la unidad organizativa que va a mover se encuentre vacía" -ForegroundColor Yellow
#Write-Output "";
#$objeto = read-host " Nombre de unidad organizativa a mover"
#Write-Output "";
#$nuevaUO = read-host " Nombre de la unidad organizativa donde mover"
#Write-Output "";
#$nuevaUO = read-host " Nombre de la nueva unidad organizativa: "
#Write-Output "";


$datos1 = Get-Content ".\scripts\obj\gui\docs\moveruogui1.txt"

$datos2 = Get-Content ".\scripts\obj\gui\docs\moveruogui2.txt"

        try {

            Get-ADObject -Filter "Name -eq '$datos1'" > .\scripts\obj\gui\docs\moveruogui3.txt

            Get-ADObject -Filter "Name -eq '$datos2'" > .\scripts\obj\gui\docs\moveruogui4.txt
            
            $contador1 = (Get-Content .\scripts\obj\gui\docs\moveruogui3.txt | where{$_-match"$datos1"}).Count

            $contador2 = (Get-Content .\scripts\obj\gui\docs\moveruogui4.txt | where{$_-match"$datos2"}).Count
            
            #echo $contador
            
            if ($contador1 -ne 0 -and $contador2 -ne 0) {

                $string1 = Get-Content .\scripts\obj\gui\docs\moveruogui3.txt | where{$_-match"$datos1"}

                $string2 = Get-Content .\scripts\obj\gui\docs\moveruogui4.txt | where{$_-match"$datos2"}
                #echo $string
                
                $tag1 = $string1.Split(" ",4)[0]

                $tag2 = $string2.Split(" ",4)[0]
               

                #echo $tag1

                #echo $tag2

                Set-ADOrganizationalUnit -Identity "$tag1" -ProtectedFromAccidentalDeletion $false

                Move-ADObject "$tag1" -TargetPath "$tag2"

                #Write-Host " La unidad organizativa $objeto se ha movido correctamente a $nuevaUO" -ForegroundColor DarkGreen

                echo 0 > .\scripts\obj\gui\docs\compuouo.txt
            }

            else {

                #Write-Host " Error con los nombres de la unidad organizativa" -ForegroundColor DarkRed

                echo 100 > .\scripts\obj\gui\docs\compuouo.txt

            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error") {
            }
            #Write-Host " Error, algunos de los datos que ha introducido son incorrectos" -ForegroundColor DarkRed

            echo 100 > .\scripts\obj\gui\docs\compuouo.txt
        }

