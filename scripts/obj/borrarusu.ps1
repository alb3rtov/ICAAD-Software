Write-Output "";
$nombreUsuario = read-host " Nombre del usuario a borrar"

#$nombreDominio = read-host " Nombre de dominio: "
#Write-Output "";
#$extensionDominio = read-host " Extension de dominio: "
#Write-Output "";

#$longitud = $nombreUO.Length 

try {
Get-ADUser -Filter "Name -like '$nombreUsuario'" > .\scripts\obj\docs\borrarusu.txt

$contador = (Get-Content .\scripts\obj\docs\borrarusu.txt | where{$_-match"$nombreUsuario"}).Count


    if ($contador -ne 0) {
    


            $string = Get-Content .\scripts\obj\docs\borrarusu.txt | where{$_-match"$nombreUsuario"}

            $tag = $string.Split(":",4)[1]

            #echo $tag

            Remove-ADUser -Identity "$tag" -Confirm:$false # borra la unidad organizativa

            Write-Output "";
            Write-Host " Usuario $nombreUsuario elimando correctamente" -ForegroundColor DarkGreen

    }
    else {
        Write-Output "";
        Write-Host " El usuario $nombreUsuario no existe" -ForegroundColor DarkRed
    }

}

catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Output "";
            Write-Host " Introduzca algún dato" -ForegroundColor DarkRed
        }