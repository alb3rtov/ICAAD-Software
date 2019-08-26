Write-Output "";
$OUName = read-host " Name of Organizational Unit"
Write-Output "";

#$longitud = $OUName.Length

echo "" > .\scripts\obj\cmd\temp\showObjOU.txt

if ($OUName.Length  -gt 4) {
    Get-ADOrganizationalUnit -Filter "Name -like '$OUName'" > .\scripts\obj\cmd\temp\showObjOU.txt

    $counter = (Get-Content .\scripts\obj\cmd\temp\showObjOU.txt | where{$_-match"$OUName"}).Count

    if ($counter -ne 0) {

        try {

            $string = Get-Content .\scripts\obj\cmd\temp\showObjOU.txt | where{$_-match"$OUName"}

            $tag = $string.Split(":",4)[1]

            #echo $tag

            Get-ADObject -SearchBase "$tag" -SearchScope Subtree -Filter * | Select-Object DistinguishedName, Name, ObjectClass

            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host "";
            Write-Host " Error with the name of OU" -ForegroundColor DarkRed
        }
    }
    else {
        Write-Host " OU $OUName doesn't exist" -ForegroundColor DarkRed
    }
}

else {
    Write-Host "  You must to enter a name of OU with at least 4 characters" -ForegroundColor DarkRed
}
