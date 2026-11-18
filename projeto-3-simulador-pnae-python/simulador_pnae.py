# Projeto 3 — Simulador PNAE (versão demonstrativa)
# Matrículas reais: Censo_2024_Excel.xlsx enviado pelo usuário, Censo 2024.
# Repasse per capita 2026; custo da refeição hipotético, sem pesquisa de preço.
VALOR_CRECHE = 1.57
VALOR_PRE_ESCOLA = 0.82
VALOR_FUNDAMENTAL = 0.57
CUSTO_ALIMENTOS_REFEICAO = 1.57  # HIPÓTESE solicitada: igual ao repasse de creche 2026; NÃO é preço pesquisado
ESCOLA = "EMEF MARIOMA PEREIRA DA SILVA"
CODIGO_INEP = "11050594"
DEPENDENCIA = "Municipal"
SITUACAO = "Em atividade"
MUNICIPIO = "Alta Floresta D'Oeste"
UF = "RO"
DIAS_LETIVOS = 200
MATRICULAS_CRECHE = 0
MATRICULAS_PRE_ESCOLA = 0
MATRICULAS_FUNDAMENTAL = 280

def ler_numero(mensagem):
    while True:
        numero = input(mensagem)
        if numero.isdigit():
            return int(numero)
        print("Você digitou um número incorreto! Digite novamente.")

def classificar_porte(numMatriculas):
    # Limites PROVISÓRIOS: conferir critério da aula.
    if numMatriculas <= 50:
        return "Micro"
    elif numMatriculas <= 200:
        return "Pequena"
    else:
        return "Grande"

def calcular_repasse(matriculas, dias, valorAluno):
    return matriculas * dias * valorAluno

def calcular_cobertura(totalMatriculas, diasLetivos, custoRefeicao, totalRepasse):
    custoAnual = totalMatriculas * diasLetivos * custoRefeicao
    if custoAnual > 0:
        cobertura = totalRepasse / custoAnual * 100
    else:
        cobertura = 0
    if totalRepasse >= custoAnual:
        diferenca = 0
    else:
        diferenca = custoAnual - totalRepasse
    return custoAnual, cobertura, diferenca

print("*** SIMULADOR PNAE — CENSO ESCOLAR 2024 ***")
print("Escola:", ESCOLA)
print("Código INEP:", CODIGO_INEP)
print("Município:", MUNICIPIO, "-", UF)
print("Dependência:", DEPENDENCIA)
print("Situação:", SITUACAO)
print("Dias letivos:", DIAS_LETIVOS)
creche = MATRICULAS_CRECHE
preEscola = MATRICULAS_PRE_ESCOLA
fundamental = MATRICULAS_FUNDAMENTAL
totalMatriculas = creche + preEscola + fundamental
porte = classificar_porte(totalMatriculas)
repasseCreche = calcular_repasse(creche, DIAS_LETIVOS, VALOR_CRECHE)
repassePreEscola = calcular_repasse(preEscola, DIAS_LETIVOS, VALOR_PRE_ESCOLA)
repasseFundamental = calcular_repasse(fundamental, DIAS_LETIVOS, VALOR_FUNDAMENTAL)
totalRepasse = repasseCreche + repassePreEscola + repasseFundamental
custoAnual, cobertura, diferenca = calcular_cobertura(
    totalMatriculas, DIAS_LETIVOS, CUSTO_ALIMENTOS_REFEICAO, totalRepasse
)
print("\n*** MATRÍCULAS E PORTE ***")
print("Creche:", creche)
print("Pré-escola:", preEscola)
print("Fundamental:", fundamental)
print("Total:", totalMatriculas)
print("Porte:", porte, "(critério provisório)")
print("\n*** REPASSE ***")
print(f"Creche: R$ {repasseCreche:.2f}")
print(f"Pré-escola: R$ {repassePreEscola:.2f}")
print(f"Fundamental: R$ {repasseFundamental:.2f}")
print(f"REPASSE TOTAL: R$ {totalRepasse:.2f}")
print("\n*** COBERTURA DOS ALIMENTOS (HIPÓTESE NÃO VALIDADA) ***")
print(f"Custo por refeição: R$ {CUSTO_ALIMENTOS_REFEICAO:.2f}")
print(f"Custo anual: R$ {custoAnual:.2f}")
print(f"Cobertura federal: {cobertura:.2f}%")
print(f"Complementação: R$ {diferenca:.2f}")
if totalRepasse >= custoAnual:
    print("O repasse cobre o custo estimado.")
else:
    print("É necessária complementação de recursos.")
