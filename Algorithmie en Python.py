## 1. Algorithme de TRI A BULLES

# Ecrire ue fonction qui trie un tableau d'entiers en utilisant l'algo de trie à bulles

# Le tri à bulle compare  les elements adjacents en les échange s'ils sont dans le mauvais ordre.
# On repete ce processus jusqu'à ce que le tableau soit trié.
def tri_a_bulles(X):
    n = len(X)
    for i in range(n): # la boucle doit va s'itérer n fois pour etre en ordre 
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Fonctionnement de l'algorithme :

# Le tri à bulles fonctionne en comparant chaque paire d'éléments adjacents et 
# en les échangeant s'ils sont dans le mauvais ordre.
# Après chaque itération de la boucle externe, le plus grand élément non trié 
# "remonte" à sa position correcte (comme une bulle qui remonte à la surface, 
# d'où le nom).
# Ce processus est répété jusqu'à ce que tout le tableau soit trié.



# Exemple
arr=[64, 34, 25, 12, 22, 11, 90]
len(arr)
tri_a_bulles(arr)
print(arr)

## 2. TRI PAR SELECTION : 

#  Parcourt le tableau à plusieurs reprises pour trouver l'élément minimum 
# et le place à la bonne position.
# Ecrire une fonction qui tri un tableau d'entiers en utilisant l'algo de tri par selection


def tri_par_selection(X):
    n =len(X)
    for i in range(n):
        # recherche de l'indice du minimum dans la portion non triée du tableau
        min_index = i 
        for j in range(i+1,n):
            if arr[j]< arr[min_index]:
                min_index = j
                # (alors) Echanger l'element minimum avec l'element en cours de tri
                arr[i], arr[min_index] = arr[min_index], arr[i]

# Exemple: 
arr =[ 64, 25, 12, 22, 11]
tri_par_selection(arr)
print(arr)

# Fonctionnement de l'algorithme :

# Le tri par sélection fonctionne en divisant le tableau en deux parties : une partie 
# triée et une partie non triée. À chaque itération de la boucle externe, on trouve le 
# plus petit élément dans la portion non triée et on le place à la fin de la portion triée.
# Ce processus est répété jusqu'à ce que tout le tableau soit trié.


# la boucle exterieur parcourt le tableau de gauche à droite et selctionne l"élement
# minimum dans la portion non triée du tableau. La boucle interieure parcourt la portion non triée
# pour trouver l'indice de l'element minimum. Une fois trouvé, l"element  minimum est échangé avec 
# l'element en cours de tri.

## 3. TRI PAR INSERTION

# Detail : Construit une liste triée d'elements un par un. A chaque itération, il prend un élemnent
# non trié et l'insere à la bonne position dans la partie déja triée du tableau

def tri_par_insertion(X):
    for i in range(1, len(X)):
        "On commence une boucle qui parcourt le tableau à partir du deuxième élément (indice 1) 
        "jusqu'au dernier élément (indice len(X) - 1).
        "La variable i représente l'indice de l'élément actuel à insérer dans la portion triée."
        cle = X[i]
        "Cet élément est celui que l'on va insérer à la bonne position dans la portion triée."
        j= i - 1
        "On initialise la variable j à i - 1. Cela représente l'indice de l'élément précédent 
        "dans le tableau, à partir duquel on commence à comparer la clé."
        while j >=0 and cle < X[j]:
            "On commence une boucle while qui continue tant que :
            "j >= 0 : On n'a pas dépassé le début du tableau.
            "cle < X[j] : La clé est plus petite que l'élément à l'indice j.
            "Cette boucle permet de déplacer les éléments plus grands que la 
            "clé vers la droite pour faire de la place pour la clé."
            X[j+1]=X[j]
            "On décale l'élément à l'indice j vers la droite (à l'indice j + 1).
            "Cela permet de libérer de l'espace pour insérer la clé."
            j-=1
            "On décrémente j pour comparer la clé avec l'élément précédent dans le tableau."
            X[j+1]=cle 
            "Une fois la bonne position trouvée (c'est-à-dire lorsque la clé n'est plus plus 
            "petite que X[j]), on insère la clé à l'indice j + 1."

# Cette algorithme parcourt le tableau de gauche à droite, en considérant chaque élement comme une
# clé à inserer dans la portion déja triée du tableau. A chaque étape, l'algorithme compare
# la clé avec les élements de la portion triée, déplace les élements plus grands vers la droite et 
# insere la clé à la position correcte.

# 
# Première itération (i = 1) :
# cle = 25 (élément à insérer).
# On compare 25 avec 64 et on décale 64 vers la droite.
# Résultat après la première itération : [25, 64, 12, 22, 11].
# Deuxième itération (i = 2) :
# cle = 12 (élément à insérer).
# On compare 12 avec 64 et 25, et on décale ces éléments vers la droite.
# Résultat après la deuxième itération : [12, 25, 64, 22, 11].

# Exemple:
arr = [64, 25, 12, 22, 11]
tri_par_insertion(arr)
print("Tableau trié :", arr)


# Sortie : Tableau trié : [11, 12, 22, 25, 64]