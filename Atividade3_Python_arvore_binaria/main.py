
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def printValue(self):
        print(self.value)

    def insertNode(self, node):
        
        if node.value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.insertNode(node)
            return

        if node.value >= self.value:
            if self.right is None:
                self.right = node
            else:
                self.right.insertNode(node)
            return
        
        # print("Valor {} não inserido - Valor já inserido".format(node.value))
    
    def is_leaf(self):
        return True if self.left is None and self.right is None else False

    def getChildrenAmount(self):

        amount = 0

        if self.right is not None:
            amount += 1

        if self.left is not None:
            amount += 1
        
        return amount

    def remove(self, node):

        # ----------- LEAF -----------#

        #remoção folha Esquerda
        if self.left:
            if self.left.value == node.value and self.left.is_leaf():
                self.left = None
                return True

        #remoção folha Direita
        if self.right:
            if self.right.value == node.value and self.right.is_leaf():
                self.right = None
                return True

        # ----------- LEAF -----------#

        # ----------- ONE CHILD -----------#
        #remoção 1 child Esquerda
        if self.left:
            if self.left.value == node.value and self.left.getChildrenAmount() == 1:

                if self.left.left:
                    self.left = self.left.left
                    return True

                if self.left.right:
                    self.left = self.left.right
                    return True
        
        #remoção 1 child Direita
        if self.right:
            if self.right.value == node.value and self.right.getChildrenAmount() == 1:

                if self.right.left: #recebe o da esquerda
                    self.right = self.right.left
                    return True

                if self.right.right: #recebe o da direita
                    self.right = self.right.right
                    return True
        
        # ----------- ONE CHILD -----------#

        
        # ----------- TWO CHILD -----------#

        if self.left: 

            if self.left.value == node.value and self.left.getChildrenAmount() == 2:
                chosenNode = self.left.right.getMin()

                self.remove(chosenNode) #Remove o nó mais a esquerda

                #set proximos
                chosenNode.left = self.left.left
                chosenNode.right = self.left.right

                #set anterior
                self.left = chosenNode

        if self.right:

            if self.right.value == node.value and self.right.getChildrenAmount() == 2:
                chosenNode = self.right.right.getMin()

                self.remove(chosenNode) #Remove o nó mais a esquerda

                #set proximos
                chosenNode.left = self.right.left
                chosenNode.right = self.right.right

                #set anterior
                self.right = chosenNode


        # ----------- TWO CHILD -----------#
        

        if self.left:    
            if self.left.remove(node):
                return True
        
        if self.right:
            if self.right.remove(node):
                return True
        
        return False


    def printTree(self):
        
        print(self.value)

        if self.left:
            self.left.printTree()
        # else:
        #     print(str(self.value) + "-left: None")
        
        if self.right:
            self.right.printTree()
        # else:
        #     print(str(self.value) + "-right: None)"

    def getDepth(self):

        if (self.left is None) and (self.right is None): #se for uma folha retorna 1
            return 1
        
        leftDepth = 0
        rightDepth = 0

        if self.left is not None: #pega o comprimeto da esquerda caso não for nulo
            leftDepth = self.left.getDepth()
        
        if self.right is not None: #pega o comprimeto da direita caso não for nulo
            rightDepth = self.right.getDepth()

        #retora o comprimento que for maior
        return (rightDepth + 1) if rightDepth > leftDepth else (leftDepth + 1)

    def countLeaves(self):
        if (self.right is None) and (self.left is None):
            return 1
        
        leftLeaves = 0
        rightLeaves = 0

        if self.right:
            rightLeaves = self.right.countLeaves()
        
        if self.left:
            leftLeaves = self.left.countLeaves()
        
        return leftLeaves + rightLeaves

    def countNodes(self):

        leftNodes = 0
        rightNodes = 0

        if self.right:
            rightNodes = self.right.countNodes()
        
        if self.left:
            leftNodes = self.left.countNodes()

        return 1 + leftNodes + rightNodes

    def getMin(self):

        if self.left == None:
            return self
        else:
            return self.left.getMin()

#--------------------------------------------------#     

class Tree:

    def __init__(self, root = None):
        self.root = root

    def insertNode(self, node):
        
        if self.root is None:
            self.root = node
            return
        
        self.root.insertNode(node)
    
    def removeNode(self, node):
        if self.root is None:
            return
        
        if self.root.is_leaf() and self.root.value == node.value:
            self.root = None
            return

        self.root.remove(node)

    @classmethod
    def createTree(cls, values):
        tree = Tree()

        for value in values:
            node = Node(value)
            tree.insertNode(node)
        
        return tree

    def printTree(self):
        if self.root is None:
            print("Árvore Nula")
            return
        
        self.root.printTree()

    def showDepth(self):
        if self.root is None:
            print("Profundidade: 0")
            return
        
        print("Profundidade: " + str(self.root.getDepth()))

    def showLeavesAmount(self):

        if self.root is None:
            print("Leaves: " + 0)
        
        print("Leaves: " + str(self.root.countLeaves()))

    def showNodesAmount(self):

        if self.root is None:
            print("Nodes: " + 0)

        print("Nodes: " + str(self.root.countNodes()))

    def printMetaData(self):
        self.showDepth()
        self.showNodesAmount()
        self.showLeavesAmount()
#--------------------------------------------------#

values = [14, 15, 4, 9, 7, 18, 3, 5, 16, 4, 20, 17, 9, 14, 5] #SLIDE 9
values2 = [8, 4, 2, 6, 12, 10, 14, 13, 15, 11, 1, 3, 5] #SLIDE 12
values3 = [50, 30, 100, 20, 40, 35, 45, 37] #https://pt.wikipedia.org/wiki/%C3%81rvore_bin%C3%A1ria_de_busca#Remo%C3%A7%C3%A3o
values4 = [15, 5, 16, 3, 12, 20, 18, 23, 10, 13, 6, 7] #SLIDE 10


tree = Tree.createTree(values)
tree2 = Tree.createTree(values2)
tree3 = Tree.createTree(values3)
tree4 = Tree.createTree(values4)



print("\nSlide 9")
tree.printMetaData()
print("\nSlide 12")
tree2.printMetaData()
print("\nWiki")
tree3.printMetaData()
print("\nSlide 10")
tree4.printMetaData()

tree3.printTree()
tree3.removeNode(Node(30))
tree3.printTree()