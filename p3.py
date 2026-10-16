# Type Conversion
age="23"
print(int(age))

age1=float(age)
print(age1)

age2=str(age1)
print(age2)

list1 = ["mango","chikku","banana"]
tuple1 = ("Google","Microsoft","Infosys")
set1 = {"kannada","english","hindi"}

print(tuple(list1))
print(list(tuple1))
print(set(list1))

# Giving input from the user

girl=input("enter the name of girl : ")
girl_age=int(input("Enter the girl age: "))
boy=input("enter the name of boy: ")
boy_age=int(input("Enter the boy age: "))

age_diff= boy_age - girl_age
print("age_Difference :",age_diff)

print("Hello "+girl+" How are you?")
print(f"my name is {girl} and i am {girl_age} years old")





 



