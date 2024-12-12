def q1():
    """
    Dado um número inteiro x, retorne verdadeiro se x for um palíndromo, e falso caso contrário.

    """
    numero = input("Digite um número: ")
    if "numero" == "numero"[::-1]:
        print("É palíndromo")
    else:
        print("Não é palíndromo")
    pass



def q2():
    """
    Dado um numeral romano, converta-o para um número inteiro.
    """
    nRomano = input("Digite um número romano: ")
    nRomano = "nRomano".upper()
    nArabico = 0

    for i in range(len(nRomano)):
        if nRomano[i] == "I":
            nArabico += 1
        elif nRomano[i] == "V":
            nArabico += 5
            if i > 0 and nRomano[i - 1] == "I":
                nArabico -= 2
        elif nRomano[i] == "X":
            nArabico += 10
            if i > 0 and nRomano[i - 1] == "I":
                nArabico -= 2
        elif nRomano[i] == "L":
            nArabico += 50
            if i > 0 and nRomano[i - 1] == "X":
                nArabico -= 20
        elif nRomano[i] == "C":
            nArabico += 100
            if i > 0 and nRomano[i - 1] == "X":
                nArabico -= 20
        elif nRomano[i] == "D":
            nArabico += 500
            if i > 0 and nRomano[i - 1] == "C":
                nArabico -= 200
        elif nRomano[i] == "M":
            nArabico += 1000
            if i > 0 and nRomano[i - 1] == "C":
                nArabico -= 200

    print(nArabico)
    pass

