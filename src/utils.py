"""
Cryptographic utilities for DEE-RSA benchmarks.
"""

import os
import hashlib
import random


def generate_random_message(bits, modulus):
    """Generate a random message uniformly in [0, modulus-1]."""
    try:
        # Use OS entropy source where available
        rand_bytes = os.urandom((bits + 7) // 8)
        rand_int = int.from_bytes(rand_bytes, "big")
        return rand_int % modulus
    except Exception:
        return random.randrange(modulus)


def sha256_hash(data):
    """Compute SHA-256 hash (used for conditioning)."""
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def verify_wiener_bound(e_val, n_bits, d_val):
    """Check that private exponent d satisfies Wiener's bound."""
    N = 2 ** n_bits
    threshold = (1.0 / 3.0) * (N ** 0.25)
    return d_val > threshold
