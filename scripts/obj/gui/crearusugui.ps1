#Write-Output "";
#Write-Host " [*] Los usuarios se crean automáticamente deshabilitados por seguridad de la contraseña" -ForegroundColor Yellow
#Write-Output "";
#Write-Host " [*] Utiliza la 5º opcion del menú para habilitar/deshabilitar usuarios de AD" -ForegroundColor Yellow
#Write-Output "";
#$nombreUsuario = read-host " Nombre de usuario a crear"
#Write-Output "";
#$contrasena = read-host -AsSecureString " Contraseña"
#Write-Output "";


$datos1 = Get-Content ".\scripts\obj\gui\docs\crearusugui1.txt"

$datos2 = Get-Content ".\scripts\obj\gui\docs\crearusugui2.txt"


Get-ADUser -Filter "Name -eq '$datos1'" > .\scripts\obj\gui\docs\crearusugui3.txt


$contador = (Get-Content .\scripts\obj\gui\docs\crearusugui3.txt | where{$_-match"$datos1"}).Count


#$confirmacion = read-host " ¿Desea especificar una unidad organizativa (por defecto: CN=Users)? (s/n)"
#Write-Output "";


#Write-Output "";

    if ($contador -eq 0) {
    
        try {

            #echo $contador2


                #echo $tag

                New-ADUser -Name $datos1 -AccountPassword (ConvertTo-SecureString -AsPlainText "$datos2" -Force) -Enable $false

                #Write-Host " Usuario $nombreUsuario creado correctamente en$tag" -ForegroundColor DarkGreen
                
                 echo 0 > .\scripts\obj\gui\docs\compcusu.txt

            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            #Write-Host " Error, algún dato es erróneo" -ForegroundColor DarkRed

             echo 100 > .\scripts\obj\gui\docs\compcusu.txt


        }
    }

    else {
       # Write-Host " El usuario $nombreUsuario ya está creado" -ForegroundColor DarkRed

        echo 100 > .\scripts\obj\gui\docs\compcusu.txt
    }

    