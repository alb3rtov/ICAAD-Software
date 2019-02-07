#Write-Output "";
#Write-Host " [*] Los usuarios se crean automáticamente deshabilitados por seguridad de la contraseña" -ForegroundColor Yellow
#Write-Output "";
#Write-Host " [*] Utiliza la 5º opcion del menú para habilitar/deshabilitar usuarios de AD" -ForegroundColor Yellow
#Write-Output "";
#$nombreGrupo = read-host " Nombre de grupo a crear"
#Write-Output "";



$datos = Get-Content ".\scripts\obj\gui\docs\creargrupogui.txt"



try {

    Get-ADGroup -Filter "Name -eq '$datos'" > .\scripts\obj\gui\docs\creargrupogui.txt

}

catch [System.Management.Automation.RuntimeException] {
      
        if ($_.Exception.Message -ilike "Error"){
        }

    #Write-Host " Error, algún dato es erróneo" -ForegroundColor DarkRed
    #Write-Output "";

}

$contador = (Get-Content .\scripts\obj\gui\docs\creargrupogui.txt | where{$_-match"$datos"}).Count


#$confirmacion = read-host " ¿Desea especificar una unidad organizativa (por defecto: CN=Users)? (s/n)"
#Write-Output "";



#Write-Host " [*] Unidades organizativas encontradas" -ForegroundColor Yellow

#Get-ADOrganizationalUnit -Filter 'Name -like "*"' | Format-Table Name,DistinguishedName -A

   # $nombreUO = read-host " Ruta donde crear el grupo (UO o contenedor)"
   # Write-Output "";

    if ($contador -eq 0) {
    
        try {

            #echo $contador2


                #echo $tag

                New-ADGroup -Name "$datos" -GroupScope Global

                #Write-Host " Grupo $nombreGrupo creado correctamente en$tag" -ForegroundColor DarkGreen

                echo 0 > .\scripts\obj\gui\docs\compcgrupo.txt
       

            }

        catch [System.Management.Automation.RuntimeException] {
            if ($_.Exception.Message -ilike "Error"){
            }
            #Write-Host " Error, algún dato es erróneo" -ForegroundColor DarkRed

            echo 100 > .\scripts\obj\gui\docs\compcgrupo.txt
        }
    }

    else {
        #Write-Host " El grupo $nombreGrupo ya está creado" -ForegroundColor DarkRed

        echo 100 > .\scripts\obj\gui\docs\compcgrupo.txt

    }

    
 
