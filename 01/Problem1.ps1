$Frequencies = Get-Content .\Input.txt
[int]$Total = 0
$Frequencies | % {
    $Total += [int] $_
}

return $Total