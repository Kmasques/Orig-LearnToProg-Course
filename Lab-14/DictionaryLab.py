gpas = {

    }



def showMenu():
    print "A: Convert celsius to fahrenheit"
    print "B: Convert fahrenheit to celsius"
    print "X: Exit"

showMenu()
option = raw_input("Option: ")
while option !="X":
    if option == "A":
        Temp = input("Temperature to convert: ")
        print(celsiusToFahrenheit(float(Temp)))
    if option == "B":
        Temp = input("Temperature to convert: ")
        print(fahrenheitToCelsius(float(Temp)))

    else:
        print "Please choose another option"
        
    showMenu()
    option = raw_input("Option: ")






