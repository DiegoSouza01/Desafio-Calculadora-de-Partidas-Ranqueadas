# Definindo as funções
def calcular_saldo_e_nivel(vitorias, derrotas):
    # Calcular o saldo de vitórias
    saldo_vitorias = vitorias - derrotas
    
    # Determinar o nível do jogador baseado no número de vitórias
    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
    
    return saldo_vitorias, nivel

# Função principal para exibir a mensagem final
def exibir_resultado(vitorias, derrotas):
    saldo_vitorias, nivel = calcular_saldo_e_nivel(vitorias, derrotas)
    print(f"O Herói tem de saldo de {saldo_vitorias} está no nível de {nivel}")

# Simulação de uso da função com entradas fictícias
vitorias = 55
derrotas = 30

exibir_resultado(vitorias, derrotas)

      O Herói tem de saldo de 25 está no nível de Ouro
