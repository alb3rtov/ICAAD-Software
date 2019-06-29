
#Write-Output "";
#$nombreGPO = read-host " Nombre de la nueva GPO"
#Write-Output "";



$datos = Get-Content ".\scripts\obj\gui\docs\buscargpogui.txt"

Get-GPO -all >  .\scripts\obj\gui\docs\buscargpogui.txt

$contador1 = (Get-Content .\scripts\obj\gui\docs\buscargpogui.txt | where{$_-match"$datos"}).Count


if ($contador1 -ne 0) {

   
   try {

            Get-GPO -Name "$datos" > .\scripts\obj\gui\docs\buscargpogui.txt

            echo 0 > .\scripts\obj\gui\docs\compbgpo.txt

           
          
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
           
            #Write-Host " Error con alguno de los datos introducidos" -ForegroundColor DarkRed

            echo 100 > .\scripts\obj\gui\docs\compbgpo.txt
        }
    }
   


else {
 
            #Write-Host " La GPO $nombreGPO no existe" -ForegroundColor DarkRed

            echo 100 > .\scripts\obj\gui\docs\compbgpo.txt
}