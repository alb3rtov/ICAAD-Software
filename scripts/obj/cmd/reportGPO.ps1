
Write-Output "";
Write-Host " [*] The path generation of the report it will be $Home" -ForegroundColor Yellow

Write-Output "";
$GPOName = read-host " Name of the GPO for generate the report"
Write-Output "";


Get-GPO -all >  .\scripts\obj\cmd\temp\reportGPO.txt

$counter1 = (Get-Content .\scripts\obj\cmd\temp\reportGPO.txt | where{$_-match"$GPOName"}).Count


if ($counter1 -ne 0) {

   try {

            Get-GPO -Name "$GPOName" | Get-GPOReport -ReportType HTML -Path $Home\report_$GPOName.html   > /null


            Write-Host " Report of $GPOName generated correctly" -ForegroundColor DarkGreen
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
