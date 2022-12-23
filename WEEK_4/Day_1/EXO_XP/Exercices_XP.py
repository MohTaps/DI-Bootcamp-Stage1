# Exercise 1

print(4*"Hello World\n")

# Exercise 2

print((99**3)*8)
print()
print()

# Exercise 3

5 < 3
output : False

3 == 3
output : True

3 == "3"
output : False

"3" > 3
output : Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'str' and 'int'

"Hello" == "hello"
output : False

# Exercise 4

computer_brand = "HP Elitebook 8440p"
print(f"I have a {computer_brand} computer")

# Exercise 5

name = "Mohamed Wendkuni TAPSOBA"
age = 22
shoe_size = 42
info = f"Je suis {name} et j'ai {age} ans et je chausse la pointure {shoe_size}.\n J'habite au Burkina Faso, je suis etudiant en Informatique 3eme annee a l'Universite Joseph Ki Zerbo."
print(info)
print()
print()

# Exercise 6

a = int(input("Veuillez entrer la valeur de a : "))
b = int(input("Veuillez entrer la valeur de b : "))
if a > b:
    print("Hello World")
else:
    print("Good bye")
    
# Exercise 7

nombre = int(input("Entrer un nombre : "))
if nombre == 0:
    print("0 n'est ni paire ni impaire")
elif nombre % 2 == 0:
    print(f"Le nombre {nombre} est paire")
else:
    print(f"Le nombre {nombre} est impaire")
print()
print()
    

# Exercise 8

my_name = "Mohamed"
your_name = input("Entrer votre nom : ")
if my_name.lower() == your_name.lower():
    print(f"Waouh!!! quelle surprise nous sommes des homonymes parfaits, tres ravi de faire votre connaissance")
else:
    print(f"Ravi de faire votre connaissance")
print()
print()
    

# Exercise 9

user = float(input("Saluuuttt Veuillez entrer votre taille en pouce : "))
if user*2.54 >= 145:
    print(f"Oui vous etes autorise a rouler car vous etes assez grand")
else:
    print(f"Desole vous n'etes pas autorise a rouler car vous n'avez pas la taille minimale requise, vous devrez grandir un peu plus avant d'y etre autoriser")