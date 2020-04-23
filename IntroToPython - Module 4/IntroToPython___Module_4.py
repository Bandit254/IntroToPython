#Nested Conditionals
number = 1
if number>=2:
    if number>2:
        print("number is 3")
    else:
        print("number is 2")
else:
    print("number is 1")

sandwich_type = input('Enter the type of sandwich you want: "c" for Cheese or "v" for Veggie Special:  ')
if sandwich_type.lower()=="c":
    cheese_type = input(' Pick "c" for Cheddar or "m" for Manchego: ')
    if cheese_type.lower()=="c":
        print("Here is your Cheddar Cheese Sandwich")
    else:
        print("Here is your Manchego Cheese Sandwich")
else:
    print("Here is your Veggie Special")

#Escape Sequences - used for formatting:
# \n = newline
# \t = tab
# \' = single quote
# \" = double quote
# \\ = single backslash
print("Hellow World \n I am formatting print")
student_age = 17
student_name = "Hiroto Yamaguchi"
print("STUDENT NAME\t\tAGE")
print(student_name,'\t'+str(student_age))
print("\"quotes in quotes\"")
print("I\'ve said, \"Save your notebook,\" so let\'s do it!")
print("for a newline use \\n")

#While Loops
while True:
    print("Write forever, unless there is a break")
    break

number_guess = "0"
secret_number = "5"
while True:
    number_guess = input("guess the number, 1 to 5: ")
    if number_guess==secret_number:
        print("Yes,",number_guess,"is correct!\n")
        break
    else:
        print(number_guess,"is incorrect")

while True:
    f_name = input("enter a single-word first name: ")
    if f_name.isalpha():
        break
    else:
        print(f_name,"is not a single word\n")
print("Welcome, ",f_name+"!")

#Incrementing a variable

votes=3
votes = votes+1
print(votes)
votes+=1
print(votes)

#Decrementing a variable
votes=votes-1
print(votes)
votes-=1
print(votes)
seat_count = 0
while True:
    seat_count=seat_count+1
    print("Seat Count = ",seat_count)
    if seat_count>=4:
        print("No seats remaining!")
        break
while True:
    print("Remaining Seats = ",seat_count)
    seat_count-=1
    if seat_count<=0:
        print("Final seat count remaining = ",seat_count)
        break

#While Boolean Loops
greet_count=5
while greet_count>0:
    print(greet_count,"!")
    greet_count-=1
print("\nIGNITION!")

seat_count=0
while seat_count<=4:
    print("Seat Count = ",seat_count)
    seat_count+=1

#While Boolean String Tests
student_fname = ""
while student_fname.isalpha()==False:
    student_fname=input("Enter a first name (letters, no spaces): ")
print("\n"+student_fname.title(),"has been entered as first name")

message = "hi"
while message.isupper()!=True:
    message = input("Sorry, can\'t hear you, please yell the message: ")
print('message: "'+ message +'" received')

number=""
while number.isdigit()!=True:
    number = input("Enter a positive integer: ")
print(number,"is an integer")

#Required Code Submission
message = input("Enter a word or integer: ")
while message=="":
    message = input("Enter a word or integer: ")
def str_analysis(message):
    if message.isalpha()==True:
        final_message ="\""+message+"\" is all alphabetical characters!"
    elif message.isdigit()==True:
        number = int(message)
        if number>99:
            final_message =str(number)+" is a big number!"
        else:
           final_message = str(number)+" is a small number!"
    else:
        final_message = message+" is neither all letters or all numbers!"
    return final_message

print(str_analysis(message))


