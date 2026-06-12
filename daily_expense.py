def higher(my_expenses):
    superieure = my_expenses[0]
    for el in my_expenses :
        if el > superieure :
            superieure = el
    return superieure        

def my_sumation (elements):
    mysum = 0
    for element in elements :
        mysum += element
    return mysum    
    
total_exp = int(input ("How many times have you spent money this week?"))

list_exp = []

for i in range(1,total_exp +1):
    expense = int(input(f"expense {i} :"))
    list_exp.append (expense)
  
total = my_sumation(list_exp)
average = total/7

print( "Expense Summary", "\n", "Number of expenses :", total_exp, "\n", 
"Total money spent :", total, "Frw", "\n", "Average money spent per day :", average," Frw", "\n", 
"Highest expense :" , higher(list_exp), " Frw")