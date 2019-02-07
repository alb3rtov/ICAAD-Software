﻿Write-Output "";
$zonainversa = read-host " Para borrar la zona escriba el Id. del red (Ej: 192.168.50.0/24)"


$a,$b,$c,$d = $zonainversa.Split('.')

$arpa = ".in-addr.arpa"

$punto = "."

$nombrezona = $c + $punto + $b + $punto + $a + $arpa

#echo $nombrezona
try {

Remove-DnsServerZone -Name "$nombrezona" -Confirm:$False -Force

Write-Output "";
Write-Host " Zona borrada correctamente" -ForegroundColor DarkGreen
}

catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            
            Write-Output "";
            Write-Host " Error con alguno de los datos introducidos" -ForegroundColor DarkRed
}


