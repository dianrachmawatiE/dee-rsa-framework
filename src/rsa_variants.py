"""
RSA Variant Implementations for DEE-RSA Benchmarks

Each implementation follows the DEE-RSA Phase I specification requirements:
complete key generation, encryption, and decryption with documented parameters.
"""

import random
from math import gcd


def is_prime(n, k=40):
    """Miller-Rabin primality test with k rounds."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_prime(bits):
    """Generate a random prime of specified bit length."""
    while True:
        p = random.getrandbits(bits)
        p |= (1 << (bits - 1)) | 1
        if is_prime(p):
            return p


def mod_inverse(a, m):
    """Extended Euclidean algorithm for modular inverse."""
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


def lcm(a, b):
    """Least common multiple."""
    return abs(a * b) // gcd(a, b)


class ClassicalRSA:
    """Textbook RSA with 2-prime modulus n = p*q."""

    def __init__(self, bits=2048, e=65537):
        self.bits = bits
        self.e = e

    def keygen(self):
        p = generate_prime(self.bits // 2)
        q = generate_prime(self.bits // 2)
        while abs(p - q) < 2 ** (self.bits // 4):
            q = generate_prime(self.bits // 2)
        self.n = p * q
        phi = (p - 1) * (q - 1)
        while gcd(self.e, phi) != 1:
            self.e += 2
        self.d = mod_inverse(self.e, phi)
        self._p, self._q = p, q
        return self.n, self.e, self.d

    def encrypt(self, m):
        return pow(m, self.e, self.n)

    def decrypt(self, c):
        return pow(c, self.d, self.n)


class MultiPrimeRSA:
    """Multi-Prime RSA with 3-prime modulus n = p*q*r (Collins et al., 1998)."""

    def __init__(self, bits=2048, e=65537, num_primes=3):
        self.bits = bits
        self.e = e
        self.num_primes = num_primes

    def keygen(self):
        self.primes = []
        for _ in range(self.num_primes):
            self.primes.append(generate_prime(self.bits // self.num_primes))
        self.n = 1
        phi = 1
        for p in self.primes:
            self.n *= p
            phi *= (p - 1)
        while gcd(self.e, phi) != 1:
            self.e += 2
        self.d = mod_inverse(self.e, phi)
        self.dp = [self.d % (p - 1) for p in self.primes]
        return self.n, self.e, self.d

    def encrypt(self, m):
        return pow(m, self.e, self.n)

    def decrypt(self, c):
        N = self.n
        m = 0
        for i, p in enumerate(self.primes):
            Ni = N // p
            Mi = mod_inverse(Ni, p)
            m += pow(c % p, self.dp[i], p) * Mi * Ni
        return m % N


class RebalancedRSA:
    """Rebalanced RSA with large public exponent and small CRT private exponents."""

    def __init__(self, bits=2048, w=160):
        self.bits = bits
        self.w = w

    def keygen(self):
        p = generate_prime(self.bits // 2)
        q = generate_prime(self.bits // 2)
        while abs(p - q) < 2 ** (self.bits // 4):
            q = generate_prime(self.bits // 2)
        self.n = p * q
        phi = (p - 1) * (q - 1)
        self.e = generate_prime(self.bits - 10)
        while gcd(self.e, phi) != 1:
            self.e += 2
        self.d = mod_inverse(self.e, phi)
        self.dp = self.d % (p - 1)
        self.dq = self.d % (q - 1)
        self._p, self._q = p, q
        return self.n, self.e, self.d

    def encrypt(self, m):
        return pow(m, self.e, self.n)

    def decrypt(self, c):
        mp = pow(c % self._p, self.dp, self._p)
        mq = pow(c % self._q, self.dq, self._q)
        q_inv_p = mod_inverse(self._q, self._p)
        m = mp - mq
        if m < 0:
            m += self._p
        h = (m * q_inv_p) % self._p
        return mq + h * self._q


class XRSA:
    """XRSA: 4-Prime RSA variant with XOR obfuscation (Imam et al., 2022).
    
    Key generation uses two intermediate exponents E1, E2, produces E',
    then applies XOR with modulus N to produce final public/private keys.
    Encryption/decryption recover E'/D' via XOR before modular exponentiation.
    No CRT acceleration is used in the original algorithm.
    """

    def __init__(self, bits=2048, e=65537):
        self.bits = bits
        self.e = e
        self.num_primes = 4

    def keygen(self):
        p1 = generate_prime(self.bits // 4)
        p2 = generate_prime(self.bits // 4)
        p3 = generate_prime(self.bits // 4)
        p4 = generate_prime(self.bits // 4)
        self.primes = [p1, p2, p3, p4]
        
        self.N = p1 * p2 * p3 * p4
        phi_N = (p1 - 1) * (p2 - 1) * (p3 - 1) * (p4 - 1)
        
        x = p1 * p2
        phi_x = (p1 - 1) * (p2 - 1)
        y = p3 * p4
        phi_y = (p3 - 1) * (p4 - 1)
        
        E1 = generate_prime(phi_x.bit_length() - 2)
        while gcd(E1, phi_x) != 1:
            E1 = generate_prime(phi_x.bit_length() - 2)
            
        E2 = generate_prime(phi_y.bit_length() - 2)
        while gcd(E2, phi_y) != 1:
            E2 = generate_prime(phi_y.bit_length() - 2)
            
        while gcd(E1 * E2, phi_N) != 1:
            E2 = generate_prime(phi_y.bit_length() - 2)
            while gcd(E2, phi_y) != 1:
                E2 = generate_prime(phi_y.bit_length() - 2)
        
        E_prime = (E1 * E2) % self.N
        D_prime = mod_inverse(E_prime, phi_N)
        
        self.E = E_prime ^ self.N
        self.D = D_prime ^ self.N
        self._n = self.N
        self._d = D_prime
        
        return self.N, self.E, self.D

    def encrypt(self, m):
        E_recovered = self.E ^ self.N
        return pow(m, E_recovered, self.N)

    def decrypt(self, c):
        D_recovered = self.D ^ self.N
        return pow(c, D_recovered, self.N)
