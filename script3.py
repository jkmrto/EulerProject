import Funciones as fun

inicio = 2
div_value = 600851475143
fin = 0
resultado = []

print(resultado)

while (fin == 0):
    #print("Valor: {}".format(valor_dividir))
    limite = int((div_value / 2) + 1)

    for div in range(inicio, limite, 1):

        if fun.is_div(div_value, div):
            div_value = int(div_value / div)
            resultado.append(div)
            break

    if div == limite - 1:
        fin = 1
        resultado.append(div_value)

print(resultado)
