struct Response {
    unsigned int number;
    unsigned short int amountGen;
};

int getAmountOfNumbers(int number){
    unsigned int currentNumber = number;

    unsigned short int numbersAmount = 1; //o próprio numero

    while (currentNumber != 1){
        if (currentNumber % 2 == 0) //se o numero for par
            currentNumber /= 2;
        else
            currentNumber = currentNumber * 3 + 1; // se for ímpar

        numbersAmount += 1;
    }
    return numbersAmount;
}


struct Response metodoTrivial(){
    struct Response response = (struct Response) {.number=0, .amountGen=0};

    for(int i=2; i < 1000000; i++){
        int currentNumber = i;
        //printf(" -- %d", currentNumber);
        //quantidade de numeros gerados
        unsigned short int numbersAmount = getAmountOfNumbers(currentNumber);

        if (numbersAmount > response.amountGen){
            response.number = i;
            response.amountGen = numbersAmount;
        }
    }
    return response;
}
