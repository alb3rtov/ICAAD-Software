#Write-Output "";
#$nombreGrupo = read-host " Nombre del grupo"
#Write-Output "";
#$nombreUsuario = Read-Host " Nombre del usuario"
#Write-Output "";

#$longitud = $nombreUO.Length 


$datos1 = Get-Content ".\scripts\obj\gui\docs\introusugrupogui1.txt"

$datos2 = Get-Content ".\scripts\obj\gui\docs\introusugrupogui2.txt"


try {

Get-ADGroup -Filter "Name -like '$datos1'" > .\scripts\obj\gui\docs\introusugrupogui1.txt

Get-ADUser -Filter "Name -like '$datos2'" > .\scripts\obj\gui\docs\introusugrupogui2.txt

$contador1 = (Get-Content .\scripts\obj\gui\docs\introusugrupogui1.txt | where{$_-match"$datos1"}).Count

$contador2 = (Get-Content .\scripts\obj\gui\docs\introusugrupogui2.txt | where{$_-match"$datos2"}).Count

    if ($contador1 -ne 0 -and $contador2 -ne 0) {

        Add-ADGroupMember -Identity "$datos1" -Members "$datos2"

       # Write-Host " El usuario $nombreUsuario se ha introducido correctamente en el grupo $nombreGrupo" -ForegroundColor DarkGreen

       echo 0 > .\scripts\obj\gui\docs\compiusugrupo.txt

    }

    else {

       # Write-Host " $nombreGrupo o $nombreUsuario no existe" -ForegroundColor DarkRed

       echo 100 > .\scripts\obj\gui\docs\compiusugrupo.txt
    }

}

 catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
           # Write-Host "";
           # Write-Host " Error con alguno de los datos introducidos" -ForegroundColor DarkRed

           echo 100 > .\scripts\obj\gui\docs\compiusugrupo.txt
 }