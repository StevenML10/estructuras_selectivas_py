Et = int(input("Ingrese Su Estrato: "))
Ed = int(input("Ingrese Su Edad: "))
Vm = int(input("Ingrese El Valor Completo De La Matricula: "))
if Et == 1 and Ed < 18:
    Valor = Vm - (Vm * 0.2)
    print("El Valor Total de La Matricula Es De: ", Vm)
    print("Su Descuento Es Del 20%")
    print("Usted Debe Pagar: ", Valor)
elif Et == 1 and Ed >= 18:
    Valor = Vm - (Vm * 0.15)
    print("El Valor Total de La Matricula Es De: ", Vm)
    print("Su Descuento Es Del 15%")
    print("Usted Debe Pagar: ", Valor)
elif Et == 2 and Ed < 18:
    Valor = Vm - (Vm * 0.1)
    print("El Valor Total de La Matricula Es De: ", Vm)
    print("Su Descuento Es Del 10%")
    print("Usted Debe Pagar: ", Valor)
elif Et == 2 and Ed >= 18:
    Valor = Vm - (Vm * 0.05)
    print("El Valor Total de La Matricula Es De: ", Vm)
    print("Su Descuento Es Del 5%")
    print("Usted Debe Pagar: ", Valor)
else: 
    print("Vuelve A Intentarlo")