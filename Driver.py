# Proyecto 2: Meetguin 
# Autores:
#     Sofía Rueda     Carné: 19099
#     Hansel López    Carné: 19026
#     Martín España   Carné: 19258
#Referencias bibliograficas: https://github.com/elena/py2neo-quickstart#step-1-connect-to-graph-using-py2neo
#https://www.youtube.com/watch?time_continue=229&v=3JMhX1sT98U&feature=emb_title

# Importando modulo Perfiles.py
import Perfiles as profiles

# Base de datos
from py2neo import*
graph = Graph("bolt://localhost:7687", auth=("neo4j","1234"))

graph.delete_all()

# Se insertan usuarios preguardados desde archivo: txt
profiles.readTXT()


# Bandera del menu principal
loginIsActive = True
menuIsActive = True


def registro():
    
    print("\n*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_* REGISTRO I *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n")
    nombre = input("~ Ingrese su nombre: ")
    sexo = input("~ Ingrese su sexo (femenio/masculino): ")
    edad = input("~ Ingrese su edad: ")
        
    user = Node("Persona", name= nombre, sex= sexo, age= edad)
    tx = graph.begin()
    tx.create(user)
    tx.commit()
    
    # Preguntas para encontrar match 
    print("\n*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_* REGISTRO II *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n")
    print("\nA continuación se le presentara una serie de preguntas para determinar su nivel de compatibilidad con otros usuarios. Las preguntas se responden a partir de una escala del 1 al 5, ingrese el numero con la opción que le interese.\n")
    
    print("1. ¿Qué tanto le importa el matrimonio?\n\n - 1. No me importa para nada \n - 2. No me importa \n - 3. Me da igual \n - 4. Me importa \n - 5. Me importa mucho")
    num1 = int(input())
    print("   \n---> ¿Qué tanto debería importarle a su pareja?\n\n - 1. No le importa para nada \n - 2. No le importa \n - 3. Le da igual \n - 4. Le importa \n - 5. Le importa mucho")
    num2 = int(input())
    
    print("\n2. ¿Qué tan importante es la religión para usted?\n\n - 1. No me importa para nada \n - 2. No me importa \n - 3. Me da igual \n - 4. Me importa \n - 5. Me importa mucho")
    num3 = int(input())
    print("   \n---> ¿Qué tan importante debería ser para su pareja?\n\n - 1. No le importa para nada \n - 2. No le importa \n - 3. Le da igual \n - 4. Le importa \n - 5. Le importa mucho")
    num4 = int(input())
    
    print("\n3. ¿Le interesa tener hijos y formar una familia?\n\n - 1. No me importa para nada \n - 2. No me importa \n - 3. Me da igual \n - 4. Me importa \n - 5. Me importa mucho")
    num5 = int(input())
    print("   \n---> ¿Qué tan interesada debería estar su pareja?\n\n - 1. No le importa para nada \n - 2. No le importa \n - 3. Le da igual \n - 4. Le importa \n - 5. Le importa mucho")
    num6 = int(input())
    
    print("\n4. ¿Qué tan importante es saber dónde esta su pareja?\n\n - 1. No me importa para nada \n - 2. No me importa \n - 3. Me da igual \n - 4. Me importa \n - 5. Me importa mucho")
    num7 = int(input())
    print("   \n---> ¿Qué tan importante debería ser para su pareja?\n\n - 1. No le importa para nada \n - 2. No le importa \n - 3. Le da igual \n - 4. Le importa \n - 5. Le importa mucho")
    num8 = int(input())
    
    print("\n5. ¿Qué tan importante es sentirse físicamente atraído a su pareja?\n\n - 1. No me importa para nada \n - 2. No me importa \n - 3. Me da igual \n - 4. Me importa \n - 5. Me importa mucho")
    num9 = int(input())
    print("   \n---> ¿Qué tan importante debería ser para su pareja?\n\n - 1. No le importa para nada \n - 2. No le importa \n - 3. Le da igual \n - 4. Le importa \n - 5. Le importa mucho")
    num10 = int(input())
    
    #porcentaje de compatibilidad
    suma = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10
    porcentaje = (suma*100)/50

    #crear nodo con puntaje 
    puntaje = Node("Puntaje", score= porcentaje)
    tx = graph.begin()
    tx.create(puntaje)
    tx.commit()
    
    #se crea una relacion entre las personas y sus puntajes
    #user1 = graph.nodes.match(name=nombre).first()
    #puntaje = graph.match(nodes=[user1], r_type="OBTUVO_PUNTAJE")
    graph.create(Relationship(user, "OBTUVO_PUNTAJE", puntaje))
