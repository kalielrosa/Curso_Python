dista = float(input("Distância da viajem por KM: "))
if dista <= 200:
    print("Sua passagem custa {:.2f}".format(200 * 0.50))
else: 
    print("Sua passagem custa {:.2f}".format(200 * 0.45))