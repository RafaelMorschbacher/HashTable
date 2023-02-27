file_names = open('nomes_10000.txt')


def get_names(file):
    lines = file.readlines()
    names = []
    for line in lines:
        name = line.strip()
        names.append(name)
    return names


names = get_names(file_names)
test_array = ['Chole Kaspar', 'Zedekiah Brody', 'Jesslyn Tallulah', 'Leilany Zari', 'Ellena Zyion']

def hashPolinomial(input, M):
    length = len(input)
    a = 31
    polinomio = 0
    for j in range(0, length):
        polinomio = polinomio + ord(input[j]) * a ** j
    key = polinomio % M
    return key

def insertName(name, hash_table, M, hashFunction):

    key = hashFunction(name, M)

    bucket = hash_table[key]
    bucket.append(name)

    print(key)
    print(bucket)



def createHashTable(M, arr, hashFunction):
    hash_table = [[]] * M

    for name in arr:
        insertName(name, hash_table, M, hashFunction)

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


table = createHashTable(10, test_array, hashPolinomial)

# for bucket in table:
#     print(bucket)

#insertName("Rafael", table, 10000, hashPolinomial)

#print(searchName("Rafael Cunha", table, 10000, hashPolinomial))
