from os import system


# Exercice 1 :  Qu'apprenez-Vous ?


def display_message():
    print("J'apprend le cour de python sur Developper Institute.")
print()
display_message()
print()
system('pause')
system('cls')



#Exercice 2 : Quel Est Votre Livre Préféré ?

def favorite_book(titre):
    print()
    print(f"L'un de mes livres preferer est le roman {titre}")
favorite_book("Soleil des independances")
print()
system('pause')
system('cls')




# Exercice 3 : Quelques Géographies


def describe(ville,pays):
    print(f"La ville de {ville} se trouve au {pays}")
describe("Ouagadougou","BURKINA FASO")
print("")

print("PAYS DU MONDE comme valeur de pays par defaut\n")
def describe(ville,pays="PAYS DU MONDE"):
    print(f"La ville de {ville} se trouve dans un {pays}")
new_ville = input("Entrer le nom d'une ville svp : ")
print()
describe(new_ville)
print()
system('pause')
system('cls')




# Exercice 4 : Aléatoire


import random

def comparaison_des_nombres(nombre):
    nombre_aleatoire = random.randint(1, 100)
    if nombre == nombre_aleatoire:
        print("\nFizzzzzzzzzzzzzzzzzz ! Les deux nombres sont égaux.")
    else:
        print(f"\nBuzzzzzzzzzzzzzzzzz ! Les deux nombres sont différents. Votre nombre : {nombre}, le nombre mystere est  {nombre_aleatoire}.")

nombre = int(input("\nVeuillez entrer le nombre de votre choix (entre 1 et 100) svp : "))
comparaison_des_nombres(nombre)
print()
system('pause')
system('cls')



# Exercice 5 : Créons Des Chemises Personnalisées !

def make_shirt(taille,message):
    print(f"\nLa taille de ce T-Shirt est {taille} et le texte sur ce T-Shirt est : {message}\n")

make_shirt('S','La plus petite taille')


def make_shirt(taille="3XL",message="I Love Python"):
    print(f"\nLa taille de ce T-Shirt est {taille} et le texte sur ce T-Shirt est : {message}\n")

print("Plus grande taille avec message par defaut\n")
make_shirt()

print("\nTaille choisie et message par defaut")
make_shirt('XXL')


print("\nTaille choisie et message quelquonque")
make_shirt("L","Taille large")
print()
system('pause')
system('cls')




# Exercice 6: Magiciens


magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(mes_magiciens):
    for magician in mes_magiciens:
        print(f"Veuillez accueillir Mr {magician}\n")

def show_magician(mes_magiciens):
    print(new)



def make_great(mes_magiciens):
    new=[]
    for magician in mes_magiciens:
        new.append("The great " + magician)
    return new

show_magicians(magician_names)

new=make_great(magician_names)
show_magician(new)
print()
system('pause')
system('cls')






# Exercice 7: Conseils De Température


from os import system

import random

def get_random_temp():
    return random.randint(-10, 40)

print("\n**************Un petit test pour les temperatures aleatoires*****************\n")
for i in range(5):
    print(f"\tIl fait {get_random_temp()} degree celcius aujourd'hui\n\n")


print("\n\n *************Affichage d'une temperature prise au hasard****************\n")

def main():
    le_temp = get_random_temp()
    if le_temp < 0:
        print(f"\nAujourd'hui, il fait {le_temp} degre Celcius.  Brrr, c'est glacial! Portez des couches supplémentaires aujourd'hui\n")
    elif le_temp > 0 and le_temp <= 16:
        print(f"\nAujourd'hui, il fait {le_temp} degre Celcius.  Assez froid! N'oubliez pas votre manteau\n")
    elif le_temp > 16 and le_temp <= 23:
        print(f"\nAujourd'hui, il fait {le_temp} degre Celcius.  Il fera normalement un beau temp, avec un vent doux\n")
    elif le_temp > 24 and le_temp <= 32:
        print(f"\nAujourd'hui, il fait {le_temp} degre Celcius.  Une temperature assez clemente\n")
    elif le_temp > 32 and le_temp <= 40:
        print(f"\nAujourd'hui, il fait {le_temp} degre Celcius.  Tres haute temperature, il fera chaud, hydratez vous\n")

main()
system('pause')
system('cls')

print("\n*******************Utilisation du nom correct des saisons svp ****************")

def get_random_temp(saison):
    if saison == 'hiver':
        return random.randint(-10, 16)
    elif saison == 'printemps':
        return random.randint(17, 23)
    elif saison == 'ete':
        return random.randint(33, 40)
    elif saison == 'automne':
        return random.randint(24, 32)

'''for saison in ['hiver', 'printemps', 'ete', 'automne']:
    print(f" Ex\n{get_random_temp(saison)}")'''


def get_random_temp(saison):
    if saison == 'hiver':
        return random.randint(-10, 16)
    elif saison == 'printemps':
        return random.randint(17, 23)
    elif saison == 'ete':
        return random.randint(33, 40)
    elif saison == 'automne':
        return random.randint(24, 32)

def main():
    saison = input("Veuillez entrer une des 4 saisons de l'annee svp (hiver, printemps, ete, automne): ").lower()
    temp = get_random_temp(saison)
    if temp < 0:
        print(f"\nAujourd'hui, il fait {temp} degre Celcius.  Brrr, c'est glacial! Portez des couches supplémentaires aujourd'hui.\n")
    elif temp >= 0 and temp <= 16:
        print(f"\nAujourd'hui, il fait {temp} degre Celcius.  Assez froid! N'oubliez pas votre manteau.\n")
    elif temp > 16 and temp <= 23:
        print(f"\nAujourd'hui, il fait {temp} degre Celcius.  Il fera normalement un beau temp, avec un vent doux.\n")
    elif temp > 23 and temp <= 32:
        print(f"\nAujourd'hui, il fait {temp} degre Celcius.  Une temperature assez clemente.\n")
    elif temp > 32:
        print(f"\nAujourd'hui, il fait {temp} degre Celcius.  Tres haute temperature, il fera chaud, hydratez vous.\n")

main()
system('pause')
system('cls')



print("********************Utilisation du numero du mois de 1 a 12 svp ********************")

def get_random_temp2(mois):
    if mois in (12,1,2):
        temperature=random.uniform(-10,16)
        temperature=round(temperature,1)
    elif mois in (3,4,5):
        temperature=random.uniform(16,23)
        temperature=round(temperature,1)
    elif mois in (9,10,11):
        temperature=random.uniform(23,32)
        temperature=round(temperature,1)
    elif mois in (6,7,8):
        temperature=random.uniform(32,40)
        temperature=round(temperature,1)
    return temperature


def main2():
    mois = int(input("\nVeuillez saisir le numero du mois auquel nous sommes actuellement (1=janvier,.....): "))
    temp = get_random_temp2(mois)
    if mois in (12,1,2):
        print(f"\nAujourd'hui, il fait {temp} degre Celcius.  Brrr, c'est glacial! Portez des couches supplémentaires aujourd'hui.")
    elif mois in (3,4,5):
        print(f"\nAujourd'hui, il fait {temp} degre Celcius.  Il fera normalement un beau temp, avec un vent doux.")
    elif mois in (9,10,11):
        print(f"\nAujourd'hui, il fait {temp} degre Celcius.  Une temperature assez clemente.")
    elif mois in (6,7,8):
        print(f"\nAujourd'hui, il fait {temp} degre Celcius.  Tres haute temperature, il fera chaud, hydratez vous.")

main2()
