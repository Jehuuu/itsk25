<#
Loo programm, mis loeb eelmise skripti väljundit (output.txt) ning arvutab
iga rea ja veeru summa. Kogu tulemus tuleb konsooli, seega esmalt näitab
kuidas numbrid on failis ning siis info rea summade kohta ja veeru summade
kohta. Lõppu näitab leitud suurim ja väikseim number.
#>

$src = "output.txt" # arvud loeme eelmises ülesandes loodud failist

Write-Host ""
Write-Host "Maatriks:"
$failiSisu = Get-Content $src
$failiSisu | Write-Output
Write-Host "" # tühi rida

$maatriks = @() # massiiv
$koikNumbrid = @() # kõik numbrid ühte kohta, et leida suurim ja väikseim
    foreach ($ridaStringina in $failiSisu) { # käime läbi iga rea faili sisus
        $numbridReas = $ridaStringina -split '\s+' | ForEach-Object { [int]$_ }
        $maatriks += ,$numbridReas # lisame rea maatriksisse
        $koikNumbrid += $numbridReas # lisame kõik numbrid ühte kohta
}

Write-Host "Rea summad:" # siia kirjutame rea summa.
$reaIndeks = 1
    foreach ($rida in $maatriks) {
        $reaSumma = ($rida | Measure-Object -Sum).Sum  # kasutan Measure-Object cmdlet'i, et leida rea summa
        Write-Host "Rea $reaIndeks summa on: $reaSumma"
        $reaIndeks++
}
Write-Host ""

Write-Host "Veeru summad:" # siia kirjutan veeru summa.
$veergudeArv = $maatriks[0].Count # leian mitu veergu on esimeses reas.

    for ($i = 0; $i -lt $veergudeArv; $i++) { # käin läbi kõik veerud alates nullist
        $veeruNumbrid = $maatriks | ForEach-Object { $_[$i] } # kogun kokku kõik arvud mis asuvad veerus $i
        $veeruSumma = ($veeruNumbrid | Measure-Object -Sum).Sum # arvutan nende arvude summa.
        Write-Host "Veeru $($i + 1) summa on: $veeruSumma" # kasutan $($i + 1) veerunumbri jaoks.
}
Write-Host ""

$suurim = ($koikNumbrid | Measure-Object -Maximum).Maximum # leian suurima arvu kõikide numbrite seast
$vaikseim = ($koikNumbrid | Measure-Object -Minimum).Minimum # leian väikseima arvu kõikide numbrite seast

Write-Host "Suurim arv: $suurim"
Write-Host "Väikseim arv: $vaikseim"
Write-Host ""
