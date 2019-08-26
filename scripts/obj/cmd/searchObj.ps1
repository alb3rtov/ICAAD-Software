
Write-Output "";
$objectName = read-host " Search a AD object"
Write-Output "";

        try {
            Get-ADObject -Filter "Name -eq '$objectName'" > .\scripts\obj\cmd\temp\searchObj.txt

            $counter = (Get-Content .\scripts\obj\cmd\temp\searchObj.txt | where{$_-match"$objectName"}).Count

            if ($counter -ne 0) {
                Get-ADObject -Filter "Name -eq '$objectName'"
            }

            else {
                Write-Host " The object $objectName doesn't exist" -ForegroundColor DarkRed
            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " You must to enter some data" -ForegroundColor DarkRed
        }
