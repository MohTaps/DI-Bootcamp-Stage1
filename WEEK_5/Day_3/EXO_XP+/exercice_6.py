'''from datetime import date

def date_Naissance(date1,date2):
    x = (date2-date1).days
    min=x*1330
    return min
date1= date(2018, 12, 13)
date2 = date(2022, 1, 1)
print("Vous avez vecu",date_Naissance(date1, date2), "minutes")'''


from datetime import datetime, timedelta

def age_en_minutes(date_annive):
    date_annive = datetime.strptime(date_annive, "%Y-%m-%d")
    today = datetime.now()
    age = today - date_annive
    age_in_minutes = int(age.total_seconds() / 60)
    print("Vous avez vécu " + str(age_in_minutes) + " minutes.")

annee = int(input("Entrer votre annee de naissance : "))
mois = int(input("Entrer le mois de naissance : "))
jour = int(input("Entrer votre jour de naissance : "))
print()
age_en_minutes(f"{annee}-{mois}-{jour}")
