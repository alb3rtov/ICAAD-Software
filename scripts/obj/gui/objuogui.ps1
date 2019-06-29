#Write-Output "";
#$nombreUO = read-host " Nombre de unidad organizativa"
#Write-Output "";

#$longitud = $nombreUO.Length 


$datos = Get-Content ".\scripts\obj\gui\docs\objuogui.txt"


    Get-ADOrganizationalUnit -Filter "Name -like '$datos'" > .\scripts\obj\gui\docs\objuogui2.txt

    $contador = (Get-Content .\scripts\obj\gui\docs\objuogui2.txt | where{$_-match"$datos"}).Count

    if ($contador -ne 0) {
    
        try {

            $string = Get-Content .\scripts\obj\gui\docs\objuogui2.txt | where{$_-match"$datos"}

            $tag = $string.Split(":",4)[1]

            #echo $tag

            Get-ADObject -SearchBase "$tag" -SearchScope Subtree -Filter * | Select-Object DistinguishedName, Name, ObjectClass > .\scripts\obj\gui\docs\objuogui2.txt

            echo 0 > .\scripts\obj\gui\docs\compouo.txt

            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            #Write-Host "";
            #Write-Host " Error con el nombre de unidad organizativa" -ForegroundColor DarkRed

            echo 100 > .\scripts\obj\gui\docs\compouo.txt
        }
    }
    else {
        #Write-Host " La unidad organizativa $nombreUO no existe" -ForegroundColor DarkRed

        echo 100 > .\scripts\obj\gui\docs\compouo.txt
    }


