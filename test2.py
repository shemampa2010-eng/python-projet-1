print ("Choisissez une opération: ")
print ("1. Addition")
print ("2. Soustraction")
print ("3. Multiplication")
print("4. Division")
operation = input("Entrez le numéro de votre choix (1,2,3,4) : ")
if operation == "1":
    num1 = float(input("Entrez le premier chiffre : "))
    num2 = float(input("Entrez le deuxième chiffre : "))
    answer = num1 + num2
print("La somme de ces deux chiffres est: " + str(answer))
if operation == "2":
    num1 = float(input("Entrez le premier chiffre : "))
    num2 = float(input("Entrez le deuxième chiffre : "))
    difference = num1 - num2
    print("difference")
if operation == "3":
    num1 = float(input("Entrez le premier chiffre : "))
    num2 = float(input("Entrez le deuxième chiffre : "))
    answer = num1 * num2
    print("Le produit de ces deux chiffres est: " + str(produit))
if operation == "4":
    num1 = float(input("Entrez le premier chiffre : "))
    num2 = float(input("Entrez le deuxième chiffre : "))
    quotient = num1 / num2
    print("Le quotient de ces deux chiffres est: " + str(quotient))
if operation not in ("1", "2", "3", "4"):
    print("Choix invalide. Veuillez choisir une opération valide.")
