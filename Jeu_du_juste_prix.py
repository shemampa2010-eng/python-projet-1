import random
juste_prix = random.randint(1, 100)

while True:
    
    prix_hestimee = int(input("Entrez votre estimation: "))
    if juste_prix < prix_hestimee:
        print("C'est moins que ça")
    elif juste_prix > prix_hestimee:
        print("C'est plus que ça")
    else:
        print("Félicitations! Vous avez trouvé le juste prix!")
        break
    answer = input("Do you want to continue? (yes/no): ")
    if answer == "no":
        print("À bientôt!")
        break