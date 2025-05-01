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
        min_index = i 
        for j in range(i+1,n): # recherche de l'indice du minimum dans la portion non triée du tableau
            if X[j]< X[min_index]:
                min_index = j
                # (alors) Echanger l'element minimum avec l'element en cours de tri
                X[i], X[min_index] = X[min_index], X[i]

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
    # [expression for variable in iterable if condition]
    # expression : Ce que vous voulez ajouter à la nouvelle liste (ici, x).
    # for variable in iterable : Parcourt chaque élément de l'itérable (ici, x dans X).
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

# Description du pb : Ecrire une fonction qui calcule le PGCD de deux nombres entiers positifs, a et b,
# ou a et b sont donnés. Le PGCD de deux nombres est le plus grand nombre entier qui divise à la fois a et b
# sans laisser de reste

# Algorithme d'euclide: PGCD(a,b)=PGCD(b,a modulo b)

def PGCD(a, b):
    while b: # Tant que b n'est pas égal à 0
        a, b = b, a % b # On met à jour a et b ,a devient b et b devient egale au reste (a % b) 
        # NB : Le modulo c'est le reste dela divison euclidienne
    return a # # Quand b devient 0, a est le PGCD

# et le PGCD c'est le reste de la division, ici 6 

# Exemple d'utilisation :
nbr1 = 48
nbr2 = 18
resultat = PGCD(nbr1,nbr2)
print(f"le PGCD de {nbr1} et {nbr2} est de {resultat}")

## 12. Calcul du plus petit commun multiple (PPCM)

def PPCM (a,b):
    # le PPcm est le produit de deux nombres divisé par leur PGCD
    def PGCD(x, y):
        while y :
            x,y = y, x%y
        return x
    return (a*b)//PGCD(a,b)

# Exemple :
nbre1 = 12
nbre2 = 18
resultat = PPCM(nbre1, nbre2)
print(f"Le PPCM de {nbre1} et {nbre2} est de {resultat}")
        
### 13. Recherche nombres premiers dans une plage donnée

# Probleme: Recherche de nombres premiers dans une plage donnée
# detail: fonction qui recherche et renvoie tous les nombres premiers
# dans une plage donnée de 1 à n, ou n est le nombre donné, un nombre
# premier est un nombre entier positif superieur à 1 qui n'a aucun diviseur autre que 1 et lui meme

    
def est_nombre_premier(nombre): 
    if nombre <= 1:
        return False
    for i in range(2, int(nombre**0.5) + 1): # la boucle vérifie les diviseurs potentiels de 2 à int(nombre**0.5)
        # La boucle for parcourt tous les entiers de 2 à la racine carrée de nombre (arrondie à l'entier supérieur).
        # Si un nombre n n'est pas premier, il a au moins un diviseur inférieur ou égal à sa racine carrée. 
        # Cela permet de réduire le nombre de divisions à effectuer.
        if nombre % i == 0: # Vérifie si nombre est divisible par i (c-a-d si le reste de la division de nombre par i est 0).
            return False # cela signifie que nombre a un diviseur autre que 1 et lui-même, donc il n'est pas premier.
    return True # Si aucun diviseur n'est trouvé après la fin de la boucle, la fonction retourne True, indiquant que le nombre est premier.

def recherche_nombres_premiers(n):
    nombres_premiers = []
    for nombre in range(2, n + 1):
        if est_nombre_premier(nombre):
            nombres_premiers.append(nombre)
    return nombres_premiers

# Exemple :
n = 30
nbr_premiers = recherche_nombres_premiers(n) 
print(f"Les nombres premiers dans la plage de 1 à {n} sont: {nbr_premiers}")

# Fonctionnement : dans la premiere partie, on commence par verifier si le nbre 
# donné est premier. Il parcourt tous les entiers de 2 à la racine carrée
# du nombre et verifie si le  nombre est divisible par l'un d'entre eux. si tel est le cas,
# le nombre n'est pas premier.

## 14. Calcul de la somme des chiffres d'un nombre

# Probleme: ecrire une fonction qui calcule la somme des chiffres d'un nombre entier donné.
# Par exemple, pour le nbre 123, la somme des chiffres est 1 + 2 + 3 = 6

