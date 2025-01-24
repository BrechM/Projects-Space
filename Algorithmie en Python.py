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
        "On commence une boucle qui parcourt le tableau à partir du deuxième élément (indice 1)"
        "jusqu'au dernier élément (indice len(X) - 1)."
        "La variable i représente l'indice de l'élément actuel à insérer dans la portion triée."
        cle = X[i]
        "Cet élément est celui que l'on va insérer à la bonne position dans la portion triée."
        j= i - 1
        "On initialise la variable j à i - 1. Cela représente l'indice de l'élément précédent "
        "dans le tableau, à partir duquel on commence à comparer la clé."
        while j >=0 and cle < X[j]:
            "On commence une boucle while qui continue tant que : "
            "j >= 0 : On n'a pas dépassé le début du tableau. "
            "cle < X[j] : La clé est plus petite que l'élément à l'indice j."
            "Cette boucle permet de déplacer les éléments plus grands que la "
            "clé vers la droite pour faire de la place pour la clé."
            X[j+1]=X[j]
            "On décale l'élément à l'indice j vers la droite (à l'indice j + 1)."
            "Cela permet de libérer de l'espace pour insérer la clé."
            j-=1
            "On décrémente j pour comparer la clé avec l'élément précédent dans le tableau."
            X[j+1]=cle 
            "Une fois la bonne position trouvée (c'est-à-dire lorsque la clé n'est plus " 
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

## TRI RAPIDE (Quicksort):

#il utilise une approche de division, et concatene pour trier un tableau
# Il choisit un element pivot, divise le tableau en deux sous-tableaux,
# puis recursivement trie les sous-tableaux 

