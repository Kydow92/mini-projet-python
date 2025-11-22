# Exercice 1 – Calculatrice simple
# Demande à l’utilisateur 2 nombres
# Affiche : addition, soustraction, multiplication, division
# Bonus : afficher le résultat arrondi à 2 décimales

from operator import add, sub, mul, truediv

ops = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}

def calc():
    """ Cette fonction est une mini calculatrice, elle ne prend pas 
    de paramètres. Elle demande à l'utilisateur de saisir 2 nombres (entiers)
    ainsi qu'un opérateur (+, -, * ou /) puis renvoie le résultat du calcul """
    while True:
        try: 
            n1 = int(input("Saisir le premier nombre : "))
            n2 = int(input("Saisir le deuxième nombre : "))
            break
        except: 
            print("Mauvais type, entrer des nombres entiers")
    while True:
        operateur = input("Saisir l'opération (+, -, *, /) : ")
        if operateur in ops:
            break
        else:
            print("Mauvais type, entrer l'un des opérateurs suivants : +, -, *, /")
    return ops[operateur](n1, n2)


if __name__ == "__main__":
    for i in range(5):
        print(calc())