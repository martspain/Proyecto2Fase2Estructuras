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
    
    #Se crean los intervalos de puntaje
    interOne = Node("IntervaloUno", minimum = 1, maximum = 10)
    interTwo = Node("IntervaloDos", minimum = 11, maximum = 20)
    interThree = Node("IntervaloTres", minimum = 21, maximum = 30)
    interFour = Node("IntervaloCuatro", minimum = 31, maximum = 40)
    interFive = Node("IntervaloCinco", minimum = 41, maximum = 50)
    interSix = Node("IntervaloSeis", minimum = 51, maximum = 60)
    interSeven = Node("IntervaloSiete", minimum = 61, maximum = 70)
    interEight = Node("IntervaloOcho", minimum = 71, maximum = 80)
    interNine = Node("IntervaloNueve", minimum = 81, maximum = 90)
    interTen = Node("IntervaloDiez", minimum = 91, maximum = 100)
    
    tx = graph.begin()
    tx.create(interOne)
    tx.create(interTwo)
    tx.create(interThree)
    tx.create(interFour)
    tx.create(interFive)
    tx.create(interSix)
    tx.create(interSeven)
    tx.create(interEight)
    tx.create(interNine)
    tx.create(interTen)
    
    tx.commit()
    

    
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
        
        #Haciendo la relacion con el intervalo de puntaje correspondiente
        if porcentaje > 0 and porcentaje <= 10:
            graph.create(Relationship(puntaje, "ESTA_EN", interOne))
        elif porcentaje > 10 and porcentaje <= 20:
            graph.create(Relationship(puntaje, "ESTA_EN", interTwo))
        elif porcentaje > 20 and porcentaje <= 30:
            graph.create(Relationship(puntaje, "ESTA_EN", interThree))
        elif porcentaje > 30 and porcentaje <= 40:
            graph.create(Relationship(puntaje, "ESTA_EN", interFour))
        elif porcentaje > 40 and porcentaje <= 50:
            graph.create(Relationship(puntaje, "ESTA_EN", interFive))
        elif porcentaje > 50 and porcentaje <= 60:
            graph.create(Relationship(puntaje, "ESTA_EN", interSix))
        elif porcentaje > 60 and porcentaje <= 70:
            graph.create(Relationship(puntaje, "ESTA_EN", interSeven))
        elif porcentaje > 70 and porcentaje <= 80:
            graph.create(Relationship(puntaje, "ESTA_EN", interEight))
        elif porcentaje > 80 and porcentaje <= 90:
            graph.create(Relationship(puntaje, "ESTA_EN", interNine))
        elif porcentaje > 90 and porcentaje <= 100:
            graph.create(Relationship(puntaje, "ESTA_EN", interTen))
    

# Funcion que calcula el porcenaje aleatoreamente    
def calcularPorcentajeRandom():
    import random
    cantidad=10
    rango=0
    rango = random.randint(1,4) 
    n=0
    numeros = []
    while n < cantidad:
        if rango == 1:
            numero = random.randint(1,2)
            numeros.append(numero)
            n = n + 1
        elif rango == 2:
            numero = random.randint(1,5)
            numeros.append(numero)
            n = n + 1
        elif rango == 3:
            numero = random.randint(4,5)
            numeros.append(numero)
            n = n + 1
        elif rango == 4:
            numero = random.randint(2,4)
            numeros.append(numero)
            n = n + 1
    suma = numeros[0] + numeros[1] + numeros[2] + numeros[3] + numeros[4] + numeros[5] + numeros[6] + numeros[7] + numeros[8] + numeros[9]
    porcentaje = (suma*100)/50
    return porcentaje

def relateIntervals(number, nodeOne):
    matcher = NodeMatcher(graph)
    InterOne = matcher.match("IntervaloUno").first()
    InterTwo = matcher.match("IntervaloDos").first()
    InterThree = matcher.match("IntervaloTres").first()
    InterFour = matcher.match("IntervaloCuatro").first()
    InterFive = matcher.match("IntervaloCinco").first()
    InterSix = matcher.match("IntervaloSeis").first()
    InterSeven = matcher.match("IntervaloSiete").first()
    InterEight = matcher.match("IntervaloOcho").first()
    InterNine = matcher.match("IntervaloNueve").first()
    InterTen = matcher.match("IntervaloDiez").first()
    
    #Haciendo la relacion con el intervalo de puntaje correspondiente
    if number > 0 and number <= 10:
        graph.create(Relationship(nodeOne, "ESTA_EN", InterOne))
    elif number > 10 and number <= 20:
        graph.create(Relationship(nodeOne, "ESTA_EN", InterTwo))
    elif number > 20 and number <= 30:
        graph.create(Relationship(nodeOne, "ESTA_EN", InterThree))
    elif number > 30 and number <= 40:
        graph.create(Relationship(nodeOne, "ESTA_EN", InterFour))
    elif number > 40 and number <= 50:
        graph.create(Relationship(nodeOne, "ESTA_EN", InterFive))
    elif number > 50 and number <= 60:
        graph.create(Relationship(nodeOne, "ESTA_EN", InterSix))
    elif number > 60 and number <= 70:
        graph.create(Relationship(nodeOne, "ESTA_EN", InterSeven))
    elif number > 70 and number <= 80:
        graph.create(Relationship(nodeOne, "ESTA_EN", InterEight))
    elif number > 80 and number <= 90:
        graph.create(Relationship(nodeOne, "ESTA_EN", InterNine))
    elif number > 90 and number <= 100:
        graph.create(Relationship(nodeOne, "ESTA_EN", InterTen))

def newInput():
    while True:
        while True:
            try:
                entry = input('\n Escriba aqui: ')
                entry = int(entry)
                break
            except ValueError:
                print('                   (¡Has ingresado texto en vez de un numero como opcion, por favor vuelvelo a intentar!)')
                print('____________________________________________________________________________________________________________________________')
                print('                                              Para continuar presione: (Enter)')
                input()
        if entry > 0:
            if entry <= 5: # Aqui se coloca el numero maximo de opciones que se quiere validar en la entrada
                break
            else:
                print('                         (Has ingresado una opcion fuera del Rango, por favor vuelvelo a intentar!)')
                print('____________________________________________________________________________________________________________________________')
                print('                                           Para continuar presione: (Enter)')
                input()
                continue
        else:
            print('                         (Has ingresado una opcion fuera del Rango, por favor vuelvelo a intentar!)')
            print('____________________________________________________________________________________________________________________________')
            print('                                           Para continuar presione: (Enter)')
            input()
            continue
    return entry
        

    