def somme_chiffres(nombre):
    somme = 0
    while nombre > 0: # Démarre une boucle while qui continue tant que nombre est supérieur à 0.
        # La 1ere iteration se fait sur 123, ensuite sur 12 et la derniere sur 1. A la 3eme iteration, nombre = 0 donc la boucle s'arrete
        chiffre =nombre % 10 # On Extrait le dernier chiffre de nombre en utilisant modulo (%) 10.
        somme+=chiffre # Ajoute le chiffre extrait à la variable somme.
        # si somme = 0 et chiffre = 3, alors somme devient 3.
        nombre //= 10
        # Supprime le dernier chiffre de nombre en utilisant la division entière (//).
        # si nombre = 123, alors 123 // 10 donne 12.
    return somme # Retourne la valeur de somme après que la boucle while a terminé son exécution.


# Exemple:
nbr = 1234
resultat = somme_chiffres(nbr)
print(f"La somme des chiffres de {nbr} est de {resultat}")

## 15. Calcul du nombre de chiffres dans un nombre entier

# Probleme : calcul du nombre de chiffres dans un nombre entier
# Detail: ecrire une fonction qui calcule le nombre de chiffres dans 
# un nombre donné. 

def nombre_d_chiffres(n):
    if n == 0: # # Si n vaut 0, il a un seul chiffre
        return 1
    count = 0
    while n != 0: # # Tant que n n'est pas égal à 0
        count += 1
        n = n // 10  # Divise n par 10 pour supprimer le dernier chiffre
        # Etape de la boucle
        # n = 123, count = 1.
        # n = 12, count = 2.
        # n = 1, count = 3.
        # n = 0, la boucle s'arrête.
    return count
    
    # Exemple:
    nbr = 12345
    resultat = nombre_d_chiffres(nbr)
    print(f"{nbr} a {resultat} chiffres.")
# ou
print(nombre_d_chiffres(12345))  # Output: 5
print(nombre_d_chiffres(0))      # Output: 1

# Ce probleme es couramment utilisé en informatique pour effectuer
# desoperations basées sur la longueur ou la structure d'un nombre, 
# par exemple pour formater des nombre ou extraire des parties specifques
# d'un nombre

### 16. Recherche du minimum ou du maximumdan un tableau

# Detail: Ecrire deux fonctions distinctes : une pour trouver le minimum
# et une pour trouver le maximum dans un tableau donné d'entiers



def trouver_minimum(tableau):
    # Cette partie vérifie si le tableau passé en argument est vide.
    if not tableau: # Si le tableau est vide, cette condition est vraie.
        raise ValueError("Le tableau est vide") # Si le tableau est vide, la fonction lève une exception ValueError avec le message "Le tableau est vide". Cela permet de gérer le cas où il n'y a rien à comparer.
    
    minimum = tableau[0] # On initialise la variable minimum avec la première valeur du tableau.
    for element in tableau: # La boucle parcourt chaque élément du tableau un par un.
        if element < minimum: # cela signifie qu'on a trouvé un élément plus petit que le minimum actuel.
            minimum = element # On met alors à jour minimum avec cette nouvelle valeur (minimum = element).
    return minimum

def trouver_maximum(tableau):
    if not tableau:
        raise ValueError("Le tableau est vide")
    
    maximum = tableau[0]
    for element in tableau:
        if element > maximum:
            maximum = element
    return maximum

# Exemple
arr = [64, 25, 12, 22, 11]
mini = trouver_minimum(arr)
maxi = trouver_maximum(arr)
print(f"Le minimum dans le tableau est de {mini}.")
print(f"Le maximu das le tableau est de {maxi}")

# Utiliser pour trouver des valeurs extremes (maximum et minimum)
# dans un ensemble de données

### 17. Inversion d'une chaine de caracteres

# Detail: ecrire une fonction qui rend une chaine  de caractere en entrée
# et renvoie une nouvelle chaine de caractere de caracteres qui est l'inversion
# de la chaine d'origine

def inverser_chaine(chaine):
    return chaine[::-1]

# Exemple:
chaine = "Brech"
chaine_inverse = inverser_chaine(chaine)
print(f"Chaine d'origine: {chaine}")
print(f"Chaine inversée:{chaine_inverse}")

# Souvent utiliser dans les applications de manipulation de chaine de caractere

### 18. Verification de palindromes

# detail: ecrire une fonction qui verifie si une chaine de caractere donnée est un palindrome
# palindrome est une sequence qui se lit de la meme maniere de gauche à droite, en ignorant les 
# espaces, la casse (majuscules ou minuscules) et la ponctuation

