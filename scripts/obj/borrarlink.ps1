Write-Output "";
$nombreGPO = read-host " Nombre de la GPO a borrar"
Write-Output "";


Get-GPO -all >  .\scripts\obj\docs\borrarlink1.txt

$contador1 = (Get-Content .\scripts\obj\docs\borrarlink1.txt | where{$_-match"$nombreGPO"}).Count

echo "" > .\scripts\obj\docs\borrarlink2.txt


if ($contador1 -ne 0) {

$nombreDominio = read-host " Nombre de dominio"
Write-Output "";
$extensionDominio = read-host " Sufijo de dominio"
Write-Output "";

$confirmacion = read-host " ¿El link que desea borrar de $nombreGPO se encuentra dentro de una unidad organizativa? (s/n)"
Write-Output "";


if ($confirmacion -eq "s" -or $confirmacion -eq "S") {

   Write-Host " [*] Unidades organizativas encontradas" -ForegroundColor Yellow


   Get-ADOrganizationalUnit -Filter 'Name -like "*"' | Format-Table Name,DistinguishedName -A


   $nombreUO = read-host " Nombre de unidad organizativa"

   Get-ADOrganizationalUnit -Filter "Name -like '$nombreUO'" > .\scripts\obj\docs\borrarlink2.txt

   $contador = (Get-Content .\scripts\obj\docs\borrarlink2.txt | where{$_-match"$nombreUO"}).Count

   if ($contador -ne 0) {
   
   try {

            $string = Get-Content .\scripts\obj\docs\borrarlink2.txt | where{$_-match"$nombreUO"}

            $tag = $string.Split(":",4)[1]

            #echo $tag
            #echo $nombreGPO

            $newtag = $tag.Substring(1)

            Remove-GPLink -Name "$nombreGPO" -Target "$newtag" > /null

            Write-Output "";
            Write-Host "El link de $nombreGPO en $newtag se ha eliminado correctamente" -ForegroundColor DarkGreen
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host "";
            Write-Host " Error con alguno de los datos introducidos" -ForegroundColor DarkRed
        }
    
   }
   
   else {
   Write-Host "";
   Write-Host " La unidad organizativa $nombreUO no existe" -ForegroundColor DarkRed
   
   

   }

} 

Elseif ($confirmacion -eq "n" -or $confirmacion -eq "N") {




    try {

            Remove-GPLink -Name "$nombreGPO" -Target "DC=$nombreDominio,DC=$extensionDominio" > /null

            Write-Host "El link de $nombreGPO en DC=$nombreDominio,DC=$extensionDominio se ha eliminado correctamente" -ForegroundColor DarkGreen
        }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            Write-Host " Error con alguno de los datos introducidos" -ForegroundColor DarkRed
        }

        }





Else {

            Write-Host " Eliga una opción correcta" -ForegroundColor DarkRed
}

}

else {
 
            Write-Host " La GPO $nombreGPO no existe" -ForegroundColor DarkRed
}