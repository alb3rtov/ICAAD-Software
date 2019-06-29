Write-Output "";
$nombreGrupo = read-host " Nombre del grupo"
Write-Output "";
$nombreUsuario = Read-Host " Nombre del usuario"
Write-Output "";

#$longitud = $nombreUO.Length 

try {

Get-ADGroup -Filter "Name -like '$nombreGrupo'" > .\scripts\obj\docs\iusugrupo1.txt

Get-ADUser -Filter "Name -like '$nombreUsuario'" > .\scripts\obj\docs\iusugrupo2.txt

$contador1 = (Get-Content .\scripts\obj\docs\iusugrupo1.txt | where{$_-match"$nombreGrupo"}).Count

$contador2 = (Get-Content .\scripts\obj\docs\iusugrupo2.txt | where{$_-match"$nombreUsuario"}).Count

    if ($contador1 -ne 0 -and $contador2 -ne 0) {

        Add-ADGroupMember -Identity "$nombreGrupo" -Members "$nombreUsuario"

        Write-Host " El usuario $nombreUsuario se ha introducido correctamente en el grupo $nombreGrupo" -ForegroundColor DarkGreen

    }

    else {

        Write-Host " $nombreGrupo o $nombreUsuario no existe" -ForegroundColor DarkRed
    }

}

 catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host "";
            Write-Host " Error con alguno de los datos introducidos" -ForegroundColor DarkRed
 }