def  est_palindrome(chaine):
    # Nettoyer la chaine (ignorer espaces, casses et ponctuation) 
    # e.lower() : Convertit chaque caractère e de la chaîne en minuscule avec .lower().
    # Ne conserver que les caractères alphanumériques (lettres et chiffres) grâce à e.isalnum().
    # Ignorer les espaces, la ponctuation et autres caractères spéciaux.
    # Les caractères filtrés sont ensuite assemblés dans une nouvelle chaîne grâce à "".join().
    chaine = "".join(e.lower() for e in chaine if e.isalnum())
    # Sortie après nettoyage : "eluparcettecrapule"
    return chaine == chaine[::-1]

print(est_palindrome("Elu par cette crapule"))  # True

# Nettoyage : "Élu par cette crapule" devient "eluparcettecrapule".
# Inverse : "eluparcettecrapule".
# Résultat : True.

print(est_palindrome("bonjour"))  # False

# Solution : l'algorithme pour verifier si une chaine de caracteres est un palindrome commence 
# par nettoyer la chaine en ignorant les espaces, la casse et la ponctuation. Ensuite, il compare
# la chaine nettoyée avec son ineverse

### 19. Comptage des voyelles dans une chaine de caracteres:

# Detail : Ecrire une fonction qui compte le nombre de voyelles de voyelles (a,e,i,o,u)
# dans une chaine de caracteres donnée, en ignorant la casse (majuscules ou minuscules).
# Par exemple pour la chaine "Hello World", il y'a 3 voyelles (e,o,o).

def nbre_d_voyelles(chaine):
    voyelles = "AEIOUaeiou"
    compteur = 0
    for caractere in chaine: # caractere = chaque lettre
        # Une boucle for est utilisée pour parcourir chaque caractère de la chaîne chaine.
        # À chaque itération, la variable caractere prend la valeur du caractère courant dans la chaîne.
        if caractere in voyelles:
            # Pour chaque caractère, on vérifie s'il est présent dans la chaîne voyelles.
            # L'expression caractere in voyelles renvoie True si le caractère est une voyelle, sinon False.
            compteur+=1
    return compteur 


def nbre_d_voyelles(chaine):
    # Convertir la chaîne en minuscules pour simplifier la vérification
    chaine = chaine.lower()
    # Définir les voyelles
    voyelles = "aeiouy"
    # Compter le nombre de voyelles dans la chaîne
    compte = sum(1 for e in chaine if e in voyelles) # e etant chaque caractere(ou lettres) de chaine
    return compte

# Exemple:
chaine = "Hello World"
resultat = nbre_d_voyelles(chaine)
print(f"La chaine '{chaine}' contient {resultat} voyelles.")

# L'algorithme pour compter les voyelles dans une chaine de caracteres commence
# par definir une liste de caracteres de voyelles (majuscules et minuscules). Ensuite,
# il utilise une boucle for pour parcour chaque caractere de la chaine donnée et verifie
# si ce caractere est présent dans la liste des voyelles. Si c'est le cas, le compteur est 
# incrémenté.

# Ce probleme est couramment utilisé pour effectuer des analyses de texte et de chaines
# de caracteres, notamment dans le traitement automatique du langage naturel (NLP) et la 
# recherche d'informations. 

### 20. Calcul de la moyenne d'un tableau de nombres :

# Detail: ecrire une fonction qui calcule la moyenne des nombres d'un tableau donné.
# La moyenne est calculée en ajoutant tous les nombres du tableau et en divisant le 
# total par le nombre de nombres dans le tableau

def calculer_moyenne(tableau):
    if not tableau:
        return 0.0 # Si le tableau est vide, la moyenne est 0.0
    
    somme = sum(tableau)
    nombre_d_elements = len(tableau)
    moyenne = somme / nombre_d_elements
    return moyenne

    
# Exemple:
tableau = [10, 20, 30, 40, 50]
moyenne = calculer_moyenne(tableau)
print(f"(La moyenne des nombres dans le tableau est {moyenne}.)")


### 21. Recherche de la médiane dans un tableau tableau non trié:

# Probleme: recherche de la mediane dans un tableau non trié peut etre un peu plus complexe
# que dans un tableau trié. Trié le tableau ou utiliser une approche de selection pour trouver
# l'element median

def mediane(tableau):
    n = len(tableau)

    if n%2==0:
        indice1=n//2
        indice2= indice1-1
        mediane = (tableau[indice1] + tableau[indice2])/2
    else:
        indice = n//2
        mediane = tableau[indice]
    return mediane

