print ("[1] Registro de usuario")
Nombre = input("Ingresa tu primer nombre:").strip()
Apellido = input("Ingresa tu primer apellido:").strip()
Segundo_Apellido = input("Ingresa tu segundo apellido:").strip()

#Concatenación y métodos de texto 
Nombre_Completo = f"{Nombre} {Apellido} {Segundo_Apellido}"
Nombre_Mayusculas = Nombre_Completo.upper()
Nombre_Mayusculas = Nombre_Completo.upper()
Longitud_Nombre =len(Nombre_Completo.replace(" ", " ")) #Cuentas letras sin espacios

print (f" -> Usuario Registrado: {Nombre_Completo}")
print (f" -> Tu nombre tiene {Longitud_Nombre} letras. ")
print ("-" * 40)
