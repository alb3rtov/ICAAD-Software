#Write-Output "";
#$nombreUsuario = read-host " Nombre de usuario para reset de contraseña"
#Write-Output "";
#$contrasena1 = read-host -AsSecureString " Nueva contraseña"
#Write-Output "";
#$contrasena2 = read-host -AsSecureString " Repita nueva contraseña"
#Write-Output "";


$datos1 = Get-Content ".\scripts\obj\gui\docs\resetpassword1.txt"

$datos2 = Get-Content ".\scripts\obj\gui\docs\resetpassword2.txt"

$datos3 = Get-Content ".\scripts\obj\gui\docs\resetpassword3.txt"

#$Ptr1 = [System.Runtime.InteropServices.Marshal]::SecureStringToCoTaskMemUnicode($datos2)
#$result1 = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($Ptr1)
#[System.Runtime.InteropServices.Marshal]::ZeroFreeCoTaskMemUnicode($Ptr1)
#$result1

#$Ptr2 = [System.Runtime.InteropServices.Marshal]::SecureStringToCoTaskMemUnicode($datos3)
#$result2 = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($Ptr2)
#[System.Runtime.InteropServices.Marshal]::ZeroFreeCoTaskMemUnicode($Ptr2)
#$result2

#if ($result1 -eq $result2) {
if ($datos2 -eq $datos3) {

try {

    Get-ADUser -Filter "Name -eq '$datos1'" > .\scripts\obj\gui\docs\resetpassword4.txt

}

catch [System.Management.Automation.RuntimeException] {
      
        if ($_.Exception.Message -ilike "Error"){
        }

    #Write-Host " Error, algún dato es erróneo" -ForegroundColor DarkRed
    #Write-Output "";

}

$contador = (Get-Content .\scripts\obj\gui\docs\resetpassword4.txt | where{$_-match"$datos1"}).Count


    if ($contador -ne 0) {
    
        try {

                Get-ADUser -Filter "Name -eq '$datos1'" | Set-ADAccountPassword -Reset -NewPassword (ConvertTo-SecureString -AsPlainText "$datos3" -Force)

                #Write-Host " Contraseña restablecida al usuario $datos1" -ForegroundColor DarkGreen
            
                echo 0 > .\scripts\obj\gui\docs\compresetp.txt

            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            #Write-Host " Error, algún dato es erróneo" -ForegroundColor DarkRed

            echo 100 > .\scripts\obj\gui\docs\compresetp.txt
        }
    }

    else {
        #Write-Host " El usuario $nombreUsuario no existe" -ForegroundColor DarkRed

        echo 100 > .\scripts\obj\gui\docs\compresetp.txt
    }

   
}

else {


        #Write-Host " Las contraseñas no coinciden" -ForegroundColor DarkRed

        echo 100 > .\scripts\obj\gui\docs\compresetp.txt
}