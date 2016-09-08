import Funciones as fun

lista = list(range(1, 1000, 1))


def filtering(number, numbers):
    for i in numbers:
        if fun.is_div(number, i):
            return True
    return False

multiples = [l for l in lista if filtering(l, [3, 5])]

print(sum(multiples))
