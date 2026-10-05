O projeto tem como objetivo desenvolver um dashboard interativo com dados do Censo Escolar 2024, utilizando o Excel e o Power Query para tratar, organizar e analisar informações sobre as escolas brasileiras.

O painel permite visualizar indicadores educacionais, como tamanho das escolas e condições de infraestrutura, incluindo água, energia, esgoto e coleta de lixo.

Atualizações em relação à versão anterior

A versão inicial do projeto utilizava um recorte dos dados do estado de São Paulo. Na versão atualizada, foi incorporada a base completa do Censo Escolar 2024, abrangendo os municípios de todo o Brasil.

Para garantir o desempenho, foi implementado um filtro dentro do Power Query, utilizando os campos UF e Município em um Inner Join. Dessa forma, a consulta principal é reduzida aos dados do município selecionado pelo grupo antes da criação das tabelas dinâmicas.

Também foram utilizados merges com as tabelas auxiliares de Dependência, Localização, Localização Diferenciada e Situação, além da criação de colunas condicionais para classificar o tamanho das escolas e os indicadores de infraestrutura.

Como usar
Abra a planilha no Microsoft Excel.
Acesse a aba em que estão as células nomeadas UF e Município.
Informe a UF e o município que deseja analisar.
Na guia Dados, clique em Atualizar Tudo.
Aguarde a conclusão da atualização do Power Query e das tabelas dinâmicas.
Acesse a aba do dashboard para visualizar os indicadores, gráficos e segmentações de dados.
Para analisar outro município, altere os valores de UF e Município e clique novamente em Atualizar Tudo.
Disclaimers
Inteligência Artificial

A inteligência artificial foi utilizada como ferramenta de apoio para auxiliar na compreensão das etapas de tratamento de dados, na elaboração de fórmulas e na resolução de dúvidas durante o desenvolvimento. A implementação, revisão e validação do projeto são de responsabilidade dos integrantes do grupo.

Dados

O projeto utiliza dados do Censo Escolar 2024, com finalidade acadêmica e analítica. As informações são tratadas no Power Query e filtradas conforme o município selecionado. As análises e os indicadores apresentados dependem da qualidade e da disponibilidade dos dados da base utilizada.

Participação

O projeto foi desenvolvido coletivamente pelos integrantes do grupo: [Albert Lupu,Artur José,Frederico Costa, José Ronaldo,Rogério Cristovão,Valentina Rosalba].

A importação da base nacional, a construção do pipeline no Power Query, os merges com as tabelas auxiliares, a criação dos indicadores e a elaboração do dashboard foram realizados por José Ronaldo e Rogério

A automação foi testada por meio da alteração dos campos UF e Município, seguida do comando Atualizar Tudo. O grupo verificou se a consulta filtrava corretamente os dados do município selecionado e se as tabelas dinâmicas, os gráficos e o dashboard eram atualizados de acordo com os novos dados. Testado por Artur,Albert,Fred e Valentina
