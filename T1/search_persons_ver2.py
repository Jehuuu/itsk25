filename = "data/Persons.csv"
total = 0

phrase  = input("sisesta otsitav fraas (min 2 märku):")

if len(phrase.strip()) > 1:
    phrase = phrase.strip().lower() # korrasta otsingu fraas
    f = open(filename,  "r", encoding="utf-8") # ava fail lugemiseks
    contents = f.readlines()[1:] # alates teisest reast
    f.close() # sulge fail
    for line in contents: # käi list rea kaupa läbi
        line = line.strip() #korrasta rida (eemalda reavahetus rest \n)
        if phrase in line.lower(): # kas fraas on olemas
            print(line) #väljasta nimed ridades
            total += 1 # suurenda loendurit
    
    print(f"leiti {total} nime.") # leitud ridade nimede arv, näitab ekraanil
        
else:
    print("otsingu fraas on liiga lühike!")
