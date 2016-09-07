import Funciones as fun

final = 10

factores = list(range(1, final+1))
estado = [1] * final

#fun.imprime(factores)
fun.imprime(estado)

primos = fun.factores_primos(final)
print(primos)


cuenta_primos = fun.get_count(primos)

print(cuenta_primos)




