#Write-Output "";
#$recursocompartido = read-host " Nombre del recurso a compartir"

$datos1 = Get-Content ".\scripts\obj\gui\docs\compartircarpetagui1.txt" #nombre del recurso

$datos2 = Get-Content ".\scripts\obj\gui\docs\compartircarpetagui2.txt" # ruta

$datos3 = Get-Content ".\scripts\obj\gui\docs\compartircarpetagui3.txt" # cuenta

$datos4 = Get-Content ".\scripts\obj\gui\docs\compartircarpetagui4.txt" #permiso

net share > .\scripts\obj\gui\docs\recursos.txt

$contador = (Get-Content .\scripts\obj\gui\docs\recursos.txt | where{$_-match"$datos1"}).Count

if ($contador -eq 0) {

    #Write-Output "";
    #$ruta = read-host " Ruta del recurso a compartir"

        if ($datos2.Length -ne 0) {

            $comprobarruta = Test-Path $datos2
            #$ruta.Length
            net user > .\scripts\obj\gui\docs\usuarios.txt

                if ($comprobarruta -eq $True ) {
                    #Write-Output "";
                    #Write-Host " [*] Usuarios encontrados" -ForegroundColor Yellow

                    #Get-ADUser -Filter * | Format-Table Name,DistinguishedName

                   # Write-Output "";
                   # $cuenta = read-host " Nombre de la cuenta (usuario/grupo) al que desea dar permisos"

                   

                    $contador2 = (Get-Content .\scripts\obj\gui\docs\usuarios.txt | where{$_-match"$datos3"}).Count

                        if ($contador2 -ne 0) {

                            #Write-Output "";
                            #$permiso = read-host " Tipo de permiso que desea conceder a $cuenta (R/C/F)"
                            #Write-Output "";
                            #$descripcion = read-host " Descripción del recurso"
                            #Write-Output "";
                            #$confirmacion = read-host " ¿Desea que el recurso sea oculto? (s/n)



                                    if ($datos4 -eq "1") {

                                    New-SmbShare  -Name "$datos1" -Path "$datos2" -ReadAccess "$datos3" | Out-Null

                                    #Write-Host " $recursocompartido ha sido compartido" -ForegroundColor DarkGreen
                                    #Write-Output "";

                                    echo 0 > .\scripts\obj\gui\docs\compcrc.txt
                                    }

                                    elseif ($datos4 -eq "2") {

                                    #echo "New-SmbShare -Name "$recursocompartido" -Path "$ruta" -$permdef "$cuenta"  "
    
                                    New-SmbShare -Name "$datos1" -Path "$datos2" -ChangeAccess "$datos3" | Out-Null
    
                                    #Write-Host " $recursocompartido ha sido compartido" -ForegroundColor DarkGreen
                                    #Write-Output "";

                                    echo 0 > .\scripts\obj\gui\docs\compcrc.txt
                                    }

                                    elseif ($datos4 -eq "3") {


                                    New-SmbShare  -Name "$datos1" -Path "$datos2" -FullAccess "$datos3" | Out-Null

                                    echo 0 > .\scripts\obj\gui\docs\compcrc.txt
    
                                   # Write-Host " $recursocompartido ha sido compartido" -ForegroundColor DarkGreen
                                   # Write-Output "";
                                   # Write-Output "";
                                    }

                                    else {
                                    #Write-Output "";
                                    #Write-Host " Introduzca un valor válido (R/C/F)" -ForegroundColor DarkRed
                                    echo 100 > .\scripts\obj\gui\docs\compcrc.txt

                                    }
  
                                


                        }

                        else {
                        #Write-Output "";
                        #Write-Host " La cuenta $cuenta no existe" -ForegroundColor DarkRed
                        echo 100 > .\scripts\obj\gui\docs\compcrc.txt

                        }


                }

                else {
               # Write-Output "";
               # Write-Host " El directorio $ruta no existe" -ForegroundColor DarkRed
                echo 100 > .\scripts\obj\gui\docs\compcrc.txt

                }

        }

        else {
        #Write-Output "";
        #Write-Host " Introduca alguna ruta de recurso compartido " -ForegroundColor DarkRed
        echo 100 > .\scripts\obj\gui\docs\compcrc.txt

        }
}

else {
#Write-Output "";
#Write-Host " $recursocompartido ya existe o el nombre debe ser más de 4 caracteres" -ForegroundColor DarkRed

echo 100 > .\scripts\obj\gui\docs\compcrc.txt

}