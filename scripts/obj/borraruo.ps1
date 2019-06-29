Write-Output "";
Write-Host " [*] Antes de borrar una unidad organizativa, asegúrese de que se encuentre vacía" -ForegroundColor Yellow
Write-Output "";
$nombreUO = read-host " Nombre de unidad organizativa"
Write-Output "";
#$nombreDominio = read-host " Nombre de dominio: "
#Write-Output "";
#$extensionDominio = read-host " Extension de dominio: "
#Write-Output "";

#$longitud = $nombreUO.Length 

echo "" > .\scripts\obj\docs\borraruo.txt

if ($nombreUO.Length  -gt 4) {
    Get-ADOrganizationalUnit -Filter "Name -like '$nombreUO'" > .\scripts\obj\docs\borraruo.txt

    $contador = (Get-Content .\scripts\obj\docs\borraruo.txt | where{$_-match"$nombreUO"}).Count

    if ($contador -ne 0) {
    
        try {

            $string = Get-Content .\scripts\obj\docs\borraruo.txt | where{$_-match"$nombreUO"}

            $tag = $string.Split(":",4)[1]

            #echo $tag

            Set-ADOrganizationalUnit -Identity "$tag" -ProtectedFromAccidentalDeletion $false # quita la proteccion de la uo

            Remove-ADOrganizationalUnit -Identity "$tag" -Confirm:$false # borra la unidad organizativa

            #Write-Output "";
            #Write-Host " Unidad $nombreUO borrada correctamente" -ForegroundColor DarkGreen
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host "";
            Write-Host " Error al borrar la unidad organizativa" -ForegroundColor DarkRed
        }
    }
    else {
        Write-Host " La unidad organizativa $nombreUO no existe" -ForegroundColor DarkRed
    }
}

else {
    Write-Host " Debe introducir un nombre de más de 4 carácteres" -ForegroundColor DarkRed
}

