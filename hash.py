file_names = open('nomes_10000.txt', 'r')
file_consultas = open('consultas.txt', 'r')


def get_names(file):
    lines = file.readlines()
    names = []
    for line in lines:
        name = line.strip()
        names.append(name)
    return names


names = get_names(file_names)
consultas = get_names(file_consultas)
test_array = ['Chole Kaspar', 'Zedekiah Brody', 'Jesslyn Tallulah', 'Leilany Zari', 'Ellena Zyion']


# LISTA ENCADEADA - inicio
# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

    # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # print method for the linked list
    def printLL(self):
        current = self.head
        print('[')
        while current:
            print(current.data)
            current = current.next
        print(']')

    def size(self):
        current = self.head
        node_count = 0
        while current:
            node_count = node_count + 1
            current = current.next
        return node_count


# LISTA ENCADEADA - final

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
    linked_list = hash_table[key]
    linked_list.insert(name)


def createHashTable(M, arr, hashFunction):
    hash_table = []
    for i in range(0, M):
        hash_table.append(LinkedList())
    # hash_table = [LinkedList()] * M

    for name in arr:
        insertName(name, hash_table, M, hashFunction)

    return hash_table


def searchName(name, hash_table, M, hashFunction):
    key = hashFunction(name, M)
    acessos = 1

    if not hash_table[key]:
        return -1  # not found

    current_node = hash_table[key].head

    while current_node.data != name and current_node.next is not None:
        current_node = current_node.next
        acessos = acessos + 1

    if current_node.data == name:
        return acessos
    else:
        return -1  # not found


def searchList(names, hash_table, M, hashFunction, output_file):
    for name in names:
        search = searchName(name, hash_table, M, hashFunction)
        if search == -1:
            output_file.write(name + ' MISS\n')
        else:
            output_file.write(name + ' HIT ' + str(search) + '\n')


def table_stats(hash_table, M, consultas, hashFunction, output_file):
    used_cells = 0
    max_list = 0
    min_list = float('inf')
    for cell in hash_table:

        cell_length = cell.size()

        if cell.head is not None:
            used_cells = used_cells + 1

        if cell_length > max_list:
            max_list = cell_length
        if cell_length < min_list:
            min_list = cell_length


    empty_cells = M - used_cells

    occupation_ratio = used_cells/M

    output_file.write("PARTE1: ESTATISTICAS DA TABELA HASH:\n")
    output_file.write('NUMERO DE ENTRADAS DA TABELA USADAS: ' + str(used_cells) + '\n')
    output_file.write('NUMERO DE ENTRADAS DA TABELA VAZIAS: ' + str(empty_cells) + '\n')
    output_file.write('TAXA DE OCUPACAO ' + str(round(occupation_ratio*100, 3)) + '%' + '\n')
    output_file.write('MINIMO TAMANHO DE LISTA: ' + str(min_list) + '\n')
    output_file.write('MAXIMO TAMANHO DE LISTA: ' + str(max_list) + '\n')

    output_file.write("\nPARTE2: ESTATISTICAS DA CONSULTAS:\n")

    searchList(consultas, hash_table, M, hashFunction, output_file)

def experiment(M, database, consultas, hashFunction):
    table = createHashTable(M, database, hashPolinomial)
    output_file = open('experimento' + str(M) + '.txt', 'w')
    table_stats(table, M, consultas, hashFunction, output_file)

# TESTE
for M in [503, 2503, 5003, 7507]:
    experiment(M, names, consultas, hashPolinomial)



#table = createHashTable(2000, names, hashPolinomial)
# for LL in table:
#     LL.printLL()

#searchList(consultas, table, 1000, hashPolinomial)

#table_stats(table, 2000, consultas, hashPolinomial, file_output)
