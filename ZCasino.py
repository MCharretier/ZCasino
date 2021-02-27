#MODULES:
from math import ceil
from fonctions import *

#VARIABLES:
money = recupMoney ()
utilisator = recupUtilisator ()

#PROGRAMME:
if utilisator not in money.keys():
    money[utilisator] = 1000
    print (f"Bienvenue {utilisator}, bon jeu !")
else:
    print (f"{utilisator}, il vous restait {money[utilisator]}$ la derniere fois que vous avez joué.")


while money[utilisator] > 0:
    
    print (f"Vous avez {money[utilisator]}$ .")
    luckyNb = randomNb ()
    
    try:
        nbBet = int (input ('Choisissez un nombre entier entre 1 et 50 sur lequel vous voulez parier: '))
    except ValueError:
        print ('Veuillez recommencer en saisissant un NOMBRE ENTIER compris entre 1 et 50 !')
        print ("...")
        continue
        
    if nbBet >= 1 and nbBet <= 50: 
        try:
            moneyBet = int (input ("Choisissez une somme d'argent (nombre entier) à miser:"))
        except ValueError:
            print ('Veuillez recommencer en saisissant un NOMBRE ENTIER !')
            print ("...")
            continue
        
        if money[utilisator] >= moneyBet:
            money[utilisator] -= moneyBet
            
            if nbBet == luckyNb:
                money[utilisator] += moneyBet*3
                print (f"{luckyNb} ! Bravo, vous remportez {moneyBet*3}$ !")
                print ("...")
            
            elif nbBet%2 == luckyNb%2:
                money[utilisator] += ceil(moneyBet/2)
                print (f"Même couleur ! Vous récupérez la moitié de votre mise ({ceil(moneyBet/2)}$)!")
                print ("...")
            
            else:
                print("Perdu... Retentez votre chance !")
                print ("...")
                
        else:
            print ("Vous n'avez pas assez d'argent, recommencez !")
            print ("...")
                
    else:
        print("Veuillez recommencer en saisissant un nombre entier compris entre 1 et 50.")
        print ("...")
                          
print ("C'est la fin... vous n'avez plus d'argent...")
saveMoney (money)
os.system("pause")