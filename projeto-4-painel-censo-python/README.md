# Projeto 4 — Painel Interativo do Censo Escolar em Python

## Objetivo
Painel interativo com escolas em atividade de 30 municípios de quatro regiões paulistas, baseado no recorte do Censo Escolar 2024. Permite comparar matrículas, características, infraestrutura e localização geográfica.

## Como usar
Coloque `painel.py` e `escolas_sp_regioes_2024_geo.csv` na mesma pasta. Execute:
```bash
python -m pip install pandas streamlit
python -m streamlit run painel.py
```
Escolha a região e o município. Indicadores, gráficos, mapa e lista mudam com os filtros.

## Elementos do painel
| Elemento | Coluna |
| --- | --- |
| Filtros | `regiao`, `municipio` |
| Indicadores | contagem de escolas; soma de `matriculas` |
| Características | `porte` (calculado de `matriculas`), `dependencia` |
| Infraestrutura | `agua`, `energia` |
| Mapa | `latitude`, `longitude` |
| Lista | `regiao`, `municipio`, `escola`, `dependencia`, `matriculas`, `porte` |

**Classificação de porte adotada neste painel:** Pequena (até 200 matrículas), Média (201–400) e Grande (mais de 400). São faixas operacionais definidas no código para fins de visualização; não devem ser interpretadas como classificação oficial do INEP.

## Interpretação dos resultados
Os filtros de região e município são combinados: ao selecionar uma região, a lista de municípios passa a considerar apenas as escolas dessa região. Os indicadores, gráficos, mapa e tabela são recalculados para o subconjunto selecionado. Os gráficos mostram contagens de escolas por porte, dependência administrativa, abastecimento de água e fonte de energia; o mapa mostra somente escolas com coordenadas disponíveis.

## O que o painel mostra
Na base da disciplina, a Região Metropolitana de SP tem 1.263 escolas e 572.377 matrículas; o Vale do Ribeira tem 338 escolas e 63.777 matrículas. O recorte não cobre todo o estado.

## Organização do programa
| Python | Equivalente no Projeto 2 |
| --- | --- |
| `classifica_porte` | coluna calculada |
| `pd.read_csv` | importação da base |
| `st.selectbox` | segmentações |
| `st.metric` | indicadores |
| `st.bar_chart` | gráficos dinâmicos |
| `st.map` | mapa de escolas |
| `st.dataframe` | tabela filtrada |

## Prints do resultado

As capturas abaixo registram a execução do painel em dois momentos, com diferentes seleções de filtros. As imagens estão mantidas com seus nomes originais para preservar os arquivos já enviados ao GitHub.

### Primeira sequência de capturas — visão inicial do painel

**Captura 1**

![Captura do painel 1](<Captura de tela 2026-11-19 101355.png>)

**Captura 2**

![Captura do painel 2](<Captura de tela 2026-11-19 101411.png>)

**Captura 3**

![Captura do painel 3](<Captura de tela 2026-11-19 101438.png>)

**Captura 4**

![Captura do painel 4](<Captura de tela 2026-11-19 101449.png>)

### Segunda sequência de capturas — novo conjunto de filtros

**Captura 5**

![Captura do painel 5](<Captura de tela 2026-11-19 110248.png>)

**Captura 6**

![Captura do painel 6](<Captura de tela 2026-11-19 110320.png>)

**Captura 7**

![Captura do painel 7](<Captura de tela 2026-11-19 110328.png>)

**Captura 8**

![Captura do painel 8](<Captura de tela 2026-11-19 110431.png>)

**Captura 9**

![Captura do painel 9](<Captura de tela 2026-11-19 110439.png>)

**Captura 10**

![Captura do painel 10](<Captura de tela 2026-11-19 110444.png>)


## Uso de Inteligência Artificial (disclaimer)

**Ferramenta utilizada:** ChatGPT (OpenAI).

**Como foi utilizada:** apoio à revisão do código em Python, à organização das funcionalidades do painel e à redação e formatação da documentação do projeto. O uso da ferramenta não substitui a conferência dos resultados nem os testes realizados pelo grupo.

**Exemplo de solicitação feita à IA:** “me dê o passo a passo para fazer o código funcionar”.

**Verificação:** o painel foi executado no Anaconda Prompt e os filtros foram testados; as capturas publicadas documentam diferentes seleções. Os dados não foram gerados pela IA.

## Fonte de Dados (disclaimer)
**Fonte oficial:** Censo Escolar 2024, INEP.  
**Link:** https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar  
**Descrição:** recorte disponibilizado para a disciplina, com escolas em atividade de 30 municípios de quatro regiões de SP, matrículas, características, infraestrutura e coordenadas.  
**Colunas:** `regiao`, `municipio`, `escola`, `matriculas`, `dependencia`, `agua`, `energia`, `latitude`, `longitude`; `porte` é derivada das matrículas.

## Participação do Grupo (disclaimer)
**Aprendizado:** filtragem e análise de dados com pandas e criação de dashboard com Streamlit.  
**Integrantes:** Albert, Artur, Frederico, José Ronaldo, Rogério e Valentina.  
**Papel de cada integrante:**
- **Artur:** desenvolvimento dos códigos e elaboração de parte do README.
- **Valentina:** produção dos prints e elaboração do README.
- **Frederico:** apoio no desenvolvimento dos códigos.
- **Rogério, Albert e José Ronaldo:** organização e publicação dos arquivos no GitHub.
