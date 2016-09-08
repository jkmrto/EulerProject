#palindromic number of three digits

#Los numeros de partida seran el 999
#Supongo que el resultado sera de 6 cifras

#Se podria hacer de otra manera mas algoritmica


maximo = 0
resultado = []

for i  in range(800,1000,1):
    for j in range(800,1000,1):
        producto = i * j;
        if (int(producto / 100000) > 0):
            print("{0}*{1}={2}".format(i,j,producto))
            parte_1 = int(producto/1000)

            parte_2_1 = producto % 10
            parte_2_2 = int(producto/10) % 10
            parte_2_3 = int(producto/100) % 10 #- parte_2_2 * 10 - parte_2_1
            parte_2 = parte_2_1*100 + parte_2_2*10 + parte_2_3

            print("Descomposicion parte 2:{0}".format(parte_2))
            print("Descomposicion parte 1:{0} \n".format(parte_1))

            if(parte_2 == parte_1):
                resultado.append(producto)

                if(producto > maximo):
                    maximo = producto


print(resultado)
print("Maximo: {}".format(maximo))