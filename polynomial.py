import numpy as np
import math


class Polynomial:
    def __init__(self, p):
        self.__polynomial = []
        self.polynomial = p

    def __call__(self, p):
        self.__polynomial.clear()
        self.polynomial = p

    @property
    def polynomial(self):
        return self.__polynomial

    @polynomial.setter
    def polynomial(self, p):
        try:
            self.__polynomial.clear()
            for ind, val in enumerate(p, 1):
                if not isinstance(val, int):
                    self.__polynomial = []
                    raise Exception(f"'{val}' is not int, type error")
                self.__polynomial.append(val)
        except Exception as e:
            print(e)

    def __len__(self):
        return len(self.polynomial)

    def __next__(self):
        return self.polynomial.next()

    def __iter__(self):
        return self.polynomial.__iter__()

    def __getitem__(self, key):
        if key in range(0, len(self)):
            return self.polynomial[key]

    def __setitem__(self, key, value):
        try:
            self.polynomial[key] = value
        except IndexError:
            print('index error')

    def __str__(self):
        return 'Polynomial({})'.format(self.polynomial)

    def format(self):
        print('Polynomial({})'.format(self.polynomial))

    def add(self, key, value):
        if (not isinstance(key, int)) | (not isinstance(value, int)):
            return
        p = self.polynomial.copy()
        if key in range(0, len(self)):
            p[key] += value
        else:
            for i in range(len(self), key):
                p.append(0)
            p.append(value)
        return Polynomial(p)

    def __add__(self, other):
        try:
            res = Polynomial(self.polynomial.copy())
            if isinstance(other, int):
                res = res.add(len(res) - 1, other)
                return res
            elif isinstance(other, Polynomial):
                for i in range(0, len(other)):
                    res = res.add(i, other[i])
                return res
            else:
                raise Exception(f"'{other}' is not Polynomial, type error")
        except Exception as e:
            return e

    def __radd__(self, other):
        try:
            res = Polynomial(self.polynomial.copy())
            if isinstance(other, int):
                res = res.add(len(res) - 1, other)
                return res
            elif isinstance(other, Polynomial):
                for i in range(0, len(other)):
                    res = res.add(i, other[i])
                return res
            else:
                raise Exception(f"'{other}' is not Polynomial, type error")
        except Exception as e:
            return e

    def __sub__(self, other):
        try:
            res = Polynomial(self.polynomial.copy())
            if isinstance(other, int):
                res = res.add(len(res) - 1, -other)
                return res
            elif isinstance(other, Polynomial):
                for i in range(0, len(other)):
                    res = res.add(i, -other[i])
                return res
            else:
                raise Exception(f"'{other}' is not Polynomial, type error")
        except Exception as e:
            return e

    def __rsub__(self, other):
        try:
            res = Polynomial(self.polynomial.copy())
            if isinstance(other, int):
                res = res.add(len(res) - 1, -other)
                return -res
            elif isinstance(other, Polynomial):
                for i in range(0, len(other)):
                    res = res.add(i, -other[i])
                return -res
            else:
                raise Exception(f"'{other}' is not Polynomial, type error")
        except Exception as e:
            return e

    def __mul__(self, other):
        try:
            if isinstance(other, int):
                res = Polynomial(self.polynomial.copy())
                for i in range(0, len(self)):
                    res[i] *= other
                return res
            elif isinstance(other, Polynomial):
                res = Polynomial([])
                for i in range(0, len(self)):
                    for j in range(0, len(other.polynomial)):
                        res = res.add(i + j, self[i] * other[j])
                return res
            else:
                raise Exception(f"'{other}' is not Polynomial, type error")
        except Exception as e:
            return e

    def __rmul__(self, other):
        try:
            if isinstance(other, int):
                res = Polynomial(self.polynomial.copy())
                for i in range(0, len(self)):
                    res[i] *= other
            elif isinstance(other, Polynomial):
                res = Polynomial([])
                for i in range(0, len(self)):
                    for j in range(0, len(other.polynomial)):
                        res = res.add(i + j, self[i] * other[j])
            else:
                raise Exception(f"'{other}' is not Polynomial, type error")
        except Exception as e:
            return e

    def __remove_nulls(self):
        p = Polynomial(self)
        for i in range(0, len(self)):
            if self[i] == 0:
                p.polynomial.pop(0)
            else:
                break
        return p

    def __eq__(self, other):
        try:
            if isinstance(other, int):
                return self.__remove_nulls().polynomial ==\
                       Polynomial([other]).__remove_nulls().polynomial
            elif isinstance(other, Polynomial):
                return self.__remove_nulls().polynomial ==\
                       other.__remove_nulls().polynomial
            else:
                raise Exception(f"'{other}' is not Polynomial, type error")
        except Exception as e:
            return e

    def __ne__(self, other):
        try:
            if isinstance(other, int):
                return self.__remove_nulls().polynomial !=\
                       Polynomial([other]).__remove_nulls().polynomial
            elif isinstance(other, Polynomial):
                return self.__remove_nulls().polynomial !=\
                       other.__remove_nulls().polynomial
            else:
                raise Exception(f"'{other}' is not Polynomial, type error")
        except Exception as e:
            return e

    def __neg__(self):
        p = []
        for i in self.polynomial:
            p.append(-1 * i)
        return Polynomial(p)

    def substitute_number(self, number):
        try:
            if not isinstance(number, int):
                raise Exception(f"'{number}' is not int")
            else:
                a = 0
                for i in range(0, len(self)):
                    a += self[i] * pow(number, len(self) - i - 1)
                return a
        except Exception as e:
            return e

    def __solve_the_linear_equation(self):
        return -self[1]

    def __solve_the_quadratic_equation(self):
        a, b, c = self[0], self[1], self[2]
        d = b ** 2 - 4 * a * c
        if d == 0:
            return -b / 2 * a
        elif d > 0:
            return (-b - d ** 0.5) / 2 * a, (-b + d ** 0.5) / 2 * a
        else:
            return complex(-b / (2 * a), -math.fabs(d) ** 0.5 / (2 * a)), \
                   complex(-b / (2 * a), math.fabs(d) ** 0.5 / (2 * a))

    def __solve_the_bi_quadratic_equation(self):
        a, b, c = self[0], self[2], self[4]
        t = Polynomial([a, b, c]).__solve_the_quadratic_equation()
        if isinstance(t, float) | isinstance(t, int):
            return -t ** 0.5, -t ** 0.5
        else:
            return -t[0] ** 0.5, t[0] ** 0.5, -t[1] ** 0.5, t[1] ** 0.5

    def __solve_the_cubic_equation(self):
        pass
        # a, b, c, d = self[0], self[1], self[2], self[3]
        # p = (3 * a * c - b ** 2) / (3 * a ** 2)
        # q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
        # Q = (p / 3) ** 3 + (q / 2) ** 2
        # alpha = (-q/2 + Q ** 2) ** (1 / 3)
        # beta = (-q/2 - Q ** 2) ** (1 / 3)
        # x1 = alpha + beta
        # x2 = complex(-alpha / 2 - beta / 2, (alpha - beta) / 2 * 3 ** 0.5)
        # x3 = complex(-alpha / 2 - beta / 2, -(alpha - beta) / 2 * 3 ** 0.5)
        # if Q != 0:
        #     return x1, x2, x3
        # else:
        #     return x1 if p == q == 0 else x1, x2.real

    def solve(self):
        try:
            if len(self) == 1:
                raise Exception("It's constant")
            elif len(self) == 2:
                return self.__solve_the_linear_equation()
            elif len(self) == 3:
                return self.__solve_the_quadratic_equation()
            elif len(self) == 4:
                return self.__solve_the_cubic_equation()
            elif len(self) == 5:
                if (self[1] == 0) & (self[3] == 0):
                    return self.__solve_the_bi_quadratic_equation()
                else:
                    raise Exception("Solve of this equations yet not supported")
            else:
                raise Exception("Solve equations of degree > 4 is impossible")
        except Exception as e:
            return e

    def __to_s(self):
        output = []
        for i in range(0, len(self)):
            if i == len(self) - 1:
                s = ""
            elif i == len(self) - 2:
                s = "x"
            else:
                s = "x^"
            if self[i] == 1:
                if output:
                    if i != 0:
                        output.append(" + ")
                if i == len(self) - 1:
                    output.append("1")
                output.append(s)
            elif self[i] == -1:
                output.append(" - ")
                if i == len(self) - 1:
                    output.append("1")
                output.append(s)
            elif self[i] > 0:
                if i != 0:
                    if output:
                        output.append(" + ")
                output.append(self[i])
                output.append(s)
            elif self[i] < 0:
                output.append(" - ")
                output.append(self[i] * (-1))
                output.append(s)
            if self[i] != 0:
                if i < len(self) - 2:
                    output.append(len(self) - i - 1)
        return output

    def print(self):
        output = self.__to_s()
        print(*output, sep='')