# Se muestra el banner y el titulo del app
print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
print("                         _____ \n                      ,888888b. \n                  .d888888888b \n             _..-'.`*'_,8888888888b \n                 ,'..-..`\"ad888888888b. \n                     ``-. `*Y888888b. \n                         \\   `Y888888b. \n                      :     Y8888888b. \n                         :      Y88888888b. \n                       |    _,8ad88888888. \n                      : .d88888888888888b. \n                         \\d888888888888888888 \n                        8888;'''`88888888888 \n                         888'     Y8888888888 \n                         `Y8      :8888888888 \n                          |`      '8888888888 \n                          |        8888888888 \n                          |        8888888888 \n                          |        8888888888 \n                          |       ,888888888P \n                          :       ;888888888' \n                           \\      d88888888' \n                          _.>,    888888P' \n                       <,--''`.._>8888( \n                      `>__...--' `''` SSt \n")
print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*Bienvenido a Meetguin*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")


# Se pregunta al usuario si ya ha iniciado sesión.
# En caso contrario se le incita a crear una cuenta.
#        |
#        V
# Ciclo del login
while loginIsActive:
    opcion = input("\nBienvenido. ¿Ya tienes cuenta? \n1. Sí, deseo iniciar sesión. \n2. No, me gustaría crear una cuenta. \n3. Salir. \n")
    if opcion == "1":
        #------------------------------------------------------------------
        # Aqui se verifica si ya tiene cuenta revisando en la base de datos
        #------------------------------------------------------------------
        loginIsActive = False
    elif opcion == "2":
        registro()
        
        #--------------------------------------------------------
        # Aqui se añaden los datos del usuario a la base de datos
        #--------------------------------------------------------
        loginIsActive = False
    elif opcion == "3":
        loginIsActive = False
        menuIsActive = False
    else:
        print("\nPorfavor, ingrese una opción valida \n")

# Ciclo del menu principal
while menuIsActive:
    print("\n \n(o_(o_(o_(o_ \n//\\//\\//\\//\\ \nU_/U_/U_/U_/_ \n")
    print(" __  __ \n|  \\/  | \n| \\  / | ___ _ __  _   _ \n| |\\/| |/ _ \\ '_ \\| | | | \n| |  | |  __/ | | | |_| | \n|_|  |_|\\___|_| |_|\\__,_|")
    print("\n(o_(o_(o_(o_ \n//\\//\\//\\//\\ \nU_/U_/U_/U_/_ \n")
     
    eleccion = input("1. Buscar nuevo MeetMate. \n2. Ver mis MeetMates \n3. Acerca de... \n4. Salir \n")
    
    if eleccion == "1":
        #----------------------------------------------------------------------------------------
        # Se procede a ejecutar el algoritmo de recomendación para ver la siguiente recomendación
        #----------------------------------------------------------------------------------------
        print("")
    elif eleccion == "2":
        #----------------------------------------------------------------------
        # Se carga de la base de datos la lista de matches que tenga el usuario 
        #----------------------------------------------------------------------
        print("")
    elif eleccion == "3":
        print("\n \n(o_(o_(o_(o_ \n//\\//\\//\\//\\ \nU_/U_/U_/U_/_ \n")
        print("MeetGuin es una aplicación destinada a la interacción entre personas. Si tienes ")
        print("\n(o_(o_(o_(o_ \n//\\//\\//\\//\\ \nU_/U_/U_/U_/_ \n")
        
    elif eleccion == "4":
        #graph.delete(registro(user))
        #graph.delete(registro(puntaje))

        menuIsActive = False
    else:
        print("\nPorfavor, ingrese una opcion válida... \n")
    
 
     
    
    
    
    
    
    
    
    
    
    
    