dcdiag > .\scripts\comp\docs\dcdiag.txt

Get-Content .\scripts\comp\docs\dcdiag.txt | where{$_-match"no es un servidor de directorio"} > .\scripts\comp\docs\checkdcdiag.txt



