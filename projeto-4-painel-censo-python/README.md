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

Porte: Pequena (até 200 matrículas), Média (201–400) e Grande (mais de 400), conforme código inicial da Aula 21.

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
**Pendente:** adicionar dois prints reais do painel, com combinações diferentes dos filtros (por exemplo, todas as regiões e Vale do Ribeira).

## Uso de Inteligência Artificial
**Ferramenta:** ChatGPT (OpenAI).  
**Uso:** revisão do código da Aula 21, novos filtros e gráficos, organização da documentação.  
**Exemplo de prompt real:** “o que vc precisa para concluirt tudo”.  
**Ajustes manuais:** a equipe deve registrar os ajustes que realmente fizer após testar o painel.

## Fonte de Dados
**Fonte oficial:** Censo Escolar 2024, INEP.  
**Link:** https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar  
**Descrição:** recorte disponibilizado para a disciplina, com escolas em atividade de 30 municípios de quatro regiões de SP, matrículas, características, infraestrutura e coordenadas.  
**Colunas:** `regiao`, `municipio`, `escola`, `matriculas`, `dependencia`, `agua`, `energia`, `latitude`, `longitude`; `porte` é derivada das matrículas.

## Participação do Grupo
**Aprendizado:** filtragem e análise de dados com pandas e criação de dashboard com Streamlit.  
**Integrantes:** Albert, Artur, Frederico, José Ronaldo, Rogério e Valentina.  
**Papel de cada integrante:**
- **Artur:** desenvolvimento dos códigos e elaboração de parte do README.
- **Valentina:** produção dos prints e elaboração do README.
- **Frederico:** apoio no desenvolvimento dos códigos.
- **Rogério, Albert e José Ronaldo:** organização e publicação dos arquivos no GitHub.
