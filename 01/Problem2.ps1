$Frequencies = Get-Content $PSScriptRoot\Input.txt
[int]$Total = 0
$Seen = New-Object System.Collections.Generic.HashSet[int]

$index = 0
while (!$Seen.Contains($Total))
{
    $Seen.Add($Total) | Out-Null

    if ($index -ge $Frequencies.Length)
    {
        $index = 0
    }

    $Total += [int] $Frequencies[$index]
    $index++
}

return $Total