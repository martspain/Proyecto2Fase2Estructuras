
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
# Nodo puntaje
Puntaje_juan = Node("Puntaje", score= 84)
# Relationships
graph.create(Relationship(Juan, "OBTUVO_PUNTAJE", Puntaje_juan))
# Inicializar base de datos
tx = graph.begin()
tx.create(Juan)
tx.create(Puntaje_juan)
tx.commit()




        

    