#Write-Output "";
#$nombreGPO = read-host " Nombre de la GPO a borrar"
#Write-Output "";



$datos = Get-Content ".\scripts\obj\gui\docs\borrargpogui.txt"


Get-GPO -all >  .\scripts\obj\docs\borrargpo.txt

$contador1 = (Get-Content .\scripts\obj\docs\borrargpo.txt | where{$_-match"$datos"}).Count


if ($contador1 -ne 0) {

   
   try {

            Remove-GPO -Name "$datos" > /null

           
            #Write-Host " GPO $nombreGPO borrada correctamente" -ForegroundColor DarkGreen
            echo 0 > .\scripts\obj\gui\docs\compbogpo.txt
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
           
           # Write-Host " Error con alguno de los datos introducidos" -ForegroundColor DarkRed
           echo 100 > .\scripts\obj\gui\docs\compbogpo.txt
        }
    }
   


else {
 
           # Write-Host " La GPO $nombreGPO no existe" -ForegroundColor DarkRed
           echo 100 > .\scripts\obj\gui\docs\compbogpo.txt
}