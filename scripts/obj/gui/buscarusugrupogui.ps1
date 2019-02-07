#Write-Output "";
#$nombreGrupo = read-host " Nombre del grupo"
#Write-Output "";




$datos = Get-Content ".\scripts\obj\gui\docs\buscarusugrupogui.txt"





#echo $longitud


Get-ADGroup -Filter "Name -like '$datos'" > .\scripts\obj\gui\docs\buscarusugrupogui.txt

$contador = (Get-Content .\scripts\obj\gui\docs\buscarusugrupogui.txt| where{$_-match"$datos"}).Count


echo "" > .\scripts\obj\gui\docs\buscarusugrupogui1.txt

    if ($contador -ne 0) {
    
        try {

            #$string = Get-Content .\scripts\obj\usugrupo.txt | where{$_-match"$nombreGrupo"}

            #$tag = $string.Split(":",4)[1]

            #echo $tag

            Get-ADGroupMember "$datos" -recursive | Select-Object Name, DistinguishedName > .\scripts\obj\gui\docs\buscarusugrupogui1.txt

            echo 0 > .\scripts\obj\gui\docs\compusugrupo.txt

            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            #Write-Host "";
            #Write-Host " Error con el nombre del grupo" -ForegroundColor DarkRed

            echo 100 > .\scripts\obj\gui\docs\compusugrupo.txt
        }
    }
    else {
        #Write-Host " El grupo $nombreGrupo no existe" -ForegroundColor DarkRed

        echo 100 > .\scripts\obj\gui\docs\compusugrupo.txt
    }

