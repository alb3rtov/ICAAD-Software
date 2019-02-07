Write-Output "";
Write-Host " [*] Por defecto, la ruta de generación del archivo CSV es el directorio de este programa" -ForegroundColor Yellow
Write-Output "";
$ruta = read-host " Ruta y nombre donde generar el CSV (Ej: C:\grupos.csv)"
Write-Output "";

$csv = ".csv"

$ruta > .\scripts\obj\docs\exportgrupo.txt 

$contador = (Get-Content .\scripts\obj\docs\exportgrupo.txt | where{$_-match"$csv"}).Count


if ($contador -ne 0) {

try {
Get-ADGroup -Filter * -Properties * | Export-Csv $ruta
Write-Host " $ruta generado correctamente" -ForegroundColor DarkGreen
}

catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Error con la ruta" -ForegroundColor DarkRed
        }

}

else {

  Write-Host " Debe añadir la extensión .csv" -ForegroundColor DarkRed
}