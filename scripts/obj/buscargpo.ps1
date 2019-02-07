
Write-Output "";
$nombreGPO = read-host " Nombre de la nueva GPO"
Write-Output "";


Get-GPO -all >  .\scripts\obj\docs\buscargpo.txt

$contador1 = (Get-Content .\scripts\obj\docs\buscargpo.txt | where{$_-match"$nombreGPO"}).Count


if ($contador1 -ne 0) {

   
   try {

            Get-GPO -Name "$nombreGPO"

           
          
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
           
            Write-Host " Error con alguno de los datos introducidos" -ForegroundColor DarkRed
        }
    }
   


else {
 
            Write-Host " La GPO $nombreGPO no existe" -ForegroundColor DarkRed
}