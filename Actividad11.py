impuestos = {}
vehiculos = {}
carros2 = {}
cantidad = int(input("Ingrese la cantidad de propietarios que desee ingresar: "))
for i in range(cantidad):
    print(f"Propietario {i+1}")
    nit = int(input("Ingrese su NIT: "))
    nombre = input("Ingrese su nombre: ")
    numero = input("Ingrese su numero de telefono: ")
    cantidadVehiculos = int(input("Ingrese el numero de vehiculos que poseea: "))
    vehiculos = {}
    for i in range(cantidadVehiculos):
        print(f"Vehiculos {i+1}")
        placa = input("Ingrese el numero de placa: ").upper()
        marca = input("Ingrese la marca de su vehiculo: ")
        modelo = input("Ingrese el modelo de su vehiculo: ")
        ano = int(input("Ingrese el año de su vehiculo: "))
        estadoImpuesto = input("Ya pago impuesto? (s/n) ").lower()
        vehiculos[placa]= {
            "marca": marca,
            "modelo": modelo,
            "año": ano,
            "estadoImpuesto": estadoImpuesto
        }

    impuestos[nit] = {
        "nombre": nombre,
        "numero": numero,
        "cantidadVehiculos": cantidadVehiculos,
    }

print("Resumen")
for nit in impuestos:
    carros = impuestos[nit]
    print("Nit:", nit)
    print("Nombre:", carros["nombre"])
    print("Numero:", carros["numero"])
    print("Cantidad de vehiculo:", carros["cantidadVehiculos"])
    print("vehiculos:")
    for placa in vehiculos:
        carros2 = vehiculos[placa]
        print("- ", "|", placa, "|",carros2["marca"],"|",carros2["modelo"],"|", carros2["año"],"Impuestos: ",carros2["estadoImpuesto"])

buscar = int(input("Ingrese el nit por el cual quiere buscar al propietario: "))
if buscar in impuestos:
    impuestoPagados = 0
    impuestoNoPagados = 0
    if carros2["estadoImpuesto"] == "s":
        impuestoPagados +=1
    else:
        impuestoNoPagados +=1
    print(f"Carros con impuestos pagados: {impuestoPagados}")
    print(f"Carros con impuestos No pagados: {impuestoNoPagados}")
else:
    print("Ese propietario no existe")