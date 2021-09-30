"""
Árbol AVL - Implementación en Python
"""

from __future__ import print_function

"""
Declaramos la clase "Node", con cada una de sus propiedades.
"""
class Node:
    
    #Constructor de los nodos, donde se le asignan un valor, su Factor de Balanceo(BF) y la referencia a su padre, hijoIzq e HijoDer
    def __init__(self, label):
        self.label = label
        self._parent = None
        self._left = None
        self._right = None
        self._height = 0
        self.BF = 0

    #Metodo para comparar 2 objetos <Nodo>
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.label == other.label
        return False

    @property
    def right(self):
        return self._right

    #Al settear un hijo, el hijo debe referenciar al padre tambien
    @right.setter
    def right(self, node):
        self._right = node

        if node is not None:
            self._right.parent = self

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node
        
        if node is not None:
            self._left.parent = self

    @property
    def parent(self):
        return self._parent

    #Al settear el padre, tiene que settearse la altura del padre +1
    @parent.setter
    def parent(self, node):
        self._parent = node

        if node is not None:
            self.height = self._parent.height + 1
        else:
            self.height = 0

    @property
    def height(self):
        return self._height

    #Al settearse la altura, tiene que settearle la alturas a sus hijos tambien
    @height.setter
    def height(self, value):

        self._height = value

        if self._right is not None:
            self._right.height = self._height + 1
        if self._left is not None:
            self._left.height  = self._height + 1




        