# Exemple:
tableau=[12, 4, 7, 9, 2, 23, 16]
mediane = mediane(tableau)
print(f"La mediane du tableau est {mediane}")

### 22. Verification de l'unicité des elements dans un tableau

# Description: ecrire une fonction qui verifie si tous les elements d'un tableau
# donné sont uniques. c-a-d qu'aucun element n'apparait plus d'une fois dans le tableau

def sont_uniques(tableau):
    ensemble = set() # set() : Un ensemble est une collection non ordonnée d'éléments uniques. Il est utilisé ici pour garder une trace des éléments déjà rencontrés dans le tableau.
    for element in tableau:
        if element in ensemble:
            return False
        ensemble.add(element) # Si l'élément n'est pas déjà dans l'ensemble, il est ajouté à l'ensemble pour garder une trace des éléments déjà rencontrés.
    return True

# Exemple:
tableau1 = [1, 2, 3, 4, 5]
tableau2 = [1, 2, 3, 3, 4, 5]

resulat1 = sont_uniques(tableau1)
resulat2 = sont_uniques(tableau2)

print(f"Les elements du tableau 1 sont uniques : {resulat1}")
print(f"Les elements du tableau 2 sont uniques : {resulat2}")

### 23. Rotation d'une chaine de caracteres

# Descrip: ecrire une fonction qui effectue une rotation d'une chaine de caractere donnée.
# La rotation coniste à deplacer un certain nombre de caracteres d'une extremité de la chaine vers l'autre

def rotation_chaine(chaines, rotation):
    n = len(chaines)
    rotation = rotation % n # on utilise ceci pour eviter une rotation supérieure à la longueur de la chaîne
    # S'assurer que la rotation est dans la plage
    chaine_rot = chaine[-rotation:]+ chaine[:-rotation]
    # chaine[-rotation:] : Extrait la sous-chaîne composée des (rotation) derniers caractères de chaine
    # chaine[:-rotation] : Extrait la sous-chaîne composée de tous les caractères sauf les rotation derniers.
    # - pour signifier la queue de la chaine de caractere
    return chaine_rot

# Exemple 
chaine = "abcdef"
rotation = 3
# Puisque 3 est plus petit que 6, il ne peut pas être divisé par 6, donc le reste est 3.
chaine_rot = rotation_chaine(chaine, rotation)
print(f"Chaine d'origine :{chaine}")
print(f"Chaine apres rotation de {rotation} caracteres: {chaine_rot}")

### 24. Fusion de deux tableaux triés:

## Desc: ecrire une fonction qui fusionne deux tableaux triés en un seul tableau trié.

def fusionner_tableaux(tableau1, tableau2):
    resultat = []
    i,j = 0, 0
    while i < len(tableau1) and j < len(tableau2):
        if tableau1[i] < tableau2[j]:
            resultat.append(tableau1[i])
            i+=1 # On passe à la valeur suivante
        else:
            resultat.append(tableau2[j])
            j+=1 # On passe à la valeur suivante

    # Ajout des éléments restants de tableau1
    # tableau1[i:] : Extrait tous les éléments restants de tableau1 à partir de l'indice i.
    # resultat.extend(tableau1[i:]) : Ajoute ces éléments à la fin de resultat.
    resultat.extend(tableau1[i:])
    resultat.extend(tableau2[j:])

    return resultat 

# Exemple:
tableau1 = [1, 3, 5]
tableau2 = [2, 4, 6]
resultat_fusion = fusionner_tableaux(tableau1, tableau2)
print(f"Tableau fusionné : {resultat_fusion}")

## Cette algorithme permet de combiner efficacement deux ensembles de données triées
# tout en preservant l'ordre.

### 25. Calcul de la somme cumulée d'un tableau 

## Descrip : ecrire une fonction qui prend un tableau d'entiers en entrée et renvoie
# un nouveau tableau ou chaque element est la somme cumulée des elements correspondants
# du tableau d'entrée.

def somme_cumulée(tableau):
    somme = 0
    somme_cumulee = []

    for element in tableau:
        somme+=element
        somme_cumulee.append(somme)
    return somme_cumulee

# Exemple:
tableau = [1, 2, 3, 4]
resultat_somme_cumulee= somme_cumulée(tableau)
print(f"Tableau d'origine : {tableau}")
print(f"Tableu de somme cumulée : {resultat_somme_cumulee}")

