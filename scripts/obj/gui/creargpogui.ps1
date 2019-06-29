#Write-Output "";
#Write-Host " [*] Por defecto, la GPO se creará en 'Objetos de directiva de grupo'" -ForegroundColor Yellow
#Write-Output "";
#$nombreGPO = read-host " Nombre de la nueva GPO"
#Write-Output "";



$datos = Get-Content ".\scripts\obj\gui\docs\creargpogui.txt"

Get-GPO -all >  .\scripts\obj\gui\docs\creargpogui1.txt

$contador1 = (Get-Content .\scripts\obj\gui\docs\creargpogui1.txt | where{$_-match"$datos"}).Count


if ($contador1 -eq 0) {

   
   try {

            new-gpo -name "$datos" > /null

           
            #Write-Host " GPO $nombreGPO creada correctamente" -ForegroundColor DarkGreen
            echo 0 > .\scripts\obj\gui\docs\compcgpo.txt
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
           
           # Write-Host " Error con alguno de los datos introducidos" -ForegroundColor DarkRed

           echo 100 > .\scripts\obj\gui\docs\compcgpo.txt
        }
    }
   


else {
 
          #  Write-Host " La GPO $nombreGPO ya existe" -ForegroundColor DarkRed

            echo 100 > .\scripts\obj\gui\docs\compcgpo.txt
}