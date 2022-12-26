'''# Exercise 1


# question 1

my_fav_numbers = {"76001688","76605385","54039620","66681682","64879317","72684947","54678447","64000000"}
print(my_fav_numbers)
print(len(my_fav_numbers))
print("************************************************************************************************************")
# question 2

my_fav_numbers.add("73679924")
my_fav_numbers.add("60598102")
print(my_fav_numbers)
print(len(my_fav_numbers))
print("************************************************************************************************************")

# question 3

my_fav_numbers.remove("64000000")
print(my_fav_numbers)
print(len(my_fav_numbers))
print("************************************************************************************************************")
# question 4

friend_fav_numbers = {"64973152","64052051","64279452","75364491","55282524"}
print(friend_fav_numbers)
print(len(friend_fav_numbers))
print("************************************************************************************************************")

# question 5

our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)
print(len(our_fav_numbers))'''



# Exercise 2

'''Non il n'est pas possible d'ajouter des entier a ce tuple d'entiers car un tuple n'est pas modifiable une fois crreer car il n'a pas de methode append ou extend. Les tuples sont immuables.
Cependant on peut creer un nouveau tuple et faire concatenation avec l'ancien tuple avec l'operateur + '''



# Exercise 3

'''basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
print("************************************************************************************************************")

# question 1

basket.remove("Banana")
print(basket)
print("************************************************************************************************************")

# question 2

basket.remove("Blueberries")
print(basket)
print("************************************************************************************************************")

# question 3

basket.append("Kiwi")
print(basket)
print("************************************************************************************************************")

# question 4

basket.insert(0,"Apples")
print(basket)
print("************************************************************************************************************")

# question 5

repetition = basket.count("Apples")
print(repetition)
print("************************************************************************************************************")

compteur = 0
for i in basket:
	if i == "Apples":
		compteur += 1
		print(compteur)

# question 6

basket.clear()
print(basket)
print("************************************************************************************************************")

# question 7

print(basket)
print("************************************************************************************************************")'''



# Exercise 5


# question 1

'''for i in range(1,21):
	print(i)

# question 2

mes_nombres = list(range(1,21))
for i in mes_nombres:
	if mes_nombres.index(i)%2 == 0:
		print(i)'''


# Exercice 6

'''votre_nom = input("Veuillez entrer votre nom : ")
my_name = "Mohamed"
while votre_nom.lower() != my_name.lower():
	print("Oups!!!")
	votre_nom = input("Veuillez entrer votre nom : ")
print("Supeerrrr")'''

# Exercice 7

'''fruits = input("Veuillez entrer votre ou vos fruits preferer separer d'un espace svp : ")
fruits_pref = fruits.split(" ")
print("Voici la liste de vos fruits preferer : ",fruits_pref)
print()
fruit = input("Veuillez entrer un nouveau fruit :")
if fruit in fruits_pref:
	print("Vous avez choisi l'un de vos fruits préférés! Prendre plaisir! ")
else:
	print("Vous avez choisi un nouveau fruit. J'espère que vous apprécierez")
	fruits_pref.append(fruit)
	print("La nouvelle liste de vos fruit preferer sont : ", fruits_pref)'''


# Exercice 8

'''ma_pizza = []
prix_unit_garni = 10
mes_garnitures = input("Veuillez entrer la garniture de votre pizza (taper quitter pour arreter) :")
quitter = "quitter"
while mes_garnitures.lower() != quitter.lower():
	ma_pizza.append(mes_garnitures)
	print("Vous venez d'ajouter " + mes_garnitures + " à votre pizza.")
	mes_garnitures = input("Veuillez entrer la garniture de votre pizza (taper quitter pour arreter) :")
print("Voici les differentes garnitures de votre pizza :", ma_pizza)
prix_pizza = prix_unit_garni + (len(ma_pizza) * 2.5)
print("Le prix total de votre pizza est de " + str(prix_pizza) + " dollars.")'''


# Exercice 9


# Exercice 10


# Exercice 11