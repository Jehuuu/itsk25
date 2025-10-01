"""
Loo programm, mis:

1. Genereerib 20 juhuslikku täisarvu vahemikus 1–100.
2. Salvestab need koos tänase kuupäevaga faili andmed.txt.
3. Loeb failist need arvud uuesti sisse.
4. Kasutab funktsiooni (enda loodud funktsioon), mis arvutab: summa, keskmise ja suurima arvu.
5. Kuvab tulemused ekraanile (funktsiooni tulemused + failist loetud arvud).
6. Kirjuta funktsioonile dokumentatsioon (vaata vajadusel linke lõpust)

Näidis: failisisu on järgnev:
Kuupäev: 18.09.2025 22:07:10
Arvud: 53 40 54 25 96 78 45 30 12 63 9 90 97 97 71 3 59 53 15 64

Näidis tulemus ekraanile:
Failist loetud arvud: [53, 40, 54, 25, 96, 78, 45, 30, 12, 63, 9, 90, 97, 97, 71, 3, 59, 53, 15, 64]
Summa: 1054
Keskmine: 52.70
Suurim arv: 97
"""

# import
import random
from datetime import datetime
import csv

dst = "andmed.txt" # salvestame genereeritud numbrid faili andmed.txt
src = "andmed.txt" # koduse ülesande kolmandas punktis on eelnevalt loodud faili sisu vaja uuesti sisse lugeda.

genereeritud_numbrid = [random.randint(1, 100) for _ in range(20)] # genereerime 20 juhuslikku täisarvu vahemikus 1 kuni 100

now = datetime.now() # anname muutuja now väärtuseks tänase kuupäeva ja kellaaja
formatted_string = now.strftime("%d.%m.%Y %H:%M:%S") #formaadime kuupäeva ja kellaaja vastvalt ülesandes nõutule.

with open(dst, "w", encoding="utf-8") as q: # loome kirjutamisõigusega faili anmded.txt
       contents = csv.reader(q,delimiter=";") # faili sisu muutjasse
       q.write("Kuupäev: " + formatted_string + "\n") # kirjutame faili kuupäeva reavahetusega
       q.write("Arvud: " + str(genereeritud_numbrid).strip("[]") + "\n") # kirjutan faili genereeritud numbrid ilma nurksulgudeta ja lõppu lisan reavahetuse
       
with open(src, "r", encoding="utf-8") as r: # avame faili anmded.txt lugemisõigusega
    contents = csv.reader(r, delimiter=";") # ja loeme faili sisu muutujasse
    for row in contents: # totsin välja vajaliku rea
        if row and row[0].startswith("Arvud:"): # kui rida pole tühi ja algab sõnaga Arvud:
            numbers_str = row[0].replace("Arvud: ", "").strip("[]") # eemaldame sõna Arvud: ja nurksulgude
            genereeritud_numbrid = [int(num) for num in numbers_str.split(", ")] # teisendame stringi listiks täisarvudest

def calculate_stats(numbers): # siia panin kirja funktsiooni, mis arvutab summa, keskmise ja suurima arvu
    total = sum(numbers) # summa
    average = total / len(numbers) if numbers else 0 # keskmine
    maximum = max(numbers) if numbers else None # suurim numberarv
    return total, average, maximum  

summa, keskmine, suurim = calculate_stats(genereeritud_numbrid) # teostan vajalikud arvutused varaseamlt genrereeritud numbritest
print(f"Failist loetud arvud: {genereeritud_numbrid}") # kuvab ekraanil tulemuse nii nagu ülesandes nõutud
print(f"Summa: {summa}") # kuvab tulemuse summa 
print(f"Keskmine: {keskmine}") # kuvab tulemuse keskmine
print(f"Suurim: {suurim}") # kuvab tulemuse suurim number

"""
Ma väga loodan, et sain õigesti aru p.6 dokuementatsiooni kirjutaisest
""" 