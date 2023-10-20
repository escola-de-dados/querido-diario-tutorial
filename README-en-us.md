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
      1. [Specific cases](#specific-cases-)
  6. [Anatomy of a scraper](#anatomy-of-a-scraper-)
      1. [Initial parameters](#initial-parameters-)
      2. [Output parameters](#output-parameters-)
  7. [Hello world: make your first request](#hello-world-make-your-first-request-)
  8. [Dissecting the log](#dissecting-the-log-)
  9. [Building a real scraper](#building-a-real-scraper-)
      1. [Identifying and testing selectors](#identifying-and-testing-selectors-)
      2. [Writing the scraper code](#writing-the-scraper-code-)
      3. [Tips to test a scraper](#tips-to-test-a-scraper-)
  10. [Sending your contribution](#sending-your-contribution-)

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

* `import datetime`: package to handle dates.
* `from gazette.items import Gazette`: We call the file of official gazettes found by the scrapers `Gazette`, it will also store metadata fields for each publication.
* `from gazette.spiders.base import BaseGazetteSpider`: is the project's base spider, which already brings some useful features.

### Initial parameters

Each scraper has a [Python class](https://www.youtube.com/watch?v=52ns4X7Ny6k&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=41), which executes certain routines for each page of websites that publish Official Gazettes. All classes have at least the basic information below:

* `name`: Scraper name in the same pattern as the file name, without the extension. Example: `sp_paulinia`.
* `TERRITORY_ID`: city code at IBGE. Check the project file [`territories.csv`](https://github.com/okfn-brasil/querido-diario/blob/main/data_collection/gazette/resources/territories.csv) to find out your city's code . Example: `2905206`.
* `allowed_domains`: Domains on which the scraper will act. Pay attention to the brackets. They indicate that it is a list, even though it only has one element. Example: `["paulinia.sp.gov.br"]`
* `start_urls`: list of scraper navigation start URLs (normally just one). The response to this initial request is forwarded to the variable `response`, of the standard Scrapy method called `parse`. We'll see more about this soon. Again, pay attention to the brackets. Example:`["http://www.paulinia.sp.gov.br/semanarios/"]`
* `start_date`: Date representation in the format year, month and day (YYYY, M, D) with `datetime.date`. It is the initial date of publication of the Official Gazette in the question system, that is, the date of the first publication available online. Find this date by searching and manually enter it into this variable. Example: `datetime.date(2017, 4, 3)`.

### Output parameters

Additionally, each scraper also needs to return some information by default. This happens using the `yield` expression on `Gazette` items created.

* `date`: The publication date of the gazette.
* `file_urls`: returns the official gazette publication URLs as a list. A document can have more than one URL, but this is not common.
* `power`: Accepts `executive` or `executive_legislative` settings. Here, we define whether the official gazette has information only from the executive branch or also from the legislative branch. To define this, you need to manually look in the publications to see if there is information from the City Council ("câmara municipal") aggregated in the same document, for example.
* `is_extra_edition`: We indicate here whether it is an extra edition of the Official Gazette or not. Extra editions are complete editions of the diary that are published outside the scheduled schedule.
* `edition_number`: Edition number of the DO in question.

Let's now look at our example code.

## Hello world: make your first request 👋

Scrapy starts by making a request to the URL defined in the `start_urls` parameter. The response from this request goes to the standard `parse` method, which will store the response in the `response` variable.

So, one way to say "Hello, world!" in the Querido Diario project it would be with code like the one below.

```python
import datetime
from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider

class SpPauliniaSpider(BaseGazetteSpider):
    name = "sp_paulinia"
    TERRITORY_ID = "2905701"
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

The code downloads the HTML from the initial URL, but does not actually download any official gazette. We set this parameter to today, just to have a basic operational version of the code. However, when building a real scraper, you will need to indicate the correct dates of publications.

Either way, this gives you the foundation to understand how scrapers operate and where to start developing your own.

To run the code, you can follow the following steps:

1. Crie um arquivo na pasta `data_collection/gazette/spiders/` do repositório criado no seu computador a partir do seu fork do Querido Diário;
2. Abra o terminal na raíz do projeto;
3. Ative o ambiente virtual, caso não tenha feito antes, como indicado na seção _"[Configurando um ambiente de desenvolvimento](#configurando-um-ambiente-de-desenvolvimento)"_ (`source .venv/bin/activate`, por exemplo);
4. No terminal, vá para a pasta `data_collection`;
5. No terminal, rode o raspador com o comando `scrapy crawl nome_do_raspador` (nome que está no atributo `name` da classe do raspador). Ou seja, no exemplo rodamos: `scrapy crawl sp_paulinia`.

## Dissecting the log 📄

If everything went well, a huge log should appear in the terminal.

It starts with something like `[scrapy.utils.log] INFO: Scrapy 2.4.1 started (bot: gazette)` and brings a series of information about the environment initially. But the part that interests us most begins just after the line `[scrapy.core.engine] INFO: Spider opened` and ends at the line `[scrapy.core.engine] INFO: Closing spider (finished)`. Let's see below.

![](img/output1.png)

The line `DEBUG: Scraped from <200 http://www.paulinia.sp.gov.br/semanarios/>` tells us whether we can access the specified address (code 200).

When developing a scraper, look mainly for *WARNING* and *ERROR* warnings. They are the ones who will provide the most important information for you to understand the problems that occur.

After the scraper is finished, we have the lines in the *monitors* section, which will bring an execution report. It is normal for errors to appear, like the one below.

![Exemplo de erro do Scrapy](img/scrapy_erro.png)
<!-- Imagem gerada no site carbon.now.sh -->

It is a warning that nothing has been shaved in the last few days. Okay, this is just an initial test to familiarize ourselves with the project.

## Building a real scraper 🛠️

Here, everything will depend on the way each website is built. But we have separated some general tips that can help you.

First, browse the website to understand how the official gazettes are available. Try to find a consistent pattern that is not susceptible to occasional changes for the robot to extract the necessary information. For example, if publications are separated into several tabs or pages, first make sure that they all follow the same pattern. If this is the case, then you can start by doing the scraper for the most recent page and then repeat the steps for the others, through a loop, for example.

As we saw, the `response` variable returns all the content of our scraper's home page. It has several attributes, such as `text`, which brings all the HTML of the page in question as a *string*. But we are not interested in all the HTML on the page, only in specific information, so all scraping work consists precisely of separating the wheat from the chaff to filter the data of interest to us. We do this through CSS, XPath or regular expression selectors.

### Identifying and testing selectors

An easy way to test your scraper selectors is using Scrapy Shell. Try running, for example, the command `scrapy shell "http://www.paulinia.sp.gov.br/semanarios"`. You can now interact with the page via the command line and you should see the commands we have available.

![Output do Scrapy Shell](img/scrapy_shell.png)
<!-- Imagem gerada no site carbon.now.sh -->

The most important element in our case is `response`. This command should return code 200 if access to the site was successful.

The command `response.css("a")` would return information about all the links on the page in question. You can also use `response.xpath` to identify selectors.

The easiest way to actually identify the selectors that we will use is through the "Web Inspector". This is a function available in practically all modern browsers. Just click on the right side of the page and select the "Inspect" option. So, we can view the HTML code, copy and search for XPath and CSS selectors.

Try running the command `response.xpath("//div[@class='container body-content']//div[@class='row']//a[contains(@href, 'AbreSemanario')]/ @href")` and see the results. This XPath selector first searches for `div` tags anywhere on the page, which have the class `container body-content`. Within these tags, we then look for other `div` with the `row` class. And, anywhere within the latter, finally, we look for `a` tags (links) whose `href` attribute contains the word `AbreSemanario` and ask to return the value of only the `href` attribute. 

There are several ways to write selectors for the same object. You can get an idea of ​​how to assemble the selector by inspecting the page that provides the DOs.

If you run the above command, you will see a list of objects like this: `<Selector xpath="//div[@class='container body-content']//div[@class='row']//a [contains(@href, 'AbreSemanario')]/@href" data='AbreSemanario.aspx?id=1064'>`.

What really interests us is what is inside the `data` parameter, that is, the part of the URL that allows us to access each publication. Then, add `getall()` to the end of the previous command: `response.xpath("//div[@class='container body-content']//div[@class='row']//a[ contains(@href, 'AbreSemanario')]/@href").getall()`.

If the goal was to select only the first item in the list, we could use `.get()`.

Sometimes it may be necessary to use regular expressions (regex) to "clean up" the selectors. [Escola de dados has a tutorial on the subject](https://escoladedados.org/tutoriais/expressao-regular-pode-melhorar-sua-vida/) and you will find several other materials on the internet with examples of common regex, like this one that addresses [expressions to identify dates](https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s04.html) - something that can be very useful when working with official gazettes.

After identifying the selectors, it's time to build your scraper in the `.py` file in the `spiders` folder.

### Writing the scraper code

Normally, to complete your scraper you will need to make some extra requests. It is possible to identify which requests need to be made through the "Network Analyzer" in browsers. [Giulio Carvalho's talk at Python Brasil 2020](https://youtu.be/nhEPZ3r5zGY) shows how this analysis of requests from a website can be carried out and then converted into a scraper for Querido Diário.

If you need to make a `GET` request, the `scrapy.Request` request object should be enough. The `scrapy.FormRequest` object is normally used for `POST` requests, which send some data in `formdata`.

Whenever a request is made from a page, it is made using the `yield` expression and its response will be sent to some method in the scraper class. In other words, in addition to an item (Gazette), as we have already seen, `yield` can return a request for another page. Requests have some essential parameters (other parameters can be seen in the Scrapy documentation):

* `url`: The URL of the page that will be accessed;
* `callback`: The scraper class method to which the response will be sent (by default, the `parse` method is used);
* `formdata` (in `FormRequest`): A dictionary containing fields and their values ​​that will be sent.

In the complete example for the city of Paulínia (SP), on the home page we have links to all the years where gazettes are available and for each year all gazettes are listed on the same page. Then, a request is made to access each year's page (the home page is already the current year) using `scrapy.FormRequest` (in this case, a `.from_response` method that already takes advantage of many things from the current `response`, including the URL itself). The response to this request must go to the `parse_year` method, which will extract all metadata found on the page. With this, the extraction of Paulínia's gazettes is complete 😄.

Check it out what the scraper looks like in the following example (there are some comments to explain parts of the code):

```python
# Importing the necessary packages
import datetime
import scrapy
from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider

# Scraper class definition
class SpPauliniaSpider(BaseGazetteSpider):

    # Initial parameters
    name = "sp_paulinia"
    TERRITORY_ID = "2905206"
    start_date = datetime.date(2010, 1, 4)
    allowed_domains = ["www.paulinia.sp.gov.br"]
    start_urls = ["http://www.paulinia.sp.gov.br/semanarios"]

    # The parse below will start from the start_url above
    def parse(self, response):
        # Our selector creates a list with the HTML code where the years are located
        years = response.css("div.col-md-1")
        # Making a loop to actually extract the year
        for year in years:
            # For each item in the list (year) we will get an XPath selector.
            # We also say that we want the result as an integer (int)
            year_to_scrape = int(year.xpath("./a/font/text()").get())

            # To avoid making unnecessary requests, if the year is already the year of the home
            # page (start page is the current year) or is prior to the year of
            # start date of the search, we will not make the request
            if (
                year_to_scrape < self.start_date.year
                or year_to_scrape == datetime.date.today().year
            ):
                continue

            # With Scrapy it is possible to use regex directly on the element with the methods
            # `.re` and `.re_first` (most of the time is enough and we don't need
            # to use methods from the `re` library)
            event_target = year.xpath("./a/@href").re_first(r"(ctl00.*?)',")

            # The `.from_response` method, in this case, is very useful as it takes several
            # elements of type <input> that are already inside the <form> element
            # located on the page and automatically fills them in formdata, thus
            # it is possible to save many lines of code
            yield scrapy.FormRequest.from_response(
                response,
                formdata={"__EVENTTARGET": event_target},
                callback=self.parse_year,
            )

        # `yield from` allows us to `yield` on each result of the generating method
        # `self.parse_year`, so here we are giving `yield` to all  `Gazette `items
        #  scraped from home page
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

            # This website "hides" the direct PDF link behind a series of
            # redirects, however, as in the project settings it is allowed
            # that downloaded files are redirected, it is possible to place the "false" link
            # already in the `Gazette` item and the project will be able to download the document
            yield Gazette(
                date=gazette_date,
                edition_number=edition_number,
                file_urls=[response.urljoin(document_href)],
                is_extra_edition=is_extra_edition,
                power="executive",
            )
```
To help debug any problems when building the code, you can insert the line `import pdb; pdb.set_trace()` in any part of the scraper to inspect its code (context, variables, etc.) during execution.

### Running the scraper

To run the scraper, run the following command in the terminal:

```
scrapy crawl name_of_scraper
```

In the case above, it would be:

```
scrapy crawl sp_paulinia
```
The above command will download the Official Gazette files to the `data` folder. During the development process, it is often useful to also use the following additional parameters when running the scraper:

- `-s FILES_STORE=""`: Tests the scraper without downloading any files locally. This is useful for quickly testing whether all requests are working.

- `-o output.csv`: Adds the extracted items to a CSV file. You can also use another extension like `.json` or `.jsonlines`. This makes it easier to analyze what is being scraped.

- `-s LOG_FILE=logs.txt`: Saves log results to a text file. If the log is very large, it is useful so that errors do not go unnoticed.

- `-a start_date=2020-12-01`: It is also very important to test whether the date filter in the scraper is working. Using this argument, requests will only be made considering the defined period of time. This example tests for publications on or after December 1, 2020. The scraper's `start_date` attribute is used internally, so if the argument is not passed, the default (first publication date) is used instead.

To run the command using all the previous options in `sp_paulinia`, we would use the following code:

```
scrapy crawl sp_paulinia -a start_date=2020-12-01 -s FILES_STORE="" -s LOG_FILE=logs.txt -o output.json
```

## Sending your contribution 🤝

When committing the code to the [querido-diario repository](https://github.com/okfn-brasil/querido-diario), mention the scraper issue in your city. You can include a message like `Close #20`, for example, where #20 is the identifying number of the created issue. Also add a description commenting on your options when developing the scraper or any uncertainties.

Typically adding just one scraper only requires a single commit. But if more than one commit is needed, try to maintain a certain level of separation between what each commit is doing and also make sure your messages are clear and correspond to what the commits actually do.

A good practice is to always update the branch you are developing with what is in the project's updated `main`. So, if the project has had updates, you can resolve any conflicts before even making the Pull Request.

If you have any questions, open your Pull Request in draft mode (_draft_) and report your questions so that people from the project can try to help you 😃. The [Discord discussion channel](https://discord.com/invite/nDc9p4drm4) is also open to answering questions and exchanging ideas.
