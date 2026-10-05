. Objetivo

O objetivo deste projeto é desenvolver um painel interativo no Microsoft Excel, utilizando o Power Query para importar, tratar e organizar os dados do Censo Escolar 2024. O dashboard permite analisar informações sobre as escolas de um município selecionado, incluindo tamanho das instituições, dependência administrativa, localização e condições de infraestrutura.

A ferramenta utiliza tabelas dinâmicas, gráficos dinâmicos e segmentações de dados para facilitar a visualização e a análise dos indicadores educacionais.

2. Como usar
Faça o download da planilha disponível neste repositório e abra o arquivo no Microsoft Excel.
Habilite a edição, caso seja solicitado.
Acesse a aba destinada à seleção do município.
Preencha as células nomeadas UF e Município com o estado e o município que deseja analisar.
Na guia Dados, clique em Atualizar Tudo.
Aguarde o Power Query concluir a importação, o tratamento e a filtragem dos dados.
Acesse a aba do dashboard para visualizar os gráficos, as tabelas dinâmicas e os indicadores.
Utilize as segmentações de dados para filtrar as informações e explorar os resultados.
Para analisar outro município, altere os campos UF e Município e clique novamente em Atualizar Tudo.
3. Atualizações em relação à versão anterior

A versão inicial do projeto utilizava um recorte do Censo Escolar 2024 referente ao estado de São Paulo. Nesta versão atualizada, foi incorporada a base nacional completa, abrangendo os municípios de todo o Brasil.

Para possibilitar o processamento eficiente da base completa, foi implementado um filtro diretamente no Power Query, por meio de um Inner Join entre a consulta principal e a tabela de seleção do município, utilizando os campos UF e Município.

Também foram realizados Left Joins com as tabelas auxiliares de Dependência, Localização, Localização Diferenciada e Situação, permitindo complementar as informações das escolas.

Além disso, foram criadas colunas condicionais para classificar o tamanho das escolas e os indicadores de infraestrutura relacionados a água, energia, esgoto e coleta de lixo.

O painel foi configurado para atualizar automaticamente por meio do comando Atualizar Tudo, permitindo que as informações sejam modificadas de acordo com o município selecionado, sem a necessidade de refazer manualmente as tabelas dinâmicas e os gráficos.

4. Disclaimers
4.1. Inteligência Artificial

A inteligência artificial foi utilizada como ferramenta de apoio durante o desenvolvimento do projeto, auxiliando na compreensão dos procedimentos do Power Query, na elaboração de fórmulas, na organização dos dados e na resolução de dúvidas técnicas. As decisões, a implementação, a revisão e a validação do projeto são de responsabilidade dos integrantes do grupo.

4.2. Dados

O projeto utiliza dados do Censo Escolar 2024, disponibilizados pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP). A base foi utilizada para fins acadêmicos, sendo submetida a procedimentos de filtragem, tratamento e organização por meio do Power Query. Os resultados apresentados dependem da qualidade, da consistência e da disponibilidade dos dados originais.

4.3. Participação

O projeto foi desenvolvido coletivamente pelos integrantes do grupo: Albert Lupu,Artur José,Frederico Costa,José Ronaldo,Rogerio, Valentina

As atividades envolveram a importação da base nacional do Censo Escolar 2024, a construção e a configuração das consultas no Power Query, a aplicação dos filtros por UF e Município, a realização dos merges com as tabelas auxiliares, a criação dos indicadores de infraestrutura e tamanho das escolas e a elaboração do dashboard com tabelas dinâmicas, gráficos e segmentações de dados.

A automação foi testada por meio da alteração dos campos UF e Município e da execução do comando Atualizar Tudo. O grupo verificou se os dados eram filtrados corretamente para o município selecionado e se as tabelas dinâmicas, os gráficos e o dashboard eram atualizados conforme a nova seleção.

Integrantes e respectivas contribuições: Fazer o GitHub, Fred,Artur,Albert
PowerQuety Artur,Rogerio,José Ronaldo desenvolveram oa dados
