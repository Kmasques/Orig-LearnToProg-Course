def celciusToFahrenheit(celciusTemperature):
    fahrenheit = celsiusTemperature * (9.0/5.0) + 32.0
    return fahrenheit

def fahrenheitToCelcius (fahrenheitTemperature):
    celsius = (fahrenheitTemperature - 32.0) * (5.0/9.0)
    return celcius

def showMenu():
    print "A: Convert celcius to fahrenheit"
    print "B: Convert fahrenheit to celcius"
    print "X: Exit"

showMenu()
option = raw_input("option: ")
while option !="X":
    if option = "A":
    value = input("Temperature to convert: ")
        print (celciusToFahrenheit(float(value)))
