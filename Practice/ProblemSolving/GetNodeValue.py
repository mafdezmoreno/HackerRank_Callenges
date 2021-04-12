#https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem

class Nodo():
    
    hijo = None
    valor = -1
    n_hijos = 0

    def __init__(self, valor = None) -> None:
        self.valor = valor
        pass

class SinglyLinkedList():
    
    cola = None
    inicio = None

    def insert_node(self, valor) -> None:
        
        if self.inicio == None:
            self.inicio = Nodo(valor)
            self.cola = self.inicio
        else:
            temp = Nodo(valor)
            self.cola.hijo = temp
            self.cola = temp
            self.inicio.n_hijos +=1
            hijos = self.inicio.n_hijos
            nodo = self.inicio.hijo
            while nodo != None:
                hijos -= 1
                nodo.n_hijos = hijos
                nodo = nodo.hijo
        pass
    
    def imprime(self):
        nodo = self.inicio
        while nodo != None:
            print(nodo.valor, ": ", nodo.n_hijos, end = " | ")
            nodo = nodo.hijo
        print()

def getNode(nodo, position_tail):

    for _ in range(nodo.n_hijos-position_tail+1):
        temp = nodo.valor
        nodo = nodo.hijo
    print(temp)
    pass

if __name__ == '__main__':

    with open("GetNodeValue00.txt") as file:

        tests = int(next(file))

        for tests_itr in range(tests):
            llist_count = int(next(file))

            llist = SinglyLinkedList()

            for _ in range(llist_count):
                llist_item = int(next(file))
                llist.insert_node(llist_item)

            position = int(next(file))
            llist.imprime()

            result = getNode(llist.inicio, position)
