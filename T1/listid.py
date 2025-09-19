places = [] # tühi list

places.append("Kehtna") # lisa lõppu
places.append("Tallinn") # lisa lõppu
places.append("Kullamaa") # lisa lõppu
places[1:1] = ["Tartu", "Pärnu"] # lisa Kehtna ja Tallinna vahele
places.extend(["Viljandi", "Kehtna","Rapla"]) # lisa mitu kohta korraga
places.insert(2, "Are")

print(places) # prindib kogu listi

# Kustutamine
places.remove ("Kehtna") # kustutab esimesena leitud Kehtna
places.pop(6) # kustutab 7. indeksi ehk viimase
del places[2] # kustutab kolmanda

print(places)

# Ülesanne lisa Rapla lõppu ja peale Pärnut
places.insert(2, "Pärnu")
places.insert(-1, "Rapla")
places.insert(3, "Rapla")

print(places)

place = places[-1] # muutuja saab väärtiuseks listi viimase elemendi
index = places.index(place) # mitmes element on Rapla (ainult üks)
count = places.count(place) # loe kokku mitu Raplat on nimekirjas
print(index, count)

if place in places: # kui Rapla on listis
    print(f"{place} on nimkeirjas") # siis prindi see

# Koopia nimekirjast
list_copy = places.copy() # kopeeri list
list_list = list(places) # teine võimalus kopeerimiseks

print(places)
print(list_list)
print(list_copy)   

print() # tühi rida

list_copy.sort() # sorteeri koopia tähestikujärjekorda A-Z
list_list.sort(reverse=True) # sorteeri teine koopia Z-A
print(list_copy)
print(list_list)

new_sorted_list = sorted(places, reverse=False) # kolmas võimalus sorteerimiseks
print(new_sorted_list)

# tühjenda listi sisu
new_sorted_list.clear()

list_copy.clear()
list_list.clear()
print(new_sorted_list  )
print(list_copy)
print(list_list  )
print(places) # prindib kogu listi

#väljasta litsi places viimane element ilma [-1] kasutamata
print(places[len(places)-1]) 
print(places)

# väljasta konsooli elemndi Pärnu keskmine täht trükitähena
print(places[places.index("Pärnu")][len("Pärnu")//2].upper())  
print(places[2][2].upper())
city = places[2] # Elememnt
char = city[2].upper() #Täht
print(char)

