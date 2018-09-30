# coding=utf-8

from gcd import xgcd

# primes
p = 187963
q = 163841
m = p * q

# Euler φ function
phi = m - p - q + 1

k = 48611  # must gcd(phi(primeProduct), exp) = 1

# k * u - φ(m) * = 1
u = xgcd(k, phi)


# encode
def encode(integers):
    result = list(map(lambda x: pow(x, k, m), integers))
    return result


# find x where x^k = b mod(m)
def congruence(b):
    return pow(b, u, m)


def decode(integers):
    result = list(map(lambda x: congruence(x), integers))
    return result


if __name__ == '__main__':
    words = [30251215, 25282425, 30302512, 15]
    print(words)

    secrets = encode(words)
    print(secrets)

    decodes = decode(secrets)
    print(decodes)
