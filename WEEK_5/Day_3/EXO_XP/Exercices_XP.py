# Exercice 2 : Devises

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
    	return f"{self.amount} {self.currency}"

    def __int__(self):
    	return self.amount

    def __repr__(self):
    	return f"'{self.amount} {self.currency}'"

    def __add__(self, autre):
        choix=True
        try :
            if self.currency == autre.currency :
                print(self.amount + autre.amount)
                return Currency(self.currency,self.amount + autre.amount)
            else :
                choix=False
        except :
            if choix :
                print(self.amount + autre)
                return Currency(self.currency,self.amount + autre)
        if not choix :
            raise TypeError("Cannot add between Currency type <dollar> and <shekel>")

c1 = Currency('dollars', 5)
c2 = Currency('dollars', 10)
c3 = Currency('shekels', 1)
c4 = Currency('shekels', 10)
print(str(c1))
print()
print(int(c1))
print()
print(repr(c1))
print()
c1 + 5
print()
c1 + c2
print()
print(c1)
print()
c1 += 5
print()
print(c1)
print()
c1 += c2
print()
print(c1)

c1 + c3