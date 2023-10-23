# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# Función de orden superior que toma una función como argumento
def aplicar_funcion(func, x):
    return func(x)

# Definir una función simple
def cuadrado(x):
    return x * x

def cubo(x):
    return x * x * x

# Aplicar la función cuadrado a un valor
resultado = aplicar_funcion(cuadrado, 5)
print("Cuadrado de 5:", resultado)

# Aplicar la función cubo a un valor
resultado = aplicar_funcion(cubo, 3)
print("Cubo de 3:", resultado)

# Función que devuelve una función
def seleccionar_funcion(potencia):
    if potencia == 2:
        return cuadrado
    elif potencia == 3:
        return cubo

# Obtener una función en función de un valor
func = seleccionar_funcion(2)
resultado = aplicar_funcion(func, 4)
print("Cuadrado de 4:", resultado)

func = seleccionar_funcion(3)
resultado = aplicar_funcion(func, 2)
print("Cubo de 2:", resultado)
