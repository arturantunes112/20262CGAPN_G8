# Projeto 3 — Simulador de Repasse do PNAE em Python

> **Dados de matrículas verificados na planilha Censo Escolar 2024 enviada pelo grupo.** A estimativa de custo alimentar e as faixas de porte continuam provisórias.

## Objetivo
Simular o repasse anual federal do PNAE por etapa de ensino e compará-lo a uma hipótese de custo dos ingredientes de uma refeição por aluno por dia letivo.

## Como executar
Com Python 3, execute `python simulador_pnae.py` nesta pasta. Os parâmetros e os dados da escola estão no início do arquivo. O programa não precisa de bibliotecas externas.

## Escola escolhida e fonte dos dados
- **Nome:** EMEF Marioma Pereira da Silva
- **Código INEP:** 11050594
- **Município/UF:** Alta Floresta D'Oeste / RO
- **Dependência administrativa:** 3 — Municipal
- **Situação de funcionamento:** 1 — Em atividade
- **Creche:** 0 matrícula
- **Pré-escola:** 0 matrícula
- **Ensino fundamental:** 280 matrículas
- **Total da educação básica:** 280 matrículas
- **Dias letivos usados na simulação:** 200

**Fonte:** planilha `Censo_2024_Excel.xlsx` enviada pelo usuário, aba `Microdados`, registro `CO_ENTIDADE = 11050594`. Campos conferidos: `NO_ENTIDADE`, `CO_ENTIDADE`, `NO_MUNICIPIO`, `SG_UF`, `TP_DEPENDENCIA`, `TP_SITUACAO_FUNCIONAMENTO`, `QT_MAT_BAS`, `QT_MAT_INF` e `QT_MAT_FUND`. Como `QT_MAT_INF = 0`, as matrículas de creche e pré-escola são zero. `QT_MAT_FUND = 280`.

## Parâmetros do simulador
| Parâmetro | Valor |
|---|---:|
| Repasse federal por aluno/dia — creche | R$ 1,57 |
| Repasse federal por aluno/dia — pré-escola | R$ 0,82 |
| Repasse federal por aluno/dia — ensino fundamental | R$ 0,57 |
| Custo **hipotético** dos ingredientes por refeição | R$ 1,57 |
| Refeições por aluno/dia | 1 |
| Dias letivos | 200 |

**Atenção:** R$ 1,57 é um valor de **repasse federal para creche**, não um preço de compra de ingredientes pesquisado em São Paulo ou Rondônia. Ele foi mantido como **hipótese numérica solicitada pelo usuário**. Para satisfazer integralmente a exigência de pesquisa de custo alimentar, ainda é preciso substituir esse parâmetro por um custo documentado de ingredientes, com fonte, data e justificativa. Não incluir mão de obra, gás ou outros custos operacionais nessa estimativa de ingredientes.

## Fórmulas
- Repasse por etapa = matrículas da etapa × dias letivos × repasse por aluno/dia.
- Repasse total = soma dos repasses das etapas.
- Custo anual hipotético = total de matrículas × dias letivos × custo hipotético por refeição.
- Cobertura (%) = repasse total ÷ custo anual hipotético × 100, quando o custo for positivo.
- Complementação = máximo entre zero e (custo anual hipotético − repasse total).

## Resultado com a escola selecionada
| Indicador | Resultado |
|---|---:|
| Matrículas | 280 |
| Porte pelo critério provisório do código | Grande |
| Repasse creche | R$ 0,00 |
| Repasse pré-escola | R$ 0,00 |
| Repasse fundamental | R$ 31.920,00 |
| **Repasse anual total** | **R$ 31.920,00** |
| Custo anual **hipotético** dos ingredientes | R$ 87.920,00 |
| Cobertura **hipotética** do repasse | 36,31% |
| Complementação **hipotética** | R$ 56.000,00 |

O repasse cobre 36,31% do custo **assumido neste cenário**, não necessariamente do custo real da escola. Como as matrículas são de 2024, os valores de repasse são de 2026 e o custo por refeição é hipotético, não se deve interpretar o resultado como uma prestação de contas da escola ou do município.

## Critério de porte
A função `classificar_porte` utiliza provisoriamente: até 50 matrículas = Micro; de 51 a 200 = Pequena; acima de 200 = Grande. **Essas faixas precisam ser confirmadas com a orientação da disciplina** antes da entrega final.

## Organização do código e relação com o Projeto 1
| Parte | Função | Relação com o Projeto 1 |
|---|---|---|
| Parâmetros | Valores, escola e matrículas | Células de entrada |
| `ler_numero` | Validação de inteiros (disponível para entrada interativa) | Validação de dados |
| `classificar_porte` | Classificação do porte | Fórmula condicional |
| `calcular_repasse` | Cálculo do repasse por etapa | Fórmula de repasse |
| `calcular_cobertura` | Custo, cobertura e complementação | Ampliação do simulador |
| Programa principal | Demonstrativo impresso | Tela de resultados |

## Reflexão e limitações
A simulação ilustra como o repasse federal pode ser inferior ao custo de alimentação assumido, exigindo outras fontes de financiamento no cenário. O cálculo é sensível ao custo unitário e ao número de refeições servidas. Para a reflexão final, relacionar os resultados às três leituras exigidas pela disciplina (Todos Pela Educação, Observatório da Alimentação Escolar e Brasil de Fato), após conferência dos textos originais. A simulação abrange apenas creche, pré-escola e fundamental; não modela modalidades adicionais ou diferentes valores por jornada.

## Evidências da execução
O arquivo `resultado_teste.txt` contém um demonstrativo textual. **Ainda é necessário anexar capturas reais do terminal com a execução atualizada**; um arquivo de texto não substitui o print solicitado.

## Declaração de uso de Inteligência Artificial
Ferramenta: ChatGPT (OpenAI). Uso: apoio na elaboração e revisão do código Python, na organização do README, na conferência dos dados da escola na planilha e na atualização dos arquivos do Projeto 3 no GitHub. Solicitações feitas incluíram: “veja os dados das escolas escolha uma e coloque no codigo” e “atualize o que for necessario no github”. Os integrantes devem revisar o resultado e registrar outras utilizações de IA, se houver.

## Declaração de dados
Matrículas e características da escola: planilha `Censo_2024_Excel.xlsx` (Censo Escolar 2024) enviada pelo grupo, com filtro pelo código INEP 11050594. Valores de repasse: parâmetros de 2026 informados no exercício/conversa; verificar a resolução oficial do FNDE na versão final. Custo por refeição: hipótese de R$ 1,57, **sem fonte de preço de ingredientes**, ainda pendente de substituição por referência documental.

## Participação do grupo
- Artur José, Rogerio Gialuissi e Frederico: código de simulação e GitHub.
- José Ronaldo: vídeo e capturas de tela.
- Valentina e Albert: apoio no GitHub.

Os integrantes devem conferir a descrição das contribuições antes da entrega.
