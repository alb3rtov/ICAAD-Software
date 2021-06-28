$hash = $null

$hash = @{}

$proc = Get-ComputerInfo OsName,CsNetworkAdapters

$hash.add("OsName",$proc.OsName)
$hash.add("CsNetworkAdapters",$proc.CsNetworkAdapters)

return $hash