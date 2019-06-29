
Write-Output "";
$nombreUO = read-host " Buscar unidad organizativa"
Write-Output "";

        try {
            Get-ADOrganizationalUnit -Filter "Name -like '$nombreUO'" > .\scripts\obj\docs\buscaruo.txt
            
            $contador = (Get-Content .\scripts\obj\docs\buscaruo.txt | where{$_-match"$nombreUO"}).Count

            if ($contador -ne 0) {
                Get-ADOrganizationalUnit -Filter "Name -like '$nombreUO'"
            }

            else {
                Write-Host " La unidad organizativa $nombreUO no existe" -ForegroundColor DarkRed
            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Debe introducir algún dato" -ForegroundColor DarkRed
        }




