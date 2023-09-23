# solo se una un igual
mail = input("Ingrese un correo electrónico: ")

# falta definir la cantidad
cantidad = 0
# Solo se una un igual
x = 0
#la función es len(), no leng())
while x < len(mail):
    # Corregir el uso de paréntesis para acceder a un carácter específico
    if mail[x] == "@":
        cantidad = cantidad + 1
    
    # Corregir la sintaxis para incrementar el contador x en 1, tambien eliminar un igual
    x = x + 1
if cantidad == 1:
    print("El correo electronico dado solo contiene un caracter @.")
else:
    print("Incorrecto.")
