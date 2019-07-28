Write-Output "";
$computerName = read-host " New name for the computer"
Write-Output "";

try {

Rename-Computer -NewName $computerName

}

catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Error, enter a correct name" -ForegroundColor DarkRed
        }
