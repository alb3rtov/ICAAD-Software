Write-Output "";
$nombreGPO = read-host " Nombre de la GPO a borrar"
Write-Output "";


Get-GPO -all >  .\scripts\obj\docs\borrargpo.txt

$contador1 = (Get-Content .\scripts\obj\docs\borrargpo.txt | where{$_-match"$nombreGPO"}).Count


if ($contador1 -ne 0) {

   
   try {

            Remove-GPO -Name "$nombreGPO" > /null

           
            Write-Host " GPO $nombreGPO borrada correctamente" -ForegroundColor DarkGreen
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