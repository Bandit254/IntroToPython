#Controlling program flow with Boolean statements (if, else, pass)
if True:
    print("This statement prints if the Boolean evaluates to True")

else:
    print("This statement prints if the first Boolean evaluates to False")
print()
someone_i_know = True
if someone_i_know:
    print("How have you been?")
else:
    print("Nice to meet you!")
print()
#if you don't want anything to occur after the if statement, use "pass"
if someone_i_know:
    print("How have you been?")
else:
    pass

favorite_book=input("Enter the title of your favorite book:")
if favorite_book.istitle():
    print(favorite_book," - nice capitalization in that title!")
else:
    print(favorite_book," - you should capitalize each word in the title!")

a_number = input("enter a positive number: ")
if a_number.isdigit():
    print(a_number,"is a positive integer")
else:
    print(a_number,"is not a positive integer")
print()
#Comparison operators - > , < , >= , <= , != , ==
#operators that return true or false
x = 3
print(x,"is not equal to 9:", x != 9)
print(x,"is equal to 3:", x==3)

x = 23
if x>25:
    print("x is already greater than 25")
else:
    print("x was",x)
    x=26
    print("x is now",x)
print()
#String comparison
msg = "Save the notebook"
if msg == "save the notebook":
    print("message as expected")
else:
    print("message not as expected")
print()
prediction = "save the notebook"
if msg.lower()==prediction.lower():
    print("message as expected")
print()
l_name = input("Enter last name: ")
if l_name.lower()<="c":
    print("Welcome to the a, b, c line")
else:
    print("sorry, the is the a, b, c line")
print()

#elif 
weather = input("Enter the current weather (sunny, rainy, snowy): ")

if weather.lower()=="sunny":
    print("Wear a T-shirt")
elif weather.lower()=="rainy":
    print("Bring an umbrella and boots")
elif weather.lower()=="snowy":
    print("Wear a warm coat and hat")
else:
    print("Sorry, not sure what to suggest for",weather)

print()

#Casting - input is always a string, so you need to change the input data type if you need something else
weight1 = '60'
weight2 = 170

total_weight=int(weight1)+weight2
print(total_weight)
print()
age_new_student = input("Enter the age of the student: ")
grad_age = float(age_new_student)+3.75
grad_age_msg = "Age upon graduation: "+str(grad_age)
print(grad_age_msg)

print()

#Math operators
print(11*19)
print(188/4)
print((42+8)*3)
print()

#Module 3 final code submission
min = 2.5
max=100.0
price=17.54
order_amount=input("Enter cheese order weight (numeric value): ")
if float(order_amount)>max:
    print(float(order_amount),"is more than currently available stock")
elif float(order_amount)<min:
    print(float(order_amount),"is below minimum order amount")
else:
    print(float(order_amount),"costs $",price)