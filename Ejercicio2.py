"""Escribir un programa que permita emitir la FACTURA 
correspondiente, a una compra de un artículo determinado, del 
que se adquieren una o varias unidades. El IVA a aplicar es de 15%
y si el Sub Total (precio de venta por cantidad), es mayor de 1000, 
se aplicará un descuento del 12%."""
import os
print("********Programa de facturacion********")
print("-" * 30)

while True:
    eleccion = input("Desea Registrar una venta (Sí - No): ").upper()
    os.system('cls')
    
    if eleccion == "SI":
        producto = int(input("Seleccione un producto por su numero \n1.Banana\n2.Sandia\n3.Melon\n4.Mango\nIngrese su eleecion: "))
        os.system('cls')
        if producto == 1:
            try:
                 precioBanana = 10
                 print(f"El precio de Banana es de 10C$ + 15% de IVA")
                 cantidad = int(input(f"Ingrese la cantidad de Banana a escoger: "))
                 print("-" * 40)
                 print(f"En tu caso llevas {cantidad} Bananas * 10C$ + 15%")
                 subtotal = cantidad * precioBanana
                 IVA = subtotal * 15 /100
                 Precio_IVA = subtotal + IVA
                 if Precio_IVA > 1000:
                     os.system('cls')
                     precio_Descuento = Precio_IVA * 12 /100
                     total_Descuento = Precio_IVA - precio_Descuento
                     print("********FACTURA DE COMPRA********")
                     print("Haz superado los 1000C$ obtienes un descuento del 12%")
                     print(f"Tu subtotal antes del descuento es de {Precio_IVA}C$")
                     print(f"Precio con descuento es de C${total_Descuento}C$")
                     print("-" * 40)
                 else:
                     print("********FACTURA DE COMPRA********")
                     print("No haz superado los 1000C$ no recibes descuento")
                     print(f"Tu total a pagar es de {Precio_IVA}C$")
                     print("-" * 40)
            except ValueError:
               print("Ingrese un valor adecuado")
        if producto == 2:
            try:
                 precioBanana = 35
                 print(f"El precio de Sandia es de 35C$ + 15% de IVA")
                 cantidad = int(input(f"Ingrese la cantidad de Sandia a escoger: "))
                 print("-" * 40)
                 print(f"En tu caso llevas {cantidad} Sandias * 10C$ + 15%")
                 subtotal = cantidad * precioBanana
                 IVA = subtotal * 15 /100
                 Precio_IVA = subtotal + IVA
                 if Precio_IVA > 1000:
                     os.system('cls')
                     precio_Descuento = Precio_IVA * 12 /100
                     total_Descuento = Precio_IVA - precio_Descuento
                     print("********FACTURA DE COMPRA********")
                     print("Haz superado los 1000C$ obtienes un descuento del 12%")
                     print(f"Tu subtotal antes del descuento es de {Precio_IVA}C$")
                     print(f"Precio con descuento es de C${total_Descuento}C$")
                     print("-" * 40)
                 else:
                     print("********FACTURA DE COMPRA********")
                     print("No haz superado los 1000C$ no recibes descuento")
                     print(f"Tu total a pagar es de {Precio_IVA}C$")
                     print("-" * 40)
            except ValueError:
               print("Ingrese un valor adecuado")
        if producto == 3:
            try:
                 precioMelon = 65
                 print(f"El precio del Melon es de 65C$ + 15% de IVA")
                 cantidad = int(input(f"Ingrese la cantidad de Melon a escoger: "))
                 print("-" * 40)
                 print(f"En tu caso llevas {cantidad} Melon * 65C$ + 15%")
                 subtotal = cantidad * precioBanana
                 IVA = subtotal * 15 /100
                 Precio_IVA = subtotal + IVA
                 if Precio_IVA > 1000:
                     os.system('cls')
                     precio_Descuento = Precio_IVA * 12 /100
                     total_Descuento = Precio_IVA - precio_Descuento
                     print("********FACTURA DE COMPRA********")
                     print("Haz superado los 1000C$ obtienes un descuento del 12%")
                     print(f"Tu subtotal antes del descuento es de {Precio_IVA}C$")
                     print(f"Precio con descuento es de C${total_Descuento}C$")
                     print("-" * 40)
                 else:
                     print("********FACTURA DE COMPRA********")
                     print("No haz superado los 1000C$ no recibes descuento")
                     print(f"Tu total a pagar es de {Precio_IVA}C$")
                     print("-" * 40)
            except ValueError:
               print("Ingrese un valor adecuado")        
                     
                