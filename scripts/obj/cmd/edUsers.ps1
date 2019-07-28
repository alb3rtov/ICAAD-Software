
Write-Output "";
$confirmation = read-host " ¿Do you enable (e) or disable (d) users? (e/d)"
Write-Output "";

echo "" > .\scripts\obj\cmd\temp\edUsers.txt

if ($confirmation -eq "e" -or $confirmation -eq "E") {
    $userName1 = read-host " Choose the name of the user to enable"
    Write-Output "";


        try {
            Get-ADUser -Filter "Name -eq '$userName1'" > .\scripts\obj\cmd\temp\edUsers.txt

            $counter = (Get-Content .\scripts\obj\cmd\temp\edUsers.txt | where{$_-match"$userName1"}).Count

            if ($counter -ne 0) {

                Enable-ADAccount -Identity $userName1
                Write-Host " The user $userName1 has been enabled" -ForegroundColor DarkGreen
            }

            else {
                Write-Host " The user $userName1 doesn't exist" -ForegroundColor DarkRed
            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " You must to enter some data" -ForegroundColor DarkRed
        }

}

ElseIf ($confirmation -eq "d" -or $confirmation -eq "D") {
    $userName2 = read-host " Choose the name of the user to disable"
    Write-Output "";


        try {
            Get-ADUser -Filter "Name -eq '$userName2'" > .\scripts\obj\cmd\temp\edUsers.txt

            $contador = (Get-Content .\scripts\obj\cmd\temp\edUsers.txt | where{$_-match"$userName2"}).Count

            #echo $contador

            if ($contador -ne 0) {

                Disable-ADAccount -Identity $userName2
                Write-Host " The user $userName2 has been disabled" -ForegroundColor DarkGreen
            }

            else {
                Write-Host " The user $userName2 doesn't exist" -ForegroundColor DarkRed
            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " You must to enter some data" -ForegroundColor DarkRed
        }

}

else {
    Write-Host " Choose a correct option" -ForegroundColor DarkRed
}
