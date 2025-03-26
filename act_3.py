'''
Elabore un programa que permita calcular el salario neto de un empleado despues de descontar
los descuentos por conceptos de salud, pension, ARL
Debe solicitar:
    1: Tipo de empleado
        a- contrato a termino indefinido
        b- contrato por prestacion de servicio
        c- contrato de aprendizaje
        d- contrato freelance
    => freelance se solicita el numero de horas trabajadas y valor por hora
    y el total se calcula num hora * valor hora
    
'''

contrato = input("Ingrese el tipo de contrato: a- contrato a termino indefinido b- contrato por prestacion de servicio c- contrato de aprendizaje d- contrato freelance. : ")
total = 0


if contrato == "a":
    print("Eligio: Contrato a termino indefinido")
elif contrato == "b":
    print("Eligio: Contrato por prestacion de servicio")
elif contrato == "c":
    print("Eligio: Contrato de aprendizaje")
    sal_min = int(input("Digite el salario minimo: "))
    total = sal_min - (sal_min * 0.25)
elif contrato == "d":
    print("Eligio: Contrato freelance")
    num_hora = int(input("Digite el numero de horas trabajadas: "))
    val_hora = int(input("Digite el numero de valor por hora trabajada: "))
    total = num_hora * val_hora
else:
    print("Error")
print("El total de su salario es:", total)