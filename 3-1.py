minuter = int(input("Hur många minuter kommer du ringa på en månad? "))

if minuter <= 33 :
    print("Du borde köpa Kontant abonnemanget")
elif minuter <= 66 :
    print("Du borde köpa Normal abonnemanget")
elif minuter > 66 :
    print("Du borde köpa Plus abonnemanget")