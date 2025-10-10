"""Täiendus: näita minu nime leiti. leiti xx nime."""
import csv
total = 0

filename = "data/Persons.csv"

phrase = input("sisesta otsitav fraas (min 2 märki):")

if len(phrase) > 1:
    with open(filename, "r", encoding="utf-8") as f:
        contents = csv.reader(f, delimiter=";")
        for row in contents:
            phrase = phrase.lower() # tee väiketäheks
            first = row[0].lower() # tee väiketäheks (eesnimi)
            last = row[1].lower() # tee väiketäheks (perenimi)
            if phrase in first or phrase in last:
                print(";".join(row)) # tee list stringiks
                total +=1

        print(f"leiti {total} nime.")

else:
    print("otsitav fraas on liiga lühike")