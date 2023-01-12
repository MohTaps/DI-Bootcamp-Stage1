from datetime import date

def temps(date1,date2):
    x = (date1-date2).days
    return x

date1= date(2024, 1, 1)

date2 = date(2023, 1, 12)
print("IL reste",temps(date1, date2), "jours pour atteindre le 1er janvier 2024")