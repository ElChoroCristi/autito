#voy a intentar programar un auto, a ver si despues los uso para hacer carreras jajaja

#definire algunas funciones básicas
#creo que necesito primero generar algun tipo de "llave"
# def llave():
try:
    with open ("Weveo\key_pass.txt", "r") as s:
        if s == True:
            pass
except FileNotFoundError:
    with open ("Weveo\key_pass.txt", "w") as f:
        key_pass = str(input("Indique nueva Clave --> "))
        f.write(key_pass)
        
# def llave():
llave = bool
with open ("Weveo\key_pass.txt", "r") as s:
    your_password = str(s.read)
    x = 0
    while 3 > x > -1: 
        try_password = str(input('Ingrese su "llave" --> '))
        if try_password != your_password:
            print("There is no Key")
            llave = False
            x += 1
            pass
        elif try_password == your_password:
            x = x - (x + 1)
            print("Lucky you, there is a key")
    llave = True

# def turn_on():
# engine_on = False
# if saved_pass == "":
#     new_pass = str(input("Ingrese una nueva contrasena --> "))
#     pass

# print(saved_pass)
    # while engine_on = False:
    #     passtry = int(input)