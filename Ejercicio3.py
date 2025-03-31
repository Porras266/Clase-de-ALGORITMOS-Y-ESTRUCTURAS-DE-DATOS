#3. Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, 
# ofreciendo un descuento del 15% por la compra de más de 3 docenas y 10% en caso contrario.
#  Además, por la compra de más de 3 docenas se obsequia una unidad del producto por cada docena 
# en exceso sobre 3. Diseñe un programa que determine el monto de la compra, el monto del descuento,
#  el monto a pagar y el número de unidades de obsequio por la compra de cierta cantidad de docenas 
# del producto.

#15 % por mas de 3 docenas
#por la compra de 3 docenas se obsequia 1 docena por docena en exceso de 3
#10% en caso contrario
#determinar el monto de la compra, el monto de descuento, el monto a pagar y el numero de unidades que 
import os
print("********Registro de supermecado********")
print("-" * 40)
precio_PapasLB = 120

while True:
    eleccion = input("Desea Registrar una venta (Sí - No): ").upper()
    os.system('cls')
    if eleccion == "SI":
        print(f"Venta de Papas Precio por 1 Libra {precio_PapasLB}C$")
        libras_Llevar = int(input("Ingrese cuantas libras desea llevar: "))
        libras_Regalar = max(0, libras_Llevar - 3)
        total_Libras = libras_Llevar + libras_Regalar
        subtotal = precio_PapasLB * libras_Llevar
        if libras_Llevar >= 4:
            os.system('cls')
            descuento = subtotal * 15 / 100
            total = subtotal - descuento
            print(f"Tu subtotal sin descuento aplicado es de {subtotal}C$")
            print(f"Llevas {libras_Llevar} libras se te regalaran {libras_Regalar} libras por tu compra")
            print(f"Tu total aplicando el 15% de descuento es {subtotal}C$ - {descuento}C$")
            print("-" * 40)
            print(f"pagas {libras_Llevar} Libras y llevas *{total_Libras}* libras tu total es de {total}C$")
        else:
            os.system('cls')
            print(f"Tu subtotal sin descuento aplicado es de {subtotal}C$")
            descuento2 = subtotal * 10 / 100
            total2 = subtotal - descuento2
            print(f"Tu total aplicando el 10% de descuento es {subtotal}C$ - {descuento2}C$")
            print("-" * 40)
            print(f"pagas {libras_Llevar} Libras tu total es de {total2}C$")
    elif eleccion == "NO":
     print("Gracias por su visita")
     input("Presione enter para terminar")
     break
    else:
      print("Opción inválida. Por favor, ingrese 'Sí' o 'No'.")
      
 