# Declaramos la clase AVL
class AVL:

    def __init__(self):
        self.root = None

        """
        Operación de inserción para agregar nuevos nodos
        al árbol.
        """


    #Descripto en pseudocódigo
    
    def search(self, value):
        curr_node = self.root
        found = False

        while not found and curr_node is not None:

            if value == curr_node.label:
                found = True
                break

            elif value > curr_node.label:
                curr_node = curr_node.right
                continue

            else:
                curr_node = curr_node.left
                continue

            
        return found

    
    
    #Descripto en pseudocódigo
    
    def insert(self, value):
        node = Node(value)

        if node is not None:

            if self.root is None:
                self.root = node
                self.root.parent = None
            else:
                curr_node = self.root
                dad_node = None

                while True:
                    if curr_node is not None:

                        dad_node = curr_node

                        if node.label < curr_node.label:
                            curr_node = curr_node.left
                        elif node.label > curr_node.label:
                            curr_node = curr_node.right
                        else:
                            print("El valor: '", node.label, "' no se agregó puesto que ya estaba en el árbol.")
                            return
                    else:
                        if node.label < dad_node.label:
                            dad_node.left = node
                        else:
                            dad_node.right = node

                        self.rebalance(node)
                        break


    # Operación de chequeo por rotación
    
    def rebalance(self, node):
        n = node
        parent_node = node.parent

        
        while parent_node is not None:
            
            if n == parent_node.right:

                if parent_node.BF > 0:

                    aux_parent = parent_node.parent
                    if n.BF < 0:
                        raizSubArbol = self.rotate_RightLeft(n, parent_node)
                    else:
                        raizSubArbol = self.rotate_Left(n, parent_node)
                
                else:

                    if parent_node.BF < 0:
                        parent_node.BF = 0
                        break

                    parent_node.BF = 1
                    n = parent_node
                    parent_node = n.parent
                    
                    continue

            elif n == parent_node.left:
                
                if parent_node.BF < 0:

                    aux_parent = parent_node.parent
                    if n.BF > 0:
                        raizSubArbol = self.rotate_LeftRight(n, parent_node)
                    else:
                        raizSubArbol = self.rotate_Right(n, parent_node)

                else:

                    if parent_node.BF > 0:
                        parent_node.BF = 0
                        break
                    
                    parent_node.BF = -1
                    n = parent_node
                    parent_node = n.parent
                    continue


            if aux_parent is not None:

                if parent_node == aux_parent.left:
                    aux_parent.left = raizSubArbol
                
                else:
                    aux_parent.right = raizSubArbol
            
            else:
                raizSubArbol.parent = None
                self.root = raizSubArbol
                


            break
                

    def rotate_Left(self, right_child, parent):
        aux = right_child.left
        parent.right = aux
        right_child.left = parent


        #chequeo y cambio los factores de balanceo
        if ( right_child.BF == 0):
            parent.BF = 1
            right_child.BF = -1
        else:
            parent.BF = 0
            right_child.BF = 0
        
        return right_child


    def rotate_Right(self, left_child, parent):
        aux = left_child.right
        parent.left = aux
        left_child.right = parent


        # Chequeo y cambio los factores de balanceo
        if ( left_child.BF == 0):
            parent.BF = 1
            left_child.BF = -1
        else:
            parent.BF = 0
            left_child.BF = 0
        
        return left_child

    def rotate_RightLeft(self, right_child, parent):
        third_node = right_child.left
        
        # __START__ : primera Rotacion
        aux1 = third_node.right
        right_child.left = aux1
        third_node.right = right_child

        # __START__ : segunda Rotacion
        aux2 = third_node.left
        parent.right = aux2
        third_node.left = parent


        #Chequeo y cambio los factores de balanceo
        if third_node.BF == 0:
            parent.BF = 0
            right_child.BF = 0
        else:

            if third_node.BF > 0:
                parent.BF = -1
                right_child.BF = 0
            else:
                parent.BF = 0
                right_child.BF = 1
        
        third_node.BF = 0

        return third_node


    def rotate_LeftRight(self, left_child, parent):
        third_node = left_child.right

        # __START__ : primera rotacion
        aux1 = third_node.left
        left_child.right = aux1
        third_node.left = left_child

        # __START__ : segunda Rotacion
        aux2 = third_node.right
        parent.left = aux2
        third_node.right = parent


        #Chequeo y cambio los factores de balanceo
        if third_node.BF == 0:
            parent.BF = 0
            left_child.BF = 0
        else:

            if third_node.BF < 0:
                parent.BF = -1
                left_child.BF = 0
            else:
                parent.BF = 0
                left_child.BF = 1
        
        third_node.BF = 0

        return third_node

    def perLevel(self):
        abierto = [self.root]
        while len(abierto) > 0 and abierto[0] is not None:

            if abierto[0].left is not None:
                abierto.append(abierto[0].left)
            
            if abierto[0].right is not None:
                abierto.append(abierto[0].right)

            print(abierto[0].label)

            abierto.pop(0)
    
    
    '''
    Codigo para insertar numeros (estrictamente numeros) desde archivo, puesto que queda más claro el orden con numeros.
    Se presupone un archivo bien armado, con un numero por linea y terminador de linea '\n'
    '''

    def insertFromFile(self, inputFile):
        file = open(inputFile, "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            line = line[:-1]
            t.insert(int(line))
        


    def checkIfTreeIsAVL(self, node):

        if node is not None:
            
            if abs(node.BF) > 1:
                return False

            if not self.checkIfTreeIsAVL(node.left):
                return False
            
            if not self.checkIfTreeIsAVL(node.right):
                return False

        return True 

    def checkIfTreeIsAVL_nonRecursive(self, node):

        if node is not None:
            abierto = [node]
            while len(abierto) > 0:

                if abs(abierto[0].BF) > 1:
                    return False

                if abierto[0].left is not None:
                    abierto.append(abierto[0].left)
                
                if abierto[0].right is not None:
                    abierto.append(abierto[0].right)

                abierto.pop(0)
        
        return True
            
    def checkIfTreeIsComplete(self, node):
    
        if node is not None:
            abierto = [node]
            while len(abierto) > 0:

                if abs(abierto[0].BF) > 0:
                    return False

                if abierto[0].left is not None:
                    abierto.append(abierto[0].left)
                
                if abierto[0].right is not None:
                    abierto.append(abierto[0].right)

                abierto.pop(0)
        
        return True

    def insertCountNPrint(self, inputFile, outputFile): 

        # Inserto los elementos desde archivo a través del método implementado anteriormente
        self.insertFromFile(inputFile)


        # Busco todos los nodos hojas e imprimo su altura en el archivo <outputFile>
        diccionario = {"-2":[], "-1":[], "0": [], "1":[], "2": []}
        hojas = []
        abierto = [self.root]
        while len(abierto) > 0 and abierto[0] is not None:

            diccionario[str(abierto[0].BF)].append(abierto[0])

            if abierto[0].left is None and abierto[0].right is None:
                hojas.append(abierto[0])
            
            else:

                if abierto[0].left is not None:
                    abierto.append(abierto[0].left)
                
                if abierto[0].right is not None:
                    abierto.append(abierto[0].right)


            abierto.pop(0)


        file = open(outputFile, "w")
        
        file.write("Hojas: \n")
        for hoja in hojas:
            file.write("  " + str(hoja.label) + ": Nivel " + str(hoja.height) + "\n")

        file.write("\n\nNodos por Factor de balanceo: \n")
        suma = 0

        for factBalan, nodos in diccionario.items():
            file.write("  \"" + str(factBalan) + "\": \n")
            for nodo in nodos:
                file.write("    -> " + str(nodo.label) + "\n")
                suma+=1
            file.write("  Total = " + str(len(nodos)) + "\n\n")

        file.write("Cantidad de Nodos Totales = " + str(suma) )

        if self.checkIfTreeIsComplete(self.root):
            file.write(" = 2^(nivelMax+1) - 1 (Porque es Árbol Completo)")

        file.write("\n")
        file.close()
        if (self.checkIfTreeIsAVL_nonRecursive (self.root) == True):
            print("Este árbol está balanceado.")
        else:
            print("Este árbol no está balanceado.")




if __name__ == '__main__':
    t = AVL()

    #Por favor, si se esta ejecutando en otro Sistema Operativo no Linux o MacOS, cambiar el "/" por "\"
    t.insertCountNPrint("Inputs/arbolLlenoANivel3.txt" , "Outputs/ArbolLlenoANivel3_output.txt")
    
    #imprimo los nodos por nivel
    t.perLevel()
