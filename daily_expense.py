total_exp = int(input ("How many times have you spent money today?"))
list_exp = []
for i in range(1,total_exp +1):
    expense = int(input(f"expense {i} :"))
    list_exp.append (expense)
