#$proc = Get-ComputerInfo OsName,CsNetworkAdapters,OsTotalVisibleMemorySize
$stdout = Get-NetAdapter -Name "*" | Select-Object "Name"

return $stdout

