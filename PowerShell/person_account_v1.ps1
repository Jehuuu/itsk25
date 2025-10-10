<#
Luua ettenatud kasutajatele kasutajanimi ja e-posti aadress
KASUTAJANIMI
    eesnimi.perenimi
    eesnimes eemaldada tühik ja/või sidekriips Mari Liis, Mari-Liis
    eemaldada rõhumärgid ja täpitäehd (äöõüž)
    kasutajanimi on läbivalt väikeste tähtedega
EPOSTIAADTRESS
    kasutajanimi@asutus.ee
KELLLELE TEHA
    Sündinud 1990-1999 k.a.
UUE FAILI SISU ON:
eesnimi;perenimi;isikukood;kasutajanimi;epost
Eesnimi;Perenimi;Sünniaeg;Sugu;Isikukood <-- originaal

https://stackoverflow.com/questions/7836670
#>

$src = Join-Path -path $PSScriptRoot -ChildPath ".\Persons.csv"
$dst = Join-Path -path $PSScriptRoot -ChildPath ".\Persons_accounts_v1.csv"
$domain = "@asutus.com"
$header = "Eesnimi;Perenimi;Isikukood;Kasutajanimi;EPost"
$pattern = "dd.MM.yyyy" # Kuupäeva vorming failis
$counter = 0


function Remove-Diacritics {
    # https://stackoverflow.com/questions/7836670
    param ([String]$src = [String]::Empty)
    $normalized = $src.Normalize( [Text.NormalizationForm]::FormD )
    $sb = new-object Text.StringBuilder
    $normalized.ToCharArray() | % { 
        if( [Globalization.CharUnicodeInfo]::GetUnicodeCategory($_) -ne [Globalization.UnicodeCategory]::NonSpacingMark) {
        [void]$sb.Append($_)
    }
  }
  $sb.ToString()
}
# Kas uus fail on olemas
if(Test-path $dst) {
    Remove-Item $dst
}

# Kirjutame uude faili päise
Out-File -FilePath $dst -Append -InputObject $header

# Loeme originaalfaili ja töötleme ridu
Import-Csv $src -Delimiter ";" | ForEach-Object {
   $date_str = $_.Sünniaeg
   $isvalid = [DateTime]::ParseExact($date_str, $pattern, $null)
   if($isvalid){
        $date = [datetime]::ParseExact($date_str, $pattern, $null)
        if($date.Year -ge 1990 -and $date.Year -le 1999){
            $counter++

            $first_name = $_.Eesnimi
            $last_name = $_.Perenimi

            # Eemaldame tühiku ja sidekriipsu eesnimest
            $first_name = $first_name -replace " ",""
            $first_name = $first_name -replace "-",""

            # loome kasutajanime
            $username = Remove-Diacritics($first_name, $last_name -join ".").ToLower()

            # loome e-posti
            $email = $username + $domain

            # Teeme massiivi veergudest
            $array = $_.Eesnimi, $_.Perenimi, $_.Sünniaeg, $username, $email

            # Teeme uue rea faili
            $new_line = $array -join ";"

            # Write-Host $new_line
            Out-File $dst -Append -InputObject $new_line
        }
   } 
}
Write-Host "Valmis, $counter tk."  