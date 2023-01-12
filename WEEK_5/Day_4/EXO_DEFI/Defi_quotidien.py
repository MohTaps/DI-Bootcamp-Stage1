from typing import Counter


class Text:
    def __init__(self,chaine):
        self.chaine=chaine
    #method
    def frequency(self):
        str=self.chaine.split(' ')
        str2=[]
        for i in str:
            if i not in str2:
                str2.append(i)
        for i in range(0,len(str2)):
            print("Frequence de ",str2[i],'de:',str.count(str2[i]))
    #method
    def current_word(self):
        str=self.chaine.split(' ')
        f=Counter(str)
        max=0
        word=[]
        for i in f:
            if(f[i]>max):
                max=f[i]
                word=i
        print("Mot le plus courant:",word)
    #method
    def unique_word(self):
        str=self.chaine.split(' ')
        str2=[]
        for i in str:
            if i not in str2:
                str2.append(i)
        print("Mot sans doublons:",end=" ")
        for i in range(0,len(str2)):
            print(str2[i],end=" ")
        print("")
    @classmethod
    def from_file(cls,nom_fichier):
        text = ""
        with open("the_stranger.txt", "r") as f :
            for x in f :
                text += x[0:len(x)-1]
        return text
            
#instance
texte=Text("my")
print()
text =Text(texte.from_file("the_stranger.txt"))
print()
text.frequency()
print()
text.current_word()
print()
text.unique_word()

