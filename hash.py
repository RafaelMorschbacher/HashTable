file_names = open('nomes_10000.txt')


def get_names(file):
    lines = file.readlines()
    names = []
    for line in lines:
        name = line.strip()
        names.append(name)
    return names


names = get_names(file_names)


def hashPolinomial(input, M, i):
    length = len(input)
    a = 31
    polinomio = 0
    for j in range(0, length):
        polinomio = polinomio + ord(input[j]) * a ** j
    key = (polinomio + i) % M
    return key


def createHashTable(M, arr, hashFunction):
    hash_table = [None] * M

    i = 0  # collision counter

    for name in arr:
        key = hashFunction(name, M, i)

        while hash_table[key] is not None:
            i = i + 1
            key = hashFunction(name, M, i)
        hash_table[key] = name
    return hash_table


def searchName(name, hash_table, M, hashFunction):
    key = hashFunction(name, M, 0)

    if hash_table[key] is None:
        return 'NÃO ENCONTRADO'

    i = 0
    while hash_table[key] != name and hash_table[key] != None:
        i = i + 1
        key = hashFunction(name, M, i)
    return hash_table[key]


table = createHashTable(10000, names, hashPolinomial)
print(table)
print(searchName("Mikenzie Symone", table, 10000, hashPolinomial))
print(searchName("Rafael Cunha", table, 10000, hashPolinomial))
