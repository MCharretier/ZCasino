import pickle
import os
from random import randrange


#RECUPERATION MONEY
def recupMoney ():
    if os.path.exists ("saves.txt"):
        with open ("saves.txt" , "rb") as saves:
            oldMoney = pickle.Unpickler (saves)
            money = oldMoney.load()
    else:
        open ("saves.txt" , "a").close()
        money = {}
    return money
  
  
#SAVE MONEY        
def saveMoney (money):
    with open ("saves.txt" , "wb") as saves:
        newMoney = pickle.Pickler (saves)
        newMoney.dump (money)


#RECUPERATION UTILISATOR
def recupUtilisator ():
    utilisator = str (input ("Quel est votre nom?"))
    utilisator = utilisator.capitalize ()
    if not utilisator.isalnum ():
        print ("Nom non valide !")
        return recupUtilisator ()
    else:
        return utilisator
   
   
#RANDOM NUMBER        
def randomNb ():
    luckyNb = randrange (1 , 51)
    return luckyNb