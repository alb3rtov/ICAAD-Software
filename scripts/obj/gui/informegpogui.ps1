
#Write-Output "";
#Write-Host " [*] La ruta de generación del informe será $Home" -ForegroundColor Yellow

#Write-Output "";
#$nombreGPO = read-host " Nombre de la GPO para generar informe"
#Write-Output "";


$datos = Get-Content ".\scripts\obj\gui\docs\informegpogui.txt"

Get-GPO -all >  .\scripts\obj\gui\docs\informegpogui.txt

$contador1 = (Get-Content .\scripts\obj\gui\docs\informegpogui.txt | where{$_-match"$datos"}).Count


if ($contador1 -ne 0) {

   try {

            Get-GPO -Name "$datos" | Get-GPOReport -ReportType HTML -Path $Home\informe_$datos.html > /null

            echo 0 > .\scripts\obj\gui\docs\compigpo.txt

           
           # Write-Host " Informe de $nombreGPO generado correctamente" -ForegroundColor DarkGreen
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
           
            #Write-Host " Error con alguno de los datos introducidos" -ForegroundColor DarkRed

            echo 100 > .\scripts\obj\gui\docs\compigpo.txt
        }
    }
   


else {
 
            #Write-Host " La GPO $nombreGPO no existe" -ForegroundColor DarkRed

            echo 100 > .\scripts\obj\gui\docs\compigpo.txt
}