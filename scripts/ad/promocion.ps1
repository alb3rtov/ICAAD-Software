Write-Output "";
$dominio = read-host " Introduzca nombre de dominio (ej: ASIR.LOCAL)"
Write-Output "";
$contrasena = read-host -AsSecureString " Contraseña para la cuenta administrador (modo seguro)"
Write-Output "";

if ($contrasena.Length -gt 7) {
try {

Install-ADDSForest -DomainName $dominio -SafeModeAdministratorPassword $contrasena -Confirm:$false


}

catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Error con alguno de los datos introducidos" -ForegroundColor DarkRed
        }


}

else {
     Write-Host " Introduzca una contraseña con al menos 8 carácteres" -ForegroundColor DarkRed
}