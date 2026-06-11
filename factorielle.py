n= int(input("Wanna find the factorial of which number?"))
factorial = 1
for i in range (n, 1, -1):
    factorial = factorial *i
print (factorial)    