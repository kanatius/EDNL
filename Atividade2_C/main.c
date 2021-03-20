#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define QTD_DIG_MATRIC 5

void printTime(clock_t c1, clock_t c2){
    double diff = (double)(c2 - c1) / CLOCKS_PER_SEC;
    printf("Tempo: %f\n", diff);
}

int ifMatValid(int matricula){
    //verifica se a matrícula é válida
    if(matricula < 10 ^ (QTD_DIG_MATRIC+1))
        return 1;
    return 0;
}

int hashFunctionStep1(int matricula){
    return matricula/10;
}

int hashFunctionStep2(int matricula){
    return matricula%10;
}

struct Funcionario{
    int matricula;
    char nome[40];
};

struct Funcionario** createFuncList(int qtd_digits){

    int size = pow(10, (qtd_digits -1));
    //printf("%d", size);

    struct Funcionario** funcionarios;
    funcionarios = (struct Funcionario**) malloc(sizeof(struct Funcionario) * size);
    return funcionarios;
}

void insertFuncionario(struct Funcionario** funcList, struct Funcionario* funcionario){

    if(!ifMatValid(funcionario->matricula)){
        //printf("Matrícula invalida");
        return;
    }

    int pos1 = hashFunctionStep1(funcionario->matricula);
    int pos2 = hashFunctionStep2(funcionario->matricula);

    //printf("Matricula: %d\n", funcionario->matricula);
    //printf("Pos1: %d\n", pos1);
    //printf("Pos2: %d\n", pos2);

    if(!funcList[pos1]){
        //cria a lista na posição caso ainda não foi criada
        short tam = 10;
        funcList[pos1] = (struct Funcionario*) malloc(sizeof(struct Funcionario) * tam);

        for(short i=0; i < tam; i++){
            funcList[pos1][i].matricula = 0;
        }
    }
    if(funcList[pos1][pos2].matricula == 0){
        funcList[pos1][pos2] = *funcionario;
        //printf("Funcionario cadastrado com sucesso!\n");
    }else{
        //printf("Matrícula ja esta em uso\n");
    }
}

struct Funcionario findFunc(struct Funcionario** funcList, int matricula){

    int pos1 = hashFunctionStep1(matricula);
    int pos2 = hashFunctionStep2(matricula);

    if (funcList[pos1]){
        if (funcList[pos1][pos2].matricula != 0){
            return funcList[pos1][pos2];
        }
    }
    return (struct Funcionario) {.matricula = 0, .nome = "------------"};
}

int main(){


    struct Funcionario** funcList = createFuncList(QTD_DIG_MATRIC);

    struct Funcionario func = (struct Funcionario) {.matricula = 205, .nome = "Natan"};
    struct Funcionario func2 = (struct Funcionario) {.matricula = 20020, .nome = "Maria"};
    struct Funcionario func3 = (struct Funcionario) {.matricula = 20020, .nome = "Felipe"};
    struct Funcionario func4 = (struct Funcionario) {.matricula = 10020, .nome = "Felipe"};

    clock_t t1, t2;

    t1 = clock();

    insertFuncionario(funcList, &func);
    insertFuncionario(funcList, &func2);
    insertFuncionario(funcList, &func3);
    insertFuncionario(funcList, &func4);

    //printf("\nProcurando funcionarios:\n");

    struct Funcionario f1 = findFunc(funcList, 205); //Natan
    struct Funcionario f2 = findFunc(funcList, 20020); //Maria
    struct Funcionario f3 = findFunc(funcList, 23233);
    struct Funcionario f4 = findFunc(funcList, 10020); //Felipe

    //sleep(1);

    t2 = clock();


    printf("f1: %s\n", f1.nome);
    printf("f2: %s\n", f2.nome);
    printf("f3: %s\n", f3.nome);
    printf("f4: %s\n", f4.nome);

    printTime(t1,t2);

    for(int i=0; i < pow(10, QTD_DIG_MATRIC -1); i++){
        funcList[i] = NULL;
        free(funcList[i]);
    }
    return 0;
}
