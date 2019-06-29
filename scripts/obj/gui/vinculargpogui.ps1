
$datos1 = Get-Content ".\scripts\obj\gui\docs\vinculargpogui1.txt"


$datos2 = Get-Content ".\scripts\obj\gui\docs\vinculargpogui2.txt"



Get-GPO -all > .\scripts\obj\gui\docs\vinculargpogui3.txt

$contador1 = (Get-Content .\scripts\obj\gui\docs\vinculargpogui3.txt | where{$_-match"$datos1"}).Count

echo "" > .\scripts\obj\gui\docs\vinculargpogui4.txt


if ($contador1 -ne 0) {


#   Write-Host " [*] Unidades organizativas encontradas" -ForegroundColor Yellow


  # Get-ADOrganizationalUnit -Filter 'Name -like "*"' | Format-Table Name,DistinguishedName -A


   #$nombreUO = read-host " Nombre de unidad organizativa"

         Get-ADOrganizationalUnit -Filter "Name -like '$datos2'" > .\scripts\obj\gui\docs\vinculargpogui4.txt

         $contador = (Get-Content .\scripts\obj\gui\docs\vinculargpogui4.txt | where{$_-match"$datos2"}).Count

            if ($contador -ne 0) {
   
                try {

                    $string = Get-Content .\scripts\obj\gui\docs\vinculargpogui4.txt | where{$_-match"$datos2"}

                    $tag = $string.Split(":",4)[1]

                    #echo $tag
                    #echo $nombreGPO

                    $newtag = $tag.Substring(1)

                    New-GPLink -Name "$datos1" -Target "$newtag" > /null

                  #  Write-Output "";
                  #  Write-Host " $nombreGPO vinculada a $newtag" -ForegroundColor DarkGreen

                    echo 0 > .\scripts\obj\gui\docs\compvgpo.txt
                    }

                catch [System.Management.Automation.RuntimeException] {
                    if ($_.Exception.Message -ilike "Error"){
                    }
                    # Write-Host "";
                    # Write-Host " Error con alguno de los datos introducidos" -ForegroundColor DarkRed
                    echo 100 > .\scripts\obj\gui\docs\compvgpo.txt
                }
    
            }
  
  else {
  # Write-Host "";
  # Write-Host " La unidad organizativa $nombreUO no existe" -ForegroundColor DarkRed
  echo 100 > .\scripts\obj\gui\docs\compvgpo.txt
   
   
}





}

else {
 
            #Write-Host " La GPO $nombreGPO no existe" -ForegroundColor DarkRed
            echo 100 > .\scripts\obj\gui\docs\compvgpo.txt


}