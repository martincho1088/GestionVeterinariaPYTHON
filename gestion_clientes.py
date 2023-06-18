from asyncore import ExitNow
from tkinter import END
import clases
import os
import pickle


fichero_clientes = "clientes.pkl"
datos_modificados = False
lista_clientes = [] 
if os.path.exists(fichero_clientes):
    with open(fichero_clientes, 'rb') as f:
        lista_clientes = pickle.load(f)

### MENU ###
def mostrar_opciones():
    print("\n")
    print("1- ALTA")
    print("2- BAJA")
    print("3- MODIFICACIÓN")
    print("4- CONSULTA_CLIENTE")
    print("5- CONSULTA GLOBAL")
    print("6- GUARDAR")
    print("7- SALIR")
    print("8- LADRAR")
    opcion = int(input("Introduzca una opción: "))
    print("\n")
    return opcion

def obtener_cliente(dni):
    for cliente in lista_clientes:
        if cliente.dni == dni: return cliente

def alta_cliente():
    global datos_modificados
    print("Por favor introduzca los siguientes datos:")
    dni =input("DNI: ")
    if obtener_cliente(dni)==None:
        nombre_cliente = input("Nombre del cliente: ")
        nombre_perro = input("Nombre del perro: ")
        raza = input("Raza: ")
        perro = clases.Perro(nombre_perro, raza)
        cliente = clases.Cliente(nombre_cliente, dni, perro)
        lista_clientes.append(cliente)
        print("Cliente dado de alta!!")
        datos_modificados=True
    else:
        print("Ya existe un cliente con el DNI " + dni + "-------")

def modificacion_cliente():
    global datos_modificados
    dni = input("DNI del cliente a modificar? ")
    cliente = obtener_cliente(dni)
    if cliente==None:
        print("---El cliente con DNI " + dni + ", no existe-----")
    else:
        print("Por favor, rellena los siguientes datos:")
        nombre_cliente = input("Nombre del cliente: ")
        if nombre_cliente != "":
            cliente.nombre = nombre_cliente
        nombre_perro = input("Nombre del Perro: ")
        if nombre_perro != "":
            cliente.perro.nombre = nombre_perro
        raza = input("Tipo de raza: ")
        if raza != "":
            cliente.perro.raza = raza
        print("----CLIENTE MODIFICADO---")
        datos_modificados = True

def informacion_cliente():
    dni = input("Introduce el DNI del cliente a consultar: ")
    cliente = obtener_cliente(dni)
    if cliente ==None:
        print("----El cliente con DNI " + dni + ", no existe----")
    else:
        print("-----CLIENTE:-----" + "\nNombre: " + cliente.nombre + "\nDNI: " + cliente.dni + "\nNombre de perro: " + 
        cliente.perro.nombre + "\nRaza: " + cliente.perro.raza)
def informacion_clientes():
    tabla = []
    for cliente in lista_clientes:
        print("-----CLIENTE:-----" + "\nNombre: " + cliente.nombre + "\nDNI: " + cliente.dni + "\nNombre de perro: " + 
        cliente.perro.nombre + "\nRaza: " + cliente.perro.raza + "\n")
    pausa = input("Pulsa una letra para continuar")

def guardar():
    global datos_modificados
    with open(fichero_clientes, 'wb') as filestream:
        pickle.dump(lista_clientes, filestream)
    print("Información del cliente guardada!")
    datos_modificados = False

def ladrar():
    clases.Perro.ladrar("Beta")

    ##CARGAR MENU ##
while True:
    opcion = mostrar_opciones()
    if opcion == 1: alta_cliente()
    elif opcion == 3: modificacion_cliente()
    elif opcion == 4: informacion_cliente()
    elif opcion == 5: informacion_clientes()
    elif opcion == 6: guardar()
    elif opcion == 8: ladrar()
    elif opcion == 7: quit()
    if datos_modificados :
        respuesta = input("¿Quiere guardar los datos realizados?(S/N)")
        if respuesta =="s" or respuesta == "S":
            guardar()
        else:
            break
