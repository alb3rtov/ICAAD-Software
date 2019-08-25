
Write-Output "";
$GPOName = read-host " Name of the GPO"
Write-Output "";
$key = read-host " Enter the register key"
Write-Output "";
$value = read-host " Enter the name of the register value"
Write-Output "";


Get-GPO -all >  .\scripts\obj\cmd\temp\configureGPO.txt

$counter1 = (Get-Content .\scripts\obj\cmd\temp\configureGPO.txt | where{$_-match"$GPOName"}).Count


if ($counter1 -ne 0) {

   try {

            Set-GPRegistryValue -Name "$GPOName" -Key "$key" -ValueName $value -Type DWord -Value 0


            Write-Host " $GPOName configure correctly" -ForegroundColor DarkGreen
            }

    catch [System.Management.Automation.RuntimeException] {
    
	if ($_.Exception.Message -ilike "Error"){
        
	}

            Write-Host " Error with some entered data" -ForegroundColor DarkRed
        }
    }



else {

            Write-Host " GPO $GPOName doesn't exist" -ForegroundColor DarkRed
}
