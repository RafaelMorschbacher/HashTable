file_names = open('nomes_10000.txt')


def get_names(file):
    lines = file.readlines()
    names = []
    for line in lines:
        name = line.strip()
        names.append(name)
    return names

def hashFunction(input, M, i):
    length = len(input)
    a = 31
    polinomio = 0
    for j in range(0, length):
        polinomio = polinomio + ord(input[j]) * a**j
        print(ord(input[j]))
    key = polinomio % M + i
    return key

def createHashTable(M, arr):
    hash_table = [None] * M

# names = get_names(file_names)
# for name in names:
#     print(hashFunction(name, 10000, 0))

