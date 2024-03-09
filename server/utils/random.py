import random
from string import ascii_letters, digits

def random_id(length: int = 64):
    return ''.join(random.choice(ascii_letters+digits) for _ in range(length))