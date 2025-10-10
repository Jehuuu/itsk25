filename = "data/Create-MyCSV-v.csv"
column = 2 # veerg mida kokku liita
total = 0 # veeru summa

with open(filename, "r") as f:
    contents = f.readlines() # loeb faili sisu muutujasse.
    for line in contents: #rea kaupa läbi käimine
        line = line.strip() #eemalda tühikud ja reavahetus
        parts = line.split(";") #tükelda semikoolonist
        if parts[column].isdigit(): #kas kõik on numbrid
            total += int(parts[column]) #liida number juurde
            # print(parts[column]) #faili sisu kontrollimiseks, realõpus reavahetus.

print(total)