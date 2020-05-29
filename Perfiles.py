# Proyecto 2: Meetguin 
# Autores:
#     Sofía Rueda     Carné: 19099
#     Hansel López    Carné: 19026
#     Martín España   Carné: 19258

# Base de datos
from py2neo import*
graph = Graph("bolt://localhost:7687", auth=("neo4j","1234"))

# Perfiles importados desde archivo de texto almacenados de la siguiente forma: nombre,sexo,edad

#Funcion que lee el archivo
def readTXT(): 
    archivo = open("users.txt", "r") #Abriendo archivo
    for line in archivo.readlines():
        data = line.split(",", 2) #Separandolo por comas
        
        #Creando nodo del usuario
        user = Node("Persona", name= data[0], sex= data[1], age= data[2])
        tx = graph.begin()
        tx.create(user)
        tx.commit()
        
        #Creando nodo del Puntaje
        porcentaje = calcularPorcentajeRandom()
        puntaje = Node("Puntaje", score= porcentaje)
        tx = graph.begin()
        tx.create(puntaje)
        tx.commit()
        archivo.close()
        
        #Creando relacion entre nodos
        graph.create(Relationship(user, "OBTUVO_PUNTAJE", puntaje))
    
# Funcion que calcula el porcenaje aleatoreamente    
def calcularPorcentajeRandom():
    import random
    cantidad=10
    n=0
    numeros = []
    while n < cantidad:
        numero = random.randint(1,5)
        numeros.append(numero)
        n = n + 1
    suma = numeros[0] + numeros[1] + numeros[2] + numeros[3] + numeros[4] + numeros[5] + numeros[6] + numeros[7] + numeros[8] + numeros[9]
    porcentaje = (suma*100)/50
    return porcentaje
        




        

    