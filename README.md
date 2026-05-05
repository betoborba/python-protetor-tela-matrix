## Protetor de tela Matrix ## 

- Esse programa faz parte dos meus estudos de lógica de programação e estudos em python. 
-  O programa cria um loop infinito, que só é interrompido quando o usuário clicar em crtl-C. 
- A principal estrutura de dados utilizada é a lista coluna, que armazena até 70 caracteres inteiros uma para cada coluna da saída. 

Quando um número interiro na lista coluna for igual a 0, o programa exibe um espaço vazio naquela coluna. 

```python

import random, sys, time

WIDTH = 70 

```
Importado o módulo `random` para utilizar as funções `choice() e randit()`, o modulo `sys` foi usado para acessar a função `exit()` e módulo `time` para utilizar a função `sleep()`.

A variável `WIDTH` está escrita com todas as letras maiúscula porque representa uma variável constante. Uma constante é uma variável cuso valor não deve ser alterado após ser definido. 

Ao utilizar constantes torna o código mais legível. Por exemplo: 

Escrever o código `colunas = [0] * WIDTH` ao invés `colunas = [0] * 70` evita confusões futuras. 

## Try 

- A maior parte do código está encapsulado dentro de um bloco `try`, que captura o momento em que o usuário preciona ctrl-C gerando uma exceção do tipo `KeyboardInterrupt`: 

```python
# Para cada coluna, quando o contador for 0, nenhum fluxo é exibido
# Caso contrário, ele age como um contador de quandos 1s ou 0s
# Devem ser exibidos naquela coluna
try:
    colunas = [0] * WIDTH

```
- A variável colunas contém uma lista de 0 números inteiros. A quantidade de números inteiros nessa lista é igual ao valor de `WIDTH` Cada um desses números controla se uma coluna da janela de saída exibirá ou não uma sequência de números binários. 



```Python

    while True:
        # Itera sobre cada coluna
        for i in range(WIDTH): #Esse for passa por cada coluna da linha. Como WIDTH = 70, ele percorre os índices de 0 até 69.
            if random.random() < 0.2:
                # Reinicia o contador de fluxo nessa coluna
                # O comprimento do fluxo varia de 4 a 14 caracteres
                colunas[i] = random.randint(4, 14) #Isso define que aquela coluna vai exibir caracteres por uma quantidade aleatória entre 4 e 14 linhas.
```
- A intenção é que o programa seja executado indefinidamente, por isso é colocado dentro de um loop `while True`: Dentro desse loop `for` que itera sobre cada cada coluna de uma única linha. A variável do loop, `i` representa os índices da lista `colunas` ela comça em 0 e vai até `WIDTH`, mas sem incluí-la. O valor em `colunas[0]` determina o que será exibida na coluna mais à esquerda; `colunas[1]` controla a segunda coluna da esquerda e assim sucessivamente. 

- Para cada coluna, há uma chance de 2% de que o número inteiro em `coluna[i]` seja definido com um valor entre 4 e 14. 

- È calculado essa chance comparando o valor retornado por `random.random()`pois gera pontos flutuantes aleátorio entre 0.0 e 1.0 com 0.02. 

- Se quiser que o número fique mais denso, basta aumentar esse número, se preferir que fique mais esparsos, deve ser reduzido.  

```python

                # Exibe um caractere nesta coluna
            if colunas[i] == 0:
                # Altere ' ' para '-' se quiser visualizar os espaços vazios
                print(' ', end='')
            else:
                # Exibe um 0 ou 1 código original. Adaptei para matrix
                print(random.choice(['ｱ', 'ｲ', 'ｳ', 'ｴ', 'ｵ', '1', '2', '3', '4', '5', 'A', 'B', 'C', 'ｶ', 'ｷ', 'ｸ', 'ｹ', 'ｺ',
                                     '6', '7', '8', '9', '0', 'X', 'Y', 'Z', 'ｻ', 'ｼ', 'ｽ', 'ｾ', 'ｿ', 'a', 'b', 'c', 'ﾀ', 'ﾁ', 'ﾂ', 'ﾃ', 'ﾄ',
                                     'd', 'e', 'f', 'ﾅ', 'ﾆ', 'ﾇ', 'ﾈ', 'ﾉ', 'g', 'h', 'i', 'ﾊ', 'ﾋ', 'ﾌ', 'ﾍ', 'ﾎ', 'j', 'k', 'l',
                                     'ﾏ', 'ﾐ', 'ﾑ', 'ﾒ', 'ﾓ', 'm', 'n', 'o', 'ﾔ', 'ﾕ', 'ﾖ', 'p', 'q', 'r', 'ﾗ', 'ﾘ', 'ﾙ', 'ﾚ', 'ﾛ',
                                     's', 't', 'u', 'ﾜ', 'ｦ', 'ﾝ', 'v', 'w', 'x']), end='')
                colunas[i] -= 1  # Decrementa o contador desta coluna
``` 

- Se `if colunas[i] == 0:`, um espaço vazio é exibido naquela posição. Caso contrário para a lista de caracteres `random.choice`
O código também decrementa o contador `colunas[i]` 

- Se quiser vizualizar os espaços "vazios" é possivel substituir `string' '` por `'-'`

- Após o termino do bloco `else`, o bloco do loop `for` também é encerrado:

```python

 print()  # Insere uma quebra de linha ao final de cada coluna'
        time.sleep(0.1)  # Pausa de um decimo de segundo
except KeyboardInterrupt:
    sys.exit()  # Encerra o programa com Ctrl-C é precisonado

```






