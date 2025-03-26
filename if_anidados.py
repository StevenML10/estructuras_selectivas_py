'''
If anidado es un if dentro de otro if

if condicion:
    print ("mensaje")
    if condicion:
        print ("mensaje")
        if condicion:
            print ("mensaje")
                elif:
                    print ("mensaje ")
else:
    print ("mensaje")
'''

# >18 años pero no tiene documento no puede votar
# <18 años no puede votar

edad = int(input("ingrese su edad: "))

if edad >= 18:
    documento = input("Tiene documento(si/no)")
    if documento == "si":
        print ("puede votar")
    else:
        print ("no puede votar")
else:
    print ("no puede votar")