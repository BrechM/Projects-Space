#!/usr/bin/env python
# coding: utf-8

# ##  Quelques notions en  POO
# 

# In[27]:


# Un objet a des attributs et des fonctions (des choses à faire)
# Exemple: On veut creer 2 points A et B et calculer la distance entre ces 2 points : chaque point a 2 coordonnées x et une y:


# In[ ]:


# 1ere possibilité que l'on aurait imaginé:


# In[ ]:


x_A = 2
y_A = 5
x_B = 2
y_B = 1
d = distance(x_A, y_A, x_B, y_B)


# In[23]:


# en grande dimension, la premiere possibilité devient compliqué


# In[ ]:


# Seconde possibilité, on peu penser objet : comme un objet qui a 2 attributs x et y

# On encapsule
A = Point (2,5)
B = Point(2, 1)
d = distance(A,B) # ou d = A.distance(B)


# In[ ]:


# On constate que Point n'est pas défini, Point c'est ce que l'on appelle une classe orientée Objet
# A et B sont des objets de la classe Point ou des instances, a chaque foit qu'on a differents attributs, on obtient des objets differents


# In[39]:


# Importation du module math
import math


# In[53]:


# Creation d'une classe en Python
class Point:
    def __init__(self, abscisse, ordonne) :
        self.x = abscisse
        self.y = ordonne

    def distance(self, autre_point):
        squarred_d = (autre_point.x - self.x)**2 + (autre_point.y - self.y)**2
        d = math.sqrt(squarred_d)
        return d


# In[87]:


A = Point(2, 3)
B = Point(1, 5)


# In[65]:


A.x


# In[67]:


A.y


# In[75]:


A.distance(B)


# In[77]:


B.distance(A)


# In[79]:


# La fonction init est appelé constructeur. c'est dans cette fonction que nous definissons les attributs de ntre classe. Le mot self represente
# un objet ou une instance de notre classe. la fonction init atribue donc à xet y respectivement l'abscisse et l'ordonné recue

print(A) 

# In[ ]:


# elle ne donne aucune information, si l'on souhaite les informations sur ses attributs, c'est possible avec la fonction repr comme ceci


# In[81]:


class Point:
    "Cette classe represente un point qui a des coordonnées et peut calculer la distance avec d'autres points"
    def __init__(self, abscisse, ordonne) :
        self.x = abscisse
        self.y = ordonne

    def distance(self, autre_point):
        squarred_d = (autre_point.x - self.x)**2 + (autre_point.y - self.y)**2
        d = math.sqrt(squarred_d)
        return d

    def __repr__(self):
        return f"Ce point a pour abscisse {self.x} et ordonné {self.y}"


# In[83]:


un_point = Point(5, 8)


# In[85]:


print(un_point)


# In[89]:


print(A)


# In[91]:


un_point.distance(A)


# In[ ]:


# Nous pouvons faire une projection du point sur l'axe des abscisses et une autre sur l'axe des ordonnes ou qu'un point
# revienne à l'origine


# In[93]:


class Point:
    def __init__(self, abscisse, ordonne) :
        self.x = abscisse
        self.y = ordonne

    def distance(self, autre_point):
        squarred_d = (autre_point.x - self.x)**2 + (autre_point.y - self.y)**2
        d = math.sqrt(squarred_d)
        return d

    def __repr__(self):
        return f"Ce point a pour abscisse {self.x} et ordonné {self.y}"

    def origin(self):
        self.x = 0
        self.y = 0

    def projection_x(self):
        self.y = 0

    def projection_y(self):
        self.x = 0


# In[101]:


C = Point(5, 8)


# In[103]:


print(C)


# In[107]:


C.origin()


# In[109]:


print(C)


# In[111]:


# Quelques concepts clés:

## polymorphisme: Avec l'OO, on peut definir une fonction qui a la possibilité de fonctionner avec differents types de données.
# C'est l"exemple de la fonction len qui peut etre etre utilisée avec une chaine de caractere, une liste ou un dictionnaire
# pour calculer sa taille. Un exemple réel serait une classe Personne avecune fonction salutation qui laissera chaque personne saluer
# de la facon dont c'est fait dans sa culture.

## Heritage : c'est la possibilité de créer une classe en se basant sur une autre. La nouvelle classe hérite des attributs et fonctions de la précedente 
# mais aussi avoir ses propres fonctionnalités et attributs. Un exemple réel serait une classe d'Adulte qui hérite de la classe humain mais qui a ses
# propres attributs comme statut_matrimonial et des fonctions comme acheter_une_maison


# ### Debut livre sur la prog orientée objet

# In[28]:


# Exercice 1:

class Biscuit:
    ## Constructeur
    def __init__(self, nom,forme):
        ##  Initialisation des attributs à l'aide des parametres
        ## passés du construceur
        self.nom = nom
        self.forme = forme

    def cuir(self):
        """
        Cette methode sert simplement d'affichage
        sur la console afin de donner plus d'informations
        sur le biscuit
        """
        print("Ce", self.nom, "a été cuit sous forme d'une", self.forme)
        print("Bonne degustation")

# Exemples de tests / Cas d'usages

## Instanciation de l'objet "Biscuit_1" de la classe biscuit
biscuit_1 = Biscuit("Cookie pepite de chocolat", "etoile")

# Appel de la methode "cuir()" en utilisant l'instance créée

biscuit_1.cuir()





# In[38]:


# Exercice 2:

class Livre:
    def __init__(self,titre,auteur, prix):
        self.titre = titre
        self.auteur = auteur
        self.prix = prix

    def afficher_information(self):
        """
        Cette methode permet d'afficher les informations liées au livre.
        """
        print(f"Le livre intitulé '{self.titre}', écrit par l'auteur '{self.auteur}' se vend à {self.prix} euros.")

### Exemples de tests / Cas d'usage

## Instanciation de l'objet "livre_1" à partir de classe livre
livre_1 = Livre("100 exercices python pour s'entrainer", "Laurentine K.Masson", 10.99)

## Appel de methode pour  afficher les informations du livre
livre_1.afficher_information()


# In[42]:


# Exercice 3: 

class Note:
    def __init__(self,note,nomEtudiant):
        ## Initialisation des attributs de classe Note
        self.note = note
        self.nomEtudiant = nomEtudiant

    def a_reussi(self):
        """
        Cette methode permet de verifier si un etudiant a reussi ou echouer.
        La note seuil pour reussir est de 75
        Si la note de l'eleve dépasse 75, alors l"eleve a reussi
        Sinon il a échoué
        """
        if self.note > 75:
            print(f"L'etudiant(e) {self.nomEtudiant} a réussi(e)")
        else:
            print(f"L'etudiant(e) {self.nomEtudiant} a échoué(e)")

## Exemples de tests / Cas d'usages
## Creation d'une instance
note_1 = Note(80, "Julien")
## Appel de méthodes
note_1.a_reussi()
        


# In[44]:


# Autre exemple:
note_2 = Note(35,"Amelie")

## Pour acceder à l'attribut d'une instance, il suffit d'ecrire nominstance.nomAttribut
print(f"La note obtenue par {note_2.nomEtudiant} lors de la premiere correction est : {note_2.note}")


# In[48]:


## Modification de l'attribut "note" de l'instance note_2
note_2.note = 70
print(f"Apres une deuxieme correction, la note d'{note_2.nomEtudiant} est égal à {note_2.note}")
note_2.a_reussi()


# In[ ]:




