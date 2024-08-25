cadena=input("Introduce una cadena de texto. Puede incluir letras mayúsculas y minúsculas, números y espacios")
print("",cadena)
#2
if any(char.isalpha() for char in cadena) and any(char.isdigit() for char in cadena):
    print("La cadena contiene al menos una letra y un número.")
elif any(char.isalpha() for char in cadena):
 print("La cadena solo contiene una letra")
elif any(char.isdigit() for char in cadena):
 print("La cadena solo contiene un número")
else:
    print("La cadena no contiene al menos una letra y un número.")
num_letras = sum(c.isalpha() for c in cadena)
print(f"Número de letras: {num_letras}")
num_numeros = sum(c.isdigit() for c in cadena)
print(f"Número de números: {num_numeros}")
num_espacios = sum(c.isspace() for c in cadena)
print(f"Número de espacios: {num_espacios}")
#3
if num_letras>num_numeros:
    print("Predominan letras.")
elif num_numeros>num_letras:
    print("Predominan números")
elif num_numeros==num_letras:
    print("Equilibrada")
elif num_espacios==0:
    print("Incompleta")
#4
longitud=len(cadena)
if longitud >= 10:
    print("Cadena Larga")
elif longitud <= 5:
    print("Cadena Corta")