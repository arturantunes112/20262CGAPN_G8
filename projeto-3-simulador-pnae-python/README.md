# Projeto 3 — Simulador de Repasse do PNAE em Python

## Objetivo
Simular o repasse federal do PNAE por etapa de ensino e comparar o total com o custo estimado dos **ingredientes** de uma refeição por estudante/dia letivo, usando matrículas reais do Censo Escolar 2024 e valores federais de 2026.

## Execução
Instale Python 3 e execute `python simulador_pnae.py` nesta pasta. Não há dependências externas. Os parâmetros estão no topo do script. A função `ler_numero` foi preservada para validação de entradas interativas, embora esta simulação use os dados fixos da escola escolhida.

## Escola escolhida — dados verificados
| Campo | Valor |
|---|---|
| Nome | EMEF Marioma Pereira da Silva |
| INEP | 11050594 |
| Município / UF | Alta Floresta D'Oeste / RO |
| Dependência | 3 — Municipal |
| Situação | 1 — Em atividade |
| Creche | 0 |
| Pré-escola | 0 |
| Ensino fundamental | 280 |
| Total | 280 |

**Fonte dos dados:** arquivo `Censo_2024_Excel.xlsx` enviado pelo grupo, aba **Microdados**, linha com `CO_ENTIDADE = 11050594`. Campos `NO_ENTIDADE`, `NO_MUNICIPIO`, `SG_UF`, `TP_DEPENDENCIA`, `TP_SITUACAO_FUNCIONAMENTO`, `QT_MAT_BAS = 280`, `QT_MAT_INF = 0`, `QT_MAT_FUND = 280`.

## Valores e fontes
**Repasse federal por aluno/dia (2026):**
- Creche: **R$ 1,57**.
- Pré-escola: **R$ 0,82**.
- Ensino fundamental: **R$ 0,57**.

**Fonte oficial:** FNDE, página do PNAE e Resolução CD/FNDE nº 1 de 18/02/2026: https://www.gov.br/fnde/pt-br/acesso-a-informacao/acoes-e-programas/programas/pnae

**Custo de ingredientes de referência:** **R$ 4,50 por refeição**, mediana das **refeições** (não dos lanches), conforme a Tabela 1 do artigo de **Costa et al. (2025), “Custo-efetividade de lanches e refeições na alimentação escolar de um município do Sul do Brasil”**, publicado em *Cadernos de Saúde Pública*. O estudo analisou os ingredientes e os preços pagos pela Prefeitura de **Morro da Fumaça/SC em 2021**, com uma refeição por turno. A estimativa considera custos diretos dos ingredientes, não salários, gás ou outros custos operacionais.

**Fonte científica:** https://pmc.ncbi.nlm.nih.gov/articles/PMC12448751/ (Tabela 1, linha “Custo (R$)”, coluna “Refeições”: mediana **4,5**).

**Justificativa e limites:** essa referência é apropriada para comparar **ingredientes por refeição** com o repasse por aluno/dia, mas não é uma cotação local de Alta Floresta D'Oeste/RO, nem um preço atualizado para 2026. Diferenças de preços, cardápio, porções e período podem alterar o resultado. A simulação usa **uma refeição por aluno/dia** e **200 dias letivos**.

## Fórmulas
- Repasse por etapa = matrículas × dias letivos × valor federal por aluno/dia.
- Repasse total = soma dos repasses por etapa.
- Custo anual de ingredientes = total de matrículas × dias letivos × R$ 4,50.
- Cobertura (%) = repasse total ÷ custo anual × 100.
- Complementação = máximo entre zero e (custo anual − repasse total).

## Resultados da simulação
| Indicador | Resultado |
|---|---:|
| Matrículas | 280 |
| Dias letivos | 200 |
| Porte (critério provisório) | Grande |
| Repasse creche | R$ 0,00 |
| Repasse pré-escola | R$ 0,00 |
| Repasse fundamental | R$ 31.920,00 |
| **Repasse federal total** | **R$ 31.920,00** |
| Custo anual estimado dos ingredientes | R$ 252.000,00 |
| Cobertura estimada | 12,67% |
| Complementação estimada | R$ 220.080,00 |

**Interpretação:** sob a hipótese de custo de R$ 4,50 por refeição, o repasse federal de R$ 0,57 por aluno/dia cobre aproximadamente 12,67% do custo dos ingredientes. A diferença estimada ilustra a necessidade de outras fontes de recursos **neste cenário**. Não se trata de gasto observado, déficit contábil ou prestação de contas da escola em Rondônia.

## Porte da escola
A função `classificar_porte` usa **faixas provisórias**: Micro até 50 matrículas, Pequena de 51 a 200 e Grande acima de 200. **Confirmar essas faixas com a professora**, pois a planilha do Censo não fornece essa classificação diretamente.

## Relação com o Projeto 1
O Projeto 1 utilizava planilhas e fórmulas; o Projeto 3 separa entradas, cálculos e apresentação em Python. `calcular_repasse` substitui a multiplicação da planilha, `classificar_porte` reproduz uma lógica condicional e `calcular_cobertura` amplia a simulação para comparação de custos.

## Reflexão e limitações
O PNAE é uma transferência federal suplementar. A comparação mostra que, sob um custo de ingredientes extraído de pesquisa publicada, o valor transferido por aluno do ensino fundamental não cobriria o custo integral da refeição. A interpretação depende do custo unitário e do número de refeições, que podem variar por escola. Também há diferença temporal entre matrículas de **2024**, preços de ingredientes de **2021** e valores de repasse de **2026**. O código contempla apenas creche, pré-escola e fundamental; não modela atendimento integral, modalidades diferenciadas ou AEE. A reflexão final deve ser relacionada às leituras da disciplina (Todos Pela Educação, Observatório da Alimentação Escolar e Brasil de Fato) depois de conferir os textos indicados.

## Evidências da execução
O arquivo `resultado_teste.txt` registra os resultados calculados. **Ainda é necessário acrescentar capturas reais do terminal** após executar o script atualizado; não são substituídas pelo arquivo de texto.

## Declaração de uso de inteligência artificial
Ferramenta: ChatGPT (OpenAI). Utilizada para apoio na elaboração/revisão do código, escolha e conferência dos dados da escola na planilha, pesquisa da fonte de custo alimentar, redação do README e atualização dos arquivos no GitHub. Exemplos de solicitações: “veja os dados das escolas escolha uma e coloque no codigo”, “atualize o que for necessario no github” e “entao faça o que falta para mim”. O grupo deve revisar e validar as informações antes da entrega.

## Declaração de dados
- Matrículas e identificação da escola: Censo Escolar 2024, planilha `Censo_2024_Excel.xlsx` fornecida pelo grupo.
- Repasses federais: FNDE, Resolução CD/FNDE nº 1/2026 e página oficial do PNAE.
- Custo dos ingredientes: Costa et al. (2025), *Cadernos de Saúde Pública*, dados municipais de 2021, https://pmc.ncbi.nlm.nih.gov/articles/PMC12448751/.

## Participação do grupo
- Artur José, Rogerio Gialuissi e Frederico: código de simulação e GitHub.
- José Ronaldo: vídeo e capturas de tela.
- Valentina e Albert: apoio no GitHub.

As contribuições foram informadas pelo grupo e devem ser conferidas pelos integrantes antes da entrega.
