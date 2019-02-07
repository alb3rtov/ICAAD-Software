# Script to create Active Directory accounts
# v2 9/12/2012
# Todd Klindt
# http://www.toddklindt.com
#Write-Output "";
#$archivo = read-host " Nombre del archivo csv (C:\users.csv)"

$datos = Get-Content ".\scripts\obj\gui\docs\usumascsvgui.txt"

# Add the Active Directory bits and not complain if they're already there
Import-Module ActiveDirectory -ErrorAction SilentlyContinue

# set default password
# change pass@word1 to whatever you want the account passwords to be
$defpassword = (ConvertTo-SecureString "pass@word1" -AsPlainText -force)

# Get domain DNS suffix
$dnsroot = '@' + (Get-ADDomain).dnsroot

# Import the file with the users. You can change the filename to reflect your file
try {
$users = Import-Csv $datos

}

catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            #Write-Output "";
            #Write-Host " Introduzca un fichero .csv correcto" -ForegroundColor DarkRed

            echo 100 > .\scripts\obj\gui\docs\compusucsv.txt
        }


foreach ($user in $users) {
        if ($user.manager -eq "") # In case it's a service account or a boss
            {
                try {
                    New-ADUser -SamAccountName $user.SamAccountName -Name ($user.FirstName + " " + $user.LastName) `
                    -DisplayName ($user.FirstName + " " + $user.LastName) -GivenName $user.FirstName -Surname $user.LastName `
                    -EmailAddress ($user.SamAccountName + $dnsroot) -UserPrincipalName ($user.SamAccountName + $dnsroot) `
                    -Title $user.title -Enabled $true -ChangePasswordAtLogon $false -PasswordNeverExpires  $true `
                    -AccountPassword $defpassword -PassThru ` | Out-Null

                    echo 0 > .\scripts\obj\gui\docs\compusucsv.txt

                    }
                catch [System.Object]
                    {
                        #Write-Output "No pudo crear el usuario $($user.SamAccountName), $_"
                        echo 10000 > .\scripts\obj\gui\docs\compusucsv.txt
                    }
            }
            else
             {
                try {
                    New-ADUser -SamAccountName $user.SamAccountName -Name ($user.FirstName + " " + $user.LastName) `
                    -DisplayName ($user.FirstName + " " + $user.LastName) -GivenName $user.FirstName -Surname $user.LastName `
                    -EmailAddress ($user.SamAccountName + $dnsroot) -UserPrincipalName ($user.SamAccountName + $dnsroot) `
                    -Title $user.title -manager $user.manager `
                    -Enabled $true -ChangePasswordAtLogon $false -PasswordNeverExpires  $true `
                    -AccountPassword $defpassword -PassThru `  | Out-Null

                    echo 0 > .\scripts\obj\gui\docs\compusucsv.txt
                    }
                catch [System.Object]
                    {
                       # Write-Output "No pudo crear el usuario $($user.SamAccountName), $_"
                       echo 10000 > .\scripts\obj\gui\docs\compusucsv.txt
                    }
             }

   }


