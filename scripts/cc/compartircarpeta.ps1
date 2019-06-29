Write-Output "";
$recursocompartido = read-host " Nombre del recurso a compartir"

net share > .\scripts\cc\docs\recurso.txt

net user > .\scripts\cc\docs\usuarios.txt

$contador = (Get-Content .\scripts\cc\docs\recurso.txt | where{$_-match"$recursocompartido"}).Count

if ($contador -eq 0 -and $recursocompartido.Length -gt 4) {

    Write-Output "";
    $ruta = read-host " Ruta del recurso a compartir"

        if ($ruta.Length -ne 0) {

            $comprobarruta = Test-Path $ruta
            #$ruta.Length

                if ($comprobarruta -eq $True ) {
                    Write-Output "";
                    Write-Host " [*] Usuarios encontrados" -ForegroundColor Yellow

                    Get-ADUser -Filter * | Format-Table Name,DistinguishedName

                    Write-Output "";
                    $cuenta = read-host " Nombre de la cuenta (usuario/grupo) al que desea dar permisos"

                    

                    $contador2 = (Get-Content .\scripts\cc\docs\usuarios.txt | where{$_-match"$cuenta"}).Count

                        if ($contador2 -ne 0) {

                            Write-Output "";
                            $permiso = read-host " Tipo de permiso que desea conceder a $cuenta (R/C/F)"
                            Write-Output "";
                            $descripcion = read-host " Descripción del recurso"
                            Write-Output "";
                            $confirmacion = read-host " ¿Desea que el recurso sea oculto? (s/n)"



                                if ($confirmacion -eq "s" -or $confirmacion -eq "S") {

                                    $dolar = "$"

                                    $rcdef = $recursocompartido + $dolar

                                    if ($permiso -eq "R" -or $permiso -eq "r") {

                                    New-SmbShare  -Name "$rcdef" -Path "$ruta" -ReadAccess "$cuenta" -Description "$descripcion"

                                    Write-Host " $recursocompartido ha sido compartido" -ForegroundColor DarkGreen
                                    Write-Output "";
                                    }

                                    elseif ($permiso -eq "C" -or $permiso -eq "c") {
    
                                        New-SmbShare  -Name "$rcdef" -Path "$ruta" -ChangeAccess "$cuenta" -Description "$descripcion"   

                                        Write-Host " $recursocompartido ha sido compartido" -ForegroundColor DarkGreen
                                        Write-Output "";
                                    }

                                    elseif ($permiso -eq "F" -or $permiso -eq "f" ) {
        

                                        New-SmbShare  -Name "$rcdef" -Path "$ruta" -FullAccess "$cuenta" -Description "$descripcion"   
    
                                        Write-Host " $recursocompartido ha sido compartido" -ForegroundColor DarkGreen
                                          Write-Output "";
                                    }

                                    else {
    
                                        Write-Host " Introduzca un valor válido (R/C/F)" -ForegroundColor DarkRed
    
                                        Write-Host " $recursocompartido ha sido compartido" -ForegroundColor DarkGreen
                                        Write-Output "";
                                    }



                                }



                                else {



                                    if ($permiso -eq "R" -or $permiso -eq "r") {

                                    $permdef = "-ReadAccess"

                                    New-SmbShare  -Name "$recursocompartido" -Path "$ruta" -ReadAccess "$cuenta" -Description "$descripcion"

                                    Write-Host " $recursocompartido ha sido compartido" -ForegroundColor DarkGreen
                                    Write-Output "";
                                    }

                                    elseif ($permiso -eq "C" -or $permiso -eq "c") {

                                    #echo "New-SmbShare -Name "$recursocompartido" -Path "$ruta" -$permdef "$cuenta"  "
    
                                    New-SmbShare -Name "$recursocompartido" -Path "$ruta" -ChangeAccess "$cuenta" -Description "$descripcion"
    
                                    Write-Host " $recursocompartido ha sido compartido" -ForegroundColor DarkGreen
                                    Write-Output "";
                                    }

                                    elseif ($permiso -eq "F" -or $permiso -eq "f" ) {


                                    New-SmbShare  -Name "$recursocompartido" -Path "$ruta" -FullAccess "$cuenta" -Description "$descripcion"   
    
                                    Write-Host " $recursocompartido ha sido compartido" -ForegroundColor DarkGreen
                                    Write-Output "";
                                    Write-Output "";
                                    }

                                    else {
                                    Write-Output "";
                                    Write-Host " Introduzca un valor válido (R/C/F)" -ForegroundColor DarkRed

                                    }
  
                                }


                        }

                        else {
                        Write-Output "";
                        Write-Host " La cuenta $cuenta no existe" -ForegroundColor DarkRed

                        }


                }

                else {
                Write-Output "";
                Write-Host " El directorio $ruta no existe" -ForegroundColor DarkRed

                }

        }

        else {
        Write-Output "";
        Write-Host " Introduca alguna ruta de recurso compartido " -ForegroundColor DarkRed

        }
}

else {
Write-Output "";
Write-Host " $recursocompartido ya existe o el nombre debe ser más de 4 caracteres" -ForegroundColor DarkRed

}