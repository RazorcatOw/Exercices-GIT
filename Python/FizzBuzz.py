""" FizzBuzz est un jeu de programmation simple et classique souvent utilisé pour enseigner les bases de la logique et du flux de contrôle. Le jeu consiste à itérer à travers les nombres de 1 jusqu'à une limite spécifiée. Pour chaque nombre :

-Si le nombre est divisible par 3, le programme affiche "Fizz."
-Si le nombre est divisible par 7, il affiche "Buzz."
-Si le nombre est divisible à la fois par 3 et par 7, il affiche "FizzBuzz."
-Sinon, il affiche simplement le nombre.
    
Pour aller plus loin : Parcourez les nombres de 1 au nombre saisi par l'utilisateur, et à chaque fois utilisez la fonction que vous avez créée pour calculer le résultat FizzBuzz et l'afficher.
Ajoutez une petite variante au jeu :

Les nombres qui contiennent le chiffre "3" mais qui ne sont pas divisibles par 3 ou 7 afficheront Almost Fizz
"""

print("Welcome to FizzBuzz! Entrez un nombre entier.")
def fizzbuzz(i):
    if i % 3 == 0 and i % 7 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 7 == 0:
        return "Buzz"
    else:   
        if "3" in str(i):
            return "Almost Fizz"
        else:
            return i

a = int(input())
for i in range(1, a+1):
    print(fizzbuzz(i))