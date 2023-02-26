file_names = open('nomes_10000.txt')


def get_names(file):
    lines = file.readlines()
    names = []
    for line in lines:
        name = line.strip()
        names.append(name)
    return names


names = get_names(file_names)


def hashFunction(input, M, i):
    length = len(input)
    a = 31
    polinomio = 0
    for j in range(0, length):
        polinomio = polinomio + ord(input[j]) * a**j
    key = (polinomio + i)% M
    return key

def createHashTable(M, arr):

    hash_table = [None] * M

    i = 0 #collision counter

    for name in arr:
        key = hashFunction(name, M, i)
        if hash_table[key] == None:
            hash_table[key] = name
        else:
            while hash_table[key] != None:
                i = i+1
                key = hashFunction(name, M, i)
            hash_table[key] = name
    return hash_table


table = createHashTable(10000, names)
print(table)
print(table.count(None))

