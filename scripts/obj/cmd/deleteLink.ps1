Write-Output "";
$GPOName = read-host " Name of the GPO"
Write-Output "";


Get-GPO -all >  .\scripts\obj\cmd\temp\deleteLink1.txt

$counter1 = (Get-Content .\scripts\obj\cmd\temp\deleteLink1.txt | where{$_-match"$GPOName"}).Count

echo "" > .\scripts\obj\cmd\temp\deleteLink2.txt


if ($counter1 -ne 0) {

$domainName = read-host " Domain name"
Write-Output "";
$domainSuffix = read-host " Domain suffix"
Write-Output "";

$confirmation = read-host " Are the link that you want delete of $GPOName inside of a organizatinal unit? (y/n)"
Write-Output "";


if ($confirmation -eq "y" -or $confirmation -eq "Y") {

   Write-Host " [*] Organizational unit found" -ForegroundColor Yellow


   Get-ADOrganizationalUnit -Filter 'Name -like "*"' | Format-Table Name,DistinguishedName -A


   $OUName = read-host " Name of organizational unit"

   Get-ADOrganizationalUnit -Filter "Name -like '$OUName'" > .\scripts\obj\cmd\temp\deleteLink2.txt

   $counter = (Get-Content .\scripts\obj\cmd\temp\deleteLink2.txt | where{$_-match"$OUName"}).Count

   if ($counter -ne 0) {

   try {

            $string = Get-Content .\scripts\obj\cmd\temp\deleteLink2.txt | where{$_-match"$OUName"}

            $tag = $string.Split(":",4)[1]

            #echo $tag
            #echo $GPOName

            $newtag = $tag.Substring(1)

            Remove-GPLink -Name "$GPOName" -Target "$newtag" > /null

            Write-Output "";
            Write-Host "The link of $GPOName in $newtag has been deleted correctly" -ForegroundColor DarkGreen
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host "";
            Write-Host " Error with some entered data" -ForegroundColor DarkRed
        }

   }

   else {
   Write-Host "";
   Write-Host " The organizational unit $OUName doesn't exist" -ForegroundColor DarkRed



   }

}

Elseif ($confirmation -eq "n" -or $confirmation -eq "N") {




    try {

            Remove-GPLink -Name "$GPOName" -Target "DC=$domainName,DC=$domainSuffix" > /null

            Write-Host "The link of $GPOName in DC=$domainName,DC=$domainSuffix has been deleted correctly" -ForegroundColor DarkGreen
        }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Error with some entered data" -ForegroundColor DarkRed
        }

        }





Else {

            Write-Host " Choose a correct option" -ForegroundColor DarkRed
}

}

else {

            Write-Host " The GPO $GPOName doesn't exist" -ForegroundColor DarkRed
}
