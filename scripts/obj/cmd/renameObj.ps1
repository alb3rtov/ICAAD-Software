Write-Output "";
$objectName = read-host " Name of the object to rename"
Write-Output "";
$newName = read-host " New name of the object"
Write-Output "";


        try {

            Get-ADObject -Filter "Name -eq '$objectName'" > .\scripts\obj\cmd\temp\renameObj.txt


            $contador = (Get-Content .\scripts\obj\cmd\temp\renameObj.txt | where{$_-match"$objectName"}).Count

            #echo $contador

            if ($contador -ne 0) {

                $string = Get-Content .\scripts\obj\cmd\temp\renameObj.txt | where{$_-match"$objectName"}

                #echo $string

                $tag = $string.Split(" ",4)[0]

                #echo $tag

                Rename-ADObject -Identity "$tag" -NewName "$newName"


                Write-Host " The object $objectName has been renamed as $newName" -ForegroundColor DarkGreen
            }

            else {

                Write-Host " Error with the name of the objects" -ForegroundColor DarkRed

            }

        }

        catch [System.Management.Automation.RuntimeException] {

            if ($_.Exception.Message -ilike "Error") {
            }
            Write-Host " Error, some entered data are wrong" -ForegroundColor DarkRed
        }
