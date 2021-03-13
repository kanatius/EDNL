#include <stdio.h>
#include <time.h>
#include "trivial.c"
#include "melhoria1.c"

void printTime(clock_t c1, clock_t c2){
    float diff = (double)(c2 - c1) / CLOCKS_PER_SEC;
    printf("Tempo: %f\n", diff);
}

void main(){

    clock_t t1, t2;

    t1 = clock();

    struct Response responseTriv = metodoTrivial();

    t2 = clock();

    printf("Numero: %d - Quantidade: %d\n", responseTriv.number, responseTriv.amountGen);
    printTime(t1,t2);


    t1 = clock();

    struct Response responseMel = metodoMelhoria1();

    t2 = clock();

    printf("Numero: %d - Quantidade: %d\n", responseMel.number, responseMel.amountGen);
    printTime(t1,t2);

    return 0;
}
