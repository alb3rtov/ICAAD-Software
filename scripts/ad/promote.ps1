Write-Output "";
$domain = read-host " Name of domain (i.e.:ASIR.LOCAL)"
Write-Output "";
$password = read-host -AsSecureString " Password for the administrator account (secure mode)"
Write-Output "";

if ($password.Length -gt 7) {
	
	try {

		Install-ADDSForest -DomainName $domain -SafeModeAdministratorPassword $password -Confirm:$false
	
	}

	catch [System.Management.Automation.RuntimeException] {
            
		if ($_.Exception.Message -ilike "Error"){

		}
            
		Write-Host " Error with some of the entered parameters" -ForegroundColor DarkRed
        }


}

else {
     
	Write-Host " Enter a password with, at least, 8 characters" -ForegroundColor DarkRed

}
