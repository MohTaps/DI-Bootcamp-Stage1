from os import system

class Chat:
    def __init__(self, nom_chat, age_chat):
        self.nom = nom_chat
        self.age = age_chat


chat1 = Chat("Minou", 3)
chat2 = Chat("Mooss", 5)
chat3 = Chat("Filou", 2)

def chat_le_plus_vieux(chats):
  vieux_chat = chats[0]
  for chat in chats:
    if chat.age > vieux_chat.age:
      vieux_chat = chat
  return vieux_chat

chats = [chat1, chat2, chat3]
vieux_chat = chat_le_plus_vieux(chats)
print(f"\nLe plus vieux des chats est {vieux_chat.nom}, et il a {vieux_chat.age} ans.")

print()
system('pause')
system('cls')



# Exercice 2


class Chien:
  def __init__(self, nom, hauteur):
    self.nom = nom
    self.hauteur = hauteur

  def bark(self):
    print(f"{self.nom} fait woof woof!")

  def jump(self):
    print(f"{self.nom} saute plus de {self.hauteur*2} cm de haut!")

mon_chien = Chien("Rex", 50)
print(f"Le nom de mon chien est {mon_chien.nom} et sa hauteur est de {mon_chien.hauteur} cm.")
mon_chien.bark()
mon_chien.jump()

votre_chien = Chien("Teacup", 20)
print(f"Le nom de mon chien est {votre_chien.nom} et sa hauteur est de {votre_chien.hauteur} cm.")
votre_chien.bark()
votre_chien.jump()

if mon_chien.hauteur > votre_chien.hauteur:
  print(f"{mon_chien.nom} est le plus gros chien.")
else:
  print(f"{votre_chien.nom} est le plus gros chien.")




print()
system('pause')
system('cls')


# Exercice 3 

class Musique:
  def __init__(self, lyrics):
    self.lyrics = lyrics

  def Chanter(self):
    for paraph in self.lyrics:
      print(paraph)
parole = Musique(["On a fait ce qu'on a pu","On a chanter nos reves", "Et comme du fer on a cru que la paix vaincra le glaive",
 "Mais c'est la faute a qui","Qui est responsable?","Qui prendra la balle a la place du coupable","Parce que tout le monde s'en veut",
 "Tout le monde s'accuse","Tout le monde est Dieu","Donc tout le monde refuse de reconnaitre ses defaut et tout mal qu'il a pu faire"])
parole.Chanter()


