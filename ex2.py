# Exercice 2 – Conversion Celsius → Fahrenheit
# Demande à l’utilisateur une température en Celsius
# Convertis en Fahrenheit : F = C*9/5 + 32
# Affiche le résultat

def conversion_celsius_fahrenheit():
    """ Cette fonction sert à convertir une température en degré Celcius
    vers une température en degré fahrenheit. """
    while True:
        try:
            temp = float(input("Entrer une température (en C°) : "))*(9/5) + 32
            break
        except:
            print("Mauvais type, veuille entrer une température en décimal.")
    return round(temp, 2)

if __name__ == "__main__":
    for i in range(5):
        print(conversion_celsius_fahrenheit())