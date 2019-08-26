Write-Output "";
$GPOName = read-host " Name of the GPO to delete"
Write-Output "";


Get-GPO -all >  .\scripts\obj\cmd\temp\deleteGPO.txt

$counter = (Get-Content .\scripts\obj\cmd\temp\deleteGPO.txt | where{$_-match"$GPOName"}).Count


if ($counter -ne 0) {


   try {

            Remove-GPO -Name "$GPOName" > /null


            Write-Host " GPO $GPOName deleted correctly" -ForegroundColor DarkGreen
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }

            Write-Host " Error with some entered data" -ForegroundColor DarkRed
        }
    }



else {

            Write-Host " GPO $GPOName doesn't exist" -ForegroundColor DarkRed
}
