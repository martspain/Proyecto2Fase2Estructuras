# Autores:
#     Sofía Rueda     Carné: 
#     Hansel López    Carné:
#     Martín España   Carné: 19258

# Bandera del menu principal
loginIsActive = True
menuIsActive = True

# Se muestra el banner y el titulo del app
print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
print("				            _____ \n					  ,888888b. \n					.d888888888b \n				_..-'.`*'_,8888888888b \n				  ,'..-..`\"ad888888888b. \n					 ``-. `*Y888888b. \n						 \\   `Y888888b. \n						 :     Y8888888b. \n						 :      Y88888888b. \n						 |    _,8ad88888888. \n						 : .d88888888888888b. \n						 \\d888888888888888888 \n						 8888;'''`88888888888 \n						 888'     Y8888888888 \n 						 `Y8      :8888888888 \n						  |`      '8888888888 \n						  |        8888888888 \n 						  |        8888888888 \n						  |        8888888888 \n						  |       ,888888888P \n						  :       ;888888888' \n						   \\      d88888888' \n						  _.>,    888888P' \n						<,--''`.._>8888( \n						 `>__...--' `''` SSt \n")
print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*Bienvenido a Meetguin*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")

# Se pregunta al usuario si ya ha iniciado sesión.
# En caso contrario se le incita a crear una cuenta.

# Ciclo del login
while loginIsActive:
    opcion = input("\nBienvenido. ¿Ya tienes cuenta? \n1. Sí, deseo iniciar sesión. \n2. No, me gustaría crear una cuenta. \n3. Salir. \n")
    if opcion == "1":
        #------------------------------------------------------------------
        # Aqui se verifica si ya tiene cuenta revisando en la base de datos
        #------------------------------------------------------------------
        loginIsActive = False
    elif opcion == "2":
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
    print("\n(o_(o_(o_(o_ \n//\\//\\//\\//\\ \nU_/U_/U_/U_/_ \n")
    print("Menu Principal")
    menuIsActive = False
    
    
    
    
     
    
    
    
    
    
    
    
    
    
    
    