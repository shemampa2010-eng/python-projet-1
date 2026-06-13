period_exp = int(input("Over how many days? "))

all_expenses = []

for i in range(1, period_exp + 1):
    print("\n" ,"Jour", i)
    nombre_exp = int(input("How many expenses today? "))

    day_expenses = []

    for j in range(nombre_exp):
        amount = int(input("Expense amount: "))
        category = input ("Category (Food, clothes, transport, ect): ")

        
        day_expenses.append({
            "amount": amount,
            "category": category
            
            })

    all_expenses.append (day_expenses)

amountlist = []

highest_per_day = []

for k in all_expenses :
    dailyamounts = []
    for g in k :
        dailyamounts.append(g["amount"])
    highest_per_day.append ( max(dailyamounts))

    amountlist.extend (dailyamounts)    
print (amountlist)



total = sum(amountlist)

average_transaction = total / len(amountlist)

average_day = total / len(all_expenses)

highest = max(amountlist)



print("\n","   Expense Summary   ")
print("Total spent:", total, "Frw")
print("Average per transaction:", average_transaction, "Frw")
print("Average per day:", average_day, "Frw")

print("\nHighest expense per day:")
for day in range (len(highest_per_day)):
    print("Day", day + 1 , ":", highest_per_day[day], "Frw")