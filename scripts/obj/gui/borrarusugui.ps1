#Write-Output "";
#$nombreUsuario = read-host " Nombre del usuario a borrar"

#$nombreDominio = read-host " Nombre de dominio: "
#Write-Output "";
#$extensionDominio = read-host " Extension de dominio: "
#Write-Output "";

#$longitud = $nombreUO.Length 


$datos = Get-Content ".\scripts\obj\gui\docs\borrarusugui.txt"


try {
Get-ADUser -Filter "Name -like '$datos'" > .\scripts\obj\gui\docs\borrarusugui2.txt

$contador = (Get-Content .\scripts\obj\gui\docs\borrarusugui2.txt | where{$_-match"$datos"}).Count


    if ($contador -ne 0) {
    


            $string = Get-Content .\scripts\obj\gui\docs\borrarusugui2.txt | where{$_-match"$datos"}

            $tag = $string.Split(":",4)[1]

            #echo $tag

            Remove-ADUser -Identity "$tag" -Confirm:$false # borra la unidad organizativa

            echo 0 > .\scripts\obj\gui\docs\compbusu.txt

            #Write-Output "";
            #Write-Host " Usuario $nombreUsuario elimando correctamente" -ForegroundColor DarkGreen

    }
    else {
        #Write-Output "";
        #Write-Host " El usuario $nombreUsuario no existe" -ForegroundColor DarkRed

        echo 100 > .\scripts\obj\gui\docs\compbusu.txt
    }

}

catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            #Write-Output "";
            #Write-Host " Introduzca algún dato" -ForegroundColor DarkRed

            echo 100 > .\scripts\obj\gui\docs\compbusu.txt
        }