"""
Andmete generaator
Loo programm, mis genereerib juhuslike numbritega täidetud ruudukujulise maatriksi ja
Ekraanipilt 1 Numbrid failis 5x5
"""

import random
import csv

dst = "output.txt" # siia salvestan genereeritud numbrid 

def loo_maatriks(suurus): # see funktsioon genereerib suvalised numbrid vahemikus 01-99 vastavalt dailoogaknas küsitud arvule.
      return [[f"{random.randint(1, 99):02}" for _ in range(suurus)] for _ in range(suurus)] 
suurus = int(input("Palun sisesta maatriksi suurus (3-10): ")) # kasutajalt küsitkase maatriksi suurust.
if 3 <= suurus <= 10: # vahenmiku tingimus.
    maatriks = loo_maatriks(suurus) # kasutan funktsiooni loo_maatriks koos kasutajalt saadud arvuga.
    with open(dst, "w", encoding="utf-8",  newline='') as f: # loon faili output.txt kirjutamisõigusega.
        writer = csv.writer(f, delimiter=" ") # kasutan tühikut eraldajana
        writer.writerows(maatriks) # kirjutan maatriksi faili
else:
    print("arv ei sobi, palun sisesta number vahemikus 3 kuni 10.") # Ma ei saa päriselt aru :D et kas veateadet ikka oli vaja?  
