Write-Output "";
$nombreEquipo = read-host " Nuevo nombre para el equipo"
Write-Output "";

try {

Rename-Computer -NewName $nombreEquipo

}

catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Error, introduzca un nombre correcto" -ForegroundColor DarkRed
        }