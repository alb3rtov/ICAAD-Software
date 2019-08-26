
Get-WindowsFeature -name AD-Domain-Services* | where {$_.installed -eq $true}> .\scripts\cup\temp\adcheck.txt

#$counter = (Get-Content .\scripts\cup\temp\adcheck.txt).Count

#echo $counter
