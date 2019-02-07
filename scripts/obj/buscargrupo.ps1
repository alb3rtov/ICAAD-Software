
Write-Output "";
$nombreGrupo = read-host " Buscar usuario"
Write-Output "";

        try {
            Get-ADGroup -Filter "Name -eq '$nombreGrupo'" > .\scripts\obj\docs\buscargrupo.txt
            
            $contador = (Get-Content .\scripts\obj\docs\buscargrupo.txt | where{$_-match"$nombreGrupo"}).Count

            if ($contador -ne 0) {
                Get-ADGroup -Filter "Name -eq '$nombreGrupo'"
            }

            else {
                Write-Host " El usuario $nombreGrupo no existe" -ForegroundColor DarkRed
            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Debe introducir algún dato" -ForegroundColor DarkRed
        }




