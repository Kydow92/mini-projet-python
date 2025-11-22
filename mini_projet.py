# Mini-Projet de fin de journée
# Combine tous les exercices dans une seule application :
# L’utilisateur choisit ce qu’il veut faire (calculatrice / conversion / pair ou impair)
# Affiche le résultat
# Boucle pour refaire tant qu’il veut continuer

# ici je vais importer les fichiers py que je viens de faire pour les exos précédents
from ex1 import calc
from ex2 import conversion_celsius_fahrenheit
from ex3 import pair

actions = {
    "calc" : calc,
    "conversion" : conversion_celsius_fahrenheit,
    "pair" : pair
}

def application():
    """ Mini application qui permet à l'utilisateur de choisir ce qu'il veut faire
    parmi 4 options (calculatrice, conversion de degré celsius en fahrenheit, détecter si 
    un nombre est pair ou impair, et quitter l'application) """
    while True: 
        action = input("Que voulez vous faire ('calc', 'conversion', 'pair', 'stop') ? ").lower()

        if action == "stop":
            print("Merci d'avoir utilisé notre application !")
            break

        if action in actions:
            resultat = actions[action]()
            print(f"Résultat : {resultat}")
        else: 
            print("Action inconnue.")
        
if __name__ == "__main__":
    application()       