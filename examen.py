import random

def obtenir_nom(): # Funcion para obtener los elementos que añadir a la lista
    # Llista de noms incorrectes 
    noms = ["Timotei", "Timonel", "Timbaler", "Tennebaum", "TaoPaiPai", "Teruel", "Tirolés", "Traginer", "Tourmalet"]
    # Llista de cognoms incorrectes 
    cognoms = ["Chandalet", "Camembert", "Sabadell", "Chevrolet", "Caganer", "Bechamel", "Casteller", "Churumbel", "Cafeaulait", "Crivillé", "Charmander"]
    nom_al= random.choice(noms) # Escogemos aleatoriamente un nombre de la lista
    cognom_al=random.choice(cognoms) # Escogemos aleatoriamente un cognom de la lista
    juntar = f"{nom_al} {cognom_al}" # Juntamos tanto el nombre aleatorio como el apellido aleatorio
    return juntar # Le devolvemos el resultado a la funcion.
    # Aquí has de construir un nom amb un nom aleatori i un cognom aleatori de les llistes
    # retornar el nom construït

def afegir_nom(llista): # Funcion para añadir elementos a la lista
    obtenir_nom() # Llamamos a la funcion para traer el resultado aleatorio
    llista.append(obtenir_nom()) # Y sumamos a nuestra lista el resultado aleatorio, que seria por ejemplo Nom Cognom 

def llistar_noms(llista): # Funcion para listar en fila los elementos de la lista
    for llistar in llista: # Recorre cada elemento dentro de la lista
        return llistar # Devuelve los elementos de la lista

def ordenar_noms(llista):
    llista.sort() # Ordenamos en descendente la lista
    return llista # Devolvemos la lista ordenada en descendente
        
def mostrar_menu():
    print("[A] Afegir nom")
    print("[L] Llistar noms")
    print("[O] Ordenar noms")
    print("[F] Finalitzar")

def demanar_opcio(opcio, llista): # Funcion para saber que opcion quiere el usuario y ejecutarsela y comprobar que es correcta
    opcio = input("Que vols fer: ").lower() # Preguntamos que quiere añadir y ponemos el .lower para que todo lo que pille se vuelva minuscula
    while opcio not in "alof": # Mientras que opcio no sea ninguno de estos valores, seguira preguntando hasta que se lo añada el usuario el correcto
            mostrar_menu() # Mostramos el menu otra vez
            demanar_opcio(opcio, llista) # Y volvemos a preguntar hasta que termine el bucle
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
            demanar_opcio(opcio, llista) # Y volvemos a preguntar, asi con todas, hasta que diga F y finalize.
        case "l": # Llistar
            llistar_noms(llista)
            mostrar_menu()
            demanar_opcio(opcio, llista)
        case "o": # Ordenar
            ordenar_noms(llista)
            mostrar_menu()
            demanar_opcio(opcio, llista)
        case "f": #Finalitzar
            print("Has finalitzat")

# Programa principal
opcio=""
llista=[]
# Yo creo que el problema esta en la parte de funciones de cada apartado, las de comprobacion hacen  bien la comprobacion, pero las funciones no hacen su deber, por lo que a nivel comprobacion, esta bien unicamente la F, que al ser finalizacion, no llama a ninguna funcion y simplemente finaliza el programa
mostrar_menu() # Mostramos el menu
demanar_opcio(opcio, llista) # Llamamos a la funcion padre, la que manejara a todas.