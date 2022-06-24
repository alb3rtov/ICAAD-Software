$stdout = Get-NetAdapter -Name "*" | Select-Object "Name"

return $stdout

