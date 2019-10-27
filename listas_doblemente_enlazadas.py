'''

ADT Lista doblemente enlazada



ListaDoblementeEnlazada()

get_size() -> Regresa el número de elementos que haya en la cola

insert(value) -> Inserta un dato al final

find_from_head(value) -> Entra a la cabeza y busca hacia la derecha

find_from_tail(value) -> Entra a la cola y busca hacia la izquierda

remove_from_head(value) -> Entra a la cabeza y borra el primer elemento que encuentre hacia la derecha

remove_from_tail(value) -> Entra a la cola y borra el primer elemento que encuentre hacia la izquierda

insert_between(value,predecesor,sucesor) -> Inserta un dato entre dos nodos

transversal() -> Imprime los nodos de head a tail

reverse_transversal() -> Imprime los nodos de tail a head

'''


class NodoDoble:

    def __init__(self, value, siguiente, previo):
        self.data = value
        self.next = siguiente
        self.prev = previo


class ListaDoblementeEnlazada:


    def __init__(self):
        self.__head = NodoDoble(None, None, None)
        self.__tail = NodoDoble(None, None, None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0


    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def insert(self, value):
        if self.__size == 0:
            nuevo = NodoDoble(value, self.__tail, self.__head)
            self.__head.next = nuevo
            self.__tail.prev = nuevo
        else:
            nuevo = NodoDoble(value, self.__tail, self.__tail.prev)
            self.__tail.prev.next = nuevo
            self.__tail.prev = nuevo
        self.__size += 1


    def transversal(self):
        curr_Node = self.__head.next
        while curr_Node.next != None:
            print(curr_Node.data, "->", end=" ")
            curr_Node = curr_Node.next
        print("")


    def reverse_transversal(self):
        curr_Node = self.__tail.prev
        while curr_Node.prev != None:
            print(curr_Node.data, "->", end=" ")
            curr_Node = curr_Node.prev
        print("")


    def find_from_head(self, value):
        curr_node = self.__head
        encontrado = None

        while curr_node.data != value:
            curr_node = curr_node.next

        if curr_node.data == value:
            encontrado = curr_node

        return encontrado


    def find_from_tail(self, value):
        curr_node = self.__tail
        encontrado = None

        while curr_node.data != value:
            curr_node = curr_node.prev

        if curr_node.data == value:
            encontrado = curr_node

        return encontrado


    def remove_from_head(self,value):
        nodo = self.find_from_head(value)
        nodo.next.prev = nodo.prev
        nodo.prev.next = nodo.next
        self.__size -= 1

    def remove_from_tail(self, value):
        nodo = self.find_from_tail(value)
        nodo.next.prev = nodo.prev
        nodo.prev.next = nodo.next
        self.__size -= 1

    def insert_between(self,value, predecesor, sucesor):
        pred = self.find_from_head(predecesor)
        suc = self.find_from_tail(sucesor)
        nuevo = NodoDoble(value,suc,pred)
        nuevo.prev.next = nuevo
        nuevo.next.prev = nuevo
        self.__size += 1