def factorielle(nombre) :
    factorial = 1
    for i in range (nombre, 1, -1):
        factorial = factorial *i
    if n < 1 :
        print ("Sorry, the program needs a number over zero")
    else :
        print (factorial)    

n= int(input("Wanna find the factorial of which number?"))
factorielle(n )


