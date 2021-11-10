import math


class Solver:
    def demo(self, na, nb, nc):
        d = nb ** 2 - 4 * na * nc
        disc = math.sqrt(d)
        if d > 0:
            root1 = (-nb + disc) / (2 * na)
            root2 = (-nb - disc) / (2 * na)
            return root1, root2
        elif d == 0:
            return (nb + disc) / (2 * na)
        else:
            return "This equation has no roots"


if __name__ == '__main__':
    slv = Solver()

    while True:
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        result = slv.demo(a, b, c)
        print(result)
