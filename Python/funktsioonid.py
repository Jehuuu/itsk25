def welcome():
    """Vljastab staatilise tervitusteksti"""
    print("Tere, kuidas läheb?")

welcome() #väljastab teate defineeritud staatilise sõnumi.

def welcome_name(name):
    """Tagastab tervitussõnumi koos nimega."""
    return f"Tere, {name}"

def division(number1, number2):
    """teostab kahe arvu jagamise
    Args:
        number1 (float): jagatav arv
        number2 (float): jagaja (ei tohi olla null)
    
    Returns:
        float: jagtise väärtus"""
    
    if number2 !=0:
        return number1 / number2
    return -1
    
def introduce(name, age =25):
    
    """Loob lihtsa tutvustava lause
    
    :param name: isiku nimi
    :type name: str
    :param age: isiku vanus (vaikimisi 25)
    :type age, int, valikuline
    :return: tekstiline tutvustus vormis
                "Tema on <nimi> ja ta on <vanus> aastane!"
    :return: str
    """
    return f"tema on {name} ja ta on {age} aastane!"


welcome()
print(welcome_name("Teppo"))

kukimuki = welcome_name("Kukimuki") # tekitame muuutja mnida saab väljastada.
print(kukimuki)

a = 10
b = 5
print(division(a,b))
print(division(b,0))
print(division(b,a))
print(division(0,b))

print(introduce("Teppo"))
print(introduce("Juhan", 19))

"""
Ülesanne: Loo lost kolme nimega, Väljasta kolme nime tervitus."""

opilased = ["Kalle","Malle","Mati","Peeter","Karl"]

for x in range(len(opilased)): # see x siin ei pruugi olla kuigi vajalik.
    print(welcome_name(opilased[x]))

for name in opilased: # nii tegi õpetaja
    print(welcome_name(name)) # siin kasutatakse varasemalt defineeritud tegevust welcome_name

