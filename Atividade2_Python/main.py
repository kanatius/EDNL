from datetime import datetime

class Funcionario:

    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome

def insertFuncionario(funcionarios, func):

    if func.matricula not in funcionarios:
        funcionarios.update({func.matricula : func.nome})
        print("Usuário cadastrado com sucesso")
        return
    
    print("Matrícula já em uso")

def findFunc(funcionarios, matricula):
    try:
        return funcionarios[matricula]
    except:
        return None

funcionarios = {}

func1 = Funcionario(matricula=205, nome="Natan")
func2 = Funcionario(matricula=20020, nome="Maria")
func3 = Funcionario(matricula=20020, nome="Felipe")
func4 = Funcionario(matricula=10020, nome="Felipe")

#tempo antes da execução
timeBefore = datetime.now()

insertFuncionario(funcionarios, func1)
insertFuncionario(funcionarios, func2)
insertFuncionario(funcionarios, func3)
insertFuncionario(funcionarios, func4)

res1 = findFunc(funcionarios, 205)
res2 = findFunc(funcionarios, 20020)
res3 = findFunc(funcionarios, 12312) #nao cadastrado
res4 = findFunc(funcionarios, 10020)

#tempo depois da execução
timeAfter = datetime.now()

print(res1)
print(res2)
print(res3)
print(res4)

print(timeAfter - timeBefore)