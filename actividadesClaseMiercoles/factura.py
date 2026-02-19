# clase 18/02/2026 miercoles

""" 
por buenas practicas 

solo se va a crear funicones arriba y debajo del (if __name__ == '_main_' :) 
se llaman


pass =  no hacer nada 

los bloques de codigo no se deben dejar bacios 
si o si debe tener algun contenido y para mantener un bloque de codigo valido sin error se usa el pass

"""

""" 
crear un programa que por medio de funcuiones cree una factura electronica basica 
obteniendo datos desde la terminal

factura 
    producto
    precio 
    cantidad

    ------
    subtotal
    descuento 10%
    iva 19%
    neto...

"""

def Subtotal(precio , cantidad):
    return precio * cantidad

def Descuento(subtotal):
    descuento = 10/100 
    return subtotal * descuento

def Iva(subtotal) :
    iva = 19/100
    return subtotal * iva

def Neto(subtotal , iva , descuento):
    return (subtotal - descuento )+ iva

def mostrarFactura (subtotal , iva , descuento , neto , nombre , cantidad , precio ):
    print(" ")
    print("----- FACTURA -----")
    print(F"nombre del producto : {nombre}")
    print(F"precio del producto : {precio}")
    print(F"cantidad del producto : {cantidad}")
    print("----- pagar -----")
    print(F"valor subtotal : ${subtotal}")
    print(F"valor descuento 10%: ${descuento}")
    print(F"valor iva 19%: ${iva}")
    print(F"neto a pagar : ${neto}")

if __name__ == '__main__' : 
    nombreProducto = input("ingrese el nombre del producto: ")
    precioProducto = float(input("ingrese el precio del producto: "))
    cantidadProducto = int(input("ingrese la cantidad del producto: "))

    subtotal = Subtotal(precioProducto , cantidadProducto)
    descuento = Descuento(subtotal)
    iva = Iva(subtotal)
    neto = Neto(subtotal , iva , descuento)
    
    mostrarFactura(subtotal , iva , descuento , neto , nombreProducto , cantidadProducto , precioProducto)





