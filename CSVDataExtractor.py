import sys

def isfloat(s):
    """
    Verifica se a string pode ser convertida para um número de ponto flutuante.
    
    Parâmetros:
    s (str): A string a ser verificada.

    Retorna:
    bool: True se a conversão for possível, False caso contrário.
    """
    try:
        float(s)
        return True
    except ValueError:
        return False

def dados():
    """
    Lê dados da entrada padrão (stdin) e os converte em uma lista de listas.
    Converte elementos numéricos para int ou float conforme apropriado.
    
    Retorna:
    list: Lista de listas com os dados lidos e convertidos.
    """
    dados = []
    for line in sys.stdin:
        linhas = line.strip().split(',')
        for i in range(len(linhas)):
            if linhas[i].isdigit():
                linhas[i] = int(linhas[i])
            elif isfloat(linhas[i]):
                linhas[i] = float(linhas[i])
        dados.append(linhas)
    return dados

def exclui(seleção, intervalo):
    """
    Exclui colunas de uma matriz com base em um intervalo fornecido.
    
    Parâmetros:
    seleção (list): Lista de listas representando a matriz.
    intervalo (str): Intervalo de colunas a serem excluídas, no formato 'início:fim'.

    Retorna:
    list: Nova matriz com as colunas excluídas.
    """
    intervalo_separado = intervalo.split(':')
    comeco = int(intervalo_separado[0])
    final = int(intervalo_separado[1]) if intervalo_separado[1] else len(seleção[0])
    
    matriz_exclusao = []
    for linha in seleção:
        nova_linha = []
        for j in range(len(linha)):
            if j < comeco or j >= final:
                nova_linha.append(linha[j])
        matriz_exclusao.append(nova_linha)
    return matriz_exclusao

def busca(seleção, rotulo, condicao):
    """
    Busca linhas na matriz onde o valor da coluna com o rótulo fornecido satisfaz a condição.
    
    Parâmetros:
    seleção (list): Lista de listas representando a matriz.
    rotulo (str): O rótulo da coluna a ser pesquisada.
    condicao (str): Condição a ser aplicada (e.g., ' > 10').

    Retorna:
    list: Matriz contendo apenas as linhas que atendem à condição.
    """
    indice_rotulo = -1
    for j in range(len(seleção[0])):
        if seleção[0][j] == rotulo:
            indice_rotulo = j
            break
    
    if indice_rotulo == -1:
        return []

    matriz_buscada = [seleção[0]]
    for k in range(1, len(seleção)):
        if eval('seleção[k][indice_rotulo]' + condicao):
            matriz_buscada.append(seleção[k])
    
    return matriz_buscada

def restaura():
    """
    Restaura os dados a partir da entrada padrão (stdin).

    Retorna:
    list: Lista de listas com os dados restaurados.
    """
    return dados()

def conta(seleção):
    """
    Conta o número de linhas na matriz, excluindo o cabeçalho.
    
    Parâmetros:
    seleção (list): Lista de listas representando a matriz.

    Retorna:
    int: Número de linhas excluindo o cabeçalho.
    """
    return len(seleção) - 1

def média(seleção, rotulo):
    """
    Calcula a média dos valores na coluna com o rótulo fornecido.
    
    Parâmetros:
    seleção (list): Lista de listas representando a matriz.
    rotulo (str): O rótulo da coluna para calcular a média.

    Retorna:
    float: Média dos valores da coluna.
    """
    indice_rotulo = -1
    for j in range(len(seleção[0])):
        if seleção[0][j] == rotulo:
            indice_rotulo = j
            break
    
    soma = 0.0
    for k in range(1, len(seleção)):
        soma += seleção[k][indice_rotulo]
    
    return soma / (len(seleção) - 1)

def desviopadrão(seleção, rotulo):
    """
    Calcula o desvio padrão dos valores na coluna com o rótulo fornecido.
    
    Parâmetros:
    seleção (list): Lista de listas representando a matriz.
    rotulo (str): O rótulo da coluna para calcular o desvio padrão.

    Retorna:
    float: Desvio padrão dos valores da coluna.
    """
    indice_rotulo = -1
    for j in range(len(seleção[0])):
        if seleção[0][j] == rotulo:
            indice_rotulo = j
            break
    
    variaveis = []
    for k in range(1, len(seleção)):
        variaveis.append(seleção[k][indice_rotulo])

    N = len(variaveis)
    soma_numeros = sum(variaveis)
    valor_medio = soma_numeros / N
    somatoria_x_xi = sum((x - valor_medio) ** 2 for x in variaveis)
    variacao_populacional = somatoria_x_xi / N
    
    return variacao_populacional ** 0.5

