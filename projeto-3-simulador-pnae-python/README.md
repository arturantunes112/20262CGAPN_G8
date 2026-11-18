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

## Valores utilizados

Para calcular o repasse, usamos os valores por aluno/dia do PNAE em 2026:

| Etapa | Repasse por aluno/dia |
|---|---:|
| Creche | R$ 1,57 |
| Pré-escola | R$ 0,82 |
| Ensino fundamental | R$ 0,57 |

Fonte: [FNDE — Programa Nacional de Alimentação Escolar](https://www.gov.br/fnde/pt-br/acesso-a-informacao/acoes-e-programas/programas/pnae), Resolução CD/FNDE nº 1/2026.

Esses valores representam o dinheiro transferido pelo governo federal, e não o preço de uma refeição. Por isso, precisávamos de uma segunda informação para fazer a comparação.

### Como chegamos ao custo dos alimentos

Adotamos **R$ 4,50 por refeição** como referência para o custo dos ingredientes. Esse valor aparece como mediana do custo das refeições na Tabela 1 de um [estudo publicado em 2025 na revista *Cadernos de Saúde Pública*](https://pmc.ncbi.nlm.nih.gov/articles/PMC12448751/), que utilizou dados de compras de alimentos de **Morro da Fumaça (SC), em 2021**.

Escolhemos essa referência porque a atividade pede o custo dos **alimentos**, e não o custo total de funcionamento da cozinha, que também envolveria funcionários, gás e equipamentos.

É importante destacar que **R$ 4,50 não é o preço observado na escola de Rondônia**. O estudo é de outro município e usa dados de outro ano. Por isso, o valor serve como referência para uma simulação, mas não permite afirmar quanto essa escola realmente gastou com merenda em 2026. Diferenças no cardápio, nas quantidades servidas e nos preços locais podem mudar bastante o resultado.

## Como os cálculos funcionam

Consideramos **200 dias letivos** e, para estimar o custo dos ingredientes, **uma refeição por aluno por dia**.

O repasse anual é calculado multiplicando as matrículas de cada etapa pelos dias letivos e pelo valor federal correspondente. Depois, somamos os resultados.

Para estimar o gasto com os ingredientes, multiplicamos o total de alunos por 200 dias e pelo custo de R$ 4,50 por refeição. Por fim, dividimos o repasse pelo custo estimado para descobrir a porcentagem coberta e calculamos a diferença.

## Resultados

| Indicador | Resultado |
|---|---:|
| Alunos considerados | 280 |
| Dias letivos | 200 |
| Repasse anual para o ensino fundamental | R$ 31.920,00 |
| **Repasse federal total** | **R$ 31.920,00** |
| Custo anual estimado dos ingredientes | R$ 252.000,00 |
| **Parcela coberta pelo repasse federal** | **12,67%** |
| Diferença estimada a ser coberta por outras fontes | R$ 220.080,00 |

Como a escola escolhida só tem matrículas no ensino fundamental entre as três etapas analisadas, o cálculo do repasse utiliza R$ 0,57 por aluno/dia. Os valores de creche e pré-escola continuam no programa, mas não geram repasse para essa escola porque suas matrículas são zero.

Nesse cenário, o recurso federal cobriria aproximadamente **12,67%** do custo estimado dos ingredientes. Os **R$ 220.080,00** representam uma diferença **simulada**, não uma dívida ou um gasto comprovado da escola.

O programa também classifica a escola como **Grande**, considerando as faixas que usamos no código: Micro (até 50 alunos), Pequena (de 51 a 200) e Grande (acima de 200). **Ainda precisamos confirmar se essas são exatamente as faixas definidas em aula.**

## Organização do código e relação com o Projeto 1

No Projeto 1, fizemos esses cálculos com fórmulas e condições no Excel. Agora, organizamos o processo em funções para deixar cada etapa mais clara.

| Função | O que faz | Relação com o Projeto 1 |
|---|---|---|
| `ler_numero` | Verifica se uma entrada digitada é um número inteiro não negativo | Validação de dados |
| `classificar_porte` | Classifica a escola pelo número de matrículas | Condições semelhantes à função SE |
| `calcular_repasse` | Calcula o repasse de cada etapa | Fórmulas de multiplicação |
| `calcular_cobertura` | Calcula o custo anual, a cobertura e a diferença | Amplia o simulador com uma nova análise |

A função `ler_numero` foi mantida como parte da estrutura aprendida em aula, embora a simulação atual trabalhe com matrículas fixadas no início do arquivo.

## O que aprendemos e quais são os limites da simulação

Ao desenvolver o projeto, percebemos que calcular o repasse do PNAE é relativamente simples, mas entender o que esse dinheiro consegue pagar exige olhar também para o custo dos alimentos. No nosso exemplo, há uma diferença considerável entre o valor federal calculado e o custo estimado dos ingredientes. Isso ajuda a visualizar por que a participação financeira dos estados e municípios é importante para a alimentação escolar.

Ao mesmo tempo, nosso resultado precisa ser interpretado com cuidado. Usamos **matrículas de 2024**, **preços de ingredientes de 2021** e **repasses de 2026**. Além disso, consideramos apenas creche, pré-escola e ensino fundamental, sem calcular separadamente outras modalidades de atendimento. Também supomos uma única refeição por aluno por dia letivo, o que pode não corresponder à rotina de todas as escolas.

As leituras indicadas pela professora — do Todos Pela Educação, do Observatório da Alimentação Escolar e do Brasil de Fato — discutem o financiamento do PNAE e a participação de estados e municípios. Ainda precisamos conferir os textos integralmente para relacionar seus argumentos específicos aos resultados desta simulação, sem atribuir conclusões a essas fontes antes da leitura.

Leituras indicadas:
- [Todos Pela Educação — Nota técnica sobre o financiamento do PNAE (2023)](https://todospelaeducacao.org.br/wordpress/wp-content/uploads/2023/03/nota-pnae-reajuste-nos-valores-do-programa-nacional-de-alimentacao-escolar.pdf)
- [Observatório da Alimentação Escolar — Alimentação escolar e reajuste (2025)](https://alimentacaoescolar.org.br/noticias/2025/10/21/apesar-de-ousadas-novas-metas-ausencia-de-reajuste-ameaca-a-alimentacao-escolar/)
- [Brasil de Fato — Desafios do financiamento da alimentação escolar (2025)](https://www.brasildefato.com.br/podcast/bem-viver/2025/10/16/alimentacao-escolar-brasil-ainda-enfrenta-desafio-do-financiamento-diz-estudo/)

## Registro da execução

O arquivo `resultado_teste.txt` apresenta os resultados da simulação. **Ainda falta adicionar um print real do terminal com o programa em execução**, conforme solicitado na atividade.

## Uso de Inteligência Artificial

Utilizamos o **ChatGPT (OpenAI)** como apoio para revisar o código, conferir os dados da escola na planilha, localizar uma referência para o custo dos ingredientes, organizar os cálculos e melhorar a documentação do projeto. Também usamos a ferramenta para atualizar os arquivos no GitHub.

Entre os pedidos feitos à ferramenta estiveram: “faça o codigo com as informaçoes dessa escola”, “atualize o que for necessario no github” e “atualize o readme da maneira mais humana possivel”.

Os dados da escola foram conferidos na planilha, e os valores e as fontes estão identificados acima. A versão final ainda deve ser revisada pelo grupo, especialmente a classificação de porte e os registros de execução.

## Fonte de dados

- **Censo Escolar 2024 (INEP):** planilha `Censo_2024_Excel.xlsx`, aba `Microdados`, usada para identificar a escola e suas matrículas. [Portal do Censo Escolar — INEP](https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar).
- **FNDE:** valores de repasse do PNAE para 2026. [Página oficial do programa](https://www.gov.br/fnde/pt-br/acesso-a-informacao/acoes-e-programas/programas/pnae).
- **Pesquisa científica:** estudo publicado em *Cadernos de Saúde Pública* em 2025, com dados de Morro da Fumaça/SC de 2021, usado como referência para o custo dos ingredientes. [Acessar o artigo](https://pmc.ncbi.nlm.nih.gov/articles/PMC12448751/).

## Participação do grupo

De acordo com a divisão de tarefas informada:
- **Artur José, Rogerio Gialuissi e Frederico:** desenvolvimento do código e organização dos arquivos no GitHub.
- **José Ronaldo:** vídeo e capturas de tela.
- **Valentina e Albert:** apoio na organização do GitHub.

Essa divisão deve ser conferida pelos integrantes antes da entrega.
