"""Créez un programme qui reçoit une liste en entrée et imprime trois nouvelles listes basées sur les opérations de découpage suivantes :

Une liste contenant chaque troisième élément, en commençant par l'index 1 (le deuxième élément)
Une liste contenant tous les éléments du 6e élément au 1er en ordre inverse
Une liste contenant chaque deuxième élément en commençant par le milieu de la liste jusqu'à la fin"""
# Exemples de listes: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
# pizza,burger,pâtes,sushi,tacos,sandwich,salade,soupe,steak,riz,nouilles,curry,kebab,crêpes,frites

print ("Entrez une liste d'éléments, séparés chacun par une virgule:")
lst = input().split(",")
# Write your code below
print("liste 1 :", lst[1::3])
print("liste 2 :", lst[5::-1])
print("liste 3 :", lst[len(lst)//2::2])