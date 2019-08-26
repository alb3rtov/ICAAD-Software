#Write-Output "";
#Write-Host " [*] Los usuarios se crean automáticamente deshabilitados por seguridad de la contraseña" -ForegroundColor Yellow
#Write-Output "";
#Write-Host " [*] Utiliza la 5º opcion del menú para habilitar/deshabilitar usuarios de AD" -ForegroundColor Yellow
Write-Output "";
$groupName = read-host " Name of the new group"
Write-Output "";

echo "" > .\scripts\obj\cmd\temp\createGroup1.txt
echo "" > .\scripts\obj\cmd\temp\createGroup2.txt

try {

    Get-ADGroup -Filter "Name -eq '$groupName'" > .\scripts\obj\cmd\temp\createGroup1.txt

}

catch [System.Management.Automation.RuntimeException] {

        if ($_.Exception.Message -ilike "Error"){
        }

    Write-Host " Error, some data are wrong" -ForegroundColor DarkRed
    Write-Output "";

}

$counter = (Get-Content .\scripts\obj\cmd\temp\createGroup1.txt | where{$_-match"$groupName"}).Count


$confirmacion = read-host " ¿Do you want specify a Organizational Unit (default: CN=Users)? (y/n)"
Write-Output "";


if ($confirmacion -eq "y" -or $confirmacion -eq "Y") {

Write-Host " [*] Organizational units found" -ForegroundColor Yellow

Get-ADOrganizationalUnit -Filter 'Name -like "*"' | Format-Table Name,DistinguishedName -A

    $OUName = read-host " Path where create the new group (OU or container)"
    Write-Output "";

    if ($counter -eq 0) {

        try {
            Get-ADOrganizationalUnit -Filter "Name -like '$OUName'" > .\scripts\obj\cmd\temp\createGroup2.txt

            $counter2 = (Get-Content .\scripts\obj\cmd\temp\createGroup2.txt | where{$_-match"$OUName"}).Count

            #echo $contador2

            if ($counter2 -ne 0) {

                $string = Get-Content .\scripts\obj\cmd\temp\createGroup2.txt | where{$_-match"$OUName"}

                $tag = $string.Split(":",4)[1]

                #echo $tag

                New-ADGroup -Name "$groupName" -GroupScope Global -Path "$tag"

                Write-Host " Group $groupName created correctly in$tag" -ForegroundColor DarkGreen
            }

            else {
                Write-Host " The organizational unit $OUName doesn't exist" -ForegroundColor DarkRed
            }

            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Error, some data are wrong" -ForegroundColor DarkRed
        }
    }

    else {
        Write-Host " The group $groupName ALREADY exists" -ForegroundColor DarkRed
    }


}


#$longitud = $OUName.Length

else {

    if ($counter -eq 0) {

        try {
            New-ADGroup -Name "$groupName" -GroupScope Global

            Write-Host " Group $groupName created correctly" -ForegroundColor DarkGreen
            }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Error, some data are wrong" -ForegroundColor DarkRed
        }
    }
    else {
        Write-Host " The group $groupName ALREADY exists" -ForegroundColor DarkRed
    }

}