def tri_rapide(X):
    "On vérifie si la longueur du tableau X est inférieure ou égale à 1."
    "Si c'est le cas, le tableau est déjà trié (cas de base de la récursion)"
    "et on le retourne tel quel."
    if len(X)<=1:
        return X
    
    "On choisit un pivot en prenant l'élément au milieu du tableau X."
    pivot = X[len(X)//2]

    "On crée des listes contenant tous les éléments de X qui sont strictement"
    "inférieurs, eagux et superieur au pivot."
    elements_inf = [x for x in X if x < pivot]
    elements_eq = [x for x in X if x==pivot]
    elements_sup = [x for x in X if x > pivot]
    # concaténation des 3 parties
    return tri_rapide(elements_inf) + elements_eq + tri_rapide(elements_sup)

    arr = [64, 25, 12, 22, 11]
    arr_trie = tri_rapide(arr)
    print("Tableau trié:", arr_trie)

    # sortie = Tableau trié: [11, 12, 22, 25, 64]

    # resumé de cette algorithme : il commence par choisir un element pivot du tableau. Ensuite, 
    # il divise le tableau en trois parties: les elements <,= et > au pivot. les deux sous tableaux
    # contenant les elements inferieurs et superieurs sont ensuite triés récursivement en utilisant
    # le meme algo 

    # complexité en temps moyenne : 0(n log n)
    # Cet algorithme est un choix judicieux pour trier de grande quantite de données.

## 5. TRI FUSION (MERGESORT)

# Description:le tri fusion (Mergesort) est un algo de tri efficace qui divise recursivement un tableuau
# en deux moitiés triées pour obtenir le tableau final trié

def tri_fusion(X):
    # Cas de base : si le tableau a 0 ou 1 élément, il est déjà trié
    if len(X) <= 1:
        return X

    # Division du tableau en deux moitiés
    milieu = len(X) // 2
    gauche = X[:milieu]  # Extrait les éléments de l'indice 0 à milieu - 1
    droite = X[milieu:]  # Extrait les éléments de l'indice milieu à la fin

    # Appel récursif sur les deux moitiés
    gauche = tri_fusion(gauche)
    droite = tri_fusion(droite)
    "c'est ici que s'arrete l'algorithme de trie à fusion "
    " On applique le tri _a_ fusion jusqu'a ce que cette condition soit respecté len(X)<=1"
    "Dans cette seconde partie, on implemente la fusion"
    # Fusionner les deux moitiés triées
    return fusionner(gauche, droite)


def fusionner(gauche, droite):
    resultat = [] # initialisation d'une liste vide
    i = j = 0 # On initialise deux indices i et j à 0 pour parcourir les tableaux gauche et droite.

    # Fusionner les deux tableaux triés
    "On commence une boucle while qui continue tant que les deux indices i et j sont dans les" 
    "limites de leurs tableaux respectifs."
    while i < len(gauche) and j < len(droite):
        "On compare les éléments actuels de gauche et droite."
        " Si l'élément de gauche est plus petit, on l'ajoute à resultat."
        if gauche[i] < droite[j]:
            "On ajoute l'élément gauche[i] à resultat."
            resultat.append(gauche[i])
            "On incrémente l'indice i pour passer à l'élément suivant de gauche."
            i += 1
        else:
            resultat.append(droite[j])
            j += 1

    # Ajouter les éléments restants de gauche (s'il y en a)
    resultat.extend(gauche[i:]) # On ajoute les éléments restants de gauche à resultat.

    # Ajouter les éléments restants de droite (s'il y en a)
    resultat.extend(droite[j:]) # On ajoute les éléments restants de droite à resultat.

    return resultat

    # Exemple:
    arr =[64,25,12,22,11]
    arr_trie = tri_fusion(arr)
    print("Tableau trié:", arr_trie)

# l'algorithme de tri à fusion est une option efficace pour trier de grandes quantités de données"

## 6. RECHERCHE BINAIRE

# Detail : algorithme de recherche efficace utilisé pour trouver un element dans un "tableau trié"
# il divise recursivement le tableau en deux moitiés, compare l'element recherché avec l'element au milieu et réduit la recherche
# à la moitié appropriée du tableau.

# Ecrire une fonction qui effectue une recherche binaire dans un tableau trié et renvoie l'indice de 
# l'element recherché s'il est présent, sinon -1

def recherche_binaire(X, element):
    debut = 0
    fin = len(X) - 1

    while debut <=fin:
        milieu=(debut+fin)//2
    
        if X[milieu]==element:
            return milieu
        elif X[milieu]<element:
            debut=milieu + 1
        else:
            fin=milieu - 1

    return -1

# l'algorithme de recherche binaire  commence par initialiser les indices debut et fin pour deliminer
# la portion du tableau dans laquelle il recherche. Il calcule ensuite l'indice milieu qui est l'indice
# de l'element au milieu de la portion actuelle. l'algorithme compare l'element recherché avec l'element
# au milieu, et en fonction de cette comparaison, il reduit la recherche à la moitié appropriée du tableau

# Exemple
arr = [11,12,22,25,64]
element_recherche = 22
indice = recherche_binaire(arr, element_recherche)

if indice !=-1:
    print(f"L'élement {element_recherche} se trouve à l'indice {indice}.")
else:
    print(f"L'élement {element_recherche} n'a pas été trouvé dans le tableau")


## 7. Recherche séquentielle

# Cette algo recherche un élement dans un tableau en parcourant le tableau de gauche à droite et en
# comparant chaque element avec l'élement recherché

# Ecrire une fonction qui effectue une recherche séquentielle dans un tableau et renvoie l'indice de 
# l'élement recherché s'il est présent, sinon -1

def recherche_sequentielle(X, element):
    for i in range(len(X)):
        if X[i]==element:
            return i
    return -1

# Exemple
arr =[11, 12, 22, 25, 64]
element_recherche = 22

indice=recherche_sequentielle(arr, element_recherche)

if indice !=-1:
    print(f"L'element {element_recherche} se trouve à l'indice {indice}.")
else:
    print(f"L'element {element_recherche} n'a pas été été trouvé dans le tableau.")

# Détail de l'algorithme: l'algorithme sequentielle parcourt le tableau  élement par élement en 
# utilisant une boucle for. A chaque itération, il compare l'element en cour de traitement avec l'element
# recherché. Si l'element est trouvé, l'indice de cet élement est renvoyé. Si la boucle se termine sans
# trouver l'élement, -1 est renvoyé pour indiquer que l'element n'a pas été trouvé.

## 8. Factorielle d'un nombre

# Probleme : Calcul de la factorielle d'un nombre

# Detail: La factorielle d'un nombre entier positif n, notée n!, est le produit de tous les entiers 
# positifs de 1 à n.

def factorielle(n):
    if n==0:
        return 1
    else:
        resultat=1
        for i in range(1, n+1):
            resultat*=i
            "À chaque itération, on multiplie resultat par i."
            "Cela calcule progressivement la factorielle de n."
        return resultat

# Exemple :
n=5
fact = factorielle(n)
print(f"La factorielle de {n} est {fact}.")

## 9. Calcul de la somme d'une série d'entiers

# Probleme : Calcul de la somme d'une série d'entiers
# Detail de l'algo : Ecrire une fonction qui calcule la somme des entiers de 1 à n, ou n est un nombre
# entier positif donné. En d'autres termes, vous devez calculer la somme 1 + 2 + 3 +...+n.

def  somme_serie_entiers(n):
    somme = 0
    for i in range(1,n + 1):
        somme +=i
    return somme 

# Exemple:
n = 5
resultat = somme_serie_entiers(n)
print(f"La somme des entiers de 1 à {n} est {resultat}")

## 10. Calcul de la puissance d'un nombre :

# Probleme  : Calcul de la puissance d'un nombre

# Detail:  ecrire une fonction qui calcule la puissance d'un nombre x
# élevé à une puissance entiere positive n, ou x et n sont des nombres données.
# En d'autres termes, vous devez calculer x^n

def puissance(x,n):
    resultat = 1 # Pourquoi 1 ? Parce que x exposant 0 est égale 1, i,initialisation
    for _ in range(n):
        "Le symbole _ est utilisé pour indiquer que la variable d'itération (i) n'est pas"
        " utilisée dans le corps de la boucle. On pourrait aussi utiliser i, mais _ est" 
        "une convention pour ignorer la variable."
        resultat*=x
        "À chaque itération, on multiplie resultat par x."
    return resultat 

# Version recursive
def puissance(x, n):
    if n == 0:
    # On vérifie si l'exposant n est égal à 0.
    # Si n == 0, on retourne 1. Cela met fin à la récursion.
        return 1
    else:
        # Si n n'est pas égal à 0, on exécute le bloc de code suivant.
        return x * puissance(x, n - 1)

# version optimisée (exponentiation rapide):
def puissance(x, n):
    resultat = 1
    while n > 0:
        if n % 2 == 1:  # Si n est impair, On vérifie si n est impair en utilisant l'opérateur modulo (%).
            # Si n est impair, cela signifie qu'il y a un facteur supplémentaire de x à prendre en compte dans le résultat.
            resultat *= x # Si n est impair, on multiplie resultat par x.
        x *= x  # x = x^2 , On élève x au carré (x = x^2).
        n //= 2  # traduction : n = n // 2, On divise n par 2 en utilisant la division entière (//).
    return resultat

# Exercice :
x = 2
n = 5
resultat = puissance(x,n)
print(f"{x} élevé à la puissance {n} est égal à {resultat}")

## 11. Calcul du PGCD de deux nombres