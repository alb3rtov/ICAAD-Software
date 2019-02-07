﻿#Write-Output "";
#Write-Host " [*] Por defecto, la ruta de generación del archivo CSV es el directorio de este programa" -ForegroundColor Yellow
#Write-Output "";
#$ruta = read-host " Ruta y nombre donde generar el CSV (Ej: C:\objetosad.csv)"
#Write-Output "";

$datos = Get-Content ".\scripts\obj\gui\docs\exportarcsv.txt"

$csv = ".csv"

$contador = (Get-Content ".\scripts\obj\gui\docs\exportarcsv.txt" | where{$_-match"$csv"}).Count

#$ruta > .\scripts\obj\docs\exportgrupo.txt 

#$contador

#$datos

#$contador = (Get-Content .\scripts\obj\docs\exportgrupo.txt | where{$_-match"$csv"}).Count


if ($contador -ne 0) {

try {
Get-ADObject -Filter * -Properties * | Export-Csv $datos
#Write-Host " $ruta generado correctamente" -ForegroundColor DarkGreen
echo 0 > .\scripts\obj\gui\docs\compcsv.txt
}

catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            #Write-Host " Error con la ruta" -ForegroundColor DarkRed
            echo 100 > .\scripts\obj\gui\docs\compcsv.txt
        }

}

else {


  #Write-Host " Debe añadir la extensión .csv" -ForegroundColor DarkRed
  echo 100 > .\scripts\obj\gui\docs\compcsv.txt
}