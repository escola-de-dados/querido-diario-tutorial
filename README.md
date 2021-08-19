# Raspe um Diário Oficial e contribua com o Querido Diário

O [Querido Diário](https://queridodiario.ok.org.br/) é um projeto de código aberto da [Open Knowledge Brasil](https://ok.org.br/) que utiliza Python e outras tecnologias para libertar informações do Diário Oficial (DO) das administrações públicas no Brasil. A iniciativa mapeia, baixa e converte todas as páginas das publicações para um formato mais acessível, a fim de facilitar a análise de dados.

Neste tutorial, mostraremos algumas orientações gerais para construir um raspador e contribuir com o projeto Querido Diário. 

## Mapeando os Diários Oficiais
Existem formas de colaborar com o Querido Diário sem precisar programar. Você pode participar de nosso Censo, por exemplo, e ajudar a mapear os Diários Oficiais de todos os municípios brasileiros.

Se você quiser botar a mão na massa e construir seu raspador, pode começar “adotando” uma cidade. Primeiro, encontre uma cidade que ainda não esteja listado no [arquivo CITIES.md do repositório](https://github.com/okfn-brasil/querido-diario/blob/main/CITIES.md). 

O endereço do repositório do projeto é: https://github.com/okfn-brasil/querido-diario/

Para acompanhar o tutorial e construir um raspador, é necessário algum conhecimento sobre:

- Python e o pacote Scrapy
- Git e Github
- HTML,CSS, XPath

### Pareceu grego?

Se você não se sente confortável com estas tecnologias, sugerimos a leitura dos seguintes tutoriais primeiro.

* [Tutorial da documentação do Scrapy](https://docs.scrapy.org/en/latest/intro/tutorial.html)

* [Introdução a XPath para raspagem de dados](https://escoladedados.org/tutoriais/xpath-para-raspagem-de-dados-em-html/)


## Configurando um ambiente de desenvolvimento
Faça um fork do repositório oficial do Querido Diário na sua conta no Github.

Em seguida, clone este novo repositório para seu computador.

Se você usa Windows, baixe as [Ferramentas de Build do Visual Studio](https://visualstudio.microsoft.com/pt-br/downloads/#build-tools-for-visual-studio-2019) e execute o instalador. Durante a instalação, selecione a opção “Desenvolvimento para desktop com C++” e finalize o processo.

Se você usa Linux ou Mac Os, pode simplesmente executar os seguintes comandos. Eles também estão descritos no README do projeto, na parte de configuração de ambiente.

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r data_collection/requirements.txt
pre-commit install
```

Usuários de Windows devem executar os mesmo comandos, apenas trocando o segundo deles por:  `.venv\Scripts\activate.bat`


## Conhecendo os raspadores

Todos os raspadores do projeto ficam na pasta [data_collection/gazette/spiders/](https://github.com/okfn-brasil/querido-diario/tree/main/data_collection/gazette/spiders). Navegue por diferentes arquivos e repare no que há de comum e diferente no código de cada um.

Os nomes de todos os arquivos seguem o padrão: **uf_nomedacidade.py**. 

Ou seja, primeiro, temos a sigla da UF, seguido de underline e nome da cidade. Tudo em minúsculas, sem espaços, acentos ou caracteres especiais.

Veja alguns exemplos paradigmáticos de Diários Oficiais:

* **Paginação**: um bom exemplo de raspador de DO onde as publicações estão separadas em várias páginas é o [script da cidade de Manaus](https://github.com/okfn-brasil/querido-diario/blob/main/data_collection/gazette/spiders/am_manaus.py).

* **Busca de datas**: outra situação comum é quando você precisa preencher um formulário e fazer uma busca de datas para acessar as publicações. É caso por exemplo do script [ba_salvador.py](https://github.com/okfn-brasil/querido-diario/blob/main/data_collection/gazette/spiders/ba_salvador.py), que raspa as informações da capital baiana.

* **Consulta via APIs**: pode ser também que os dados sobre as publicações estejam disponíveis via API, já organizados em um arquivo JSON. É o caso do raspador de [Natal](https://github.com/okfn-brasil/querido-diario/blob/main/data_collection/gazette/spiders/rn_natal.py).

Se você navegou pelos raspadores, talvez tenha reparado que alguns códigos possuem apenas os metadados. Neste caso, tratam-se de municípios que compartilham o mesmo sistema de publicação. Então, tratamos eles conjuntamente, como associações de municípios, ao invés de repetir o mesmo raspador em cada arquivo.

Mas não se preocupe com isso, por ora. Vamos voltar ao nosso exemplo e ver como construir um raspador completo individualmente.





