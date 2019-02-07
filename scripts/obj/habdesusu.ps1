
Write-Output "";
$confirmacion = read-host " ¿Desea habilitar o deshabilitar un usuario? (h/d)"
Write-Output "";

echo "" > .\scripts\obj\docs\habdesusu.txt

if ($confirmacion -eq "h" -or $confirmacion -eq "H") {
    $nombreUsuario1 = read-host " Eliga un nombre de usuario para habilitar"
    Write-Output "";

    
        try {
            Get-ADUser -Filter "Name -eq '$nombreUsuario1'" > .\scripts\obj\docs\habdesusu.txt
            
            $contador = (Get-Content .\scripts\obj\docs\habdesusu.txt | where{$_-match"$nombreUsuario1"}).Count

            if ($contador -ne 0) {

                Enable-ADAccount -Identity $nombreUsuario1
                Write-Host " El usuario $nombreUsuario1 ha sido habilitado" -ForegroundColor DarkGreen
            }

            else {
                Write-Host " El usuario $nombreUsuario1 no existe" -ForegroundColor DarkRed
            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Debe introducir algún dato" -ForegroundColor DarkRed
        }

}

ElseIf ($confirmacion -eq "d" -or $confirmacion -eq "D") {
    $nombreUsuario2 = read-host " Eliga un nombre de usuario para deshabilitar"
    Write-Output "";

    
        try {
            Get-ADUser -Filter "Name -eq '$nombreUsuario2'" > .\scripts\obj\docs\habdesusu.txt
            
            $contador = (Get-Content .\scripts\obj\docs\habdesusu.txt | where{$_-match"$nombreUsuario2"}).Count

            #echo $contador

            if ($contador -ne 0) {

                Disable-ADAccount -Identity $nombreUsuario2
                Write-Host " El usuario $nombreUsuario2 ha sido deshabilitado" -ForegroundColor DarkGreen
            }

            else {
                Write-Host " El usuario $nombreUsuario2 no existe" -ForegroundColor DarkRed
            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Debe introducir algún dato" -ForegroundColor DarkRed
        }

}

else {
    Write-Host " Eliga una opción correcta" -ForegroundColor DarkRed
}




