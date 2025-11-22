# Exercice 3 – Pair ou impair
# Demande à l’utilisateur un nombre
# Affiche si le nombre est pair ou impair

def pair():
    """ Cette fonction détecte si un nombre est pair ou bien
    impair. """
    while True: 
        try:
            n = int(input("Saisissez un nombre : "))
            break
        except:
            print("Mauvais type, veuillez entrer un nombre entier.")
    if n % 2 == 0:
        return "Le nombre est pair"
    return "Le nombre est impair"

if __name__ == "__main__":
    for i in range(11):
        print(pair())