def correlação(seleção, rotulo1, rotulo2):
    """
    Calcula a correlação entre os valores das colunas com os rótulos fornecidos.
    
    Parâmetros:
    seleção (list): Lista de listas representando a matriz.
    rotulo1 (str): O rótulo da primeira coluna.
    rotulo2 (str): O rótulo da segunda coluna.

    Retorna:
    float: Valor da correlação entre as duas colunas.
    """
    indice_rotulo1 = -1
    indice_rotulo2 = -1
    for j in range(len(seleção[0])):
        if seleção[0][j] == rotulo1:
            indice_rotulo1 = j
        if seleção[0][j] == rotulo2:
            indice_rotulo2 = j
    
    variaveisX = []
    variaveisY = []
    for k in range(1, len(seleção)):
        variaveisX.append(seleção[k][indice_rotulo1])
        variaveisY.append(seleção[k][indice_rotulo2])

    N = len(variaveisX)
    xi = sum(variaveisX) / N
    yi = sum(variaveisY) / N

    somatoria_x_y = sum((variaveisX[i] - xi) * (variaveisY[i] - yi) for i in range(N))
    somatoria_x_xi = sum((variaveisX[i] - xi) ** 2 for i in range(N))
    somatoria_y_yi = sum((variaveisY[i] - yi) ** 2 for i in range(N))
    
    resultado_desvioX = somatoria_x_xi ** 0.5
    resultado_desvioY = somatoria_y_yi ** 0.5
    
    return somatoria_x_y / (resultado_desvioX * resultado_desvioY)

def gravacsv(seleção, arquivo):
    """
    Grava a matriz em um arquivo CSV.
    
    Parâmetros:
    seleção (list): Lista de listas representando a matriz.
    arquivo (str): Nome do arquivo CSV onde os dados serão gravados.
    """
    with open(arquivo, 'w') as arquivo_csv:
        for linha in seleção:
            linha_csv = ','.join(str(x) for x in linha)
            arquivo_csv.write(linha_csv + '\n')

def main():
    """
    Função principal que processa comandos e argumentos da linha de comando,
    realiza operações na matriz de dados e exibe resultados.
    """
    dados_lista = dados()
    seleção = [linha[:] for linha in dados_lista]

    i = 1
    while i < len(sys.argv):
        operacao = sys.argv[i]

        if operacao == 'exclui':
            intervalo = sys.argv[i+1]
            if ':' not in intervalo:
                print(f"Intervalo {intervalo} inválido")
                exit()
            comeco, final = intervalo.split(':')
            if not comeco.isdigit() or (final and not final.isdigit()):
                print(f"Intervalo {intervalo} inválido")
                exit()
            comeco = int(comeco)
            final = int(final) if final else len(seleção[0])
            if comeco < 0 or final > len(seleção[0]) or comeco > final:
                print(f"Intervalo {intervalo} inválido")
                exit()
            seleção = exclui(seleção, intervalo)
            i += 2
        
        elif operacao == 'busca':
            if i+2 >= len(sys.argv):
                print("Poucos argumentos na operação busca")
                exit()
            rotulo, condicao = sys.argv[i+1], sys.argv[i+2]
            seleção = busca(seleção, rotulo, condicao)
            if not seleção:
                print(f"Rótulo {rotulo} não encontrado")
                exit()
            i += 3

        elif operacao == 'restaura':
            seleção = restaura()
            i += 1

        elif operacao == 'conta':
            contagem = conta(seleção)
            print(contagem)
            i += 2

        elif operacao == 'média':
            if i+1 >= len(sys.argv):
                print("Poucos argumentos na operação média")
                exit()
            rotulo = sys.argv[i+1]
            if rotulo not in seleção[0]:
                print(f"Rótulo {rotulo} não encontrado")
                exit()
            media = média(seleção, rotulo)
            print(f'{media:.3f}')
            i += 2

        elif operacao == 'desviopadrão':
            if i+1 >= len(sys.argv):
                print("Poucos argumentos na operação desviopadrão")
                exit()
            rotulo = sys.argv[i+1]
            if rotulo not in seleção[0]:
                print(f"Rótulo {rotulo} não encontrado")
                exit()
            desvio = desviopadrão(seleção, rotulo)
            print(f'{desvio:.3f}')
            i += 2

        elif operacao == 'correlação':
            if i+2 >= len(sys.argv):
                print("Poucos argumentos na operação correlação")
                exit()
            rotulo1, rotulo2 = sys.argv[i+1], sys.argv[i+2]
            if rotulo1 not in seleção[0] or rotulo2 not in seleção[0]:
                if rotulo1 not in seleção[0]:
                    print(f"Rótulo {rotulo1} não encontrado")
                if rotulo2 not in seleção[0]:
                    print(f"Rótulo {rotulo2} não encontrado")
                exit()
            correlacao = correlação(seleção, rotulo1, rotulo2)
            print(f'{correlacao:.3f}')
            i += 3

        elif operacao == 'gravacsv':
            if i+1 >= len(sys.argv):
                print("Poucos argumentos na operação gravacsv")
                exit()
            arquivo = sys.argv[i+1]
            gravacsv(seleção, arquivo)
            i += 2
        
        else:
            print(f'Operação "{operacao}" inválida')
            exit()

if __name__ == '__main__':
    main()
