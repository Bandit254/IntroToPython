#A test of basic Python skills: receiving user input, assigning it to a variable, manipulating the string,
#using Boolean operators to search the string, and combining variables along with string out put in the print statement.

input_test = input("Enter the categories of foods you have eaten in the last 24hrs: ").lower()
print("It is","Dairy".lower() in input_test,'that "',input_test,'" contains "Dairy"')
print("It is","Nuts".lower() in input_test,'that "',input_test,'" contains "Nuts"')
print("It is","Seafood".lower() in input_test,'that "',input_test,'" contains "Seafood"')
print("It is","Chocolate".lower() in input_test,'that "',input_test,'" contains "Chocolate"')

