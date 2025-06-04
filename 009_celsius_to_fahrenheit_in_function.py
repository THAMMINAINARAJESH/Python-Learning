# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9 / 5) + 32
# print(f"{celsius}°C = {fahrenheit:.2f}°F")

n = float(input("Enter temperature in Celsius: "))
def celsius_fahrenheit(n):
    celsius = n
    fahrenheit = (celsius * 9 / 5) + 32
    print ( f"{celsius}°C = {fahrenheit:.2f}°F" )
celsius_fahrenheit(n)