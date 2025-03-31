import math

def calcular_area():
    while True:
        print("=" * 40)
        print("CALCULO DE SUPERFICIES (version 1.0)")
        print("=" * 40)
        print("1. Cuadrado        lado * lado")
        print("2. Rectángulo      pi*radio*radio")
        print("3. Círculo         base * altura")
        print("4. Triángulo       (base1 + base2)*altura/2")
        print("5. Trapecio        (base*altura)/2")
        print("=" * 40)     
        opcion = int(input("Ingrese el número de la figura (1-5): "))
        
        if opcion == 1:
            lado = float(input("Ingrese la longitud del lado del cuadrado: "))
            area = lado ** 2
            print(f"El área del cuadrado es: {area}")
        elif opcion == 2:
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = base * altura
            print(f"El área del rectángulo es: {area}")
        elif opcion == 3:
            radio = float(input("Ingrese el radio del círculo: "))
            area = math.pi * (radio ** 2)
            print(f"El área del círculo es: {area}")
        elif opcion == 4:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = (base * altura) / 2
            print(f"El área del triángulo es: {area}")
        elif opcion == 5:
            base_mayor = float(input("Ingrese la base mayor del trapecio: "))
            base_menor = float(input("Ingrese la base menor del trapecio: "))
            altura = float(input("Ingrese la altura del trapecio: "))
            area = ((base_mayor + base_menor) * altura) / 2
            print(f"El área del trapecio es: {area}")
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 5.")
            continue

        repetir = input("¿Desea calcular otra área? (s/n): ").lower()
        if repetir != 's':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

calcular_area()