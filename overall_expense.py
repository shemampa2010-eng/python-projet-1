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

period_exp = int(input ("Over what period would you like to view all expenses? (please enter the answer in days)"))

total_exp = int(input ("How many times have you spent money on that period ?"))

list_exp = []

for i in range(1,total_exp +1):
    expense = int(input(f"expense {i} :"))
    list_exp.append (expense)
  
total = my_sumation(list_exp)

average = total / total_exp

averagee = total / period_exp
while period_exp == total_exp:
    print( "Expense Summary over the last", period_exp , "days"  "\n", "Number of expenses :", total_exp, "\n", 
    "Total money spent :", total, "Frw", "\n", "Average money spent per transaction :", average," Frw", "\n", 
    "\n", "Highest expense :" , higher(list_exp), " Frw")
    break
else : 
    print( "Expense Summary over the last", period_exp , "days"  "\n", "Number of expenses :", total_exp, "\n", 
"Total money spent :", total, "Frw", "\n", "Average money spent per transaction :", average," Frw", "\n", 
"Average money spent per day :" ,averagee , "Frw" "\n", "Highest expense :" , higher(list_exp), " Frw")    