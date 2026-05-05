import random
import sys
import time

WIDTH = 70  # Número de colunas

# Para cada coluna, quando o contador for 0, nenhum fluxo é exibido
# Caso contrário, ele age como um contador de quandos 1s ou 0s
# Devem ser exibidos naquela coluna
try:
    colunas = [0] * WIDTH
    while True:
        # Itera sobre cada coluna
        for i in range(WIDTH):
            if random.random() < 0.2:
                # Reinicia o contador de fluxo nessa coluna
                # O comprimento do fluxo varia de 4 a 14 caracteres
                colunas[i] = random.randint(4, 14)

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
        print()  # Insere uma quebra de linha ao final de cada coluna'
        time.sleep(0.1)  # Pausa de um decimo de segundo
except KeyboardInterrupt:
    sys.exit()  # Encerra o programa com Ctrl-C é precisonado
