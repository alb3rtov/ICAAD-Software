
Write-Output "";
Write-Host " [*] The users are created automatically 'disabled' for password secure reasons" -ForegroundColor Yellow
Write-Output "";
Write-Host " [*] Use the option 5 for enable/disable users of Active Directory" -ForegroundColor Yellow
Write-Output "";
$userName = read-host " Name of the new user"
Write-Output "";
$password = read-host -AsSecureString " Password"
Write-Output "";

echo "" > .\scripts\obj\cmd\temp\createUser1.txt
echo "" > .\scripts\obj\cmd\temp\createUser2.txt

try {

    Get-ADUser -Filter "Name -eq '$userName'" > .\scripts\obj\cmd\temp\createUser1.txt

}

catch [System.Management.Automation.RuntimeException] {

        if ($_.Exception.Message -ilike "Error"){
        }

    Write-Host " Error, some data are wrong" -ForegroundColor DarkRed
    Write-Output "";

}

$counter = (Get-Content .\scripts\obj\cmd\temp\createUser1.txt | where{$_-match"$userName"}).Count


$confirmation = read-host " ¿Do you want es specify a Organizational Unit (default: CN=Users)? (y/n)"
Write-Output "";

if ($confirmation -eq "y" -or $confirmation -eq "Y") {

Write-Host " [*] Organizational units found" -ForegroundColor Yellow

Get-ADOrganizationalUnit -Filter 'Name -like "*"' | Format-Table Name,DistinguishedName -A

$OUName = read-host " Name of the organizational unit"
Write-Output "";

    if ($counter -eq 0) {

        try {
            Get-ADOrganizationalUnit -Filter "Name -like '$OUName'" > .\scripts\obj\cmd\temp\createUser2.txt

            $counter2 = (Get-Content .\scripts\obj\cmd\temp\createUser2.txt | where{$_-match"$OUName"}).Count

            #echo $contador2

            if ($counter2 -ne 0) {

                $string = Get-Content .\scripts\obj\cmd\temp\createUser2.txt| where{$_-match"$OUName"}

                $tag = $string.Split(":",4)[1]

                #echo $tag

                New-ADUser -Name $userName -AccountPassword (ConvertTo-SecureString -AsPlainText "$password" -Force) -Enable $false -Path $tag

                Write-Host " User $userName created correctly en$tag" -ForegroundColor DarkGreen
            }

            else {
                Write-Host " The Organizational Unit $OUName doesn't exist" -ForegroundColor DarkRed
            }

            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Error, some data are wrong" -ForegroundColor DarkRed
        }
    }

    else {
        Write-Host " The username $userName ALREADY exists" -ForegroundColor DarkRed
    }


 }


#$longitud = $nombreUO.Length

else {

    if ($counter -eq 0) {

        try {
            New-ADUser -Name $userName -AccountPassword (ConvertTo-SecureString -AsPlainText "$password" -Force) -Enable $false
            Write-Host " User $userName created correctly" -ForegroundColor DarkGreen
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Error, some data are wrong" -ForegroundColor DarkRed
        }
    }
    else {
        Write-Host " The username $userName ALREADY exists" -ForegroundColor DarkRed
    }

}
