Write-Output "";
Write-Host " [*] Before delete a OU, make sure that it's empty" -ForegroundColor Yellow
Write-Output "";
$OUName = read-host " Name of Organizational Unit"
Write-Output "";
#$nombreDominio = read-host " Nombre de dominio: "
#Write-Output "";
#$extensionDominio = read-host " Extension de dominio: "
#Write-Output "";

#$longitud = $OUName.Length

echo "" > .\scripts\obj\cmd\temp\deleteOU.txt

if ($OUName.Length  -gt 4) {
    Get-ADOrganizationalUnit -Filter "Name -like '$OUName'" >.\scripts\obj\cmd\temp\deleteOU.txt

    $counter = (Get-Content .\scripts\obj\cmd\temp\deleteOU.txt | where{$_-match"$OUName"}).Count

    if ($counter -ne 0) {

        try {

            $string = Get-Content .\scripts\obj\cmd\temp\deleteOU.txt | where{$_-match"$OUName"}

            $tag = $string.Split(":",4)[1]

            #echo $tag

            Set-ADOrganizationalUnit -Identity "$tag" -ProtectedFromAccidentalDeletion $false # quita la proteccion de la uo

            Remove-ADOrganizationalUnit -Identity "$tag" -Confirm:$false # borra la unidad organizativa

            #Write-Output "";
            #Write-Host " OU $OUName deleted" -ForegroundColor DarkGreen
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host "";
            Write-Host " Error deleting the OU $OUName" -ForegroundColor DarkRed
        }
    }
    else {
        Write-Host " OU $OUName doesn't exist" -ForegroundColor DarkRed
    }
}

else {
    Write-Host " You must to enter at least 4 characters for the OU name" -ForegroundColor DarkRed
}
