personnmr = input("Skriv ett personnummer. ")

first = personnmr.split("-")[0]
last = personnmr.split("-")[1]

splitfirst = list(first)
newlist = []

for i in range(len(splitfirst)) :
    x = (int(splitfirst[i]) * abs(i % 2 - 2))
    if len(str(x)) > 1:
        newlist.append(int(list(str(x))[0]))
        newlist.append(int(list(str(x))[1]))
    else :
        newlist.append(x)
           
if 10 - (sum(newlist) % 10) == int(last) % 10 :
    print("korrekt personnummer")
else :
    print("inkorrekt personnummer") 



