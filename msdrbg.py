import os, json, hashlib, hmac, time
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from sympy import isprime




# Crandall primes
_C_P: int = 297
_C_Q: int = 301

P: int = (1 << 256) + _C_P
Q: int = (1 << 256) + _C_Q
N: int = P * Q
E: int = 65537
N_BITS: int = N.bit_length()
OUTPUT_BITS: int = 128
STATE_BITS:  int = N_BITS - OUTPUT_BITS
OUTPUT_MASK: int = (1 << OUTPUT_BITS) - 1
CHALLENGE_BITS: int = 24



class MSDRBG:
    def __init__(self, seed: int) -> None:
        self._state: int = seed
        self._step_count: int = 0

    def _step(self) -> int:
        padded = self._state << OUTPUT_BITS
        y = pow(padded, E, N)
        output = y & OUTPUT_MASK
        _state = y >> OUTPUT_BITS
        self._step_count += 1
        return output
        
    def generate(self, n_blocks: int) -> list[int]:
        blocks = [self._step() for _ in range(n_blocks)]
        return blocks


# ..... To be continued
        
