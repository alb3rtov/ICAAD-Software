#Write-Output "";
#$nombreGrupo = read-host " Nombre del grupo a borrar"


$datos = Get-Content ".\scripts\obj\gui\docs\borrargrupogui.txt"

try {

Get-ADGroup -Filter "Name -like '$datos'" > .\scripts\obj\gui\docs\borrargrupogui1.txt

$contador = (Get-Content .\scripts\obj\gui\docs\borrargrupogui1.txt | where{$_-match"$datos"}).Count

    if ($contador -ne 0) {
    


            $string = Get-Content .\scripts\obj\gui\docs\borrargrupogui1.txt | where{$_-match"$datos"}

            $tag = $string.Split(":",4)[1]

            #echo $tag

            Remove-ADGroup -Identity "$tag" -Confirm:$false

            echo 0 > .\scripts\obj\gui\docs\compbogrupo.txt

            #Write-Output "";
            #Write-Host " Grupo $datos elimado correctamente" -ForegroundColor DarkGreen

    }
    else {
       # Write-Output "";
       # Write-Host " El grupo $nombreGrupo no existe" -ForegroundColor DarkRed

        echo 100 > .\scripts\obj\gui\docs\compbogrupo.txt
    }

}

catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
           # Write-Output "";
           # Write-Host " Introduzca algún dato" -ForegroundColor DarkRed

            echo 100 > .\scripts\obj\gui\docs\compbogrupo.txt
        }