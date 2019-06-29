
Write-Output "";
Write-Host " [*] Los usuarios se crean automáticamente deshabilitados por seguridad de la contraseña" -ForegroundColor Yellow
Write-Output "";
Write-Host " [*] Utiliza la 5º opcion del menú para habilitar/deshabilitar usuarios de AD" -ForegroundColor Yellow
Write-Output "";
$nombreUsuario = read-host " Nombre de usuario a crear"
Write-Output "";
$contrasena = read-host -AsSecureString " Contraseña"
Write-Output "";

echo "" > .\scripts\obj\docs\crearusu2.txt

try {

    Get-ADUser -Filter "Name -eq '$nombreUsuario'" > .\scripts\obj\docs\crearusu1.txt

}

catch [System.Management.Automation.RuntimeException] {
      
        if ($_.Exception.Message -ilike "Error"){
        }

    Write-Host " Error, algún dato es erróneo" -ForegroundColor DarkRed
    Write-Output "";

}

$contador = (Get-Content .\scripts\obj\docs\crearusu1.txt | where{$_-match"$nombreUsuario"}).Count


$confirmacion = read-host " ¿Desea especificar una unidad organizativa (por defecto: CN=Users)? (s/n)"
Write-Output "";

if ($confirmacion -eq "S" -or $confirmacion -eq "s") {

Write-Host " [*] Unidades organizativas encontradas" -ForegroundColor Yellow

Get-ADOrganizationalUnit -Filter 'Name -like "*"' | Format-Table Name,DistinguishedName -A

$nombreUO = read-host " Nombre de la unidad organizativa"
Write-Output "";

    if ($contador -eq 0) {
    
        try {
            Get-ADOrganizationalUnit -Filter "Name -like '$nombreUO'" > .\scripts\obj\docs\crearusu2.txt

            $contador2 = (Get-Content .\scripts\obj\docs\crearusu2.txt | where{$_-match"$nombreUO"}).Count

            #echo $contador2

            if ($contador2 -ne 0) {

                $string = Get-Content .\scripts\obj\docs\crearusu2.txt | where{$_-match"$nombreUO"}

                $tag = $string.Split(":",4)[1]

                #echo $tag

                New-ADUser -Name $nombreUsuario -AccountPassword (ConvertTo-SecureString -AsPlainText "$contrasena" -Force) -Enable $false -Path $tag

                Write-Host " Usuario $nombreUsuario creado correctamente en$tag" -ForegroundColor DarkGreen
            }

            else {
                Write-Host " La unidad organizativa $nombreUO no existe" -ForegroundColor DarkRed
            }

            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Error, algún dato es erróneo" -ForegroundColor DarkRed
        }
    }

    else {
        Write-Host " El usuario $nombreUsuario ya está creado" -ForegroundColor DarkRed
    }

    
 }


#$longitud = $nombreUO.Length 

else {

    if ($contador -eq 0) {
    
        try {
            New-ADUser -Name $nombreUsuario -AccountPassword (ConvertTo-SecureString -AsPlainText "$contrasena" -Force) -Enable $false
            Write-Host " Usuario $nombreUsuario creado correctamente en CN=Users,DC=ASIR,DC=TEST" -ForegroundColor DarkGreen
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Error, algún dato es erróneo" -ForegroundColor DarkRed
        }
    }
    else {
        Write-Host " El usuario $nombreUsuario ya está creado" -ForegroundColor DarkRed
    }

}
