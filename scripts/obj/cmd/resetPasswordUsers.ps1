Write-Output "";
$userName = read-host " Name of the user to reset the password"
Write-Output "";
$password1 = read-host -AsSecureString " New password"
Write-Output "";
$password2 = read-host -AsSecureString " Repeat the new password"
Write-Output "";

$Ptr1 = [System.Runtime.InteropServices.Marshal]::SecureStringToCoTaskMemUnicode($password1)
$result1 = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($Ptr1)
[System.Runtime.InteropServices.Marshal]::ZeroFreeCoTaskMemUnicode($Ptr1)
#$result1

$Ptr2 = [System.Runtime.InteropServices.Marshal]::SecureStringToCoTaskMemUnicode($password2)
$result2 = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($Ptr2)
[System.Runtime.InteropServices.Marshal]::ZeroFreeCoTaskMemUnicode($Ptr2)
#$result2


echo "" > .\scripts\obj\cmd\temp\resetPasswordUsers.txt

if ($result1 -eq $result2) {


try {

    Get-ADUser -Filter "Name -eq '$userName'" > .\scripts\obj\cmd\temp\resetPasswordUsers.txt

}

catch [System.Management.Automation.RuntimeException] {

        if ($_.Exception.Message -ilike "Error"){
        }

    Write-Host " Error, some data are wrong" -ForegroundColor DarkRed
    Write-Output "";

}

$counter = (Get-Content .\scripts\obj\cmd\temp\resetPasswordUsers.txt | where{$_-match"$userName"}).Count


    if ($counter -ne 0) {

        try {

                Get-ADUser -Filter "Name -eq '$userName'" | Set-ADAccountPassword -Reset -NewPassword (ConvertTo-SecureString -AsPlainText "$password2" -Force)

                Write-Host " The password of $userName has been reseted" -ForegroundColor DarkGreen


            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Error, some data are wrong" -ForegroundColor DarkRed
        }
    }

    else {
        Write-Host " The user $userName doesn't exist" -ForegroundColor DarkRed
    }


}

else {

        Write-Host " Las contraseñas no coinciden" -ForegroundColor DarkRed

}
