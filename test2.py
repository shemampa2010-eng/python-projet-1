print ("Choisissez une opération: ")
print ("1. Addition")
print ("2. Soustraction")
print ("3. Multiplication")
operation = input("Entrez le numéro de votre choix (1,2,3,4) : ")
if operation == "1":
    num1 = float(input("Entrez le premier chiffre : "))
    num2 = float(input("Entrez le deuxième chiffre : "))
    somme = num1 + num2
print("La somme de ces deux chiffres est: " + str(somme))
if operation == "2":
    num1 = float(input("Entrez le premier chiffre : "))
    num2 = float(input("Entrez le deuxième chiffre : "))
    difference = num1 - num2
    print("La différence de ces deux chiffres est: " + str(difference))
if operation == "3":
    num1 = float(input("Entrez le premier chiffre : "))
    num2 = float(input("Entrez le deuxième chiffre : "))
    produit = num1 * num2