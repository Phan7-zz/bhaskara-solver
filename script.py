# This code only works with second degree equation

import math

def calc(a, b, c):
    bhaskara_1 = None
    bhaskara_2 = None

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print(f'Esta equação retorna um delta negativo: {delta}\nPortanto, não pode ser resolvida no conjunto dos números reais')
        return

    delta_root = math.sqrt(delta)

    if int(math.sqrt(delta) + 0.5) ** 2 == delta: #Checking if delta has an exact square root
        bhaskara_1 = (- b + delta_root) / (a * 2)
        bhaskara_2 = (- b - delta_root) / (a * 2)
    else:
        bhaskara_1 = f'({-b} + √{delta}) / {2 * a}'
        bhaskara_2 = f'({-b} - √{delta}) / {2 * a}'

    print(f'O valor de X₁ é: {bhaskara_1}\nO valor de X₂ é: {bhaskara_2}')

def get_value(which, warn=False):
    try:
        if warn is True:
            value = float(input(f'Digite um valor válido para {letter}! '))
        else:
            value = float(input(f'Qual o valor de {which}? '))
    except ValueError:
        get_value(which, True)
    
    return value

values = []

for letter in ('A', 'B', 'C'):
    values.append(get_value(letter))

calc(values[0], values[1], values[2])
