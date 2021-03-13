def getAmountOfNumbers(number):
    
    currentNumber = number    

    numbersAmount = 1 #o próprio numero

    while currentNumber != 1:

        if currentNumber % 2 == 0: #se o numero for par
            currentNumber /= 2
            numbersAmount += 1
        else:
            # se for ímpar pula um número
            currentNumber = (currentNumber * 3 + 1)/2
            numbersAmount += 2
        
    return numbersAmount


def metodoMelhoria1():

    response = {
        "number" : 0,
        "amountGen" : 0
    }

    for i in range(1, 1000000, 2):

        currentNumber = i

        numbersAmount = getAmountOfNumbers(currentNumber)
        
        if numbersAmount > response["amountGen"]:
            response["number"] = i
            response["amountGen"] = numbersAmount

    return response