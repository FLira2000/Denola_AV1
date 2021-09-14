#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//Criando a estrutura da pilha
struct _pilha
{
    int top;
    unsigned tam;
    int* prox;
};
typedef struct _pilha Pilha;

int main()
{
    //Elaborando o programa de testes
    char exp[] = "A+B-C*D/E";
    _transpor_equacao(exp);
    return 0;
}

//Inicializando a pilha
Pilha* _inicializa_pilha( unsigned tam )
{
    Pilha* stak = (Pilha*)malloc(sizeof(Pilha));

    if (!stak)
    {

        return NULL;
    }

    stak->top = -1;
    stak->tam = tam;

    stak->prox = (int*) malloc(stak->tam * sizeof(int));

    return stak;
}

//confirmando que a pilha est· vazia
int _verifica_vazia(Pilha* stak)
{
    return stak->top == -1 ;
}

//verifica pilha
char _verifica_pilha(Pilha* stak)
{
    return stak->prox[stak->top];
}

//FunÁ„o para desempilhar a pilha
char _desempilha(Pilha* stak)
{
    if (!_verifica_vazia(stak))
    {
        return stak->prox[stak->top--] ;
    }
    return 0;
}

//Essa aqui empilha
void _empilha(Pilha* stak, char op)
{
    stak->prox[++stak->top] = op;
}

//retorna o caractere, se estiver em uppercase ou lowercase
int _verifica_operador(char ch)
{
    return (ch >= 'a' && ch <= 'z') ||(ch >= 'A' && ch <= 'Z');
}

//funÁ„o para definir o tipo de prioridade de cada operador, descrita no enunciado do exercÌcio
int _sinais_operacao(char ch)
{
    switch (ch)
    {
    case '(':
        return 1;
        break;

    case '+':
    case '-':
        return 2;
        break;
        break;

    case '*':
    case '/':
        return 3;
        break;
        break;
    }
    return -1;
}

//funÁ„o principal, que converte a operaÁ„o de prefixa para posfixa
int _transpor_equacao(char* exp)
{
    int i, j;
    Pilha* stak = _inicializa_pilha(strlen(exp));
    if(!stak)
    {
        return -1 ;
    }


    for (i = 0, j = -1; exp[i]; ++i)
    {
        if (_verifica_operador(exp[i]))
        {
            exp[++j] = exp[i];
        }

        else if (exp[i] == '(')
        {
            _empilha(stak, exp[i]);
        }

        else if (exp[i] == ')')
        {
            while (!_verifica_vazia(stak) && _verifica_pilha(stak) != '(')
            {
                exp[++j] = _desempilha(stak);
            }
            if (!_verifica_pilha(stak) && _verifica_pilha(stak) != '(')
            {
                return -1;
            }
            else
                _desempilha(stak);
        }
        else
        {
            while (_verifica_pilha(stak) && _sinais_operacao(exp[i]) <= _sinais_operacao(_verifica_pilha(stak)))
            {
                exp[++j] = _desempilha(stak);
            }
            _empilha(stak, exp[i]);
        }

    }
    while (!_verifica_vazia(stak))
    {

        exp[++j] = _desempilha(stak);
    }

    exp[++j] = '\0';
    printf( "%s", exp );
    return 0;
}
//Cabo ( :)
