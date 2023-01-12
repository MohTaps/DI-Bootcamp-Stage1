import random
import string

def chaine(length):
    str= string.ascii_letters
    return ''.join(random.choice(str) for i in range(length))
print("La chaine est :",chaine(9))