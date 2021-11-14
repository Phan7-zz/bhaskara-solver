# This code only works with complete second degree equation
import math

def calc(a, b, c):
    bhaskara_1 = None
    bhaskara_2 = None

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print(f'This equation returns a negative delta: {delta}\nThen, it cannot be solved in the real numbers group')
        return

    delta_root = math.sqrt(delta)

    if int(math.sqrt(delta) + 0.5) ** 2 == delta: #Checking if delta has an exact square root
        bhaskara_1 = (- b + delta_root) / (a * 2)
        bhaskara_2 = (- b - delta_root) / (a * 2)
    else:
        bhaskara_1 = f'({-b} + √{delta}) / {2 * a}'
        bhaskara_2 = f'({-b} - √{delta}) / {2 * a}'

    print(f'X₁: {bhaskara_1}\nX₂: {bhaskara_2}')

def get_value(which, warn=False):
    try:
        if warn is True:
            value = float(input(f'Type a valid number for {letter}! '))
        else:
            value = float(input(f'What is the value of {which}? '))
    except ValueError:
        get_value(which, True)
    
    return value

values = []

for letter in ('A', 'B', 'C'):
    values.append(get_value(letter))

calc(values[0], values[1], values[2])
