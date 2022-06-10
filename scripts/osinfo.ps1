$hash = $null

$hash = @{}

#$proc = Get-ComputerInfo OsName,CsNetworkAdapters,OsTotalVisibleMemorySize
$proc = Get-ComputerInfo OsName,OsTotalVisibleMemorySize

$hash.add("OsName",$proc.OsName)
#$hash.add("CsNetworkAdapters",$proc.CsNetworkAdapters)
$hash.add("OsTotalVisibleMemorySize",$proc.OsTotalVisibleMemorySize)

return $hash