from os import system

import re

mot = input("\nEntrer un mot sans caractere speciale ni d'espaces svp: ")

while not re.match(r'^[a-zA-Z]+$', mot):
  print("\nVeuillez bien relire les consignes, entrer uniquement des lettres.")
  mot = input("\nEntrer un mot sans caractere speciale ni d'espaces svp: ")

lettre_index = {}

for i in range(len(mot)):
    lettre = mot[i]
    if lettre in lettre_index:
        lettre_index[lettre].append(i)
    else:
        lettre_index[lettre] = [i]

print("Syntaxe correct\n")

print(lettre_index)

system("pause")
system("cls")


tous_les_produits = {
  "Water" : "$1",
  "Bread" : "$3",
  "TV" : "$1000",
  "Fertilizer" : "$20",
  "Apple" : "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2",
  "Phone": "$999",
  "Speakers" : "$300",
  "Laptop": "$5000",
  "PC": "$1200"
}

wallet = float(input("\n\tEntrer la somme totale que voulez depenser aujourd'hui : "))
produits=[]
for article in tous_les_produits.keys():
  if wallet >=float(tous_les_produits[article][1:]):
    produits.append(article)
if produits:
  produits.sort()
  print("\n\tVoici la liste des produits que vous pouvez payer : ")
  for payable in produits:
    print(payable)

else:
  print("Nothing : ")



