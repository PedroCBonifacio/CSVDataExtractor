# Programa Python para Manipulação de Dados em CSV

Este código é um programa Python que processa e manipula dados em formato CSV. Ele oferece várias operações que podem ser aplicadas aos dados, como exclusão de colunas, busca, restauração, contagem, cálculo de média, desvio padrão, correlação e gravação em arquivo CSV. A seguir está uma explicação de cada parte do código:

## Função `isfloat(s)`

- **Objetivo:** Verifica se a string `s` pode ser convertida para um número de ponto flutuante.
- **Implementação:** Usa um bloco `try-except` para tentar converter `s` para `float`. Se a conversão for bem-sucedida, retorna `True`, caso contrário, captura a exceção `ValueError` e retorna `False`.

## Função `dados()`

- **Objetivo:** Lê os dados de entrada da `stdin`, converte strings que representam números em inteiros ou floats, e os armazena em uma lista de listas.
- **Implementação:** Para cada linha de entrada, a função divide a linha por vírgulas, verifica se cada elemento é um número inteiro ou um float, e faz a conversão apropriada antes de adicionar a linha processada à lista `dados`.

## Função `exclui(seleção, intervalo)`

- **Objetivo:** Exclui colunas em um intervalo especificado.
- **Implementação:** Recebe um intervalo no formato `início:fim`, e para cada linha na seleção, exclui as colunas fora desse intervalo. O intervalo é inclusive para `início` e exclusivo para `fim`.

## Função `busca(seleção, rotulo, condicao)`

- **Objetivo:** Busca linhas na seleção que satisfaçam uma condição para um dado rótulo (nome de coluna).
- **Implementação:** Primeiro, encontra o índice da coluna correspondente ao rótulo. Em seguida, aplica a condição às linhas da seleção e retorna as que atendem à condição.

## Função `restaura()`

- **Objetivo:** Restaura os dados ao estado original.
- **Implementação:** Simplesmente retorna os dados originalmente lidos, antes de qualquer modificação.

## Função `conta(seleção)`

- **Objetivo:** Conta o número de linhas (excluindo o cabeçalho) na seleção.
- **Implementação:** Retorna o número de linhas menos um, para desconsiderar o cabeçalho.

## Função `média(seleção, rotulo)`

- **Objetivo:** Calcula a média dos valores de uma coluna especificada por `rotulo`.
- **Implementação:** Encontra o índice da coluna, soma os valores dessa coluna para todas as linhas, e divide pelo número de linhas (excluindo o cabeçalho).

## Função `desviopadrão(seleção, rotulo)`

- **Objetivo:** Calcula o desvio padrão dos valores de uma coluna especificada por `rotulo`.
- **Implementação:** Calcula a média, depois a somatória dos quadrados das diferenças entre cada valor e a média, divide pelo número de valores, e retorna a raiz quadrada desse resultado.

## Função `correlação(seleção, rotulo1, rotulo2)`

- **Objetivo:** Calcula a correlação entre duas colunas especificadas por `rotulo1` e `rotulo2`.
- **Implementação:** Calcula a média de cada coluna, em seguida a soma dos produtos das diferenças de cada valor da média das duas colunas, e divide pelo produto dos desvios padrão das duas colunas.

## Função `gravacsv(seleção, arquivo)`

- **Objetivo:** Grava a seleção de dados em um arquivo CSV.
- **Implementação:** Abre o arquivo para escrita, e grava cada linha da seleção como uma linha no arquivo, separando os elementos por vírgulas.

## Função `main()`

- **Objetivo:** Ponto de entrada do programa. Interpreta os argumentos da linha de comando e executa as operações especificadas.
- **Implementação:** Lê os dados e, em seguida, processa cada operação passada nos argumentos da linha de comando. Cada operação modifica a seleção atual de dados, e o programa pode executar várias operações em sequência.

## Execução

- **Finalização:** A função `main()` é chamada se o script for executado diretamente. Ela utiliza `sys.argv` para manipular as operações passadas via linha de comando.

Este programa é útil para manipulação e análise de dados em formato CSV, permitindo uma série de operações analíticas básicas.
