
Write-Output "";
$OUName = read-host " Search Organizational Unit"
Write-Output "";

        try {
            Get-ADOrganizationalUnit -Filter "Name -like '$OUName'" > .\scripts\obj\cmd\temp\searchOU.txt

            $counter = (Get-Content .\scripts\obj\cmd\temp\searchOU.txt | where{$_-match"$OUName"}).Count

            if ($counter -ne 0) {
                Get-ADOrganizationalUnit -Filter "Name -like '$OUName'"
            }

            else {
                Write-Host " The Organizational Unit $OUName doesn't exist" -ForegroundColor DarkRed
            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " You must to enter some data" -ForegroundColor DarkRed
        }
