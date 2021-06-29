$hash = $null

$hash = @{}

$proc = Get-ComputerInfo OsName,CsNetworkAdapters,OsTotalVisibleMemorySize

$hash.add("OsName",$proc.OsName)
$hash.add("CsNetworkAdapters",$proc.CsNetworkAdapters)
$hash.add("OsTotalVisibleMemorySize",$proc.OsTotalVisibleMemorySize)

return $hash