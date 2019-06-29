Write-Output "";
$nombreGrupo = read-host " Nombre del grupo"
Write-Output "";

$longitud = $nombreGrupo.Length 

#echo $longitud

echo "" > .\scripts\obj\docs\buscarusugrupo.txt

if ($longitud -ne 0) {

Get-ADGroup -Filter "Name -like '$nombreGrupo'" > .\scripts\obj\docs\buscarusugrupo.txt

$contador = (Get-Content .\scripts\obj\docs\buscarusugrupo.txt | where{$_-match"$nombreGrupo"}).Count

    if ($contador -ne 0) {
    
        try {

            #$string = Get-Content .\scripts\obj\usugrupo.txt | where{$_-match"$nombreGrupo"}

            #$tag = $string.Split(":",4)[1]

            #echo $tag

            Get-ADGroupMember "$nombreGrupo" -recursive | Select-Object Name, DistinguishedName

            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host "";
            Write-Host " Error con el nombre del grupo" -ForegroundColor DarkRed
        }
    }
    else {
        Write-Host " El grupo $nombreGrupo no existe" -ForegroundColor DarkRed
    }

}

else {
    Write-Host " Introduzca algún nombre de grupo" -ForegroundColor DarkRed

}