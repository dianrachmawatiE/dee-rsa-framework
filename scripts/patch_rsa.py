import sys
import random

# Define replacement for RebalancedRSA
rebalanced_rsa = '''class RebalancedRSA:
    """Rebalanced RSA (Boneh & Shacham 2002).
    Shifts workload to the encrypter by using a very large public exponent 'e',
    while keeping the private key components (r1, r2) small (e.g. 160 bits).
    """

    def __init__(self, bits=2048, k=160):
        self.bits = bits
        self.k = k

    def keygen(self):
        # Step 1: Generate primes p, q such that gcd(p-1, q-1) = 2
        while True:
            p = generate_prime(self.bits // 2)
            q = generate_prime(self.bits // 2)
            if p != q and gcd(p - 1, q - 1) == 2:
                break
        
        self.n = p * q
        phi = (p - 1) * (q - 1)
        
        # Step 2: Choose random k-bit r1, r2
        while True:
            r1 = random.getrandbits(self.k) | (1 << (self.k - 1)) | 1
            r2 = random.getrandbits(self.k) | (1 << (self.k - 1)) | 1
            if gcd(r1, p - 1) == 1 and gcd(r2, q - 1) == 1 and (r1 % 2) == (r2 % 2):
                break
                
        # Step 3: Find d using modified CRT
        a = r1 % 2
        m1 = (p - 1) // 2
        m2 = (q - 1) // 2
        a1 = (r1 - a) // 2
        a2 = (r2 - a) // 2
        
        inv_m1_m2 = mod_inverse(m1, m2)
        d_prime = (a1 + m1 * ((a2 - a1) * inv_m1_m2 % m2)) % (m1 * m2)
        self.d = 2 * d_prime + a
        
        # Step 4: Calculate e
        self.e = mod_inverse(self.d, phi)
        
        self.dp = self.d % (p - 1)
        self.dq = self.d % (q - 1)
        self._p, self._q = p, q
        
        return self.n, self.e, self.d

    def encrypt(self, m):
        return pow(m, self.e, self.n)

    def decrypt(self, c):
        # Extremely fast decryption due to small dp and dq
        mp = pow(c % self._p, self.dp, self._p)
        mq = pow(c % self._q, self.dq, self._q)
        q_inv_p = mod_inverse(self._q, self._p)
        m = mp - mq
        if m < 0:
            m += self._p
        h = (m * q_inv_p) % self._p
        return mq + h * self._q
'''

# Define TakagiRSA
takagi_rsa = '''
class TakagiRSA:
    """Takagi 1998: Fast RSA-Type Cryptosystem Modulo p^k q.
    Focuses on k=2 (modulus n = p^2 * q) for optimal speed.
    """

    def __init__(self, bits=2048):
        self.bits = bits
        self.k = 2

    def keygen(self):
        p_bits = self.bits // 3
        q_bits = self.bits - 2 * p_bits
        
        while True:
            p = generate_prime(p_bits)
            q = generate_prime(q_bits)
            if p != q:
                break
                
        self.n = (p ** 2) * q
        
        # e: public key, GCD(e, p) = GCD(e, p-1) = GCD(e, q-1) = 1
        self.e = 65537
        while gcd(self.e, p) != 1 or gcd(self.e, p - 1) != 1 or gcd(self.e, q - 1) != 1:
            self.e += 2
            
        # d: private key, ed = 1 mod LCM(p-1, q-1)
        L = lcm(p - 1, q - 1)
        self.d = mod_inverse(self.e, L)
        
        self._p, self._q = p, q
        return self.n, self.e, self.d

    def encrypt(self, m):
        return pow(m, self.e, self.n)

    def decrypt(self, c):
        p, q = self._p, self._q
        e = self.e
        
        # LANGKAH 1 — Reduksi Eksponen
        dp = self.d % (p - 1)
        dq = self.d % (q - 1)
        
        # LANGKAH 2 — Hitung Nilai Dasar Modular
        K0 = pow(c % p, dp, p)
        Mq = pow(c % q, dq, q)
        
        # LANGKAH 3 — Iterasi Ekspansi p-Adic (k=2, loop i=1)
        A0 = K0
        
        F1 = pow(A0, e, p ** 2)
        E1 = (c - F1) % (p ** 2)
        
        # Integer division
        B1 = E1 // p
        
        inv_eF1 = mod_inverse((e * F1) % p, p)
        K1 = (inv_eF1 * A0 * B1) % p
        
        # Calculate A1 in Z (full integer, no modulo)
        A1 = A0 + p * K1
        
        # LANGKAH 4 — Rekonstruksi M mod p^k
        Mp = A1
        
        # LANGKAH 5 — Siapkan Koefisien CRT
        p1 = mod_inverse(p ** 2, q)
        q1 = mod_inverse(q, p ** 2)
        
        # LANGKAH 6 — CRT: Gabungkan untuk Dapatkan M
        M = (q1 * q * Mp + p1 * (p ** 2) * Mq) % (p ** 2 * q)
        
        return M
'''

with open(r"D:\TUGAS BU DIAN\JURNAL CHAOTIC\PAPER METHODX\dee_rsa_repo\src\rsa_variants.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace RebalancedRSA
start_idx = content.find("class RebalancedRSA:")
end_idx = content.find("class XRSA:")
if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + rebalanced_rsa + "\n\n" + content[end_idx:]
else:
    print("Could not find RebalancedRSA or XRSA boundaries.")
    sys.exit(1)

# Append TakagiRSA
content += takagi_rsa

with open(r"D:\TUGAS BU DIAN\JURNAL CHAOTIC\PAPER METHODX\dee_rsa_repo\src\rsa_variants.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Patch successful!")
