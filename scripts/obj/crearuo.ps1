
Write-Output "";
$nombreUO = read-host " Nombre de unidad organizativa"
Write-Output "";
$nombreDominio = read-host " Nombre de dominio"
Write-Output "";
$extensionDominio = read-host " Sufijo de dominio"
Write-Output "";
$nombreEquipo = hostname

$confirmacion = read-host " ¿Desea añadir valores adicionales? (s/n)"
Write-Output "";

if ($confirmacion -eq "s" -or $confirmacion -eq "S") {
    $country = read-host " País (abrebiatura ej: ES, EN...)"
    Write-Output "";
    $city = read-host " Ciudad"
    Write-Output "";

} 


#$longitud = $nombreUO.Length 

echo "" > .\scripts\obj\docs\crearuo.txt

if ($nombreUO.Length  -gt 4) {
    Get-ADOrganizationalUnit -Filter "Name -like '$nombreUO'" > .\scripts\obj\docs\crearuo.txt

    $contador = (Get-Content .\scripts\obj\docs\crearuo.txt | where{$_-match"$nombreUO"}).Count

    if ($contador -eq 0) {
    
        try {
            New-ADOrganizationalUnit -name $nombreUO -server $nombreEquipo -path "DC=$nombreDominio, DC=$extensionDominio" -Country $country -City $city
            Write-Host " Unidad $nombreUO creada correctamente" -ForegroundColor DarkGreen
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Introduzca un nombre y extensión de dominio correcto" -ForegroundColor DarkRed
        }
    }
    else {
        Write-Host " La unidad organizativa $nombreUO ya esta creada" -ForegroundColor DarkRed
    }
}

else {
    Write-Host " Debe introducir un nombre para la unidad organizativa de más de 4 carácteres" -ForegroundColor DarkRed
}
