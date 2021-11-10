# ----------------------------------------
# Muestra la tabla de multiplicar de un numero
# ----------------------------------------

def tabla_multiplicar(num):
    t = []                  # lista vacia

    for i in range(10):    # la tabla de multiplicar va de 1*num, a 10*num
        n = int(num)*i+1
        t.append(n)        # inserta n al final de la lista

    return t


def mostrar_tabla(num, t):
    for i in range(len(t)):                                  # Para elemento en la lista t
        print(num + " por " + str(i) + " es " + str(t[i]))


# ----------------------------------------
# MAIN
# ----------------------------------------
# Si numero es 6, la salida deber ser:
# 6 por 1 es 6
# 6 por 2 es 12
# 6 por 3 es 18
# 6 por 4 es 24
# 6 por 5 es 30
# 6 por 6 es 36
# 6 por 7 es 42
# 6 por 8 es 48
# 6 por 9 es 54
# 6 por 10 es 60
if __name__ == "__main__":
    numero = input("Dime un número: ")

    tabla = tabla_multiplicar(numero)

    mostrar_tabla(numero, tabla)