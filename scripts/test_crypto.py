import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from rsa_variants import TakagiRSA, RebalancedRSA
import random

print('Testing RebalancedRSA...')
rsa = RebalancedRSA(bits=1024, k=160)
rsa.keygen()
m = 123456789
c = rsa.encrypt(m)
m_dec = rsa.decrypt(c)
print(f'Original: {m}, Decrypted: {m_dec}')
assert m == m_dec, 'RebalancedRSA failed'
print('RebalancedRSA OK')

print('\nTesting TakagiRSA...')
t_rsa = TakagiRSA(bits=1024)
t_rsa.keygen()
m = 987654321
c = t_rsa.encrypt(m)
m_dec = t_rsa.decrypt(c)
print(f'Original: {m}, Decrypted: {m_dec}')
assert m == m_dec, 'TakagiRSA failed'
print('TakagiRSA OK')
