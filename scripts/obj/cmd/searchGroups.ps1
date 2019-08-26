
Write-Output "";
$groupName = read-host " Search group"
Write-Output "";

        try {
            Get-ADGroup -Filter "Name -eq '$groupName'" > .\scripts\obj\cmd\temp\searchGroups.txt

            $counter = (Get-Content .\scripts\obj\cmd\temp\searchGroups.txt | where{$_-match"$groupName"}).Count

            if ($counter -ne 0) {
                Get-ADGroup -Filter "Name -eq '$groupName'"
            }

            else {
                Write-Host " El usuario $groupName no existe" -ForegroundColor DarkRed
            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Debe introducir algún dato" -ForegroundColor DarkRed
        }
