import sys
import math

def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        coef_str = input(prompt)
    coef = float(coef_str)
    return coef

def get_sign(number):
    if number >= 0:
        return '+'
    return '-'    


def get_roots(a, b, c):
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        result.append(root1)
        result.append(root2)
    return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    roots = get_roots(a,b,c)
    len_roots = len(roots)
    if len_roots == 0:
        print('У уравнения {}x^2 {} {}x {} {} нет корней'.format(a, get_sign(b), abs(b), get_sign(c), abs(c)))
    elif len_roots == 1:
        print('У уравнения {}x^2 {} {}x {} {} один корень: {}'.format(a, get_sign(b), abs(b), get_sign(c), abs(c), roots[0]))
    elif len_roots == 2:
        print('У уравнения {}x^2 {} {}x {} {} два корня: {}, {}'.format(a, get_sign(b), abs(b), get_sign(c), abs(c), roots[0], roots[1]))
    a = input('Нажмите ENTER для завершения')
    
if __name__ == "__main__":
    main()