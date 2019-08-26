dcdiag > .\scripts\cup\temp\dcdiag.txt

Get-Content .\scripts\cup\temp\dcdiag.txt | where{$_-match"is not a Directory Server"} > .\scripts\cup\temp\checkdcdiag.txt



