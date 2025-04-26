from fastapi import FastAPI

# On va creer un API qui genere les nombres aleatoires
import random 

# On va creer l'appli fastApi
app = FastAPI()
@app.get("/")

def accueil():
    return {"Message": "Bienvenu sur notre API de generation de nombre aleatoire"}