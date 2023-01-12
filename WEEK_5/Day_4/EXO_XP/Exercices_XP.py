from os import system


# Exercise 1 – Random Sentence Generator


# question 1,2,3


def get_words_from_file():
    with open('mot.txt') as f:
        mot = []
        for i in f:
            mot.append(i[0:len(i)-1])
    return mot


# question 4


def get_random_sentence(taille=9):
    import random
    ma_phrase = ""
    mots = get_words_from_file()
    for x in range (0,taille):
        ma_phrase += mots[random.randint(0,len(mots))] + ' '
    return ma_phrase


# question 5

print()
print("Un essai avec taille par defaut = 9")
print()
mot = get_random_sentence().lower()
print(mot)

# question 6

def main():
    print("\nCe programme genere une phrase aleatoire pour vous, vous lui specifier une taille, nombre de mots et il vous retourne une phrase.\n")
    taille = int(input('Entrez la taille (2 à 20) : '))
    if taille >= 2 and taille <= 20:
        print(get_random_sentence(taille))
    else:
        print('Au moins 2 mots svp')
main()

print()
system("pause")
system("cls")


# Exercice 2 : Travailler Avec JSON


import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

sampleJson = json.loads(sampleJson)
print(sampleJson['company']["employee"]['payable']['salary'])
sampleJson['company']['employee'].update({'birth_date':''})
print(sampleJson)

import json
jsonFile = 'fichierj.json'
with open(jsonFile,'w') as jasF:
    json.dump(sampleJson,jasF)