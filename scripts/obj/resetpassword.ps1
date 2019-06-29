Write-Output "";
$nombreUsuario = read-host " Nombre de usuario para reset de contraseña"
Write-Output "";
$contrasena1 = read-host -AsSecureString " Nueva contraseña"
Write-Output "";
$contrasena2 = read-host -AsSecureString " Repita nueva contraseña"
Write-Output "";

$Ptr1 = [System.Runtime.InteropServices.Marshal]::SecureStringToCoTaskMemUnicode($contrasena1)
$result1 = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($Ptr1)
[System.Runtime.InteropServices.Marshal]::ZeroFreeCoTaskMemUnicode($Ptr1)
#$result1

$Ptr2 = [System.Runtime.InteropServices.Marshal]::SecureStringToCoTaskMemUnicode($contrasena2)
$result2 = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($Ptr2)
[System.Runtime.InteropServices.Marshal]::ZeroFreeCoTaskMemUnicode($Ptr2)
#$result2


echo "" > .\scripts\obj\docs\resetpassword.txt

if ($result1 -eq $result2) {


try {

    Get-ADUser -Filter "Name -eq '$nombreUsuario'" > .\scripts\obj\docs\resetpassword.txt

}

catch [System.Management.Automation.RuntimeException] {
      
        if ($_.Exception.Message -ilike "Error"){
        }

    Write-Host " Error, algún dato es erróneo" -ForegroundColor DarkRed
    Write-Output "";

}

$contador = (Get-Content .\scripts\obj\docs\resetpassword.txt | where{$_-match"$nombreUsuario"}).Count


    if ($contador -ne 0) {
    
        try {

                Get-ADUser -Filter "Name -eq '$nombreUsuario'" | Set-ADAccountPassword -Reset -NewPassword (ConvertTo-SecureString -AsPlainText "$contrasena2" -Force)

                Write-Host " Contraseña restablecida al usuario $nombreUsuario" -ForegroundColor DarkGreen
            

            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Error, algún dato es erróneo" -ForegroundColor DarkRed
        }
    }

    else {
        Write-Host " El usuario $nombreUsuario no existe" -ForegroundColor DarkRed
    }

   
}

else {

        Write-Host " Las contraseñas no coinciden" -ForegroundColor DarkRed

}