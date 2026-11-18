# Projeto 3 — Simulador de Repasse do PNAE em Python

## Sobre o projeto

Neste projeto, nosso grupo desenvolveu um simulador em Python para calcular quanto uma escola pública recebe do governo federal por meio do Programa Nacional de Alimentação Escolar (PNAE). A ideia foi continuar o trabalho que começamos no Projeto 1, feito no Excel, mas agora usando funções e cálculos em Python.

Além de calcular o repasse, procuramos responder a outra pergunta: quanto desse dinheiro seria suficiente para pagar os alimentos usados na merenda? Para isso, escolhemos uma escola real do Censo Escolar 2024 e buscamos uma pesquisa sobre o custo dos ingredientes de uma refeição escolar.

## Como executar

É necessário ter o Python 3 instalado. Depois de baixar o arquivo `simulador_pnae.py`, basta abrir o terminal na pasta em que ele está salvo e executar:

```bash
python simulador_pnae.py
```

O programa mostra os dados da escola, as matrículas por etapa, a classificação de porte, o repasse anual, o custo estimado dos alimentos e a porcentagem coberta pelo recurso federal. Nesta versão, os dados da escola já estão definidos no início do código, então não é preciso digitá-los durante a execução. Para testar outra escola, é possível alterar esses valores no próprio arquivo.

## Escola escolhida

Para usar dados reais, consultamos a planilha `Censo_2024_Excel.xlsx`, com os microdados do Censo Escolar 2024. Na aba `Microdados`, procuramos uma escola pública em atividade e identificamos seu registro pelo código INEP (`CO_ENTIDADE`).

A escola escolhida foi a **EMEF Marioma Pereira da Silva**, localizada em **Alta Floresta D'Oeste, Rondônia**, de dependência **municipal**, com código INEP **11050594**. No Censo de 2024, ela aparece como **em atividade**.

| Etapa | Matrículas |
|---|---:|
| Creche | 0 |
| Pré-escola | 0 |
| Ensino fundamental | 280 |
| **Total utilizado no simulador** | **280** |

Para conferir essas informações, usamos os campos `NO_ENTIDADE` (nome da escola), `CO_ENTIDADE` (código INEP), `NO_MUNICIPIO` (município), `SG_UF` (estado), `TP_DEPENDENCIA` (dependência administrativa), `TP_SITUACAO_FUNCIONAMENTO` (situação da escola), `QT_MAT_INF` (educação infantil) e `QT_MAT_FUND` (ensino fundamental). Como a escola não tem matrículas na educação infantil, registramos zero para creche e pré-escola.

## O que o simulador mostra

O programa apresenta as informações da escola e uma estimativa de quanto o repasse federal consegue cobrir dos alimentos da merenda. Também mostra se seria necessário complementar esse valor com outros recursos.

A classificação de porte utilizada no código ainda precisa ser conferida com os critérios apresentados em aula.

## Organização do código e relação com o Projeto 1

No Projeto 1, fizemos esses cálculos com fórmulas e condições no Excel. Agora, organizamos o processo em funções para deixar cada etapa mais clara.

| Função | O que faz | Relação com o Projeto 1 |
|---|---|---|
| `ler_numero` | Verifica se uma entrada digitada é um número inteiro não negativo | Validação de dados |
| `classificar_porte` | Classifica a escola pelo número de matrículas | Condições semelhantes à função SE |
| `calcular_repasse` | Calcula o repasse de cada etapa | Fórmulas de multiplicação |
| `calcular_cobertura` | Calcula o custo anual, a cobertura e a diferença | Amplia o simulador com uma nova análise |

A função `ler_numero` foi mantida como parte da estrutura aprendida em aula, embora a simulação atual trabalhe com matrículas fixadas no início do arquivo.

## O que aprendemos

Ao desenvolver o projeto, percebemos que o repasse federal é apenas uma parte do financiamento da alimentação escolar. A atividade também nos ajudou a entender melhor como utilizar dados públicos em um programa e como organizar as informações para que os resultados sejam apresentados de forma clara.

O simulador é uma simplificação da realidade: considera apenas algumas etapas de ensino e não representa todas as situações de uma escola. Por isso, seus resultados devem ser entendidos como uma estimativa, e não como uma descrição exata dos gastos da unidade escolhida.

## Registro da execução

O arquivo `resultado_teste.txt` registra a execução de teste do simulador. **Ainda falta adicionar um print real do terminal com o programa em execução**, conforme solicitado na atividade.

## Uso de Inteligência Artificial

Utilizamos o **ChatGPT (OpenAI)** como apoio para revisar o código, organizar as informações, melhorar a redação do README e atualizar os arquivos no GitHub. O grupo ainda deve revisar a versão final antes da entrega.

## Participação do grupo

De acordo com a divisão de tarefas informada:
- **Artur José, Rogerio Gialuissi e Frederico:** desenvolvimento do código e organização dos arquivos no GitHub.
- **José Ronaldo:** vídeo e capturas de tela.
- **Valentina e Albert:** apoio na organização do GitHub.

Essa divisão deve ser conferida pelos integrantes antes da entrega.
