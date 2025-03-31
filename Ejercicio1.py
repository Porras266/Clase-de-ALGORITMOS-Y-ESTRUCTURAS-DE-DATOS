import os
#leer el precio de un producto, calcule el impuesto de un valor agregado

print("Este programa calcula el importe a pagar en una carretera")

while True:
    eleccion = input("\n¿Desea registrar un medio de transporte? (Sí - No): ").upper()  # Convertir a mayúsculas para evitar errores
    os.system('cls')
    
    print("-" * 55)
    if eleccion == "SI":
        nombre = input("ingrese el nombre de su medio de transporte\nAuto\nMoto\nBicicleta\nCamion \n").upper()
        #Auto
        if nombre == "AUTO":
            try:
                distancia = int(input("Ingrese cuantos Km a reccorido con su Auto: "))
                print("-" * 55)
                print("*************Baucher de pago*************")
                print("El pago del auto es de 30 cordobas por KM")
                print(f"En su caso 30 Cordobas * {distancia}Km")
                pago = distancia * 30
                print(f"Debe de pagar {pago} Cordobas")
                clear()
            except ValueError:
                print("Ingrese un valor adecuado")     
                #Moto
        elif nombre == "MOTO":
            try:
                distancia = int(input("Ingrese cuantos Km a reccorido con su Moto: "))
                print("-" * 55)
                print("**********Baucher de pago**********")
                print("El pago de Moto es de 30 cordobas por KM")
                print(f"En su caso 30 Cordobas * {distancia}Km")
                pago = distancia * 30
                print(f"Debe de pagar {pago} Cordobas")
            except ValueError:
                print("Ingrese un valor adecuado")
                #BIcleta
        elif nombre == "BICICLETA":
            try:
                print("La bicicleta paga un importe fijo de 100 cordobas")
                print("-" * 55)
                print("**********Baucher de pago**********")
                print("El pago de Bicileta es de 100 cordobas ")
                print(f"Debe de pagar 100 Cordobas")
            except ValueError:
                print("Ingrese un valor adecuado")
        elif nombre == "CAMION":
            try:
                distancia = int(input("Ingrese cuantos Km a reccorido con su Camion: "))
                Toneladas = int(input("Ingrese de cuantas toneladas es su Camion: "))
                print("-" * 55)
                print("**********Baucher de pago**********")
                print("El pago del camion es de 30 cordobas por Km y 25 Cordobas por tonelada")
                print(f"En su caso 30 Cordobas * {distancia}Km + 25 cordobas * {Toneladas}Toneladas")
                pago1 = distancia * 30
                pago2 = Toneladas * 25
                total = pago1 + pago2
                print(f"Debe de pagar *{pago1}* Cordobas por sus km y *{pago2}* cordobas por peso")
                print(f"Total *{total}* Cordobas")
            except ValueError:
                print("Ingrese un valor adecuado")
        else:
            print("Medio de transporte no reconocido. Por favor, elija entre Auto, Moto, Bicicleta o Camión.")
    elif eleccion == "NO":
        print("Gracias por su visita.")
        input("Presione Cualquier tecla para terminar")
        break  # Detiene el bucle cuando el usuario elige "NO"
    
    else:
        print("Opción inválida. Por favor, ingrese 'Sí' o 'No'.")


        



                
                


       
   





