import math


class Complex(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, num):
        a = self.real
        b = self.imag
        c = num.real
        d = num.imag
        addition = Complex(a + c, b + d)
        return addition

    def __sub__(self, num):
        a = self.real
        b = self.imag
        c = num.real
        d = num.imag
        return Complex(a - c, b - d)

    def __mul__(self, num):
        a = self.real
        b = self.imag
        c = num.real
        d = num.imag
        real_mult = (a * c) - (b * d)
        imag_mult = (a * d) + (b * c)
        return Complex(real_mult, imag_mult)

    def __truediv__(self, num):
        a = self.real
        b = self.imag
        c = num.real
        d = num.imag
        real_numer = a * c + b * d
        imag_numer = b * c - a * d
        denom = c * c + d * d
        real_div = real_numer / denom
        imag_div = imag_numer / denom
        return Complex(real_div, imag_div)

    def mod(self):
        a = self.real
        b = self.imag
        return Complex(math.sqrt(a ** 2 + b ** 2), 0)

    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            result = "0.00+%.2fi" % (self.imag)
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real, self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())

    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')




