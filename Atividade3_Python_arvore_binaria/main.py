
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

#--------------------------------------------------#     

class Tree:

    def __init__(self, root = None):
        self.root = root

    def insertNode(self, node):
        
        if self.root is None:
            self.root = node
            return
        
        self.root.insertNode(node)

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
#--------------------------------------------------#

values = [14, 15, 4, 9, 7, 18, 3, 5, 16, 4, 20, 17, 9, 14, 5]

tree = Tree()

for value in values:
    node = Node(value)
    tree.insertNode(node)


values2 = [8, 4, 2, 6, 12, 10, 14, 13, 15, 11, 1, 3, 5]

tree2 = Tree()

for value2 in values2:
    node2 = Node(value2)
    tree2.insertNode(node2)

print("\nÁrvore 1 - Slide 9")
tree.showDepth()
tree.showLeavesAmount()
tree.showNodesAmount()

print("\nÁrvore 2 - Slide 12")
# tree2.printTree()
tree2.showDepth()
tree2.showLeavesAmount()
tree2.showNodesAmount()