
Write-Output "";
$userName = read-host " Search user"
Write-Output "";

        try {
            Get-ADUser -Filter "Name -eq '$userName'" > .\scripts\obj\cmd\temp\searchUsers.txt

            $counter = (Get-Content .\scripts\obj\cmd\temp\searchUsers.txt | where{$_-match"$userName"}).Count

            if ($counter -ne 0) {
                Get-ADUser -Filter "Name -eq '$userName'"
            }

            else {
                Write-Host " The user $userName doesn't exits" -ForegroundColor DarkRed
            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " You must to enter some data" -ForegroundColor DarkRed
        }
