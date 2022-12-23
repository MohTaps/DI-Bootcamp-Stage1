import random

# question 1

chaine = input("\nVeuillez entrer une chaine de caractere svp! : ")
while len(chaine) != 10:
    if len(chaine) > 10:
        print("Chaine trop longue")
    elif len(chaine) < 10:
        print("Chaine trop courte")
    chaine = input("Veuillez entrer une chaine de caractere svp! : ")
  

# question 2
        
first = chaine[0]
last = chaine[-1]
print(f"\nLa premiere lettre de votre chaine est  {first} et la derniere lettre est  {last}\n")


# question 3

nombre = ""
for element in chaine:
    nombre = nombre + element
    print(nombre)

# question 4
    
ma_liste = list(chaine)
random.shuffle(ma_liste)
chaine1 = ""
chaine1 = chaine1.join( ma_liste)
print()
print("Le mot une fois melanger est :\n")
print(chaine1)
