FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
temperature = float(input("Enter the temperature to convert: " ))
unit= input("Is this temperature in Celsius or Fahrenheit? (C/F): ").capitalize()
if unit == "C":
    conv_temp = convert_to_celsius(temperature)
    print(f"{temperature}°C is {conv_temp}°F")
elif unit == "F":
    conv_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature}°F is {conv_temp}°C")
else:
    print("Invalid Entry, insert (C/F)")
