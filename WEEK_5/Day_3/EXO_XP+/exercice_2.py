import random
def rand(n):
    m=random.randint(1,100)
    if n==m:
        print("Success!!!!")
    else:
        print("Echec!!!")
        
nombre=int(input("Entrer un nombre : "))
while True:

    if(nombre>=1 and nombre<=100):
        rand(nombre)
        break
    else:
        nombre=int(input("Entrer un nombre compris entre 1 et 100 : "))