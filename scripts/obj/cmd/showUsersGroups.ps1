Write-Output "";
$groupName = read-host " Name of the group"
Write-Output "";

$lengthName = $groupName.Length

#echo $longitud

echo "" > .\scripts\obj\cmd\temp\showUsersGroups.txt

if ($lengthName -ne 0) {

Get-ADGroup -Filter "Name -like '$groupName'" > .\scripts\obj\cmd\temp\showUsersGroups.txt

$counter = (Get-Content .\scripts\obj\cmd\temp\showUsersGroups.txt | where{$_-match"$groupName"}).Count

    if ($counter -ne 0) {

        try {

            #$string = Get-Content .\scripts\obj\usugrupo.txt | where{$_-match"$groupName"}

            #$tag = $string.Split(":",4)[1]

            #echo $tag

            Get-ADGroupMember "$groupName" -recursive | Select-Object Name, DistinguishedName

            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host "";
            Write-Host " Error with the name of the group" -ForegroundColor DarkRed
        }
    }
    else {
        Write-Host " The group $groupName doesn't exist" -ForegroundColor DarkRed
    }

}

else {
    Write-Host " Enter some name for the group" -ForegroundColor DarkRed

}
