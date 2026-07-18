#savings tracker

#details about income
name=input("enter your name:")
print("welcome",name)
salary=int(input("enter your monthly salary :"))
rent=int(input("monthly amount spend on rent :"))
other_expenses=int(input("monthly amount spend on entertainment :"))
groceries=int(input("monthly amount spend on groceries :"))
medical_emergency=int(input("monthly amount kept for medical emergency:"))

#total expenses calculation
total_expenses=(rent + 
other_expenses + groceries + medical_emergency)
savings=salary - total_expenses
print("savings:",savings)

#financial break down
print("your total financial break down")
print("salary:",salary)
print("total_expenses:",total_expenses)
print("savings:",savings)
