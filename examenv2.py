import random

def obtenir_nom(): 
    noms = ["Timotei", "Timonel", "Timbaler", "Tennebaum", "TaoPaiPai", "Teruel", "Tirolés", "Traginer", "Tourmalet"]
    cognoms = ["Chandalet", "Camembert", "Sabadell", "Chevrolet", "Caganer", "Bechamel", "Casteller", "Churumbel", "Cafeaulait", "Crivillé", "Charmander"]
    
    nom_al= random.choice(noms) 
    cognom_al=random.choice(cognoms) 
    juntar = nom_al + " " + cognom_al
    
    return juntar

def afegir_nom(llista):
    nom_aleatori = obtenir_nom()
    llista.append(nom_aleatori)

def llistar_noms(llista): # Funcion para listar en fila los elementos de la lista
    for llista in llista: # Recorre cada elemento dentro de la lista
        print(llista) # Devuelve los elementos de la lista

def ordenar_noms(llista):
    llista.sort() # Ordenamos en descendente la lista
    print(llista) # Devolvemos la lista ordenada en descendente
        
def mostrar_menu():
    print("[A] Afegir nom")
    print("[L] Llistar noms")
    print("[O] Ordenar noms")
    print("[F] Finalitzar")

def demanar_opcio(): # Funcion para saber que opcion quiere el usuario y ejecutarsela y comprobar que es correcta
    opcio = input("Que vols fer: ").lower() # Preguntamos que quiere añadir y ponemos el .lower para que todo lo que pille se vuelva minuscula
    while opcio not in "a" "l" "o" "f": # Mientras que opcio no sea ninguno de estos valores, seguira preguntando hasta que se lo añada el usuario el correcto
            mostrar_menu() # Mostramos el menu otra vez
            demanar_opcio() # Y volvemos a preguntar hasta que termine el bucle
    match opcio: # Si la funcion cumple alguno de estos requisitos
        case "a": # Va ordenado como por mostrar menu, cuando pongamos la letra que queramos utilizar, ira a la funcion que la ejecute.
            gestionar_opcio(opcio, llista) # agregamos a llista el nombre aleatorio que nos devuelve (return) la funcion obtenir_nom()
        case "l":
            gestionar_opcio(opcio, llista)
        case "o":
            gestionar_opcio(opcio, llista)
        case "f":
            gestionar_opcio(opcio, llista)

def gestionar_opcio(opcio, llista): # Vemos si la opcion cumple con requisitos de demanar_opcio que seria que sean iguales a "ALOF"
    match opcio: # Empezamos a emparejar opciones a la variable opcio
        case "a": # en el caso de afegir nom
            afegir_nom(llista) # Llamamos a la funcion que añade el nombre y apellido aleatorios
            mostrar_menu() # Mostramos menu
            demanar_opcio() # Y volvemos a preguntar, asi con todas, hasta que diga F y finalize.
        case "l": # Llistar
            llistar_noms(llista)
            mostrar_menu()
            demanar_opcio()
        case "o": # Ordenar
            ordenar_noms(llista)
            mostrar_menu()
            demanar_opcio()
        case "f": #Finalitzar
            print("Has finalitzat")

# Programa principal
llista =[]
mostrar_menu()
opcio = demanar_opcio()