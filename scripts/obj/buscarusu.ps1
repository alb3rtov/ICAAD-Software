
Write-Output "";
$nombreUsuario = read-host " Buscar usuario"
Write-Output "";

        try {
            Get-ADUser -Filter "Name -eq '$nombreUsuario'" > .\scripts\obj\docs\buscarusu.txt
            
            $contador = (Get-Content .\scripts\obj\docs\buscarusu.txt | where{$_-match"$nombreUsuario"}).Count

            if ($contador -ne 0) {
                Get-ADUser -Filter "Name -eq '$nombreUsuario'"
            }

            else {
                Write-Host " El usuario $nombreUsuario no existe" -ForegroundColor DarkRed
            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Debe introducir algún dato" -ForegroundColor DarkRed
        }




