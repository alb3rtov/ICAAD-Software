Write-Output "";
$userName = read-host " Name of the user to delete"

#$nombreDominio = read-host " Nombre de dominio: "
#Write-Output "";
#$extensionDominio = read-host " Extension de dominio: "
#Write-Output "";

#$longitud = $nombreUO.Length

try {
Get-ADUser -Filter "Name -like '$userName'" > .\scripts\obj\cmd\temp\deleteUsers.txt

$counter = (Get-Content .\scripts\obj\cmd\temp\deleteUsers.txt | where{$_-match"$userName"}).Count


    if ($counter -ne 0) {



            $string = Get-Content .\scripts\obj\cmd\temp\deleteUsers.txt | where{$_-match"$userName"}

            $tag = $string.Split(":",4)[1]

            #echo $tag

            Remove-ADUser -Identity "$tag" -Confirm:$false # borra la unidad organizativa

            Write-Output "";
            Write-Host " User $userName deleted" -ForegroundColor DarkGreen

    }
    else {
        Write-Output "";
        Write-Host " The user $userName doesn't exist" -ForegroundColor DarkRed
    }

}

catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Output "";
            Write-Host " You must to enter some data" -ForegroundColor DarkRed
        }
