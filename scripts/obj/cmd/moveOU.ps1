
Write-Output "";
Write-Host " [*] Make sure that the OU is empty" -ForegroundColor Yellow
Write-Output "";
$object = read-host " Name of OU to move"
Write-Output "";
$newOU = read-host " Name of OU where move"
Write-Output "";


        try {

            Get-ADObject -Filter "Name -eq '$object'" > .\scripts\obj\cmd\temp\moveOU1.txt

            Get-ADObject -Filter "Name -eq '$newOU'" > .\scripts\obj\cmd\temp\moveOU2.txt

            $counter1 = (Get-Content .\scripts\obj\cmd\temp\moveOU1.txt | where{$_-match"$object"}).Count

            $counter2 = (Get-Content .\scripts\obj\cmd\temp\moveOU2.txt | where{$_-match"$newOU"}).Count

            #echo $contador

            if ($counter1 -ne 0 -and $counter2 -ne 0) {

                $string1 = Get-Content .\scripts\obj\cmd\temp\moveOU1.txt | where{$_-match"$object"}

                $string2 = Get-Content .\scripts\obj\cmd\temp\moveOU2.txt | where{$_-match"$newOU"}
                #echo $string

                $tag1 = $string1.Split(" ",4)[0]

                $tag2 = $string2.Split(" ",4)[0]


                #echo $tag1

                #echo $tag2

                Set-ADOrganizationalUnit -Identity "$tag1" -ProtectedFromAccidentalDeletion $false

                Move-ADObject "$tag1" -TargetPath "$tag2"

                Write-Host " The OU $object has been moved correctly to $newOU" -ForegroundColor DarkGreen
            }

            else {

                Write-Host " Error with the name of the OUs" -ForegroundColor DarkRed

            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error") {
            }
            Write-Host " Error, some entered data are wrong" -ForegroundColor DarkRed
        }
