limite = 44;
resultado = 0;
valor = 1;
valor_anterior = 0;

aux = valor
valor = valor + valor_anterior;
valor_anterior = aux;

while (valor < limite):

    if ((valor % 2) == 0):
        #print(valor)
        resultado += valor;

    aux = valor
    valor = valor + valor_anterior;
    valor_anterior = aux;

print(resultado)


def fib(fib1, fib2, acc, limit):
    next_fib = fib1 + fib2
    if next_fib >= limit:
        return acc
    else:
        new_acc = acc + next_fib if is_even(next_fib) else acc
        return fib(fib2, next_fib, new_acc, limit)


def is_even(num):
    return num % 2 == 0


print(fib(1,2,2,40))