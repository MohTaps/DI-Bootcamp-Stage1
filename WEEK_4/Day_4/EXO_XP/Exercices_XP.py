# Exercice 1 :  Qu'apprenez-Vous ?


'''def display_message():
    print("J'apprend le cour de python sur Developper Institute.")

display_message()'''


#Exercice 2 : Quel Est Votre Livre Préféré ?

'''def favorite_book(titre):
    print(f"L'un de mes livres preferer est le roman {titre}")
favorite_book("Soleil des independances")'''



# Exercice 3 : Quelques Géographies


'''def describe(ville,pays):
    print(f"La ville de {ville} se trouve au {pays}")
describe("Ouagadougou","BURKINA FASO")
print("")


def describe(ville,pays="PAYS DU MONDE"):
    print(f"La ville de {ville} se trouve dans un {pays}")
describe("Ouagadougou")
print()'''



# Exercice 4 : Aléatoire


'''import random

def compare_numbers(nombre):
    random_nombre = random.randint(1, 100)
    if nombre == random_nombre:
        print("Fizzzzzzzzzzzzzzzzzz ! Les deux nombres sont égaux.")
    else:
        print(f"Buzzzzzzzzzzzzzzzzz ! Les deux nombres sont différents. Votre nombre : {nombre}, nombre aléatoire : {random_nombre}.")

nombre = int(input("Entrer le nombre svp : "))
compare_numbers(nombre)'''


# Exercice 5 : Créons Des Chemises Personnalisées !

def make_shirt(size, text):
    print("The size of the shirt is " + size + " and the text is " + text)

make_shirt("Large", "I love Python")
The size of the shirt is Large and the text is I love Python

def make_shirt(size="Large", text="I love Python"):
    print("The size of the shirt is " + size + " and the text is " + text)

make_shirt()  # Uses default values for size and text
make_shirt("Medium")  # Uses default value for text
make_shirt(text="I love coding")  # Uses default value for size
make_shirt("Small", "I love skiing")  # Uses specified values for size and text

The size of the shirt is Large and the text is I love Python
The size of the shirt is Medium and the text is I love Python
The size of the shirt is Large and the text is I love coding
The size of the shirt is Small and the text is I love skiing
make_shirt(size="Large", text="I love Python")
make_shirt(text="I love coding", size="Medium")


# Exercice 6: Magiciens


noms_des_magiciens = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(noms):
    for nom in noms:
        print(nom)

show_magicians(noms_des_magiciens)


magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def make_great(names):
    great_names = []
    for name in names:
        great_names.append(" the Great" + " " name)
    return great_names

def show_magicians(names):
    for name in names:
        print(name)

new_magician_names = make_great(magician_names)
show_magicians(new_magician_names)



'''def show_magicians(magicians):
  for magician in magicians:
    print(magician)

def make_great(magicians):
  for i in range(len(magicians)):
    magicians[i] = 'the Great ' + magicians[i]

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Affiche les noms de tous les magiciens dans la liste
show_magicians(magician_names)

# Ajoute "the Great" au début de chaque nom de magicien
make_great(magician_names)

# Affiche à nouveau la liste de magiciens pour voir que les noms ont été modifiés
show_magicians(magician_names)'''


# Exercice 7: Conseils De Température



