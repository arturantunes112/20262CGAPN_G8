# Projeto 4 — Painel Interativo do Censo Escolar em Python

## Objetivo
Analisar escolas em atividade de **30 municípios de quatro regiões de São Paulo**, a partir de um recorte do Censo Escolar 2024, por meio de um painel interativo em Python.

## Como executar
Mantenha `painel.py` e `escolas_sp_regioes_2024_geo.csv` na mesma pasta. No terminal, execute:

```bash
python -m pip install pandas streamlit
python -m streamlit run painel.py
```

## Funcionalidades e resultados
O painel permite filtrar **região e município** e atualiza automaticamente indicadores de escolas e matrículas, gráficos de porte, dependência administrativa, água e energia, além do mapa e da tabela de escolas.

O porte é definido no código para visualização: **Pequena** (até 200 matrículas), **Média** (201 a 400) e **Grande** (acima de 400); não é classificação oficial do INEP.

No recorte analisado, a Região Metropolitana de São Paulo apresenta **1.263 escolas e 572.377 matrículas**, enquanto o Vale do Ribeira apresenta **338 escolas e 63.777 matrículas**. Os resultados dizem respeito apenas à base utilizada, não ao estado inteiro.

**Reflexão:** os filtros e gráficos ajudam a comparar as características das escolas entre regiões e municípios. A ausência de coordenadas em algumas unidades pode limitar sua exibição no mapa.

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
