
#Write-Output "";
#$nombreUO = read-host " Nombre de unidad organizativa"
#Write-Output "";
#$nombreDominio = read-host " Nombre de dominio"
#Write-Output "";
#$extensionDominio = read-host " Sufijo de dominio"
#Write-Output "";
$nombreEquipo = hostname

#$confirmacion = read-host " ¿Desea añadir valores adicionales? (s/n)"
#Write-Output "";

$datos1 = Get-Content ".\scripts\obj\gui\docs\crearuo1.txt"

$datos2 = Get-Content ".\scripts\obj\gui\docs\crearuo2.txt"

$datos3 = Get-Content ".\scripts\obj\gui\docs\crearuo3.txt"




#$longitud = $nombreUO.Length 

#if ($nombreUO.Length  -gt 4) {

    Get-ADOrganizationalUnit -Filter "Name -like '$datos1'" > .\scripts\obj\gui\docs\crearuo4.txt

    $contador = (Get-Content .\scripts\obj\gui\docs\crearuo4.txt | where{$_-match"$datos1"}).Count

    if ($contador -eq 0) {
    
        try {
            New-ADOrganizationalUnit -name $datos1 -server $nombreEquipo -path "DC=$datos2, DC=$datos3"
            #Write-Host " Unidad $nombreUO creada correctamente" -ForegroundColor DarkGreen
            echo 0 > .\scripts\obj\gui\docs\compcuo.txt
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            #Write-Host " Introduzca un nombre y extensión de dominio correcto" -ForegroundColor DarkRed
            echo 100 > .\scripts\obj\gui\docs\compcuo.txt
        }
    }
    else {
        #Write-Host " La unidad organizativa $nombreUO ya esta creada" -ForegroundColor DarkRed
        echo 100 > .\scripts\obj\gui\docs\compcuo.txt
    }
#}

