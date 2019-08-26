Write-Output "";
Write-Host " [*] Default, the path of the CSV file generation is directory of this program" -ForegroundColor Yellow
Write-Output "";
$path = read-host " Path and name of where generate the CSV file (i.e.: C:\users.csv)"
Write-Output "";


$csv = ".csv"

$path > .\scripts\obj\cmd\temp\exportUsers.txt

$counter = (Get-Content .\scripts\obj\cmd\temp\exportUsers.txt | where{$_-match"$csv"}).Count


if ($counter -ne 0) {
try {
Get-ADUser -Filter * -Properties * | Export-Csv $path
Write-Host " $path generated correctly" -ForegroundColor DarkGreen
}

catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Error with the path" -ForegroundColor DarkRed
        }

}

else {

  Write-Host " You must to add the .csv extension" -ForegroundColor DarkRed
}
