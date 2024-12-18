import string
import random

def generate_slug() -> str:
    a = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    return a

if __name__ == '__main__':
    generate_slug()