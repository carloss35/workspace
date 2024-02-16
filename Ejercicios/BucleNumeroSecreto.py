import random
valor_minimo = int(input("Introduce el valor mínimo: "))
valor_maximo = int(input("Introduce el valor máximo: "))
secreto = random.randint(valor_minimo,valor_maximo)
print(f'A ver si adivinas un número entero entre {valor_minimo} y {valor_maximo}')
valor = int(input("Dime un numero: "))
intentos = 0

while valor != secreto:
    if valor < secreto:
        valor=int(input("¡Demasiado pequeño! Inténtalo de nuevo:"))
        intentos += 1
    if valor > secreto:
        valor=int(input("¡Demasiado grande! Inténtalo de nuevo:"))
        intentos += 1
  
print(f"¡Acertaste! Te ha costado {intentos} intentos.")

