from datetime import datetime
from trivial import metodoTrivial
from melhoria1 import metodoMelhoria1


def trivial ():
    #tempo antes da execução
    timeBefore = datetime.now()

    response = metodoTrivial()

    #tempo depois da execução
    timeAfter = datetime.now()

    print(response)

    print((timeAfter - timeBefore))


def melhoria1():
    #tempo antes da execução
    timeBefore = datetime.now()

    response = metodoMelhoria1()

    #tempo depois da execução
    timeAfter = datetime.now()

    print(response)

    print((timeAfter - timeBefore))



#--------- TESTE ---------#


# class node :
#     def __init__(self, value=None, impar=None, par=None):
#         self.value = chave
#         self.impar = impar
#         self.par = par


# def isImpar(num):
#     if num % 2 == 1:
#         return True
#     else
#         return False


# def getParWay(number):
#     return number * 2

# def getImparWay(number):

#     if ((number - 1) % 3 == 0 and ((number - 1) / 3) > 0): #caminho do impar
#         return (number - 1) / 3

#     return None



# current = 1






#--------- TESTE ---------#


trivial()
melhoria1()