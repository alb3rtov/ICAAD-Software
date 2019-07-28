Write-Output "";
$zonainversa = read-host " Para identificar la zona de búsqueda inversa, escriba el Id. del red (Ej: 192.168.50.0/24)"
Write-Output "";

$zonainversa > .\scripts\dns\docs\zonainversa.txt

$comprobar = "/"

$contador = (Get-Content .\scripts\dns\docs\zonainversa.txt | where{$_-match"$comprobar"}).Count

#echo $contador

if ($contador -ne 0) {

try {

Add-DnsServerPrimaryZone -NetworkId "$zonainversa" -ReplicationScope "Forest"

 Write-Host " Zona inversa creada correctamente" -ForegroundColor DarkGreen
}

catch [System.Management.Automation.RuntimeException] {
           if ($_.Exception.Message -ilike "Error"){
           }
           Write-Host " Error con alguno de los datos introducidos" -ForegroundColor DarkRed
}


}

else {
    
    Write-Host " Introduzca un ID de red correcto (Ej: 192.168.50.0/24)" -ForegroundColor DarkRed

}