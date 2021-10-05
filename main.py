def is_palindrome(n):
    """
    :param copie: retinem nr n
    :param invers: formam inversul numarului n
    :param n: numarul pe care il verificam daca este palindrom
    :return: true daca nr este palindrom sau false in caz contrar
    """
    copie = n
    invers = 0
    while copie > 0:
        invers = invers * 10 + copie % 10
        copie = copie // 10
    if n == invers:
        return True
    else:
        return False


def is_prime(nr):
    """
    :param nr: numarul pe care il verificam daca este prim
    :return: true daca nr este prim si false in caz contrar
    """
    if nr < 2:
        return False
    for i in range(2,nr):
        if nr % i == 0:
            return False
    return True


def is_superprime(x):
    """
    :param copie: inversul numarului x
    :param nr_cifre: retinem numarul de cifre ale lui x
    :param var: varaibila var creste cand cifrele lui x nu sunt prime
    :param x: retine numarul pe care vrem sa il verimicam daca este super prim
    :return: returneaza daca nr x este super prim sau nu
    """
    copie = x
    nr_cifre = 0
    var=0
    while copie > 9:
        nr_cifre += 1
        copie //= 10
    # acum in nr_cifre stim cate cifre are numarul x
    copie = x
    while nr_cifre >= 0:
        cifra=copie // 10 ** nr_cifre
        # in cifra avem prima cifra a numarului x
        if is_prime(cifra):
            print(f"{cifra} este pirm")
        else:
            print(f"{cifra} nu este prim")
            var += 1
        nr_cifre -= 1
        # nr_cifra scade pentru a putea lua primele 2 cifre ale numarului x
    if var >= 1:
        print(f"Numarul  nu este super prim")
    else:
        print(f"Numarul  este super prim")


def main():
    f = False
    while f != True:
        print("  ")
        print("1 Palindrom")
        print("2 Super prim")
        print("x Iesire")
        print()
        optiune = input("Alege optiunea  ")
        print()
        if optiune == "1":
            n = int(input("Dati un nr :"))
            if is_palindrome(n):
                print("Nr este palindrom")
            else:
                print("Nr nu este palindrom")

        if optiune == "2":
            x = int(input("Dati un nr :"))
            is_superprime(x)

        if optiune == "x":
            print("Programul se inchide")
            f = True

main()