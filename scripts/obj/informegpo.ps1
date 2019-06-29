
Write-Output "";
Write-Host " [*] La ruta de generación del informe será $Home" -ForegroundColor Yellow

Write-Output "";
$nombreGPO = read-host " Nombre de la GPO para generar informe"
Write-Output "";


Get-GPO -all >  .\scripts\obj\docs\informegpo.txt

$contador1 = (Get-Content .\scripts\obj\docs\informegpo.txt | where{$_-match"$nombreGPO"}).Count


if ($contador1 -ne 0) {

   try {

            Get-GPO -Name "$nombreGPO" | Get-GPOReport -ReportType HTML -Path $Home\informe_$nombreGPO.html   > /null

           
            Write-Host " Informe de $nombreGPO generado correctamente" -ForegroundColor DarkGreen
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