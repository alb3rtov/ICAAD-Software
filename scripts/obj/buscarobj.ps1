
Write-Output "";
$nombreObjecto = read-host " Buscar objeto"
Write-Output "";

        try {
            Get-ADObject -Filter "Name -eq '$nombreObjecto'" > .\scripts\obj\docs\buscarobj.txt
            
            $contador = (Get-Content .\scripts\obj\docs\buscarobj.txt | where{$_-match"$nombreObjecto"}).Count

            if ($contador -ne 0) {
                Get-ADObject -Filter "Name -eq '$nombreObjecto'"
            }

            else {
                Write-Host " El objeto $nombreObjecto no existe" -ForegroundColor DarkRed
            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Debe introducir algún dato" -ForegroundColor DarkRed
        }




