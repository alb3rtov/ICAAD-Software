Write-Output "";
Write-Host " [*] Por defecto, la GPO se creará en 'Objetos de directiva de grupo'" -ForegroundColor Yellow
Write-Output "";
$nombreGPO = read-host " Nombre de la nueva GPO"
Write-Output "";


Get-GPO -all >  .\scripts\obj\docs\borrargpo.txt

$contador1 = (Get-Content .\scripts\obj\docs\borrargpo.txt | where{$_-match"$nombreGPO"}).Count


if ($contador1 -eq 0) {

   
   try {

            new-gpo -name "$nombreGPO" > /null

           
            Write-Host " GPO $nombreGPO creada correctamente" -ForegroundColor DarkGreen
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
           
            Write-Host " Error con alguno de los datos introducidos" -ForegroundColor DarkRed
        }
    }
   


else {
 
            Write-Host " La GPO $nombreGPO ya existe" -ForegroundColor DarkRed
}