
#Write-Output "";
#$nombreGPO = read-host " Nombre de la GPO"
#Write-Output "";
#$key = read-host " Introduzca la KEY de registro"
#Write-Output "";
#$valor = read-host " Introduca el nombre de valor de registro (Ej: ScreenSaveTimeOut)"
#Write-Output "";


$datos1 = Get-Content ".\scripts\obj\gui\docs\configuraciongpogui1.txt"

$datos2 = Get-Content ".\scripts\obj\gui\docs\configuraciongpogui2.txt"

$datos3 = Get-Content ".\scripts\obj\gui\docs\configuraciongpogui3.txt"



echo "" > .\scripts\obj\gui\docs\compcongpo.txt

Get-GPO -all >  .\scripts\obj\gui\docs\configuraciongpogui4.txt

$contador1 = (Get-Content .\scripts\obj\gui\docs\configuraciongpogui4.txt | where{$_-match"$datos1"}).Count


if ($contador1 -ne 0) {

   try {

            Set-GPRegistryValue -Name "$datos1" -Key "$datos2" -ValueName $datos3 -Type DWord -Value 0 | Out-Null

           
            #Write-Host " $nombreGPO configurada correctamente" -ForegroundColor DarkGreen
            echo 0 > .\scripts\obj\gui\docs\compcongpo.txt
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
           
           # Write-Host " Error con alguno de los datos introducidos" -ForegroundColor DarkRed
           echo 100 > .\scripts\obj\gui\docs\compcongpo.txt
        }
    }
   


else {
 
            #Write-Host " La GPO $nombreGPO no existe" -ForegroundColor DarkRed
            echo 100 > .\scripts\obj\gui\docs\compcongpo.txt
}