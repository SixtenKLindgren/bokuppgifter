import math
radie = int(input("Säg en radie på en sfär "))

volym = 4 * math.pi * radie**3 / 3
area = 4 * math.pi * radie**2

print(f"Sfärens area är : {area} och volymen är : {volym}")