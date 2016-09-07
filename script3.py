inicio = 2;
siguiente = 600851475143
# Obtiene los factores primos de un número dado
fin = 0

resultado = []

while (fin == 0):

    valor_dividir = siguiente
    print("Valor: {}".format(valor_dividir))
    limite = int((siguiente / 2) + 1)

    for x in range(inicio, limite, 1):
        # print("Bucle principal: {}".format(x))

        if ((valor_dividir % x) == 0):
            print("Divisible por: {}".format(x))
            siguiente = int(valor_dividir / x)

            # print("Nuevo: {}".format(siguiente))
            resultado.append(x)

            break

    if x == limite - 1:
        fin = 1
        resultado.append(valor_dividir)

print(resultado)
