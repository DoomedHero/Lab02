name = "Jasper"
age = 44
height = 6
favorite_color = "Red"

print(f"""{name}
Age: {age}
Height: {height}
Favorite Color {favorite_color}
""")

import math

r = int(input("Enter a circle radius: "))
circle_area = math.pi * math.pow(r,2)
print(f"Circle Area with radius {r} is {circle_area:.1f}")

print(f"Square Root of my age is {math.sqrt(age)}")

print(f"sin of height: {math.sin(height)}, cos of height: {math.cos(height)}")

print(f"Sum of Age and 5: {age + 5}")

print(f"the difference between my height and 4 is {height - 43}")

print(f"The product of my age and height is: {age * height}")

print(f"the quotient of height and 2 is: {height / 2}")

print(f"The remainder of my age divided by 3 {age % (age + 1)}")

print(f"Age raised to the power of 2 {age ** 2}")

temp_fahrenheit = int(input("enter a temperature in Fahrenheit: "))
celsius = (temp_fahrenheit - 32) * (5/9)
print(f"Temp Fahrenheit {temp_fahrenheit}°F in Celsius is {celsius}°C")