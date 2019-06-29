
Get-WindowsFeature -name AD-Domain-Services* | where {$_.installed -eq $true}> .\scripts\comp\docs\adcheck.txt

$contador = (Get-Content .\scripts\comp\docs\adcheck.txt).Count

#echo $contador
