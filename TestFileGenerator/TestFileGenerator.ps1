function new-testfile {
    <#
    .SYNOPSIS 
        loob testifailile määratud arvul juhusliku sisu ja laiendiga.
    .DESCRIPTION
        Funktsioon loob file failihalduse harjutamiseks...
    .PARAMETER Count
        Mitu faili luua (kohustuslik)
    .PARAMETER Names
        Failinimed mida kasutada. Üks kuni mitu. Vaikimisi $env:USERNAME
    .PARAMETER Path
        Kuhu failid luuakse. Vaikimisi Desktop\katsetus
    .PARAMETER ExtensionFile
        Faililaiendite loetelu. Vaikimisi extension.txt mooduli kaustas
    .EXAMPLE
        New-TestFile -Count 5
        Loob 5 faili kasutadesd sisseloginud kasutajanime failinimeks 
    .EXAMPLE
        New-TestFile -Count 3 -names "Aruanne", "Mari", "Jüri"
        Loob kolm juhuslikku faili etteantud nimedega
    #>

    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true)]
        [ValidateRange(1,1000)]
        [int]$Count, 

        [Parameter(Mandatory=$false)]
        [string[]]$Names, 

        [Parameter(Mandatory=$false)]
        [string]$Path = "$env:USERPROFILE\desktop\katsetus",

        [Parameter(Mandatory=$false)]
        [string]$extensionFile = "$PSScriptRoot\extension.txt"
    )

    # Kui nimed puuduvad kasuta kasutajanime
    if (-not $Names -or $Names.Count -eq 0) {
        $Names = @($env:USERNAME)
        Write-Verbose "Kasutan vaikimisi nime $env:USERNAME"
    }

    # Kas laiendite fail on olemas
    if(-not (Test-Path $extensionFile)) {
        Write-Error "laiendite faili ei leitud: $extensionFile"
        Write-Host "Loo liendite fail ja lisa laiendid"
        return
    }

    # Loe laiendite faili 
    $extension = Get-Content $extensionFile | Where-Object { $_.trim() -ne "" } | ForEach-Object { $_.trim() }

    if ($extension.count -eq 0) {
        Write-Error "Laiendite fail on tühi: $extensionFile"
        return
    }

    Write-Verbose "leitud $($extension.count) laiendit."

    # Loo kaust kui puudub 
    if(-not (Test-Path $Path)) {
        New-Item -Path $Path -ItemType Directory -Force | Out-Null
        Write-Host "loodud kaust $Path"
    }

    # Loome failide loenduri
    $createdCount = 0
    $skippedCount = 0
    $createdFiles = @()

    #genereeri failid
    for($i = 0; $i -lt $Count; $i++ ) {
        # vali juhuslik nimi
        $randomname = $Names | Get-Random   

        # vali juhuslik laiend
        $randomextension = $Extension | Get-Random 

        # koosta failinimi
        $filename = "$randomname.$randomextension"
        $fullPath = Join-Path $Path $filename

        # Kas fail on juba olemas
        if(Test-Path $fullPath) {
            Write-Warning "fail on juba olemas, jätan vahele: $filename"
            $skippedCount++
            continue
        }

        # Kas selline kombinatsioon on juba olemas
        if($createdfiles -contains $filename) {
            Write-Warning "selline kombinatsioon on juba olemas, jätan vahele"
            $skippedCount++
            continue
        }

        # Genereeri juhuslik sisu 
        $contentsize = Get-Random -Minimum 1 -Maximum 1025
        $randomcontent = -join ((1..$contentsize) | ForEach-Object {
            [char](get-random -Minimum 32 -Maximum 127)
        })

        # Loo fail
        try {
            Set-content -path $fullpath -Value $randomcontent -encoding UTF8 -ErrorAction Stop
            $createdCount++
            $createdFiles += $filename
            Write-Verbose "loodud $filename ($contectSize baiti)"
        } catch {
            Write-Error "Viga faili loomisel ($filename): $_"
            $skippedCount++
        }

        # teata tulemustest
        Write-Host "loodud faile: $createdcount"
        if ($skippedCount -gt 0) {
            Write-Host "Vahele jäetud (duplikaadid): $skippedcount"
        }
        Write-Host "Asukoht: $Path"

        # Tagasta objekt tulemusega
        [PSCustomObject]@{
            Created = $createdcount
            Skipped = $skippedCount
            Location = $Path
            Files = $createdFiles
        }

    }

}