#Introduction to functions
#Some functions, like print, can take many parameters.
#Other functions, like type, can only take one parameter

my_type = type(2.2)
print(my_type)

#Create a function using the 'def' keyword, the function name, parentheses and semicolon
#The actual body of the function is defined underneath the function name, indented 4x spaces
#Ending the indentation will end the function body

def say_hi():
	print("Hello there!")
	print("Goodbye!")
#call the function by simply typing the name and any input parameters:
say_hi()

def yell_it():
	phrase="Well hello there"
	print(phrase.upper(),"!")

yell_it()

#Function parameters: 
def say_this(phrase):
	print(phrase)
say_this("Hi!")

#Default parameters:
def nowSayThis(phrase="Good Night"):
	print(phrase)

nowSayThis()
nowSayThis("Goodnight Moon!")

#Functions with return values
def msg_double(phrase):
	double = phrase +" "+phrase
	return double
msg_2x = msg_double("Hey y'all!")

print(msg_2x)

def half_value(value):
	return value/2
print(half_value(42))

#Multi-parameters:
def make_schedule(period1, period2):
	schedule=("[1st] "+ period1.title() +", [2nd] "+ period2.title())
	return schedule

student_schedule=make_schedule("mathematics", "history")
print("SCHEDULE: ", student_schedule)

def format_info(name, age, school):
	return "Student: " + name+"\nAge: " +str(age)+"\nSchool: "+ school
print(format_info("Tobias Ledford", 15, "Oak"))

#Sequence
#Objects must be defined before they are called, otherwise you get a name error

birds_available = "crow robin parrot sandpiper hawk pigeon"
def bird_availability(bird):
	return bird.title(),"available is",bird in birds_available
bird = input("enter a bird to search: ").lower()
print(bird_availability("Owl"))

#Module Completion Exercise:

def fishstore(fish_entry, price_entry):
	result = fish_entry.title()+ " costs $"+price_entry
	return result
fish_entry = input("Enter a type of fish: ")
price_entry = input("Enter the price of the fish: ")
print(fishstore(fish_entry, price_entry))







