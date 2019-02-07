Write-Output "";
$nombreUO = read-host " Nombre de unidad organizativa"
Write-Output "";

#$longitud = $nombreUO.Length 

echo "" > .\scripts\obj\docs\objuo.txt

if ($nombreUO.Length  -gt 4) {
    Get-ADOrganizationalUnit -Filter "Name -like '$nombreUO'" > .\scripts\obj\docs\objuo.txt

    $contador = (Get-Content .\scripts\obj\docs\objuo.txt | where{$_-match"$nombreUO"}).Count

    if ($contador -ne 0) {
    
        try {

            $string = Get-Content .\scripts\obj\docs\objuo.txt | where{$_-match"$nombreUO"}

            $tag = $string.Split(":",4)[1]

            #echo $tag

            Get-ADObject -SearchBase "$tag" -SearchScope Subtree -Filter * | Select-Object DistinguishedName, Name, ObjectClass

            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host "";
            Write-Host " Error con el nombre de unidad organizativa" -ForegroundColor DarkRed
        }
    }
    else {
        Write-Host " La unidad organizativa $nombreUO no existe" -ForegroundColor DarkRed
    }
}

else {
    Write-Host " Debe introducir un nombre de más de 4 carácteres" -ForegroundColor DarkRed
}

