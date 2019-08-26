Write-Output "";
$reverseZone = read-host " Write the zone Id. of the network to delete it (i.e.: 192.168.50.0/24)"


$a,$b,$c,$d = $reverseZone.Split('.')

$arpa = ".in-addr.arpa"

$dot = "."

$zoneName = $c + $dot + $b + $dot + $a + $arpa

#echo $nombrezona

try {

	Remove-DnsServerZone -Name "$zoneName" -Confirm:$False -Force

	Write-Output "";
	Write-Host " Zone deleted correctly" -ForegroundColor DarkGreen
}

catch [System.Management.Automation.RuntimeException] {
            
	if ($_.Exception.Message -ilike "Error"){

	}
            
        Write-Output "";
        Write-Host " Error with some data entered" -ForegroundColor DarkRed
}


