Write-Output "";
$sharedResource = read-host " Name of the shared resource"

net share > .\scripts\sr\cmd\temp\resource.txt

net user > .\scripts\sr\cmd\temp\users.txt

$counter = (Get-Content .\scripts\sr\cmd\temp\resource.txt | where{$_-match"$sharedResource"}).Count

if ($counter -eq 0 -and $sharedResource.Length -gt 4) {

    Write-Output "";
    $path = read-host " Path of the resource/directory to share"

        if ($path.Length -ne 0) {

            $checkPath = Test-Path $path
            #$ruta.Length

                if ($checkPath -eq $True ) {
                    Write-Output "";
                    Write-Host " [*] Users found" -ForegroundColor Yellow

                    Get-ADUser -Filter * | Format-Table Name,DistinguishedName

                    Write-Output "";
                    $account = read-host " Name of the account (user/group) to add permissions"



                    $counter2 = (Get-Content .\scripts\sr\cmd\temp\users.txt | where{$_-match"$account"}).Count

                        if ($counter2 -ne 0) {

                            Write-Output "";
                            $permission = read-host " Type of the permission that you want to add to $account (R/C/F)"
                            Write-Output "";
                            $description = read-host " Resource description"
                            Write-Output "";
                            $confirmation = read-host " ¿Do you want that the resource be hidden? (y/n)"



                                if ($confirmation -eq "y" -or $confirmation -eq "Y") {

                                    $dollar = "$"

                                    $SRDef = $sharedResource + $dollar

                                    if ($permission -eq "R" -or $permission -eq "r") {

                                    New-SmbShare  -Name "$SRDef" -Path "$path" -ReadAccess "$account" -Description "$description"

                                    Write-Host " $sharedResource has been shared" -ForegroundColor DarkGreen
                                    Write-Output "";
                                    }

                                    elseif ($permission -eq "C" -or $permission -eq "c") {

                                        New-SmbShare  -Name "$SRDef" -Path "$path" -ChangeAccess "$account" -Description "$description"

                                        Write-Host " $sharedResource has been shared" -ForegroundColor DarkGreen
                                        Write-Output "";
                                    }

                                    elseif ($permission -eq "F" -or $permission -eq "f" ) {


                                        New-SmbShare  -Name "$SRDef" -Path "$path" -FullAccess "$account" -Description "$description"

                                        Write-Host " $sharedResource has been shared" -ForegroundColor DarkGreen
                                          Write-Output "";
                                    }

                                    else {

                                        Write-Host " Enter a correct value (R/C/F)" -ForegroundColor DarkRed

                                        Write-Host " $sharedResource has been shared" -ForegroundColor DarkGreen
                                        Write-Output "";
                                    }



                                }



                                else {



                                    if ($permission -eq "R" -or $permission -eq "r") {

                                    $permdef = "-ReadAccess"

                                    New-SmbShare  -Name "$sharedResource" -Path "$path" -ReadAccess "$account" -Description "$description"

                                    Write-Host " $sharedResource has been shared" -ForegroundColor DarkGreen
                                    Write-Output "";
                                    }

                                    elseif ($permission -eq "C" -or $permission -eq "c") {

                                    #echo "New-SmbShare -Name "$sharedResource" -Path "$path" -$permdef "$account"  "

                                    New-SmbShare -Name "$sharedResource" -Path "$path" -ChangeAccess "$account" -Description "$description"

                                    Write-Host " $sharedResource has been shared" -ForegroundColor DarkGreen
                                    Write-Output "";
                                    }

                                    elseif ($permission -eq "F" -or $permission -eq "f" ) {


                                    New-SmbShare  -Name "$sharedResource" -Path "$path" -FullAccess "$account" -Description "$description"

                                    Write-Host " $sharedResource has been shared" -ForegroundColor DarkGreen
                                    Write-Output "";
                                    Write-Output "";
                                    }

                                    else {
                                    Write-Output "";
                                    Write-Host " Enter a correct value (R/C/F)" -ForegroundColor DarkRed

                                    }

                                }


                        }

                        else {
                        Write-Output "";
                        Write-Host " The account $account doesn't exist" -ForegroundColor DarkRed

                        }


                }

                else {
                Write-Output "";
                Write-Host " The directory $path doesn't exist" -ForegroundColor DarkRed

                }

        }

        else {
        Write-Output "";
        Write-Host " Enter some path of the shared resource" -ForegroundColor DarkRed

        }
}

else {
Write-Output "";
Write-Host " $sharedResource ALREADY exists or the name must be more than 4 characters" -ForegroundColor DarkRed

}
