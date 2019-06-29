#Write-Output "";
#$nombreGPO = read-host " Nombre de la GPO a borrar"
#Write-Output "";


$datos1 = Get-Content ".\scripts\obj\gui\docs\borrarlinkgui1.txt"

$datos2 = Get-Content ".\scripts\obj\gui\docs\borrarlinkgui2.txt"

Get-GPO -all >  .\scripts\obj\gui\docs\borrarlinkgui3.txt

$contador1 = (Get-Content .\scripts\obj\gui\docs\borrarlinkgui3.txt | where{$_-match"$datos1"}).Count

echo "" > .\scripts\obj\gui\docs\borrarlinkgui4.txt

if ($contador1 -ne 0) {


   #$nombreUO = read-host " Nombre de unidad organizativa"

   Get-ADOrganizationalUnit -Filter "Name -like '$datos2'" > .\scripts\obj\gui\docs\borrarlinkgui4.txt

   $contador = (Get-Content .\scripts\obj\gui\docs\borrarlinkgui4.txt | where{$_-match"$datos2"}).Count

   if ($contador -ne 0) {
   
   try {

            $string = Get-Content .\scripts\obj\gui\docs\borrarlinkgui4.txt  | where{$_-match"$datos2"}

            $tag = $string.Split(":",4)[1]

            #echo $tag
            #echo $nombreGPO

            $newtag = $tag.Substring(1)

            Remove-GPLink -Name "$datos1" -Target "$newtag" > /null

            #Write-Output "";
            #Write-Host "El link de $nombreGPO en $newtag se ha eliminado correctamente" -ForegroundColor DarkGreen
             echo 0 > .\scripts\obj\gui\docs\compbolink.txt
            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            #Write-Host "";
           # Write-Host " Error con alguno de los datos introducidos" -ForegroundColor DarkRed
            echo 100 > .\scripts\obj\gui\docs\compbolink.txt
        }
    
   }
   
   else {
  # Write-Host "";
  # Write-Host " La unidad organizativa $nombreUO no existe" -ForegroundColor DarkRed
   echo 100 > .\scripts\obj\gui\docs\compbolink.txt
   

   }






}

else {
 
           # Write-Host " La GPO $nombreGPO no existe" -ForegroundColor DarkRed
           echo 100 > .\scripts\obj\gui\docs\compbolink.txt

}