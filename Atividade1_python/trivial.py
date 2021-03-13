def getAmountOfNumbers(number):
    
    currentNumber = number    

    numbersAmount = 1 #o próprio numero

    while currentNumber != 1:
        if currentNumber % 2 == 0: #se o numero for par
            currentNumber /= 2
        else:
            currentNumber = currentNumber * 3 + 1 # se for ímpar

        numbersAmount += 1
    
    return numbersAmount


def metodoTrivial():

    response = {
        "number" : 0,
        "amountGen" : 0
    }

    for i in range(1, 1000000):

        currentNumber = i

        #quantidade de numeros gerados
        numbersAmount = getAmountOfNumbers(currentNumber)
        
        if numbersAmount > response["amountGen"]:
            response["number"] = i
            response["amountGen"] = numbersAmount

    return response
    