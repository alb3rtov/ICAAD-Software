Write-Output "";
$nombreGrupo = read-host " Nombre del grupo a borrar"

try {

Get-ADGroup -Filter "Name -like '$nombreGrupo'" > .\scripts\obj\docs\borrargrupo.txt

$contador = (Get-Content .\scripts\obj\docs\borrargrupo.txt | where{$_-match"$nombreGrupo"}).Count

    if ($contador -ne 0) {
    


            $string = Get-Content .\scripts\obj\docs\borrargrupo.txt | where{$_-match"$nombreGrupo"}

            $tag = $string.Split(":",4)[1]

            #echo $tag

            Remove-ADGroup -Identity "$tag" -Confirm:$false

            Write-Output "";
            Write-Host " Grupo $nombreGrupo eliminado correctamente" -ForegroundColor DarkGreen

    }
    else {
        Write-Output "";
        Write-Host " El grupo $nombreGrupo no existe" -ForegroundColor DarkRed
    }

}

catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Output "";
            Write-Host " Introduzca algún dato" -ForegroundColor DarkRed
        }