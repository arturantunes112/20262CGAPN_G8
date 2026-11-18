# Projeto 3 — Simulador de Repasse do PNAE em Python

> **Versão demonstrativa — matrículas e faixas de porte pendentes de validação; custo alimentar hipotético.**

## Objetivo
Simular o repasse anual federal do PNAE por etapa de ensino e compará-lo ao custo estimado dos gêneros alimentícios de uma refeição diária por estudante.

## Como usar
Instale Python 3 e execute `python simulador_pnae.py` nesta pasta. Os dados do exemplo são constantes no topo do script; para outra escola, substitua matrículas, dias e custo dos alimentos.

## Escola simulada
- **EMEB Vila Quitaúna**, Osasco/SP (referência do exercício).
- Matrículas de **teste**, não verificadas no Censo 2024: creche 60, pré-escola 80, fundamental 50.
- Código INEP, dependência administrativa e situação de funcionamento: **a confirmar**.
- Para validar: consultar os microdados do Censo Escolar 2024, filtrar por nome/código da escola, UF, município, situação e dependência, e extrair matrículas por etapa. Registrar zero para etapas não oferecidas.

## Parâmetros e custo dos alimentos
- Repasse 2026 por aluno/dia: creche R$ 1,57; pré-escola R$ 0,82; fundamental R$ 0,57.
- Fonte oficial a documentar: resolução do FNDE referente aos valores de 2026.
- **R$ 1,57 por refeição é apenas uma hipótese solicitada para o exercício.** Esse número corresponde ao repasse federal de creche/ensino integral de 2026, e NÃO a um custo pesquisado dos ingredientes em São Paulo. Para cumprir o enunciado, ainda é preciso pesquisar o custo dos alimentos por refeição com fonte, link, data e justificativa.

## Resultados ilustrativos (200 dias letivos)
| Indicador | Resultado |
|---|---:|
| Matrículas | 190 |
| Repasse anual | R$ 37.660,00 |
| Custo alimentar hipotético | R$ 59.660,00 |
| Cobertura hipotética | 63,12% |
| Complementação hipotética | R$ 22.000,00 |

O porte **Pequena** reproduz o exemplo da professora, mas os limites da função são provisórios e precisam ser confirmados na aula.

## Resultados e reflexão
No cenário hipotético, o repasse federal não cobre o custo assumido dos ingredientes. Caso não haja complementação estadual ou municipal, a aquisição de gêneros alimentícios pode ser afetada. Não se pode concluir isso sobre a escola real sem validar os dados. A versão final deve discutir os resultados com as leituras indicadas nas orientações (Todos Pela Educação, Observatório da Alimentação Escolar e Brasil de Fato).



## Organização do programa
| Parte | Função | Relação com o Projeto 1 |
|---|---|---|
| Parâmetros | Valores e matrículas | Células de entrada |
| `ler_numero` | Validar inteiro | Validação |
| `classificar_porte` | Classificar escola | Fórmula de porte |
| `calcular_repasse` | Calcular por etapa | Fórmula de repasse |
| `calcular_cobertura` | Custo, cobertura e diferença | Ampliação do simulador |
| Programa principal | Exibir demonstrativo | Tela de simulação |

## Prints
Adicionar capturas reais da execução, após validar os dados e testar a cobertura.

## Uso de Inteligência Artificial
- Ferramenta: ChatGPT (OpenAI).
- Uso: elaboração e organização do código e README, cálculo de cobertura.
- Exemplo de prompt real: "faça o codigo com as informaçoes dessa escola e do preco de alimentos que enviei, e corrija o porte das escolas se estiverm errados".
- Ajustes manuais: **preencher com os ajustes efetivamente realizados pelo grupo**.

## Fonte de Dados
- INEP, Censo Escolar 2024: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar
- FNDE, valores per capita 2026: conferir e registrar link oficial da resolução.
- Referência de custo dos alimentos: **pendente**. R$ 1,57 foi fornecido como valor de repasse, não como preço de refeição.

## Participação do Grupo
- Aprendizados: **preencher após revisão coletiva**.
- Integrantes e contribuições: Artur José,Rogerio Gialuissi e Frederico fizeram o codigo de simulaçaão e o github
- José Ronaldo fez o video e tirou os prints
- valentina e Albert ajudaram no github.


