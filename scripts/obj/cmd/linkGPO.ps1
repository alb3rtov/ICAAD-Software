Write-Output "";
Write-Host " [*] Default, the GPO it will be linked at level of the domain OUs that you choose" -ForegroundColor Yellow
Write-Output "";
$GPOName = read-host " Name of the GPO"
Write-Output "";


Get-GPO -all >  .\scripts\obj\cmd\temp\linkGPO1.txt

$counter1 = (Get-Content .\scripts\obj\cmd\temp\linkGPO1.txt | where{$_-match"$GPOName"}).Count

echo "" > .\scripts\obj\cmd\temp\linkGPO2.txt

if ($counter1 -ne 0) {

$domainName = read-host " Domain name"
Write-Output "";
$domainSuffix = read-host " Domain suffix"
Write-Output "";

$confirmation = read-host " ¿Do you want to link the GPO to a organizational unit? (y/n)"
Write-Output "";



if ($confirmation -eq "y" -or $confirmation -eq "Y") {

   Write-Host " [*] Organizational units found" -ForegroundColor Yellow


   Get-ADOrganizationalUnit -Filter 'Name -like "*"' | Format-Table Name,DistinguishedName -A


   $OUName = read-host " Name of the organizational unit"

   if ($OUName.Length -ne 0) {

         Get-ADOrganizationalUnit -Filter "Name -like '$OUName'" > .\scripts\obj\cmd\temp\linkGPO2.txt

         $counter = (Get-Content .\scripts\obj\cmd\temp\linkGPO2.txt | where{$_-match"$OUName"}).Count

            if ($counter -ne 0) {

                try {

                    $string = Get-Content .\scripts\obj\cmd\temp\linkGPO2.txt | where{$_-match"$OUName"}

                    $tag = $string.Split(":",4)[1]

                    #echo $tag
                    #echo $GPOName

                    $newtag = $tag.Substring(1)

                    New-GPLink -Name "$GPOName" -Target "$newtag" > /null

                    Write-Output "";
                    Write-Host " $GPOName linked to $newtag" -ForegroundColor DarkGreen
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
   Write-Host " The organizatinal unit $OUName doesn't exist" -ForegroundColor DarkRed


}


   }

   else  {
        Write-Host "";
        Write-Host " Entered some name for the organizational unit" -ForegroundColor DarkRed



   }



}

Elseif ($confirmation -eq "n" -or $confirmation -eq "N") {




    try {

            New-GPLink -Name "$GPOName" -Target "DC=$domainName,DC=$domainSuffix" > /null


            Write-Host " $GPOName linked to DC=$domainName,DC=$domainSuffix correctly" -ForegroundColor DarkGreen
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
