Write-Output "";
Write-Host " [*] Default, the GPO it will be created in 'Group Policy Objects'" -ForegroundColor Yellow
Write-Output "";
$GPOName = read-host " Name of the new GPO"
Write-Output "";


Get-GPO -all >  .\scripts\obj\cmd\temp\createGPO.txt

$counter1 = (Get-Content .\scripts\obj\cmd\temp\createGPO.txt | where{$_-match"$GPOName"}).Count


if ($counter1 -eq 0) {


   try {
	
	new-gpo -name "$GPOName" > /null

	Write-Host " GPO $GPOName created correctly" -ForegroundColor DarkGreen
   }

   catch [System.Management.Automation.RuntimeException] {

	if ($_.Exception.Message -ilike "Error"){
        
	}

            Write-Host " Error with some of the entered data" -ForegroundColor DarkRed
        }
    }



else {

	Write-Host " The GPO $GPOName ALREADY exists" -ForegroundColor DarkRed

}
