def fibonnacci():
    nombre = int(input("Jusqu'a quel rang voulez-vous aller ? "))
    a = 0
    b = 1
    print(a,"\n",b)

    for i in range(1, nombre):
        print ("current:", a, "current:",b)
        c = a+b
        print(c)

        a= b
    
        b= c
