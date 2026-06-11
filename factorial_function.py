nombre = int(input("De quel nombre voulez vous faire le factorielle?"))
factorielle = 1
if nombre <= 0 :
    print ("Sorry, the program needs a number over 0")
else:
    for i in range (nombre, 1, -1):
        factorielle = factorielle *i
        print(factorielle)
   