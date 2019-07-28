Write-Output "";
$groupName = read-host " Name of the group"
Write-Output "";
$userName = Read-Host " Name of the user to add"
Write-Output "";

#$longitud = $nombreUO.Length

echo "" > .\scripts\obj\cmd\temp\addUsersGroups1.txt
echo "" > .\scripts\obj\cmd\temp\addUsersGroups2.txt


try {

Get-ADGroup -Filter "Name -like '$groupName'" > .\scripts\obj\cmd\temp\addUsersGroups1.txt

Get-ADUser -Filter "Name -like '$userName'" > .\scripts\obj\cmd\temp\addUsersGroups2.txt

$counter1 = (Get-Content .\scripts\obj\cmd\temp\addUsersGroups1.txt | where{$_-match"$groupName"}).Count

$counter2 = (Get-Content .\scripts\obj\cmd\temp\addUsersGroups2.txt | where{$_-match"$userName"}).Count

    if ($counter1 -ne 0 -and $counter2 -ne 0) {

        Add-ADGroupMember -Identity "$groupName" -Members "$userName"

        Write-Host " The user $userName  has been added correctly to the group $groupName" -ForegroundColor DarkGreen

    }

    else {

        Write-Host " $groupName or $userName doesn't exist" -ForegroundColor DarkRed
    }

}

 catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host "";
            Write-Host " Error with some entered data" -ForegroundColor DarkRed
 }
