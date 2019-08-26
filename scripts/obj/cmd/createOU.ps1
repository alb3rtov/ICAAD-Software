
Write-Output "";
$OUName = read-host " Name of Organizational Unit"
Write-Output "";
$domainName = read-host " Domain name"
Write-Output "";
$suffixDomain = read-host " Domain suffix"
Write-Output "";
$hostName = hostname

$confirmation = read-host " Do you want to add additional values? (y/n)"
Write-Output "";

if ($confirmation -eq "y" -or $confirmacion -eq "Y") {
    $country = read-host " Country (abbreviation i.e.: ES, EN...)"
    Write-Output "";
    $city = read-host " City"
    Write-Output "";

}


#$longitud = $OUName.Length

echo "" > .\scripts\obj\cmd\temp\createOU.txt

if ($OUName.Length  -gt 4) {
    Get-ADOrganizationalUnit -Filter "Name -like '$OUName'" > .\scripts\obj\cmd\temp\createOU.txt

    $counter = (Get-Content .\scripts\obj\cmd\temp\createOU.txt | where{$_-match"$OUName"}).Count

    if ($counter -eq 0) {

        try {
            New-ADOrganizationalUnit -name $OUName -server $hostName -path "DC=$domainName, DC=$suffixDomain" -Country $country -City $city
            Write-Host " OU $OUName created correctly" -ForegroundColor DarkGreen
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Enter a correct name and a domain suffix" -ForegroundColor DarkRed
        }
    }
    else {
        Write-Host " Organizational Unit $OUName ALREADY exists " -ForegroundColor DarkRed
    }
}

else {
    Write-Host " You must to enter a name of OU of at least 4 characters" -ForegroundColor DarkRed
}
