import Usuario
import Password

correcto=False
while correcto==False:
        nombre=input("Ingrese nombre de usuario: ")
        if Usuario.nickname(nombre) == True:
            print("Usuario creado exitosamente")
            correcto=True

while correcto==True:
    contrasena=input("Ingrese su Password: ")
    if Password.clave(contrasena)==True:
        print("Contraseña creada exitosamente")
        correcto=False