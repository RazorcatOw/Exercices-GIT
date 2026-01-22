print("Entrez une série de mots ou de nombres, séparés par un espace.")
numbers = input().split()
# Write your code below
liste_finale = []
inverse = []

for i in numbers[::-1]:
    inverse.append(i)

liste_finale.append(numbers[0])
liste_finale = liste_finale + numbers
liste_finale = liste_finale + inverse
liste_finale.append(numbers[len(numbers)-1])
liste_finale = liste_finale * 2
print(liste_finale)

