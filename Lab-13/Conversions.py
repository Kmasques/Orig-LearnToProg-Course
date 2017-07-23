def celsiusToFahrenheit(celsiusTemperature):
    fahrenheit = celsiusTemperature * (9.0/5.0) + 32.0
    return fahrenheit

def fahrenheitToCelsius (fahrenheitTemperature):
    celsius = (fahrenheitTemperature - 32.0) * (5.0/9.0)
    return celsius

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






