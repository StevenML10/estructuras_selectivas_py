'''

if condicional_1
    inst_1
    inst_2
elif condicional_2
    inst_3
elif condicional_3
    inst_4

Solo se ejecuta un caso

'''

f = input("Digite su fruta: ")

if f == "manzana" or f == "MANZANA":

    print("Apple")

elif f == "naranja" or f == "NARANJA":

    print("Orange")

elif f == "uva" or f == "UVA":

    print("Grape")

else:
    print("Error")