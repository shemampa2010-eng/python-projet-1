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

for k in all_expenses :
    dailyamouts = []
    for g in k :
        dailyamouts.append(g["amount"])
    amountlist.extend (dailyamouts)    
print (amountlist)



total = sum(amountlist)

average_transaction = total / len(amountlist)

average_day = total / len(all_expenses)

highest = max(amountlist)

highest_per_day = max(dailylist)


print("\n","   Expense Summary   ")
print("Total spent:", total, "Frw")
print("Average per transaction:", average_transaction, "Frw")
print("Average per day:", average_day, "Frw")

print("\nHighest expense per day:")
for day in highest_per_day:
    print("Day", day, ":", highest_per_day[day], "Frw")