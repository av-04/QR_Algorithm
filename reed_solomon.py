import gf256


def polymul(a, b, log, exp):
    result = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            result[i + j] ^= gf256.mul(a[i], b[j], log, exp)
    return result


def gen_poly(nsym, log, exp):
    g = [1]

    for i in range(nsym):
        g = polymul(g, [1, exp[i]], log, exp)

    return g


def reedencode(data, nsym, log, exp):
    gen = gen_poly(nsym, log, exp)
    msg = data + [0] * nsym
    for i in range(len(data)):
        coef = msg[i]
        if coef != 0:
            for j in range(len(gen)):
                msg[i + j] ^= gf256.mul(coef, gen[j], log, exp)
    return msg[-nsym:]
