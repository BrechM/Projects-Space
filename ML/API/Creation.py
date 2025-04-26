from fastapi import FastAPI

# On va creer un API qui genere les nombres aleatoires
import random 

# On va creer l'appli fastApi
app = FastAPI()
@app.get("/") # mon premier endpoint

def accueil():
    return {"Message": "Bienvenu sur notre API de generation de nombre aleatoire"}

# On va rajouter un endpoints, qui permet à acceder uniquement à une information
@app.get("/nombre_aleatoire") # mon deuxieme endpoint
def generer_nombre():
    """
        cette fonction permet de generer un nombre aleatoire entre 0 et 1000
    """
    return {"nombre_aleatoire": random.randint(0,1000)}

# On peut modifier la fonction, mettre par exemple un min max
# que l'utilisateur decide decide lui meme d'un min ou d'un max

@app.get("/nombre_aleatoire/{min}_{max}") # mon deuxieme endpoint
def generer_nombre(min: int=0, max: int =1000):
    """
        cette fonction permet de generer un nombre aleatoire entre 0 et 1000
    """
    return {"nombre_aleatoire": random.randint(min,max)}

#### Pour tester l'API : uvicorn Creation:app --reload
### pour voir la documentation, on rajoute un /docs
