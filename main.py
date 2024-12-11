import math

# Função principal
def main():
    print("Bem-vindo(a) ao Programa - Agrupamento Discreto em Estatística.")
    
    # Solicitação de unidade de medida
    unidade_medida = input("Por favor, informe a unidade de medida para os dados a serem inseridos: \n")
    print("\n")
    print("Ok. A seguir vamos aos dados. Se você inserir algum dado errado, não se preocupe.")
    print("No Final, você poderá corrigir aquele dado específico.")
    # Solicitação dos dados com opção de corrigir entradas erradas
    print("\nAtenção: Por favor, insira apenas números válidos.\n")
    dados = []
    while True:
        dado = input(f"Por favor, insira o dado {len(dados) + 1}: ")
        
        # Validação de entrada
        try:
            dado = float(dado)
            dados.append(dado)
        except ValueError:
            print("Erro! Por favor, insira um número válido.")
            resposta = input("\nDeseja apagar o último dado inserido? (s/n): ")
            if resposta.lower() == 's':
                if dados:
                    dados.pop()
                print("Último dado apagado.")
            elif resposta.lower() != 'n':
                print("\nResposta inválida! Por favor, digite 's' para sim ou 'n' para não.")
            continue
        
        # Pergunta sobre término da inserção
        continuar = input("Deseja inserir mais dados? (s/n): ")
        if continuar.lower() == 'n':
            break
    
    # Permitir correção de erros após a inserção completa
    while True:
        erro = input("Você percebeu algum erro nos dados inseridos? (s/n): ")
        if erro.lower() == 's':
            try:
                indice = int(input("Qual dado está errado? (Digite o número do dado ou 0 para cancelar): "))
                if indice == 0:
                    break
                elif 1 <= indice <= len(dados):
                    novo_valor = float(input(f"Por favor, insira o valor correto para o dado {indice}: "))
                    dados[indice - 1] = novo_valor
                else:
                    print("Índice fora do intervalo.")
            except ValueError:
                print("Por favor, insira um número válido.")
        elif erro.lower() == 'n':
            break
    
    # Cálculo da quantidade de dados e organização em ordem crescente
    quantidade_dados = len(dados)
    print(f"Quantidade de dados inseridos: {quantidade_dados}.")
    dados.sort()
    print("Dados organizados em ordem crescente:", dados)
    
    input("\n\nPodemos prosseguir? (Pressione Enter para continuar)")
    
    # Cálculo das frequências
    freq_absoluta = {}
    for valor in dados:
        freq_absoluta[valor] = freq_absoluta.get(valor, 0) + 1
    
    # Tabela de frequências
    xi = list(freq_absoluta.keys())
    fi = list(freq_absoluta.values())
    fac = [sum(fi[:i+1]) for i in range(len(fi))]
    fr = [f / quantidade_dados * 100 for f in fi]
    frac = [sum(fr[:i+1]) for i in range(len(fr))]
    
    print("\nTabela de Frequências:")
    print("Xi\tFi\tFac\tFr (%)\tFrac (%)")
    for i in range(len(xi)):
        print(f"{xi[i]}\t{fi[i]}\t{fac[i]}\t{fr[i]:.2f}%\t{frac[i]:.2f}%")
    
    print("\nComo calculamos as frequências:")
    print("- **Frequência Absoluta (Fi)**: Número de vezes que cada valor aparece no conjunto de dados.")
    print("- **Frequência Acumulada (Fac)**: Soma das frequências absolutas até o valor atual.")
    print("- **Frequência Relativa (Fr)**: Proporção de cada valor no total de dados. Fr = Fi / N * 100")
    print("- **Frequência Relativa Acumulada (Frac)**: Soma acumulada das frequências relativas.")
    
    input("\n\nPodemos prosseguir? (Pressione Enter para continuar)")
    
    # Cálculo das medidas de posição central
    media = sum(dados) / quantidade_dados
    if quantidade_dados % 2 == 0:
        mediana = (dados[quantidade_dados // 2 - 1] + dados[quantidade_dados // 2]) / 2
    else:
        mediana = dados[quantidade_dados // 2]
    moda = max(set(dados), key=dados.count)
    
    print("\nMedidas de Posição Central:")
    print(f"Média (x̅): {media}")
    print(f"Mediana (μ): {mediana}")
    print(f"Moda (Mo): {moda}")
    print("A unidade de medida será mostrada no final.")
    
    print("\nComo calculamos as medidas de posição central:")
    print("Lembre-se que você pode utilizar a tecnica de arredondamento.")
    print("- **Média (x̅)**: Soma de todos os dados dividida pelo número total de dados.")
    print("- **Mediana (μ)**: Valor central dos dados ordenados. Se o número de dados for ímpar,\n é o valor do meio; se for par, é a média dos dois valores centrais.")
    print("- **Moda (Mo)**: O valor mais frequente nos dados. Pode ser amodal, unimodal, bimodal ou multimodal.")
    
    input("\n\nPodemos prosseguir? (Pressione Enter para continuar)")
    
    # Cálculo das medidas de dispersão (Variância e Desvio Padrão)
    variancia = sum(fi[i] * ((xi[i] - media) ** 2) for i in range(len(xi))) / (quantidade_dados - 1)
    desvio_padrao = math.sqrt(variancia)
    coef_variacao = (desvio_padrao / media) * 100
    
    print("\nMedidas de Dispersão:")
    print(f"Variância (s²): {variancia:.2f}")
    print(f"Desvio Padrão (s): {desvio_padrao:.2f}")
    print(f"Coeficiente de Variação (CV): {coef_variacao:.2f}%")
    print("A unidade de medida será mostrada no final.")
    
    print("\nComo calculamos as medidas de dispersão:")
    print("- **Variância (s²)**: Média das diferenças quadráticas entre cada valor e a média. Fórmula: s² = Σ[Fi * (Xi - x̅)²] / (N - 1)")
    print("- **Desvio Padrão (s)**: Raiz quadrada da variância, indica o quanto os dados se dispersam em relação à média.")
    print("- **Coeficiente de Variação (CV)**: Expressa a variabilidade relativa em relação à média. Fórmula: CV = (s / x̅) * 100")
    
    # Exibição dos resultados finais com a unidade de medida
    print("\n\nResultados Finais:")
    print(f"Unidade de medida: {unidade_medida}")
    print("\n\nTabela de Frequências:")
    print("Xi\tFi\tFac\tFr (%)\tFrac (%)")
    for i in range(len(xi)):
        print(f"{xi[i]}\t{fi[i]}\t{fac[i]}\t{fr[i]:.2f}%\t{frac[i]:.2f}%")
    
    print("\n\nMedidas de Posição Central:")
    print(f"Média (x̅): {media} {unidade_medida}")
    print(f"Mediana (μ): {mediana} {unidade_medida}")
    print(f"Moda (Mo): {moda} {unidade_medida}")
    
    print("\n\nMedidas de Dispersão:")
    print(f"Variância (s²): {variancia:.2f} {unidade_medida}²")
    print(f"Desvio Padrão (s): {desvio_padrao:.2f} {unidade_medida}")
    print(f"Coeficiente de Variação (CV): {coef_variacao:.2f}%")
    
    # Opção de reiniciar
    reiniciar = input("Gostaria de realizar uma nova análise? (s/n): ")
    if reiniciar.lower() == 's':
        main()
    else:
        print("Encerrando o programa. Obrigado por utilizar o Programa - Agrupamento Discreto em Estatística.")

# Chamada do programa
main()
