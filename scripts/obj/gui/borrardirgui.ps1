#Write-Output "";
#Write-Host " [*] Por defecto, la ruta de generación del archivo CSV es el directorio de este programa" -ForegroundColor Yellow
#Write-Output "";
#$ruta = read-host " Ruta y nombre donde generar el CSV (Ej: C:\objetosad.csv)"
#Write-Output "";

$datos = Get-Content ".\scripts\obj\gui\docs\borrardirgui.txt"


$comprobarruta = Test-Path $datos
#Test-Path $datos

if ($comprobarruta -eq $True) {

try {
 Remove-Item -Recurse -Force -ErrorAction SilentlyContinue $datos
#Write-Host " $ruta generado correctamente" -ForegroundColor DarkGreen
echo 0 > .\scripts\obj\gui\docs\compbodir.txt
}

catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            #Write-Host " Error con la ruta" -ForegroundColor DarkRed
            echo 100 > .\scripts\obj\gui\docs\compbodir.txt
        }

}

else {

echo 100 > .\scripts\obj\gui\docs\compbodir.txt
}