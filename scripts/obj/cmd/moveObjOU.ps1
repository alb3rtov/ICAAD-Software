
Write-Output "";
$object = read-host " Name of the object to move"
Write-Output "";
$newOU = read-host " Name of the OU where move the object"
Write-Output "";
$domainName = read-host " Domain name"
Write-Output "";
$suffixDomain = read-host " Domain suffix"
Write-Output "";


        try {

            Get-ADObject -Filter "Name -eq '$object'" > .\scripts\obj\cmd\temp\moveObjOU.txt

            $counter = (Get-Content .\scripts\obj\cmd\temp\moveObjOU.txt | where{$_-match"$object"}).Count

            #echo $counter

            if ($counter -ne 0) {

                $string = Get-Content .\scripts\obj\cmd\temp\moveObjOU.txt | where{$_-match"$object"}

                #echo $string

                $tag = $string.Split(" ",4)[0]


                #echo $tag

                Move-ADObject "$tag" -TargetPath "OU=$newOU,DC=$domainName,DC=$suffixDomain"

                Write-Host " The object $object has been moved correctly" -ForegroundColor DarkGreen
            }

            else {

                Write-Host " The object $object doesn't exist" -ForegroundColor DarkRed

            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error") {
            }
            Write-Host " Error, some entered data are wrong" -ForegroundColor DarkRed
        }
