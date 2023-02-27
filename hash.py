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
        while (current):
            print(current.data)
            current = current.next
        print(']')
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
    #hash_table = [LinkedList()] * M

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


table = createHashTable(200, names, hashPolinomial)
for LL in table:
    LL.printLL()

