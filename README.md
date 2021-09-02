# 🕷️📚 Raspe um Diário Oficial e contribua com o Querido Diário

O [Querido Diário](https://queridodiario.ok.org.br/) é um projeto de código aberto da [Open Knowledge Brasil](https://ok.org.br/) que utiliza Python e outras tecnologias para libertar informações do Diário Oficial (DO) das administrações públicas no Brasil. A iniciativa mapeia, baixa e converte todas as páginas das publicações para um formato mais acessível, a fim de facilitar a análise de dados.

Neste tutorial, mostraremos orientações gerais para construir um raspador e contribuir com o projeto Querido Diário.

## 💪 Colabore com o tutorial

Este repositório está em construção. No fim do documento, listamos algumas tarefas ainda pendentes. Você pode ajudar melhorando a documentação fazendo *pull requests* neste repositório.

Se você prefere uma apresentação sobre o projeto em vídeo, confira o workshop [Querido Diário: hoje eu tornei um Diário Oficial acessível](https://escoladedados.org/coda2020/workshop-querido-diario/) da Ana Paula Gomes no [Coda.Br 2020](https://escoladedados.org/coda2020). Ainda que mudanças recentes possam ter alterado detalhes apresentados na oficina, o vídeo é uma ótima complementação a este tutorial. Você pode utilizar a *timestamp* na descrição do vídeo para assistir apenas trechos de seu interesse.

## 🔎 Mapeando e escolhendo Diários Oficiais

Existem formas de colaborar com o Querido Diário sem precisar programar. Você pode participar de nosso [Censo](https://censo.ok.org.br/), por exemplo, e ajudar a mapear os Diários Oficiais de todos os municípios brasileiros.

Se você quiser botar a mão na massa e construir seu raspador, pode começar “adotando” uma cidade. Primeiro, encontre uma cidade que ainda não esteja listada no [arquivo CITIES.md do repositório](https://github.com/okfn-brasil/querido-diario/blob/main/CITIES.md).

O endereço do repositório do projeto é: https://github.com/okfn-brasil/querido-diario/

Antes de começar a trabalhar, vale também dar uma olhada na seção [Issues](https://github.com/okfn-brasil/querido-diario/issues) e [Pull Requests](https://github.com/okfn-brasil/querido-diario/pulls). Assim, você consegue checar se já existe um raspador para a cidade escolhida que ainda não tenha sido incorporado ao projeto (*Pull Requests*) ou se há outras pessoas trabalhando no código para o município (*Issues*).

Se o raspador da sua cidade não consta como feito no [arquivo CITIES.md do repositório](https://github.com/okfn-brasil/querido-diario/blob/main/CITIES.md), não está na seção [Issues](https://github.com/okfn-brasil/querido-diario/issues), nem na aba de [Pull Requests](https://github.com/okfn-brasil/querido-diario/pulls), então, crie uma *Issue* nova para anunciar que você irá trabalhar no raspador da cidade escolhida.

## 💻 Construindo o raspador

Para acompanhar o tutorial e construir um raspador, é necessário instalar e conhecer algo sobre os seguintes softwares:

- Uso do terminal
- [Python](https://www.python.org/) e o pacote Scrapy
- [Git](https://git-scm.com/) e Github
- HTML,CSS, XPath

Se você não se sente confortável com estas tecnologias, sugerimos a leitura dos seguintes tutoriais primeiro.

- [Tutorial da documentação do Scrapy](https://docs.scrapy.org/en/latest/intro/tutorial.html)

- [Introdução a XPath para raspagem de dados](https://escoladedados.org/tutoriais/xpath-para-raspagem-de-dados-em-html/)

- [Git Handbook](https://guides.github.com/introduction/git-handbook/)

## 🌱 Configurando um ambiente de desenvolvimento

[Faça um fork do repositório](https://docs.github.com/pt/github/getting-started-with-github/quickstart/fork-a-repo) do Querido Diário na sua conta no Github.

Em seguida, clone este novo repositório para seu computador e crie uma nova branch para a cidade que irá trabalhar: `git checkout -b <sigladoestado>-<cidade>`

Vejamos um exemplo com a cidade Paulínia em São Paulo: `git checkout -b sp-paulinia`

Se você usa Windows, baixe as [Ferramentas de Build do Visual Studio](https://visualstudio.microsoft.com/pt-br/downloads/#build-tools-for-visual-studio-2019) e execute o instalador. Durante a instalação, selecione a opção “Desenvolvimento para desktop com C++” e finalize o processo.

Se você usa Linux ou Mac Os, pode simplesmente executar os seguintes comandos. Eles também estão descritos no README do projeto, na parte de configuração de ambiente.

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r data_collection/requirements.txt
pre-commit install
```

Usuários de Windows devem executar os mesmo comandos, apenas trocando o segundo deles por:  `.venv\Scripts\activate.bat`

## 🕷 Conhecendo os raspadores

Todos os raspadores do projeto ficam na pasta [data_collection/gazette/spiders/](https://github.com/okfn-brasil/querido-diario/tree/main/data_collection/gazette/spiders). Navegue por diferentes arquivos e repare no que há de comum e diferente no código de cada um.

Os nomes de todos os arquivos seguem o padrão: **uf_nomedacidade.py**.

Ou seja, primeiro, temos a sigla da UF, seguido de underline e nome da cidade. Tudo em minúsculas, sem espaços, acentos ou caracteres especiais.

Existem casos onde diversos municípios usam a mesma plataforma para publicar seus Diários Oficiais. Nestas ocasiões, você irá encontrar um único raspador para todos eles. É o caso, por exemplo, do arquivo [**ba_associacao_municipios.py**](https://github.com/okfn-brasil/querido-diario/blob/main/data_collection/gazette/spiders/ba_associacao_municipios.py).

Para se familiarizar, sugerimos que você navegue por alguns exemplos paradigmáticos de Diários Oficiais:

* **Paginação**: um bom exemplo de raspador de DO onde as publicações estão separadas em várias páginas é o [script da cidade de Manaus](https://github.com/okfn-brasil/querido-diario/blob/main/data_collection/gazette/spiders/am_manaus.py).

* **Busca de datas**: outra situação comum é quando você precisa preencher um formulário e fazer uma busca de datas para acessar as publicações. É caso por exemplo do script [ba_salvador.py](https://github.com/okfn-brasil/querido-diario/blob/main/data_collection/gazette/spiders/ba_salvador.py), que raspa as informações da capital baiana.

* **Consulta via APIs**: pode ser também que ao analisar as requisições do site, você descubra uma API escondida, com dados dos documentos já organizadas em um arquivo JSON, por exemplo. É o caso do raspador de [Natal](https://github.com/okfn-brasil/querido-diario/blob/main/data_collection/gazette/spiders/rn_natal.py).

Se você navegou pelos raspadores, talvez tenha reparado que alguns raspadores praticamente não possuem código e quase se repetem entre si. Neste caso, tratam-se de municípios que compartilham o mesmo sistema de publicação. Então, tratamos eles conjuntamente, como associações de municípios, ao invés de repetir o mesmo raspador em cada arquivo.

Mas não se preocupe com isso, por ora. Vamos voltar ao nosso exemplo e ver como construir um raspador completo para apenas uma cidade.

## 🧠 Anatomia de um raspador

Por padrão, todos os raspadores começam importando alguns pacotes. Vejamos quais são.

`import datetime`: pacote para lidar com datas.

`from gazette.items import Gazette`: item que será salvo com campos que devem/podem ser preenchidos com os metadados dos diários.

`from gazette.spiders.base import BaseGazetteSpider`: é o raspador (spider) base do projeto, que já traz várias funcionalidades úteis.

### Parâmetros inicias

Cada raspador traz uma classe em Python, que executa determinadas rotinas para cada URL de Diários Oficiais. Todas as classes possuem pelo menos as informações básicas abaixo.

`name` = Nome do raspador no mesmo padrão do nome do arquivo, sem a extensão. Exemplo: `sp_paulinia`.

`TERRITORY_ID` = código da cidade no IBGE. Confira a o arquivo [`territories.csv`](https://github.com/okfn-brasil/querido-diario/blob/main/data_collection/gazette/resources/territories.csv) do projeto para descobrir o código da sua cidade. Exemplo: `2905206`.

`allowed_domains` = Domínios nos quais o raspador irá atuar. Exemplo: `["paulinia.sp.gov.br"]`

`start_urls` = URL de início da navegação do raspador. A resposta dessa requisição inicial é encaminhada para a variável response, do método padrão do Scrapy chamado `parse`. Veremos mais sobre isso em breve. Exemplo:`["http://www.paulinia.sp.gov.br/semanarios/"]`

`start_date` = Representação de data no formato ano, mês e dia (YYYY, M, D), usando o pacote `datetime`. É a data inicial da publicação do Diário Oficial no sistema questão, ou seja, a data da primeira publicação disponível online. Encontre esta data pesquisando e inserindo essa data manualmente nesta variável. Exemplo: `datetime.date(2017, 4, 3)`.

### Parâmetros de saída

Além disso, cada raspador também precisa retornar algumas informações por padrão. Isso acontece usando a expressão `yield`.

`date` = A data da publicação em questão. Em nosso código de exemplo, definimos este parâmetro como o dia de hoje, apenas para ter uma versão básica operacional do código. Porém, ao construir um raspador real, neste parâmetro você deverá indicar as datas corretas das publicações.

`file_urls` = Retorna a URL da publicação do DO (um documento pode ter mais de uma URL, mas é raro).

`power` = Aceita os parâmetros `executive` ou `executive_legislative`. Aqui, definimos se o DO tem informações apenas do poder executivo ou também do legislativo. Para definir isso, é preciso olhar manualmente nas publicações se há informações da Câmara Municipal agregadas no mesmo documento, por exemplo.

`is_extra_edition` = Sinalizamos aqui se é uma edição extra do Diário Oficial ou não.

`edition_number` = Número da edição do DO em questão.

Vejamos novamente nosso código de exemplo.

# 👋 Hello world: faça sua primeira requisição

O Scrapy começa fazendo uma requisição para a URL definida no parâmetro `start_urls`. A resposta dessa requisição vai para o método padrão `parse`, que irá armazenar a resposta na variável `response`.

Então, uma forma de fazer um "Hello, world!" no projeto Querido Diário seria com um código como este abaixo. 

```
import datetime
from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider

class SpPauliniaSpider(BaseGazetteSpider):
    name = "sp_paulinia"
    TERRITORY_ID = "2905206"
    start_date = datetime.date(2010, 1, 4)
    allowed_domains = ["paulinia.sp.gov.br"]
    start_urls = ["http://www.paulinia.sp.gov.br/semanarios/"]

    def parse(self, response):
        yield Gazette(
            date=datetime.date.today(),
            file_urls=[response.url],
            power="executive",
        )

```

Ele não baixa nenhum DO de fato, mas dá as bases para você entender como os raspadores operam e por onde começar a desenvolver o seu próprio.

Para testar um raspador e começar a desenvolver o seu, siga as seguintes etapas:

1. Importe o arquivo para a pasta `data_collection/gazette/spiders/` (ou crie um novo) no repositório criado no seu computador a partir do seu fork do Querido Diário.
2. Abra o terminal nesta pasta.
3. Ative o ambiente virtual, caso não tenha feito antes. Rode `source .venv/bin/activate` ou o comando adequado na pasta onde o ambiente foi criado.
4. No terminal, rode o raspador com o comando `scrapy crawl nomedoraspador`. Ou seja, no exemplo rodamos: `scrapy crawl sp_paulinia`.

# 📄 Dissecando o arquivo log

Se tudo deu certo, deve aparecer um arquivo de log enorme terminal.

Ele começa com `[scrapy.utils.log] INFO: Scrapy 2.4.1 started (bot: gazette)` e traz uma série de informações sobre o ambiente inicialmente. Mas a parte que mais nos interessa começa apenas após a linha `[scrapy.core.engine] INFO: Spider opened` e termina na linha `[scrapy.core.engine] INFO: Closing spider (finished)`. Vejamos abaixo.

![](img/output1.png)

A linha `DEBUG: Scraped from <200 http://www.paulinia.sp.gov.br/semanarios/>` nos indica conseguimos acessar o endereço especificado (código 200).

Ao desenvolvedor um raspador, busque principalmente por avisos de *WARNING* e *ERROR*. São eles que trarão as informações mais importantes para você entender os problemas que ocorrem.

Depois de encerrado o raspador, temos a linha a seção do *MONITORS*, que trará um relatório de execução. É normal que apareçam erros, como este abaixo.

![Exemplo de erro do Scrapy](img/scrapy_erro.png)
<!-- Imagem gerada no site carbon.now.sh -->

Basicamente, estamos sendo avisados que nada foi raspado nos últimos dias. Tudo bem, este é apenas um teste inicial para irmos nos familiarizando com o projeto.

# 🛠️ Construindo um raspador de verdade

Aqui, tudo vai depender da forma como cada site é construído. Mas separamos algumas dicas gerais que podem te ajudar.

Primeiro, identifique um seletor que retorne todas as publicações separadamente. Se as publicações estão separadas em várias abas ou várias páginas, primeiro certifique-se de que todas elas seguem o mesmo padrão. Sendo o caso, então, você pode começar fazendo o raspador para a página mais recente e depois repetir as etapas para as demais, por meio de um loop, por exemplo.

Como vimos, a variável `response` nos retorna todo conteúdo da página inicial do nosso raspador. Ela tem vários atributos, como o `text`, que traz todo HTML da página em questão como uma *string*. Mas não temos interesse em todo HTML da página, apenas em informações específicas, então, todo trabalho da raspagem consiste justamenteem separar o joio do trigo, ou seja, utilizar seletores que vão nos permitir filtrar os dados de nosso interesse. Fazemos isso por meio de seletores CSS ou XPath.

## Identificando e testando os seletores

Uma forma fácil para testar os seletores do seu raspador é usando o Scrapy Shell. Experimente rodar por exemplo o comando `scrapy shell "http://www.paulinia.sp.gov.br/semanarios"`. Agora, você pode interagir com a página por meio da linha de comando e deve ver os comandos que temos disponíveis.

![Output do Scrapy Shell](img/scrapy_shell.png)
<!-- Imagem gerada no site carbon.now.sh -->

O elemento mais importante no nosso caso é o `response`. Se o acesso ao site foi feito com êxito, este comando deverá retornar o código 200.

Já o comando `response.css("a")` nos retornaria informações sobre todos os links das página em questão. Também é possível usar o `response.xpath` para identificar os seletores.

O modo mais fácil para de fato identificar os tais seletores que iremos utilizar é por meio do "Inspetor Web". Trata-se de uma função disponível em praticamente todos navegadores navegadores modernos. Basta clicar do lado direito na página e selecionar a opção "Inspecionar". Assim, podemos visualizar o código HTML, copiar e buscar por seletores XPath e CSS.

Experimente rodar o comando `response.xpath("//div[@class='container body-content']//div[@class='row']//a[contains(@href, 'AbreSemanario')]/@href")` e ver os resultados. Este seletor XPath busca primeiro por tags `div` em qualquer lugar da página, que tenha uma classe chamada `container body-content`. Dentro destas tags, buscamos então por outras `div` com a classe `row`. E, em qualquer lugar dentro destas últimas, por fim, buscamos por tags `a` (links) cujo atributo `href` contenha a palavra `AbreSemanario` e pedimos para retornar o valor apenas do atributo `href`. Existem várias formas de escrever seletores para o mesmo objeto. Você pode ter uma ideia de como montar o seletor inspecionando a página que disponibiliza os DOs.

Se você rodar o comando acima, irá ver uma lista de objetos como este: `<Selector xpath="//div[@class='container body-content']//div[@class='row']//a[contains(@href, 'AbreSemanario')]/@href" data='AbreSemanario.aspx?id=1064'>`.

O que realmente nos interessa é aquilo que está dentro do parâmetro `data`, ou seja, o trecho da URL que nos permite acesso a cada publicação. Então, adicione o `extract()` ao fim do comando anterior: `response.xpath("//div[@class='container body-content']//div[@class='row']//a[contains(@href, 'AbreSemanario')]/@href").extract()`.

Se o objetivo fosse selecionar apenas o primeiro item da lista, poderíamos usar o `.extract_first()`.

## Construindo o código do raspador

Após identificar os seletores, é hora de construir seu raspador no arquivo `.py` da pasta `spiders`.

Para ajudar a debugar eventuais problemas na construção do código, você pode inserir a linha `import pdb; pdb.set_trace()` em qualquer trecho do raspador para inspecionar seu código (contexto, variáveis, etc.) durante a execução.

No final do processo, teste seu raspador usando o `scrapy crawl nomedoraspador`.

# Enviando sua contribuição

Ao fazer o commit do código, mencione a issue do raspador da sua cidade. Você pode incluir uma mensagem como `Close #20`, por exemplo. Onde #20 é o número identificador da issue criada. Também adicione uma descrição comentando suas opções na hora de desenvolver o raspador ou eventuais incertezas.

# Tarefas pendentes

- [ ] Melhorar as seções 'Enviando sua contribuição' e 'Construindo o código do raspador'
- [ ] Revisar e incorporar conteúdos faltantes (e atuais) citados no artigo do [Vanz](http://jvanz.com/como-funciona-o-robozinho-do-serenata-que-baixa-os-diarios-oficiais.html).
- [ ] Revisar e incorporar conteúdos faltantes (e atuais) citados no [post](https://www.anapaulagomes.me/pt-br/2020/10/quero-tornar-di%C3%A1rios-oficiais-acess%C3%ADveis.-como-come%C3%A7ar/) feito pela Ana Paula Gomes.
