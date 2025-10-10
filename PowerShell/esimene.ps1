<#
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
    Käivita see käsklus käsureal administraatorina 
#>
Clear-Host # puhasta ekraan: cls
Get-Date # näita tänast kuupäeva

$username = Read-Host -Prompt "Sisesta enda kasutajanimi"

if($username -eq $env:USERNAME){
    Write-Host "õige kasutajanimi"
} else {
    Write-Host "vale kasutajanimi $username, eeldati: $env:USERNAME"
}

[int]$year = Read-Host "siseta aasta" # int teeb täisarvuks ja ümardab.
if($year -eq (Get-Date).Year){
    Write-Host "käesolev aasta"
} else {
    Write-Host "Mõni teine aasta: $Year"
}

# massiv
$nums = @() # tühi massiiv
$nums += 5
$nums += 2
$nums += 6
$nums += Get-Random -Minimum 1 -Maximum 10

Write-Host $nums
Write-Host $nums[-1]
Write-Host $nums[$nums.lenght-1]

$num = 0 # algväärtus
$num += 5
$num += 3
$num += Get-Random -Minimum 1 -Maximum 10

Write-Host $num

<#
liida kokku kaks juhuslikku numnrit. mõlemad vahemikus 1-10.
vastus on muutujas $random 
#>
$random = (Get-Random -Minimum 1 -Maximum 10) + (Get-Random -Minimum 1 -Maximum 10)
Write-Host $random