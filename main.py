from cipherRSA import *
if __name__ == "__main__":
    p = 278298860639
    q = 638226577273
    c = 92354190008012240514467

    m = "желтыйоттенок"

    n = p * q
    phi = (p - 1) * (q - 1)

    d = inversion(c, phi)

    print(f"p = {p}\n"
          f"q = {q}\n"
          f"N = {n}\n"
          f"φ = {phi}\n"
          f"\n"
          f"c = {c}\n"
          f"d = {d}\n")

    e = encode(m, d, n)
    msh = decode(e, c, n)
    print(f"Исходное сообщение(m):"
          f"\n\t{m}\nЗакодированное сообщение(e):"
          f"\n\t{e}\nРаскодированное сообщение(m'):"
          f"\n\t{''.join(msh)}")
