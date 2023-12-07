#        @@      @@        @@
#       @@      @@       @@
#       @@      @@      @@
# @@     @@@     @@     @@     @@@
#    @@@@@@@*        ,&@@@@@@@*
#   @                         @@     @@
#   @@                       ,@#    @@
#   @@@                     @@@  &@#
#     @@@&                @@@
#        @@@@@@@@@@@@@@@@@

from encod import Encod
from random import randint

enc = Encod()


def inversion(d, modulus):
    """
    Инверсия по модулю на основе расширенного алгоритма Евклида.
    (c*d) mod modulus
    :param d: Число, относительно которого нужно найти инверсию.
    :param modulus: Число, по которому нужно найти инверсию.
    :return: Инверсия числа d по модулю p.
    """
    u1 = modulus
    u2 = 0

    v1 = d
    v2 = 1

    while v1 != 1:
        q = u1 // v1
        t1 = u1 % v1
        t2 = u2 - (q * v2)

        u1 = v1
        u2 = v2

        v1 = t1
        v2 = t2

    if v2 < 0:
        v2 = v2 + modulus

    return v2


def __powerMod(base, exp, modulus):
    """
    Быстрое возведение в степень и деление по модулю:
            (base^exp) mod p
    :param base: Основание степени.
    :param exp: Степень.
    :param modulus: Делитель по модулю.
    :return: Деление по модулю p числа base в степени exp.
    """
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % modulus
        exp = exp // 2
        base = (base ** 2) % modulus

    return result


def encode(m, d, n):
    """
    Кодирование сообщения m шифром RSA
    :param m: Исходное сообщение.
    :param d: Открытый ключ d.
    :param n: Открытая часть n.
    :return: Закодированное сообщение.
    """
    # Преобразование из строки в цифры.
    # Функция enc.encoding приводится сначала к str, потом к int
    m = int("".join(enc.encoding(m, len(m), encod="32_lw")))

    e = __powerMod(m, d, n)  # Кодирование сообщения
    return e


def decode(e, c, n):
    """
    Декодирование сообщения e шифром RSA.
    :param e: Зашифрованное сообщение.
    :param c: Закрытый ключ c.
    :param n: Открытая часть n.
    :return: Раскодированное сообщение.
    """
    m_sh = __powerMod(e, c, n)
    m_sh = str(m_sh).split()  # Строка в массив.

    m_sh = enc.decoding(m_sh, encod="32_lw")  # Массив в буквы.
    return m_sh


def __isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def __generateRandomPrime(a, b):
    while True:
        n = randint(a, b)
        if __isPrime(n):
            return n


def __gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def __isCoprime(a, b):
    return __gcd(a, b) == 1


def __findCoprime(n):
    while True:
        i = randint(3, n-1)
        if __isCoprime(n, i):
            return i


def generateKey(a=1000, b=100000000000):
    p = __generateRandomPrime(a, b)
    q = __generateRandomPrime(a, b)
    N = p * q
    phi = (p - 1) * (q - 1)
    c = __findCoprime(phi)
    d = inversion(c, phi)

    return {
        "N": N,
        "c": c,  # Секретный ключ.
        "d": d   # Открытый ключ.
    }
