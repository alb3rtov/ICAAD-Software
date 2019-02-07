#Write-Output "";
#Write-Host " [*] Por defecto, la ruta de generación del archivo CSV es el directorio de este programa" -ForegroundColor Yellow
#Write-Output "";
#$ruta = read-host " Ruta y nombre donde generar el CSV (Ej: C:\objetosad.csv)"
#Write-Output "";

$datos = Get-Content ".\scripts\obj\gui\docs\buscarrcgui.txt"


net share > .\scripts\obj\gui\docs\recursos4.txt

$contador = (Get-Content .\scripts\obj\gui\docs\recursos4.txt | where{$_-match"$datos"}).Count

net share $datos > .\scripts\obj\gui\docs\buscarrcgui1.txt

if ($contador -ne 0) {

try {

#Write-Host " $ruta generado correctamente" -ForegroundColor DarkGreen
echo 0 > .\scripts\obj\gui\docs\compbrc.txt
}

catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            #Write-Host " Error con la ruta" -ForegroundColor DarkRed
            echo 100 > .\scripts\obj\gui\docs\compbrc.txt
        }

}

else {

echo 100 > .\scripts\obj\gui\docs\compbrc.txt

}