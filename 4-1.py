tal = []

while True :
    temptal = int(input("Skriv ett positivt tal. Skriv ett negativt tal för att avbryta "))
    if temptal >= 0 :
        tal.append(temptal)
    else :
        break
tal.sort()
print(f"Det lägsta talet var: {tal[0]} och the högsta var {tal[len(tal)-1]}")