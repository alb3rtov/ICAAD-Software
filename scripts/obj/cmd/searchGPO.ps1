
Write-Output "";
$GPOName = read-host " Name of the GPO"
Write-Output "";


Get-GPO -all >  .\scripts\obj\cmd\temp\searchGPO.txt

$contador1 = (Get-Content .\scripts\obj\cmd\temp\searchGPO.txt | where{$_-match"$GPOName"}).Count


if ($contador1 -ne 0) {


   try {

            Get-GPO -Name "$GPOName"



            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }

            Write-Host " Error with some of the entered data" -ForegroundColor DarkRed
        }
    }



else {

            Write-Host " The GPO $GPOName doesn't exist" -ForegroundColor DarkRed
}
