Write-Output "";
$groupName = read-host " Name fo the group to delete"

try {

Get-ADGroup -Filter "Name -like '$groupName'" > .\scripts\obj\cmd\temp\deleteGroups.txt

$counter = (Get-Content .\scripts\obj\cmd\temp\deleteGroups.txt | where{$_-match"$groupName"}).Count

    if ($counter -ne 0) {



            $string = Get-Content .\scripts\obj\cmd\temp\deleteGroups.txt | where{$_-match"$groupName"}

            $tag = $string.Split(":",4)[1]

            #echo $tag

            Remove-ADGroup -Identity "$tag" -Confirm:$false

            Write-Output "";
            Write-Host " Group $groupName deleted" -ForegroundColor DarkGreen

    }
    else {
        Write-Output "";
        Write-Host " The grupo $groupName doesn't exist" -ForegroundColor DarkRed
    }

}

catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Output "";
            Write-Host " Enter some data" -ForegroundColor DarkRed
        }