# Le tableau de somme cumulée est souvent utilisé pour analyser
# des données ou suivre l'evolution cumulatative de valeurs au fil
# du temps.

### 26. Conversion d'un nombre décimal en binaire

## Descr: Ecrire une fonction qui prend un nombre décimal en entrée
# et renvoie sa representation en binaire sous forme de chaine de 
# caractères.

def decimal_en_binaire(decimal):
    if decimal==0:
        return "0"

    binaire = ""
    while decimal > 0: # La boucle while continue tant que le nombre décimal est supérieur à 0.
        reste = decimal % 2
        binaire = str(reste) + binaire # str(reste) : Convertit le reste en chaîne de caractères.
        decimal = decimal // 2
    return binaire  

# Fonctionnement de l'algorithme

# Itération 1 :

# decimal = 10
# reste = 10 % 2 = 0
# binaire = "0" + "" = "0"
# decimal = 10 // 2 = 5

# Itération 2 :
# decimal = 5
# reste = 5 % 2 = 1
# binaire = "1" + "0" = "10"
# decimal = 5 // 2 = 2

# NB: lorsqu'on a une boucle while, definir dans un premier la condition qui arrete la boucle.

# Exemple :
nombre_decimal = 12
nombre_binaire = decimal_en_binaire(nombre_decimal)
print(f"Le nombre décimal {nombre_decimal} en binaire est {nombre_binaire}")

### 27. Recherche de sous-chaines dans une chaine de caracteres

# Ecrire une fonction qui recherche toutes les occurences d'une sous-chaine donnée
# dans une chaine de caracteres donnée et renvoie les indices de début de chaque
# occurence. 

def trouver_occurence(chaine, sous_chaine):
    occurence = []
    longueur_chaine = len(chaine)
    longueur_sous_chaine = len(sous_chaine)
    
    for i in range(longueur_chaine - longueur_sous_chaine+1):
        if chaine[i:i + longueur_sous_chaine]== sous_chaine: # chaine[0:4] extrait les caractères de l'indice 0 à l'indice 3
            occurence.append(i) 
    return occurence

# Exemple:
chaine = "abracadabra"
sous_chaine = "abra"
resultat_occurence = trouver_occurence(chaine, sous_chaine)
print(f"La sous_chaine '{sous_chaine}' apparait aux indices:{resultat_occurence}")

# Cette technique est couramment utilisé pour rechercher des mots, des phrases ou des motifs spécifiques
# dans les chaines de caracteres, ce qui est essentiel dans de nombreuses applications de traitement de
# texte et de manipulation de données.

### 28. Calcul de l'intersection de deux ensembles

# Descrip : Ecrire une fonction qui prend deux ensembles en entrée et renvoie un nouvel ensemble
#  contenant les éléments qui sont presents dans les deux ensembles d'origine.

def intersection_ensemble (ensemble1, ensemble2):
    intersection = ensemble1.intersection(ensemble2)
    return intersection

# Exemple 
ensemble1 = {1, 2, 3, 4}
ensemble2 = {3, 4, 5, 6}
resultat_intersection = intersection_ensemble(ensemble1, ensemble2)


# Cette approche est efficace pour trouver les elements communs à deux ensembles
# et est courament utilisée dans des opérations de comparaison et de filtrage de données

### 29. Calcul de l'union de deux ensembles:

def union_ensemble(ensemble1, ensemble2):
    union = ensemble1.union(ensemble2)
    return union

# EXEMPLE:
ensemble1 = {1, 2, 3, 4}
ensemble2 = {3, 4, 5, 6}
resultat = union_ensemble(ensemble1, ensemble2)

print(f"L'union de {ensemble1} et {ensemble2} est {resultat}")

### 30. Difference de duex ensembles :

# Desc : Ecrire une fonction qui prend deux ensembles en entrée et renvoie un nouvel ensemble contenant les elements
# présents dans le premier ensemble, mais pas dans le deuxieme
# ensemble. 

def difference_ensemble(ensemble1, ensemble2):
    diff = ensemble1.difference(ensemble2)
    return diff

# EXEMPLE:
ensemble1 = {1, 2, 3, 4}
ensemble2 = {3, 4, 5, 6}
resultat = difference_ensemble(ensemble1, ensemble2)

print(f"La difference de {ensemble1} et {ensemble2} est {resultat}")

