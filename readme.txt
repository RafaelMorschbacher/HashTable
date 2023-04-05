A função hash utilizada foi uma função polinomial, baseada no valor ascii de cada caracter da string.
Sendo x1 o valor ascii do primeiro caracter e xn do último, a função se dá da seguinte forma:
x1 * a**1 + x2 * a**2 + ... + xn * a**n
O valor de 'a' escolhido como 31, que é um dos valores recomendados para o hashing polinomial. Essa função consegue boa aleatoriedade e minimização de conflitos.
No caso de duas strings resultarem no mesmo valor, é criada uma lista do tipo Lista Encadeada na célula da tabela, onde serão armazenados valores conflitantes.
Desse modo, a tabela é uma lista de sublistas encadeadas.
O valor máximo possível de consultas é sempre igual ao tamanho da maior sublista.