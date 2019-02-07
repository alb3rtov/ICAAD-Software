#Write-Output "";
#Write-Host " [*] Por defecto, la ruta de generación del archivo CSV es el directorio de este programa" -ForegroundColor Yellow
#Write-Output "";
#$ruta = read-host " Ruta y nombre donde generar el CSV (Ej: C:\objetosad.csv)"
#Write-Output "";

$datos = Get-Content ".\scripts\obj\gui\docs\crearcarpetagui.txt"


try {
md $datos | Out-Null #> nul
#Write-Host " $ruta generado correctamente" -ForegroundColor DarkGreen
echo 0 > .\scripts\obj\gui\docs\compccc.txt
}

catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            #Write-Host " Error con la ruta" -ForegroundColor DarkRed
            echo 100 > .\scripts\obj\gui\docs\compccc.txt
        }

