
import sys
from math import pi

def main():
    start = float(sys.argv[1])
    inc = float(sys.argv[2])
    end = float(sys.argv[3])

    h1 = 'Radius (m)'
    h4 = '-' * len(h1)
    h2 = 'Area (m^2)'
    h5 = '-' * len(h2)
    h3 = 'Volume (m^3)'
    h6 = '-' * len(h3)

    print('{:>s} {:>15s} {:>15s}'.format(h1, h2, h3))
    print('{:>s} {:>15s} {:>15s}'.format(h4, h5, h6))

    radius = start
    while radius <= end:
        area = 4 * pi * radius ** 2
        volume = (4 / 3) * pi * radius ** 3
        print("{:>10.1f} {:>15.2f} {:>15.2f}".format(radius, area, volume))
        radius = radius + inc

if __name__ == '__main__':
    main()
