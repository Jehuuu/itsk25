<#
äraarvamise mäng. numbrid 1-100
Tagauks
Kui mäng on läbi, küsitakse nime ja koos sammudega kirjutatakse faili 
#>

$pc_nr = Get-Random -Minimum 1 -Maximum 100
[System.Boolean]$game_over = $false
$Global:steps = 0 # Globaalne muutuja sammud
$filename = Join-Path -Path $PSScriptRoot -ChildPath "result.txt"
# Write-Host $pc_nr $filename # kontrolliks

function writetofile {
    $name = Read-host "mängija nimi"
    ($name, $Global:steps -join ";") | Out-File -FilePath $filename -Append
}

function Show-Scoreboard {
    $content = Get-Content -Path $filename
    foreach ($line in $content) {
        Write-Host $line.split(";")
    }
}

function LetsPlay {
    [int]$user_nr = Read-Host "siseta number"
    $global:steps++ # $Global:steps += 1
    $game_over = $false

    if(($user_nr -gt $pc_nr) -and ($user_nr -ne 1000)) {
        Write-Host "väiksem"
    } elseif (($user_nr -lt $pc_nr) -and ($user_nr -ne 1000)) {
        Write-Host "suurem"
    } elseif (($user_nr -eq $pc_nr) -and ($user_nr -ne 1000)) {
        Write-Host "leidsid õige numbri $Global:steps sammuga."
        $game_over = $true
    } elseif ($user_nr -eq 1000) {
        Write-Host "leidsid mu nõrga koha. õige number on $pc_nr"
    }
    return $game_over # tagastab tulemuse $true või $false
}

while ($game_over -eq $false) {
    $game_over = LetsPlay
    if($game_over) {
        writetofile
        Show-Scoreboard
        $answer = Read-Host "kas mängime veel? [J/E]"
        if($answer -eq "j") {
            $pc_nr = Get-Random -Minimum 1 -Maximum 100
            [System.Boolean]$game_over = $false
            $Global:steps = 0
        }
    }       
}

Write-Host "mäng läbi!"