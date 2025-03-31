#4. Diseñe un programa que lea un número de tres cifras y determine si es igual al revés del número.
# Leer un número de tres cifras
numero = input("Ingrese un número de tres cifras: ")

# Validar que sea un número de tres cifras
#len funciona para contar cada espacio que tiene la cadena por ejemplo "hola" = 4, 345 = 3
# and numero.isdigit(): funciona para saber si en una captura de datos son numericos devuelve true 
if len(numero) == 3 and numero.isdigit():
    # Verificar si el número es igual al revés del número
    # la parte "numero[::-1]"  
    if numero == numero[::-1]:
        print(f"El número {numero} es igual al revés: ¡Es capicúa!")
    else:
        print(f"El número {numero} no es igual al revés.")
else:
    print("Por favor, ingrese un número válido de tres cifras.")
