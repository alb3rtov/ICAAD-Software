Write-Output "";
Write-Host " [*] Default, the path of generation of the CSV file is the directory of this program" -ForegroundColor Yellow
Write-Output "";
$path = read-host " Path and name where generate the CSV file (i.e.: C:\adObjects.csv)"
Write-Output "";

$csv = ".csv"

$path > .\scripts\obj\cmd\temp\exportObj.txt

$counter = (Get-Content .\scripts\obj\cmd\temp\exportObj.txt | where{$_-match"$csv"}).Count


if ($counter -ne 0) {

try {
Get-ADObject -Filter * -Properties * | Export-Csv $path
Write-Host " $path generated correctly" -ForegroundColor DarkGreen
}

catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Error with the path" -ForegroundColor DarkRed
        }

}

else {

  Write-Host " You must to add the extension .csv" -ForegroundColor DarkRed
}
