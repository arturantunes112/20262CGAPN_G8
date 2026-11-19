# Projeto 3 — Simulador de Repasse do PNAE em Python

## Objetivo
Simular o repasse federal do Programa Nacional de Alimentação Escolar (PNAE) e compará-lo ao custo estimado dos ingredientes, usando Python e dados de uma escola real.

## Como executar
Com Python 3 instalado, abra o terminal na pasta do projeto e execute:

```bash
python simulador_pnae.py
```

Também é possível executar `python simulador_pnae.py --teste` (exemplo do Projeto 1) ou `python simulador_pnae.py --interativo` (preenchimento manual dos dados).

## Dados e resultados
A escola escolhida foi a **EMEF Marioma Pereira da Silva**, de Alta Floresta D'Oeste (RO), código INEP **11050594**, com **280 matrículas no ensino fundamental** no Censo Escolar 2024. Consideramos 200 dias letivos, repasse de **R$ 0,57 por aluno/dia** no fundamental e custo estimado de **R$ 4,50 por refeição**.

| Indicador | Resultado |
|---|---:|
| Repasse federal anual | R$ 31.920,00 |
| Custo anual estimado dos ingredientes | R$ 252.000,00 |
| Cobertura estimada | 12,67% |
| Diferença estimada | R$ 220.080,00 |

**Reflexão:** o repasse federal cobre apenas parte do custo estimado dos ingredientes, mostrando a importância da complementação de recursos. Trata-se de uma simulação, não dos gastos reais da escola. O programa utiliza matrículas de 2024, valores federais de 2026 e custo de referência de um estudo com dados de 2021.

## Registro da execução
![Execução do simulador](IMG_1799.jpeg)

## Uso de Inteligência Artificial (disclaimer)

**Ferramenta utilizada:** ChatGPT (OpenAI).

**Como foi utilizada:** apoio à revisão e correção do código Python, à organização dos modos de execução e à estruturação e




**Limites:** os dados de matrículas e os valores citados são atribuídos às fontes identificadas abaixo, e não à IA. Os resultados são simulações, não registros de despesa efetiva.

## Fonte de Dados (disclaimer)

As informações da escola e das matrículas vieram do **Censo Escolar 2024 (INEP)**, por meio da planilha `Censo_2024_Excel.xlsx`. Esses dados identificam a unidade escolar, sua localização, sua dependência administrativa, sua situação de funcionamento e o número de matrículas.

- [INEP — Censo Escolar](https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar)
- [FNDE — PNAE e valores de repasse](https://www.gov.br/fnde/pt-br/acesso-a-informacao/acoes-e-programas/programas/pnae) — Resolução CD/FNDE nº 1/2026
- [Artigo sobre o custo de refeições escolares](https://pmc.ncbi.nlm.nih.gov/articles/PMC12448751/) — publicado em 2025, com dados de Morro da Fumaça/SC de 2021

Na planilha do Censo, utilizamos principalmente os campos `CO_ENTIDADE` (código INEP), `NO_ENTIDADE` (nome), `NO_MUNICIPIO` (município), `SG_UF` (estado), `TP_DEPENDENCIA` (rede responsável), `TP_SITUACAO_FUNCIONAMENTO` (situação da escola), `QT_MAT_INF` (matrículas na educação infantil), `QT_MAT_FUND` (matrículas no ensino fundamental) e `QT_MAT_BAS` (matrículas da educação básica).

## Participação do Grupo (disclaimer)

O projeto nos ajudou a praticar a programação em Python e a perceber como dados públicos podem ser utilizados para analisar situações concretas da administração pública. Também aprendemos a organizar os cálculos e a explicar suas limitações.

De acordo com a divisão de tarefas informada:

- **Artur José, Rogerio Gialuissi e Frederico:** desenvolvimento do código e organização do GitHub.
- **José Ronaldo:** vídeo e capturas de tela.
- **Valentina e Albert:** apoio na organização do GitHub.

**Observação:** a divisão de tarefas acima é a registrada na documentação do Projeto 3; o grupo deve validá-la antes da entrega.
