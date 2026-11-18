# PROJETO 3 - SIMULADOR DE REPASSE DO PNAE
# Escola e matrículas: Censo Escolar 2024, planilha Censo_2024_Excel.xlsx,
# aba Microdados, CO_ENTIDADE = 11050594.
# Valores de repasse 2026: FNDE, https://www.gov.br/fnde/pt-br/acesso-a-informacao/acoes-e-programas/programas/pnae
# Custo dos ingredientes: mediana de refeições (R$ 4,50) no estudo
# Costa et al. (2025), Cadernos de Saúde Pública, dados de Morro da Fumaça/SC (2021):
# https://pmc.ncbi.nlm.nih.gov/articles/PMC12448751/
# É uma referência EXTERNA e HISTÓRICA, não o preço observado na escola em RO em 2026.

import sys

VALOR_CRECHE = 1.57
VALOR_PRE_ESCOLA = 0.82
VALOR_FUNDAMENTAL = 0.57
CUSTO_ALIMENTOS_REFEICAO = 4.50

ESCOLA = "EMEF MARIOMA PEREIRA DA SILVA"
CODIGO_INEP = "11050594"
MUNICIPIO = "Alta Floresta D'Oeste"
UF = "RO"
DEPENDENCIA = "Municipal"
SITUACAO = "Em atividade"
DIAS_LETIVOS = 200
MATRICULAS_CRECHE = 0
MATRICULAS_PRE_ESCOLA = 0
MATRICULAS_FUNDAMENTAL = 280


def ler_numero(mensagem):
    while True:
        numero = input(mensagem)
        if numero.isdigit():
            return int(numero)
        print("Número inválido! Digite novamente.")


def classificar_porte(numMatriculas):
    # Critério PROVISÓRIO: confirmar faixas com a professora.
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


# Sem argumentos: roda a escola real do Censo e preserva o print do projeto.
# --teste: reproduz o exemplo do Projeto 1 (190 alunos, R$ 37.660,00).
# --interativo: permite informar uma escola e suas matrículas pelo terminal.
# Argumentos internos do Jupyter (ex.: -f) são ignorados.
if len(sys.argv) > 1 and sys.argv[1] in ("--teste", "--interativo"):
    modo = sys.argv[1]
    if modo == "--teste":
        ESCOLA = "EMEB Vila Quitaúna (escola de teste)"
        CODIGO_INEP = "Não se aplica ao teste"
        MUNICIPIO = "Osasco"
        UF = "SP"
        DEPENDENCIA = "Municipal (exemplo didático)"
        SITUACAO = "Dados fictícios de teste"
        MATRICULAS_CRECHE = 60
        MATRICULAS_PRE_ESCOLA = 80
        MATRICULAS_FUNDAMENTAL = 50
    elif modo == "--interativo":
        print("*** PREENCHIMENTO DOS DADOS DA ESCOLA ***")
        ESCOLA = input("Nome da escola: ")
        CODIGO_INEP = input("Código INEP (se souber): ")
        MUNICIPIO = input("Município: ")
        UF = input("UF: ")
        DEPENDENCIA = input("Dependência administrativa: ")
        SITUACAO = input("Situação de funcionamento: ")
        DIAS_LETIVOS = ler_numero("Dias letivos: ")
        MATRICULAS_CRECHE = ler_numero("Matrículas de creche: ")
        MATRICULAS_PRE_ESCOLA = ler_numero("Matrículas de pré-escola: ")
        MATRICULAS_FUNDAMENTAL = ler_numero("Matrículas de ensino fundamental: ")

print("*** SIMULADOR PNAE - CENSO ESCOLAR 2024 ***")
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

print("\n*** REPASSE FEDERAL PNAE 2026 ***")
print(f"Creche: R$ {repasseCreche:.2f}")
print(f"Pré-escola: R$ {repassePreEscola:.2f}")
print(f"Fundamental: R$ {repasseFundamental:.2f}")
print(f"REPASSE TOTAL: R$ {totalRepasse:.2f}")

print("\n*** COBERTURA DO CUSTO DOS INGREDIENTES ***")
print("Referência: Morro da Fumaça/SC, preços de 2021 (Costa et al., 2025)")
print(f"Custo por refeição (referência externa): R$ {CUSTO_ALIMENTOS_REFEICAO:.2f}")
print(f"Custo anual estimado: R$ {custoAnual:.2f}")
print(f"Cobertura federal estimada: {cobertura:.2f}%")
print(f"Complementação estimada: R$ {diferenca:.2f}")
if totalRepasse >= custoAnual:
    print("O repasse cobre o custo estimado dos ingredientes.")
else:
    print("O repasse não cobre todo o custo estimado dos ingredientes.")
    print("É necessária complementação de recursos neste cenário.")
print("\n*** FIM DA SIMULAÇÃO ***")
