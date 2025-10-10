import random

names = ["Mari", "Anna", "Villem", "Jüri"]

# väljasta listis olevad nimend nime kaupa eraldi real
for name in names:
    print(name)

print() # tühi rida
# Teist moodi väljastus
for x in range(len(names)): # x = 0..3
    print(names[x], random.randint(1, 122)) # prindib nime ja juhusliku arvu 1-122
print() #tühi rida

#lihtsalt numbrid
for x in range (1,5): # 1,2,3,4
    print(x, end=" ") # prindib numbrid ühele reale
print("\n") # kaks reavahetust

for x in range(0, 10, 2): # paarisarvud
    print(x, end=" |")
print("\n") # kaks reavahetust 

x = 0
while x < len(names):
    print(names[x])
    x += 1 # x = x + 1
print(x)

"""
Väljasta lisit nimed konsoli iga nimi erlai real, kuid iga nime ees on järjekorranumber. Järjekorranumber algab ühega, korrentken rida on järgnev:
1. Mari
2. Anna
3. Villem
4. Jüri

Täiendus: Tee igale nimele juhuslik vanus, kuid kirjuta see vanus listi nimega ages. Näita tulemust samas for või while loopis. 
Peale kordust näita nii names, kui ages listi siu lihtsalt nagu listid.py näitasime.
"""

for x in range(1, 5, 1): # paarisarvud
    print(x, end=". ")

print("\n") # kaks reavahetust
x = 0
ages = [] # vanused list
while x < len(names):
    ages.append(random.randint(1, 122)) # lisa listi juhuslik vanus
    print(str(x+1) + ". " + names[x], ages[x]) # prindi nime ja vanuse
    x += 1 # x = x + 1
print (names)
print (ages)

ages2 = []
for x in range(len(names)):
    ages2.append(random.randint(1, 122)) # lisa listi juhuslik vanus
print(f"{x+1}. {names[x]} {ages2[x]}") # prindi nime ja vanuse2

print (names)
print (ages2)

print ()

print("arvud")