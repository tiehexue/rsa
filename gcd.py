# k * u - φ(m) * v = 1
def xgcd(k, phi):
    old_a = k
    old_b = phi

    v, x1, u, y1 = 1, 0, 0, 1
    while k != 0:
        q, phi, k = phi // k, k, phi % k
        v, x1 = x1, v - q * x1
        u, y1 = y1, u - q * y1

    # ensure u > 0
    n = 1
    while u < 0:
        u += n * old_b
        v -= n * old_a

    return u
