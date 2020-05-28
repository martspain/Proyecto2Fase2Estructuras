
# Base de datos
from py2neo import*
graph = Graph("bolt://localhost:7687", auth=("neo4j","1234"))

# Perfiles
Juan = Node("Hombre", name="Juan", sex="Masculino", age="24")
Arturo = Node("Hombre", name="Arturo", sex="Masculino", age="28")
Roberto = Node("Hombre", name="Roberto", sex="Masculino", age="30")
Andres = Node("Hombre", name="Andres", sex="Masculino", age="40")
Alejandro = Node("Hombre", name="Alejandro", sex="Masculino", age="31")
Miguel = Node("Hombre", name="Miguel", sex="Masculino", age="27")
Ricardo = Node("Hombre", name="Ricardo", sex="Masculino", age="20")
Juan_Pablo = Node("Hombre", name="Juan Pablo", sex="Masculino", age="21")
Luis_Pedro = Node("Hombre", name="Luis Pedro", sex="Masculino", age="22")
Pedro = Node("Hombre", name="Pedro", sex="Masculino", age="23")
Luis = Node("Hombre", name="Luis", sex="Masculino", age="25")
Angel = Node("Hombre", name="Angel", sex="Masculino", age="23")
Rogelio = Node("Hombre", name="Rogelio", sex="Masculino", age="19")
Miguel_Angel = Node("Hombre", name="Miguel Angel", sex="Masculino", age="19")
Santiago = Node("Hombre", name="Santiago", sex="Masculino", age="18") 
Sebastian = Node("Hombre", name="Sebastian", sex="Masculino", age="26")
Emilio = Node("Hombre", name="Emilio", sex="Masculino", age="26")
Bryan = Node("Hombre", name="Bryan", sex="Masculino", age="21")
Boris = Node("Hombre", name="Boris", sex="Masculino", age="23")
Javier = Node("Hombre", name="Javier", sex="Masculino", age="23")
Diego = Node("Hombre", name="Diego", sex="Masculino", age="18")
Marcelo = Node("Hombre", name="Marcelo", sex="Masculino", age="18")
Juan_Diego = Node("Hombre", name="Juan Diego", sex="Masculino", age="23")
Nicolas = Node("Hombre", name="Nicolas", sex="Masculino", age="18")
Joaquin = Node("Hombre", name="Joaquin", sex="Masculino", age="19")

Fernanda = Node("Mujer", name="Fernanda", sex="Femenino", age="21")
Maria_Eugenia = Node("Mujer", name="Maria Eugenia", sex="Femenino", age="32")
Kathy = Node("Mujer", name="Kathy", sex="Femenino", age="20")
Ruth = Node("Mujer", name="Ruth", sex="Femenino", age="24")
Sarah = Node("Mujer", name="Sarah", sex="Femenino", age="22")
Sussy = Node("Mujer", name="Sussy", sex="Femenino", age="19")
Jimena = Node("Mujer", name="Jimena", sex="Femenino", age="19")
Ana_Elisa = Node("Mujer", name="Ana Elisa", sex="Femenino", age="20")
Ana_Sofia = Node("Mujer", name="Ana Sofia", sex="Femenino", age="21")
Ana_Graciela = Node("Mujer", name="Ana Graciela", sex="Femenino", age="19")
Michelle = Node("Mujer", name="Michelle", sex="Femenino", age="23")
Giselle = Node("Mujer", name="Giselle", sex="Femenino", age="25")
Rossy = Node("Mujer", name="Rossy", sex="Femenino", age="30")
Melanie = Node("Mujer", name="Melanie", sex="Femenino", age="29")
Mia = Node("Mujer", name="Mia", sex="Femenino", age="27")
Rachel = Node("Mujer", name="Rachel", sex="Femenino", age="31")
Carla = Node("Mujer", name="Carla", sex="Femenino", age="39")
Nicole = Node("Mujer", name="Nicole", sex="Femenino", age="24")
Ortencia = Node("Mujer", name="Ortencia", sex="Femenino", age="34")
Ana_Lucia = Node("Mujer", name="Ana Lucia", sex="Femenino", age="19")
Stephanie = Node("Mujer", name="Stephanie", sex="Femenino", age="28")
Summer = Node("Mujer", name="Summer", sex="Femenino", age="21")
Rocio = Node("Mujer", name="Rocio", sex="Femenino", age="37")
Esther = Node("Mujer", name="Esther", sex="Femenino", age="30")
Sally = Node("Mujer", name="Sally", sex="Femenino", age="25")
Pamela = Node("Mujer", name="Pamela", sex="Femenino", age="20")
Selena = Node("Mujer", name="Selena", sex="Femenino", age="18")
Linda = Node("Mujer", name="Linda", sex="Femenino", age="22")

# Nodo puntaje
Puntaje_juan = Node("Puntaje", score= 84)
# Relationships
graph.create(Relationship(Juan, "OBTUVO_PUNTAJE", Puntaje_juan))
# Inicializar base de datos
tx = graph.begin()
tx.create(Juan)
tx.create(Puntaje_juan)
tx.commit()




        

    