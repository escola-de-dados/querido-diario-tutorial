[Português (BR)](README.md)

# Raspe um Diário Oficial e contribua com o Querido Diário 🕷️📚

[Querido Diário](https://queridodiario.ok.org.br/) is an open-source project by “Open Knowledge Brasil” [Open Knowledge Brasil](https://ok.org.br/) that uses Python and other technologies to liberate information from the Official Gazette (DO) of public administrations in Brazil.  The initiative maps, downloads, and converts all pages of the publications into a more accessible format to facilitate data analysis.

In this tutorial, we will provide general guidelines for building a scraper and contributing to “Querido Diário” project.

If you prefer a video presentation about the project, feel free to check out the workshop [Querido Diário: hoje eu tornei um Diário Oficial acessível](https://escoladedados.org/coda2020/workshop-querido-diario/) taught by Ana Paula Gomes at [Coda.Br 2020](https://escoladedados.org/coda2020). Even though recent changes may have altered details presented in the workshop, the video is an excellent complement to this tutorial. You can use the *timestamp* in the video description to watch only the parts that interest you.

## Sumário 📑
  1. [Collaborate in this tutorial](#collaborate-in-this-tutorial-)
  2. [Mapping and Choosing Official Gazettes](#mapping-and-choosing-official-gazettes-)
  3. [Building a scraper](#building-a-scraper-)
  4. [Setting up a development environment](#setting-up-a-development-environment-)
  5. [Getting to know the scrapers](#getting-to-know-the-scrapers-)
      1. [Specific cases](#casos-particulares)
  6. [Anatomy of a scraper](#anatomia-de-um-raspador-)
      1. [Initial parameters](#parametros-iniciais)
      2. [Output parameters](#parametros-de-saida)
  7. [Hello world: make your first request](#hello-world-faca-sua-primeira-requisicao-)
  8. [Dissecting the log](#dissecando-o-log-)
  9. [Building a real scraper](#construindo-um-raspador-de-verdade-)
      1. [Identifying and testing selectors](#identificando-e-testando-os-seletores)
      2. [Writing the scraper code](#construindo-o-codigo-do-raspador)
      3. [Hints to test a scraper](#dcas-para-testar-o-raspador)
  10. [Sending your contribution](#enviando-sua-contribuicao-)

## Collaborate in this tutorial 💪

This document is constantly under construction. You can help improve this documentation by making *pull requests* to this repository.

## Mapping and Choosing Official Gazettess 🔎

There are ways to collaborate with Querido Diário without having to program. You can participate in the [Census](https://censo.ok.org.br/), for example, and help map the Official Gazettes of all Brazilian municipalities.

If you want to get your hands dirty and build your scraper, you can start by “adopting” a city. First, find a city that is not already listed in the [repository CITIES.md file](https://github.com/okfn-brasil/querido-diario/blob/main/CITIES.md).

The project repository address is: https://github.com/okfn-brasil/querido-diario/

Before starting work, it's also worth taking a look at the [Issues](https://github.com/okfn-brasil/querido-diario/issues) and [Pull Requests](https://github.com/okfn/querido-diario/pulls). This way, you can check if there is already a scraper for the chosen city that has not yet been incorporated into the project (*Pull Requests*) or if there are other people working on the code for the municipality (*Issues*).

If your city's scraper does not appear as done in the [CITIES.md file in the repository](https://github.com/okfn-brasil/querido-diario/blob/main/CITIES.md), it is not in the section [ Issues](https://github.com/okfn-brasil/querido-diario/issues), nor in the [Pull requests](https://github.com/okfn-brasil/querido-diario/pulls) tab, So, create a new *Issue* to announce that you will work at the scraper in the chosen city.

## Building a scraper 💻

To follow this tutorial and build a scraper, you need to install and know something about the following softwares:

- Use of the terminal
- [Python](https://www.python.org/) and the Scrapy package
- [Git](https://git-scm.com/) and Github
- HTML, CSS, XPath

If you are not comfortable with these technologies, we suggest the following materials:

- [Python for zombies](https://www.youtube.com/watch?v=YO58tXerKDc&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc)

- [Scrapy Documentation Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)

- [Introduction to XPath for data scraping](https://escoladedados.org/tutoriais/xpath-para-raspagem-de-dados-em-html/)

- [Git Handbook](https://guides.github.com/introduction/git-handbook/)

## Configurando um ambiente de desenvolvimento 🌱

[Fork the Querido Diario repository](https://docs.github.com/pt/github/getting-started-with-github/quickstart/fork-a-repo) in your Github account.

Then, clone this new repository to your computer and create a new branch for the city you will work on:

```sh
git checkout -b <state acronym>-<city>
```

Let's look at an example with the city Paulínia in São Paulo:

```sh
git checkout -b sp-paulinia
```

If you use Windows, download [Visual Studio Build Tools](https://visualstudio.microsoft.com/pt-br/downloads/#build-tools-for-visual-studio-2019) and run the installer. During installation, select the “Desktop development with C++” option and complete the process.

If you use Linux or Mac Os, you can simply run the following commands. They are also described in the project's README, in the environment configuration part.

```py
python3 -m venv .venv
source .venv/bin/activate
pip install -r data_collection/requirements.txt
pre-commit install
```

Windows users must execute the same commands, just replacing the `source .venv/bin/activate` with `.venv\Scripts\activate.bat`.

## Getting to know the scrapers 🕷

All project scrapers are located in the folder [data_collection/gazette/spiders/](https://github.com/okfn-brasil/querido-diario/tree/main/data_collection/gazette/spiders). Browse different files and notice what's common and different in each one's code.

The names of all files follow the pattern: **uf_nome_da_cidade.py**.

In other words, first, we have the UF acronym (federative unit, Unidade Federativa in portuguese), followed by _underscore_ and the name of the city. All in lowercase, without spaces, accents or special characters and separating words with _underscore_.

To familiarize yourself, we suggest you browse some paradigmatic examples of Official Gazettes:

* **Pagination**: a good example of a scraper where publications are separated into several pages is [from the city of Manaus](https://github.com/okfn-brasil/querido-diario/blob/main/data_collection /gazette/spiders/am_manaus.py).

* **Data search**: another common situation is when you need to fill out a form and search for data to access publications. This is the case, for example, of the script [ba_salvador.py](https://github.com/okfn-brasil/querido-diario/blob/main/data_collection/gazette/spiders/ba_salvador.py), which scrapes information from Bahia's capital.

* **Query via APIs**: also when analyzing the website's requests, you discover a hidden API, with document data already organized in a JSON file, for example. This is the case with the [Natal] scraper(https://github.com/okfn-brasil/querido-diario/blob/main/data_collection/gazette/spiders/rn_natal.py). At Escola de Dados, you can find a webinar about [data scraping through "hidden APIs"](https://escoladedados.org/2021/05/como-descobrir-apis-escondidas-para-facilitar-a- data-scraping/), which can be useful for those just starting out.

### Specific cases

You may have noticed that some scrapers have practically no code and almost repeat themselves. In this case, these are municipalities that share the same publication system. So, we treat them together, modifying only what is necessary from scraper to scraper, instead of repeating the same code in each file. This is the case, for example, of cities in Santa Catarina such as [**Abdon Batista**](https://github.com/okfn-brasil/querido-diario/blob/main/data_collection/gazette/spiders/sc_abdon_batista. py) and [**Agrolândia**](https://github.com/okfn-brasil/querido-diario/blob/main/data_collection/gazette/spiders/sc_agrolandia.py).

There are scrapers that do not have a city name because several municipalities use the same platform to publish their Official Gazettes. They are usually municipal association websites. This is the case of [**ba_associacao_municipios.py**](https://github.com/okfn-brasil/querido-diario/blob/main/data_collection/gazette/spiders/ba_associacao_municipios.py).

But for a first contribution, don't worry about these particular cases. Let's go back to our example and see how to build a complete scraper for just one city.

## Anatomy of a scraper 🧠

Por padrão, todos os raspadores começam importando alguns pacotes. Vejamos quais são:

* `import datetime`: pacote para lidar com datas.
* `from gazette.items import Gazette`: Chamamos de `Gazette` os arquivo de DOs encontrados pelos raspadores, ele irá armazenar também campos de metadados para cada publicação. 
* `from gazette.spiders.base import BaseGazetteSpider`: é o raspador (spider) base do projeto, que já traz algumas funcionalidades úteis.

### Parâmetros iniciais

Cada raspador traz uma [classe em Python](https://www.youtube.com/watch?v=52ns4X7Ny6k&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=41), que executa determinadas rotinas para cada página dos sites que publicam Diários Oficiais. Todas as classes possuem pelo menos as informações básicas abaixo:

* `name`: Nome do raspador no mesmo padrão do nome do arquivo, sem a extensão. Exemplo: `sp_paulinia`.
* `TERRITORY_ID`: código da cidade no IBGE. Confira a o arquivo [`territories.csv`](https://github.com/okfn-brasil/querido-diario/blob/main/data_collection/gazette/resources/territories.csv) do projeto para descobrir o código da sua cidade. Exemplo: `2905206`.
* `allowed_domains`: Domínios nos quais o raspador irá atuar. Tenha atenção aos colchetes. Eles indicam que se trata de uma lista, ainda que tenha apenas um elemento. Exemplo: `["paulinia.sp.gov.br"]`
* `start_urls`: lista com URLs de início da navegação do raspador (normalmente apenas uma). A resposta dessa requisição inicial é encaminhada para a variável `response`, do método padrão do Scrapy chamado `parse`. Veremos mais sobre isso em breve. Novamente, atenção aos colchetes. Exemplo:`["http://www.paulinia.sp.gov.br/semanarios/"]`
* `start_date`: Representação de data no formato ano, mês e dia (YYYY, M, D) com `datetime.date`. É a data inicial da publicação do Diário Oficial no sistema questão, ou seja, a data da primeira publicação disponível online. Encontre esta data pesquisando e a insira manualmente nesta variável. Exemplo: `datetime.date(2017, 4, 3)`.

### Parâmetros de saída

Além disso, cada raspador também precisa retornar algumas informações por padrão. Isso acontece usando a expressão `yield` nos itens criados do tipo `Gazette`.

* `date`: A data da publicação do diário. 
* `file_urls`: Retorna as URLs da publicação do DO como uma lista. Um documento pode ter mais de uma URL, mas não é algo comum.
* `power`: Aceita os parâmetros `executive` ou `executive_legislative`. Aqui, definimos se o DO tem informações apenas do poder executivo ou também do legislativo. Para definir isso, é preciso olhar manualmente nas publicações se há informações da Câmara Municipal agregadas no mesmo documento, por exemplo.
* `is_extra_edition`: Sinalizamos aqui se é uma edição extra do Diário Oficial ou não. Edições extras são edições completas do diário que são publicadas fora do calendário previsto.
* `edition_number`: Número da edição do DO em questão.

Vejamos agora nosso código de exemplo.

## Hello world: faça sua primeira requisição 👋

O Scrapy começa fazendo uma requisição para a URL definida no parâmetro `start_urls`. A resposta dessa requisição vai para o método padrão `parse`, que irá armazenar a resposta na variável `response`.

Então, uma forma de fazer um "Hello, world!" no projeto Querido Diário seria com um código como este abaixo.

```python
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

O código baixa o HTML da URL inicial, mas não descarrega nenhum DO de fato. Definimos este parâmetro como o dia de hoje, apenas para ter uma versão básica operacional do código. Porém, ao construir um raspador real, neste parâmetro você deverá indicar as datas corretas das publicações.

De todo modo, isso dá as bases para você entender como os raspadores operam e por onde começar a desenvolver o seu próprio.

Para rodar o código, você pode seguir as seguintes etapas:

1. Crie um arquivo na pasta `data_collection/gazette/spiders/` do repositório criado no seu computador a partir do seu fork do Querido Diário;
2. Abra o terminal na raíz do projeto;
3. Ative o ambiente virtual, caso não tenha feito antes, como indicado na seção _"[Configurando um ambiente de desenvolvimento](#configurando-um-ambiente-de-desenvolvimento)"_ (`source .venv/bin/activate`, por exemplo);
4. No terminal, vá para a pasta `data_collection`;
5. No terminal, rode o raspador com o comando `scrapy crawl nome_do_raspador` (nome que está no atributo `name` da classe do raspador). Ou seja, no exemplo rodamos: `scrapy crawl sp_paulinia`.

## Dissecando o log 📄

Se tudo deu certo, deve aparecer um log enorme terminal.

Ele começa com algo como `[scrapy.utils.log] INFO: Scrapy 2.4.1 started (bot: gazette)` e traz uma série de informações sobre o ambiente inicialmente. Mas a parte que mais nos interessa começa apenas após a linha `[scrapy.core.engine] INFO: Spider opened` e termina na linha `[scrapy.core.engine] INFO: Closing spider (finished)`. Vejamos abaixo.

![](img/output1.png)

A linha `DEBUG: Scraped from <200 http://www.paulinia.sp.gov.br/semanarios/>` nos indica conseguimos acessar o endereço especificado (código 200).

Ao desenvolver um raspador, busque principalmente por avisos de *WARNING* e *ERROR*. São eles que trarão as informações mais importantes para você entender os problemas que ocorrem.

Depois de encerrado o raspador, temos as linhas da seção dos *monitors*, que trará um relatório de execução. É normal que apareçam erros, como este abaixo.

![Exemplo de erro do Scrapy](img/scrapy_erro.png)
<!-- Imagem gerada no site carbon.now.sh -->

É um aviso que nada foi raspado nos últimos dias. Tudo bem, este é apenas um teste inicial para irmos nos familiarizando com o projeto.

## Construindo um raspador de verdade 🛠️

Aqui, tudo vai depender da forma como cada site é construído. Mas separamos algumas dicas gerais que podem te ajudar.

Primeiro, navegue pelo site para entender a forma como os DOs estão disponibilizados. Busque encontrar um padrão consistente e pouco sucetível a mudanças ocasionais para o robô extrair as informações necessárias. Por exemplo, se as publicações estão separadas em várias abas ou várias páginas, primeiro certifique-se de que todas elas seguem o mesmo padrão. Sendo o caso, então, você pode começar fazendo o raspador para a página mais recente e depois repetir as etapas para as demais, por meio de um loop, por exemplo.

Como vimos, a variável `response` nos retorna todo conteúdo da página inicial do nosso raspador. Ela tem vários atributos, como o `text`, que traz todo HTML da página em questão como uma *string*. Mas não temos interesse em todo HTML da página, apenas em informações específicas, então, todo trabalho da raspagem consiste justamente em separar o joio do trigo para filtrar os dados de nosso interesse. Fazemos isso por meio de seletores CSS, XPath ou expressões regulares.

### Identificando e testando os seletores

Uma forma fácil para testar os seletores do seu raspador é usando o Scrapy Shell. Experimente rodar por exemplo o comando `scrapy shell "http://www.paulinia.sp.gov.br/semanarios"`. Agora, você pode interagir com a página por meio da linha de comando e deve ver os comandos que temos disponíveis.

![Output do Scrapy Shell](img/scrapy_shell.png)
<!-- Imagem gerada no site carbon.now.sh -->

O elemento mais importante no nosso caso é o `response`. Se o acesso ao site foi feito com êxito, este comando deverá retornar o código 200.

Já o comando `response.css("a")` nos retornaria informações sobre todos os links das página em questão. Também é possível usar o `response.xpath` para identificar os seletores.

O modo mais fácil para de fato identificar os tais seletores que iremos utilizar é por meio do "Inspetor Web". Trata-se de uma função disponível em praticamente todos navegadores navegadores modernos. Basta clicar do lado direito na página e selecionar a opção "Inspecionar". Assim, podemos visualizar o código HTML, copiar e buscar por seletores XPath e CSS.

Experimente rodar o comando `response.xpath("//div[@class='container body-content']//div[@class='row']//a[contains(@href, 'AbreSemanario')]/@href")` e ver os resultados. Este seletor XPath busca primeiro por tags `div` em qualquer lugar da página, que tenha como classe `container body-content`. Dentro destas tags, buscamos então por outras `div` com a classe `row`. E, em qualquer lugar dentro destas últimas, por fim, buscamos por tags `a` (links) cujo atributo `href` contenha a palavra `AbreSemanario` e pedimos para retornar o valor apenas do atributo `href`. 

Existem várias formas de escrever seletores para o mesmo objeto. Você pode ter uma ideia de como montar o seletor inspecionando a página que disponibiliza os DOs.

Se você rodar o comando acima, irá ver uma lista de objetos como este: `<Selector xpath="//div[@class='container body-content']//div[@class='row']//a[contains(@href, 'AbreSemanario')]/@href" data='AbreSemanario.aspx?id=1064'>`.

O que realmente nos interessa é aquilo que está dentro do parâmetro `data`, ou seja, o trecho da URL que nos permite acesso a cada publicação. Então, adicione o `getall()` ao fim do comando anterior: `response.xpath("//div[@class='container body-content']//div[@class='row']//a[contains(@href, 'AbreSemanario')]/@href").getall()`.

Se o objetivo fosse selecionar apenas o primeiro item da lista, poderíamos usar o `.get()`.

Por vezes, pode ser necessário utilizar expressões regulares (regex) para "limpar" os seletores. A [Escola de Dados tem um tutorial sobre o assunto](https://escoladedados.org/tutoriais/expressao-regular-pode-melhorar-sua-vida/) e você vai encontrar diversos outros materiais na internet com exemplos de regex comuns, como este que aborda [expressões para identificar datas](https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s04.html) - algo que pode ser muito útil na hora de trabalhar com DOs.

Após identificar os seletores, é hora de construir seu raspador no arquivo `.py` da pasta `spiders`.

### Construindo o código do raspador

Normalmente, para completar o seu raspador você precisará fazer algumas requisições extras. É possível identificar quais requisições são necessárias fazer através do "Analizador de Rede" em navegadores. A [palestra do Giulio Carvalho na Python Brasil 2020](https://youtu.be/nhEPZ3r5zGY) mostra como pode ser feita essa análise de requisições de um site para depois converter em um raspador para o Querido Diário.

Se você precisar fazer alguma requisição `GET`, o objeto de requisição `scrapy.Request` deve ser o suficiente. O objeto `scrapy.FormRequest` normalmente é usado para requisições `POST`, que enviam algum dado no `formdata`.

Sempre que uma requisição for feita a partir de uma página, ela é feita utilizando a expressão `yield` e sua resposta será enviada para algum método da classe do raspador. Ou seja, além de um item (Gazette), como já vimos, o `yield` pode retornar uma requisição para outra página. As requisições têm alguns parâmetros essenciais (outros parâmetros podem ser vistos na documentação do Scrapy):

* `url`: A URL da página que será acessada;
* `callback`: O método da classe do raspador para o qual a resposta será enviada (por padrão, o método `parse` é utilizado);
* `formdata` (em `FormRequest`): Um dicionário contendo campos e seus valores que serão enviados.

No exemplo completo para a cidade de Paulínia (SP), na página inicial temos links para todos os anos onde há diários disponíveis e em cada ano todos os diários são listados na mesma página. Então, uma requisição é feita para acessar a página de cada ano (a página inicial já é o ano atual) usando `scrapy.FormRequest` (nesse caso, um método `.from_response` que já aproveita muitas coisas da `response` atual, inclusive a própria URL). A resposta dessa requisição deve ir para o método `parse_year` que irá extrair todos os metadados possíveis de ser encontrados na página. Com isso, a extração dos diários de Paulínia está completa 😄.

Veja como fica o raspador no exemplo a seguir (com comentários para explicar algumas partes do código):

```python
# Importação dos pacotes necessários
import datetime
import scrapy
from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider

# Definição da classe do raspador
class SpPauliniaSpider(BaseGazetteSpider):

    # Parâmetros iniciais
    name = "sp_paulinia"
    TERRITORY_ID = "2905206"
    start_date = datetime.date(2010, 1, 4)
    allowed_domains = ["www.paulinia.sp.gov.br"]
    start_urls = ["http://www.paulinia.sp.gov.br/semanarios"]

    # O parse abaixo irá partir da start_url acima
    def parse(self, response):
        # Nosso seletor cria uma lista com os código HTML onde os anos estão localizados
        years = response.css("div.col-md-1")
        # E fazer um loop para extrair de fato o ano
        for year in years:
            # Para cada item da lista (year) vamos pegar (get) um seletor XPath.
            # Também dizemos que queremos o resultado como um número inteiro (int)
            year_to_scrape = int(year.xpath("./a/font/text()").get())

            # Para não fazer requisições desnecessárias, se o ano já for o da página
            # inicial (página inicial é o ano atual) ou então for anterior ao ano da
            # data inicial da busca, não iremos fazer a requisição
            if (
                year_to_scrape < self.start_date.year
                or year_to_scrape == datetime.date.today().year
            ):
                continue

            # Com Scrapy é possível utilizar regex direto no elemento com os métodos
            # `.re` e `.re_first` (na maioria das vezes é suficiente e não precisamos
            # usar métodos da biblioteca `re`)
            event_target = year.xpath("./a/@href").re_first(r"(ctl00.*?)',")

            # O método `.from_response` nesse caso é bem útil pois pega vários
            # elementos do tipo <input> que já estão dentro do elemento <form>
            # localizado na página e preenche eles automaticamente no formdata, assim
            # é possível economizar muitas linhas de código
            yield scrapy.FormRequest.from_response(
                response,
                formdata={"__EVENTTARGET": event_target},
                callback=self.parse_year,
            )

        # O `yield from` permite fazermos `yield` em cada resultado do método gerador
        # `self.parse_year`, assim, aqui estamos dando `yield` em todos os itens
        # `Gazette` raspados da página inicial
        yield from self.parse_year(response)

    def parse_year(self, response):
        editions = response.xpath(
            "//div[@class='container body-content']//div[@class='row']//a[contains(@href, 'AbreSemanario')]"
        )

        for edition in editions:
            document_href = edition.xpath("./@href").get()

            title = edition.xpath("./text()")

            gazette_date = datetime.datetime.strptime(
                title.re_first(r"\d{2}/\d{2}/\d{4}"), "%d/%m/%Y"
            ).date()
            edition_number = title.re_first(r"- (\d+) -")
            is_extra_edition = "extra" in title.get().lower()

            # Esse site "esconde" o link direto do PDF por trás de uma série de
            # redirecionamentos, porém, como nas configurações do projeto é permitido
            # que arquivos baixados sofram redirecionamento, é possível colocar o link
            # "falso" já no item `Gazette` e o projeto vai conseguir baixar o documento
            yield Gazette(
                date=gazette_date,
                edition_number=edition_number,
                file_urls=[response.urljoin(document_href)],
                is_extra_edition=is_extra_edition,
                power="executive",
            )
```
Para ajudar a debugar eventuais problemas na construção do código, você pode inserir a linha `import pdb; pdb.set_trace()` em qualquer trecho do raspador para inspecionar seu código (contexto, variáveis, etc.) durante a execução.


### Rodando o raspador
Para rodar o raspador, execute o seguinte comando no terminal:

```
scrapy crawl nome_do_raspador
```

No caso acima, seria:

```
scrapy crawl sp_paulinia
```
O comando acima irá baixar os arquivos dos Diários Oficiais irá a pasta `data`. Durante o processo de desenvolvimento, muitas vezes é útil usar também os seguintes parâmetros adicionais na hora de rodar o raspador:

- `-s FILES_STORE=""`: Testar o raspador sem baixar nenhum arquivo adicionando. Isso é útil para testar rápido se todas as requisições estão funcionando.

- `-o output.csv`: Adiciona os itens extraídos para um arquivo CSV. Também é possível usar outra extensão como `.json` ou `.jsonlines`. Isso facilita a análise do que está sendo raspado.

- `-s LOG_FILE=logs.txt`: Salva os resultados do log em um arquivo texto. Se o log estiver muito grande, é útil para que erros não passem despercebidos.

- `-a start_date=2020-12-01`: Também é muito importante testar se o filtro de data no raspador está funcionando. Utilizando esse argumento, apenas as requisições necessárias para extrair documentos a partir da data desejada devem ser feitas. Este exemplo faz o teste para publicações a partir de 1 de dezembro de 2020. O atributo `start_date` do raspador é utilizado internamente, então, e o argumento não for passado, o padrão (primeira data de publicação) é utilizado no lugar.

Para rodar o comando usando todas a opções anteriores em `sp_paulinia`, usaríamos o seguinte comando:

```
scrapy crawl sp_paulinia -a start_date=2020-12-01 -s FILES_STORE="" -s LOG_FILE=logs.txt -o output.json
```

## Enviando sua contribuição 🤝

Ao fazer o commit do código, mencione a issue do raspador da sua cidade. Você pode incluir uma mensagem como `Close #20`, por exemplo, onde #20 é o número identificador da issue criada. Também adicione uma descrição comentando suas opções na hora de desenvolver o raspador ou eventuais incertezas.

Normalmente adicionar apenas um raspador necessita apenas de um único commit. Mas, se for necessário mais de um commit, tente manter um certo nível de separação entre o que cada um está fazendo e também se certifique que suas mensagens estão bem claras e correspondendo ao que os commits realmente fazem.

Uma boa prática é sempre atualizar a ramificação (_branch_) que você está desenvolvendo com o que está na `main` atualizada do projeto. Assim, se o projeto teve atualizações, você pode resolver algum conflito antes mesmo de fazer o Pull Request.

Qualquer dúvida, abra o seu Pull Request em modo de rascunho (_draft_) e relate suas dúvidas para que pessoas do projeto tentem te ajudar 😃. O [canal de discussões no Discord](https://discord.com/invite/nDc9p4drm4) também é aberto para tirar dúvidas e trocar ideias.
