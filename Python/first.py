# import 
from datetime import datetime

name = "teppo tepnadi" # string ehk sõne
age = 47 # täisarv (integer)
height = 1.85 # ujukomaarv (float)
print(name, age, height) # väljastab muutuja väärtused
print(f"kasutaja {name.title()} vanuses {age} ja pikkusega {height} meetrit istub laua taga") 
print("kasutaja " + name + " vanuses " + str(age) + " ja pikkusega " + str(height) + " meetrit istub laua taga")

# Arvutamine
birth_year = datetime.now().year - age # jooksev aasta - vanus
print(f"{name.title()} on sündinud aastal {birth_year}")# import 
print (birth_year)

name = name.title() # muuda nimi suure tähega algavaks korrasta nimi ja kasuta sama muutujat
print(name[0])
print(name[1:5]) # väljund on eppo
print(name[6:]) # väljund on Tepnadi
print(name[:5]) # väljund on Teppo  
print(name[::-1]) # väljund on i


age = input("siseta vanus: ") # kasutaja sisestab vanuse
age= int(age)
if age < 1 or age > 122:
    print("vanus peab olema vahemikus 1-122")
elif age < 18:
    print("oled alaealine") 
elif age < 65:
    print("oled tööealine")
elif age < 100:
    print("oled pensionär") 
else:
    print("oled väärikas vanur") 

    # lühike või pikk nimi
place = input("sisesta elukoht: ")
print(f"sistati: {place}")

if len(place) > 1 and len (place) <= 7:
    print(f"lühikese nimega koht {place.title()}")
elif len(place) > 7:
    print(f"pikea nimega koht {place.title()}")
else:
    print("nimi on liiga lühike")

# väljasta muutujate andmetüübid
print(type(name))
print(type(age))
print(type(height))
print(type(birth_year))
print(type(place))



