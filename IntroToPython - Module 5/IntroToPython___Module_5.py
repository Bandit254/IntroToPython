#Culminating exercise of the Intro to Python Course

reportType = ""
while reportType=="":
    reportType=input("Select which type of report you want, Totals (\"T\") or All Items (\"A\"): ")
def adding_report(reportType="T"):
    total=0
    items = ""
    print("Input an integer to add to the total or \"Q\" to quit:")
    while True:
        value=input("Enter an integer or \"Q\": ")
        if value.isdigit()==True:
            total+=int(value)
            items+=value+"\n"
        elif value.isalpha()==True & value.lower().startswith("q")==True:
            if reportType=="T":
                    print("\nTotal\n"+str(total))
                    break
            else:
                print("\nItems\n"+items)
                print("\nTotal\n"+str(total))
                break
        else:
           print(value+" is invalid Input")

adding_report(reportType)


