from math import pi, sqrt
from lib.rectangle import Rectangle
from lib.circle import Circle
from lib.square import Square


def main():
    r = Rectangle("синий", 17, 2)
    c = Circle("зеленый", sqrt(80/pi))
    s = Square("красный", 5)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()

a = input('Нажмите ENTER для завершения')
