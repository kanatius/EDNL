int getAmountOfNumbers_m1(int number){

    unsigned int currentNumber = number;

    unsigned short int numbersAmount = 1; //o próprio numero

    while (currentNumber != 1){

        if (currentNumber % 2 == 0){ //se o numero for par
            currentNumber /= 2;
            numbersAmount += 1;
        }else{
            // se for ímpar pula um número
            currentNumber = (currentNumber * 3 + 1)/2;
            numbersAmount += 2;
        }
    }

    return numbersAmount;
}

struct Response metodoMelhoria1(){

    struct Response response = (struct Response) {.number=0, .amountGen=0};

    for(int i=1; i < 1000000; i+=2){

        int currentNumber = i;

        unsigned short int numbersAmount = getAmountOfNumbers_m1(currentNumber);

        if (numbersAmount > response.amountGen){
            response.number = i;
            response.amountGen = numbersAmount;
        }
    }
    return response;
}
