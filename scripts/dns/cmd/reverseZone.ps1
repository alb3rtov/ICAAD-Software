Write-Output "";
$reverseZone = read-host " To identify the zone of search reverse, write the ID of network (i.e.: 192.168.50.0/24)"
Write-Output "";

$reverseZone > .\scripts\dns\cmd\temp\ReverseZone.txt

$check = "/"

$counter = (Get-Content .\scripts\dns\cmd\temp\ReverseZone.txt | where{$_-match"$check"}).Count

#echo $contador

if ($counter -ne 0) {

	try {

		Add-DnsServerPrimaryZone -NetworkId "$reverseZone" -ReplicationScope "Forest"

		Write-Host " Reverse zone created correctly" -ForegroundColor DarkGreen
	}

	catch [System.Management.Automation.RuntimeException] {

		if ($_.Exception.Message -ilike "Error"){
        }
        
	Write-Host " Error with some entered data" -ForegroundColor DarkRed
	
	}


}

else {
    
    Write-Host " Enter a correct ID of network (i.e.: 192.168.50.0/24)" -ForegroundColor DarkRed

}
