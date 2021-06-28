$check = Get-WindowsFeature -name AD-Domain-Services* | where {$_.installed -eq $true}

if ($check.length -eq 0) {
    return $false
} else {
    return $true
}