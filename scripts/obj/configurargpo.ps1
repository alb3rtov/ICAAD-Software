
Write-Output "";
$nombreGPO = read-host " Nombre de la GPO"
Write-Output "";
$key = read-host " Introduzca la KEY de registro"
Write-Output "";
$valor = read-host " Introduca el nombre de valor de registro"
Write-Output "";


Get-GPO -all >  .\scripts\obj\docs\configurargpo.txt

$contador1 = (Get-Content .\scripts\obj\docs\configurargpo.txt | where{$_-match"$nombreGPO"}).Count


if ($contador1 -ne 0) {

   try {

            Set-GPRegistryValue -Name "$nombreGPO" -Key "$key" -ValueName $valor -Type DWord -Value 0

           
            Write-Host " $nombreGPO configurada correctamente" -ForegroundColor DarkGreen
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
           
            Write-Host " Error con alguno de los datos introducidos" -ForegroundColor DarkRed
        }
    }
   


else {
 
            Write-Host " La GPO $nombreGPO no existe" -ForegroundColor DarkRed
}