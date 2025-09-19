"""
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
"""

import csv
import unicodedata

src = "data/Persons.csv" # algallikas
dst = "data/persons_accounts.csv" #uus fail
header = "eesnimi;perenimi;isikukood;kasutajanimi;epost" # uue faili päis
domain = "@asutus.ee" 

filename = "data/Persons.csv"

def strip_accents(s):
    """
    eemaldab rõhumärgid ja täpitähed
    https://stackoverflow.com/questions/517923/
    """
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

# print(strip_accents("äöüž")) - test

with open(src, "r", encoding="utf-8") as f: #lugemiseks algne
    with open(dst, "w", encoding="utf-8") as d: #kirjuitamiseks uus
        contents = csv.reader(f, delimiter=";") # faili sisu muutjasse
        d.write(header + "\n") # uue faili päis reavahetusega
        next(contents) # vii lugemisjärg järgmisle reale

        for row in contents:
            date = row[2] # kuupoäev eraldi muutujasse
            year = int(date.split(".")[2]) # võta aasta kuup'evast ja tee täisarv
            if year >= 1990 and year <= 1999:
                first_name = row[0] # eesnimi eraldi muutujasse
                last_name = row[1] #perenimi eraldi muutjasse

                # eemalda tühik ja sidekriips
                first_name = first_name.replace(" ","") # tühik
                first_name = first_name.replace("-","") # sidekriipos

                # kasutajanime loomine
                username = ".".join([first_name, last_name]).lower()
                username = strip_accents(username) # eemalda rõhumärgid

                # eposti loomine
                email = username + domain 
                
                # Uue rea loomine 
                new_line = ";".join(row[:2] + [row[-1], username, email])
                d.write(new_line + "\n")
                # test print(row[0], row[1], first_name, last_name, username, email)




