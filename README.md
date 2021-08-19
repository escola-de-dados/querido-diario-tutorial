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

![image](https://c.tenor.com/tqERWt8lBYEAAAAM/calculating-puzzled.gif)

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