# Approche efficace pour trouver les élements qui sont presents dans un ensemble
# mais absents das un autre,ce qui ets courament utilisé dans des des operations
# de filtrage ou de suppression de données.

# Cet algorithme s'utilise aussi pour trouver le complément de l'ensemble
# Cette approche est utile pour trouver les elements qui sont inclus dans un
# ensemble mais non inclus dans un autre, ce qui peut etre necessaire dans 
# diverses opérations de filtrage ou de comparaison de donnée

### 32. Tri topologique d'un graphe dirigé :

# Detail : le tri topologique est un algorithme utilisé pour ordonner les noeuds
# d'un graphe dirigé acyclique (DAG) de telle maniere que si un noeud A est relié 
# à un noeud B par une arete, alors A apparait avant B dans l'ordre.

# Probleme : Ecrire une fonction qui prend en entrée un graphe dirigé acyclique
# (représenté sous forme d'un dictionnaire ou chaque noeud est associé à une liste
# de ses noeuds adjacents) et renvoie un ordre topologique valide des noeuds

from collections import defaultdict, deque

def tri_topologique(graphe):
    indegree = defaultdict(int) ## Dictionnaire stockant le nombre d'arêtes entrantes de chaque nœud. 
    ## defaultdict(int) :C'est un dictionnaire qui retourne 0 par défaut si une clé n'existe pas.
    ## 'A': ['C'],
    ## 'B': ['C', 'D'],
    ## 'C': ['E'] ====> indegree[C] = 2 par exemple
    ordre_topologique = []

    ## Calculer le degré  d'entrée de chaque noeud
    for noeud, voisins in graphe.items(): 
        ## items():  récupére à la fois les clés et les valeurs sous forme de paires (clé, valeur).
        ## On parcourt chaque nœud et ses voisins dans le graphe.
        ## noeud correspond à une clé du dictionnaire, donc un sommet du graphe.
        ## voisins correspond à la valeur associée à cette clé, c'est-à-dire la liste des nœuds 
        ## vers lesquels noeud a une arête.
        for voisin in voisins:
            indegree[voisin]+=1

    ## Initialiser la file des noeuds sans prédécesseurs
    file_sans_predecesseur = deque([noeud for noeud in graphe if
                                    indegree[noeud]==0]) # permet de créer une liste contenant tous 
    ## les nœuds du graphe dont le degré d'entrée est égal à 0.
    
    ## Parcourir le graphe
    while file_sans_predecesseur:
        noeud = file_sans_predecesseur.popleft() ## On enlève (popleft()) un nœud de la file.
        ordre_topologique.append(noeud) ## On l'ajoute à l'ordre topologique.

    ## Reduire le degré d'entrée de ses voisins
    for voisin in graphe[noeud]:
        indegree[voisin]-= 1
        if indegree[voisin]==0:
            file_sans_predecesseur.append(voisin)
    
    return ordre_topologique

## Exemple:
graphe = {'A':['B','C'], 'B':['D','E'], 'C':['E'], 'D':[], 'E':[]} # Un dictionnaire où chaque clé est 
## un nœud et chaque valeur est une liste de voisins (les nœuds connectés à lui).
## les clés sont les nœuds et les valeurs sont les listes des nœuds voisins.

resultat_tri_topologique = tri_topologique(graphe)
print(f"Ordre topologique : {resultat_tri_topologique}")

## seul 'A' a un degré d'entrée de 0, donc l'output sera : Ordre topologique : ['A']

## 33. Parcours en profondeur (DFS) d'un graphe

# Detail : Le parcours en profondeur (Depth-First Search, DFS) est un algorithme utilisé pour explorer 
# ou parcourir un graphe, en commencant par un noeud de depart, en explorant autant que possible le 
# long d'une branche avant de revenir en arriere.

## Description : Ecrire une fonction qui realise un parcours en profondeur d'un graphe dirigé ou non
## dirigé et renvoie l'ordre dans lequel les noeuds ont été visités.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list) ## Exemple: Output: {'A': ['B', 'C']}

    def ajouter_arete(self, u, v):
        self.graph[u].append(v) ## ajoute v à la liste des voisins de u.

    def dfs_recursif(self, noeud, visite):
        visite.append(noeud)

        for voisin in self.graph[noeud]:
            if voisin not in visite:
                self.dfs_recursif(noeud_depart, visite)
    
        return visite
                