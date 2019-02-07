Write-Output "";
Write-Host " [*] Por defecto, la GPO se vinculará a nivel de las UOs del dominio que elija" -ForegroundColor Yellow
Write-Output "";
$nombreGPO = read-host " Nombre de la GPO"
Write-Output "";


Get-GPO -all >  .\scripts\obj\docs\vinculargpo1.txt

$contador1 = (Get-Content .\scripts\obj\docs\vinculargpo1.txt | where{$_-match"$nombreGPO"}).Count

echo "" > .\scripts\obj\docs\vinculargpo2.txt

if ($contador1 -ne 0) {

$nombreDominio = read-host " Nombre de dominio"
Write-Output "";
$extensionDominio = read-host " Sufijo de dominio"
Write-Output "";

$confirmacion = read-host " ¿Desea vincular la GPO a una unidad organizativa? (s/n)"
Write-Output "";



if ($confirmacion -eq "s" -or $confirmacion -eq "S") {

   Write-Host " [*] Unidades organizativas encontradas" -ForegroundColor Yellow


   Get-ADOrganizationalUnit -Filter 'Name -like "*"' | Format-Table Name,DistinguishedName -A


   $nombreUO = read-host " Nombre de unidad organizativa"

   if ($nombreUO.Length -ne 0) {

         Get-ADOrganizationalUnit -Filter "Name -like '$nombreUO'" > .\scripts\obj\docs\vinculargpo2.txt

         $contador = (Get-Content .\scripts\obj\docs\vinculargpo2.txt | where{$_-match"$nombreUO"}).Count

            if ($contador -ne 0) {
   
                try {

                    $string = Get-Content .\scripts\obj\docs\vinculargpo2.txt | where{$_-match"$nombreUO"}

                    $tag = $string.Split(":",4)[1]

                    #echo $tag
                    #echo $nombreGPO

                    $newtag = $tag.Substring(1)

                    New-GPLink -Name "$nombreGPO" -Target "$newtag" > /null

                    Write-Output "";
                    Write-Host " $nombreGPO vinculada a $newtag" -ForegroundColor DarkGreen
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

   else  {
        Write-Host "";
        Write-Host " Introduzca algún nombre para la unidad organizativa" -ForegroundColor DarkRed
   
   
   
   }
   


} 

Elseif ($confirmacion -eq "n" -or $confirmacion -eq "N") {




    try {
     
            New-GPLink -Name "$nombreGPO" -Target "DC=$nombreDominio,DC=$extensionDominio" > /null

            
            Write-Host " $nombreGPO vinculada a DC=$nombreDominio,DC=$extensionDominio correctamente" -ForegroundColor DarkGreen
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