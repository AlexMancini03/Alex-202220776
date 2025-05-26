# main.py

import temperature

c = float(input("Enter temperature in Celsius: "))
print(f"Fahrenheit: {temperature.celsius_to_fahrenheit(c):.2f}")

f = float(input("Enter temperature in Fahrenheit: "))
print(f"Celsius: {temperature.fahrenheit_to_celsius(f):.2f}")
