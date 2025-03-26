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
    val / mes - 15%con - 10%
    si el empleado tiene una antiguedad de >= 10 años bonificacion del 0.5% sobre el salario mensual
'''

contrato = input("Ingrese el tipo de contrato: a- contrato a termino indefinido b- contrato por prestacion de servicio c- contrato de aprendizaje d- contrato freelance. : ")
total = 0


if contrato == "a":
    print("Eligio: Contrato a termino indefinido")
    antiguedad = int(input("Ingrese la antiguedad del empleado (Año):"))
    grado = int(input("Ingrese el grado del empleado:(1-5)"))
    total = int(input("Ingrese el salario neto del empleado:"))
    salario_minimo = int(input("Ingrese el salario minimo:"))
    if grado == 1:
        total = salario_minimo*1.5
    elif grado == 2:
        total = salario_minimo*1.7
    elif grado == 3:
        total = salario_minimo*2.0
    elif grado == 4:
        total = salario_minimo*2.5
    elif grado == 5:
        total = salario_minimo*3.0
    if antiguedad >= 1 and antiguedad <= 5:
        total = total + (salario_minimo*0.01)
    elif antiguedad >= 6 and antiguedad <= 10:
        total = total + (salario_minimo*0.02)
    elif antiguedad >= 10:
        total = total + (salario_minimo*0.03)
    total = total - (total*0.25) - (total*0.22) - (total*0.001)
        

elif contrato == "b":
    print("Eligio: Contrato por prestacion de servicio")
    val_con = int(input("Digite el valor del contrato: "))
    mes_con = int(input("Digite el numero de meses del contrato: "))
    ant_con = int(input("Digite los años empleados: "))
    sal_men = val_con / mes_con
    eps = sal_men * 0.15
    pen = sal_men * 0.10
    boni = sal_men * 0.05
    total = sal_men - eps - pen
    if ant_con >= 10:
        total = total + boni

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