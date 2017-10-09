# Moses-SMT gant Docker

(please scroll down for English)

M'eo staliet Docker war hoc'h urzhiataer kit da [Get Started with Docker](https://docs.docker.com/windows/) un doare aes-kenañ a zo evit staliañ hag implijout an droidigezh emgefreek en un doare lec'hel. N'eus nemet 2 arc'had d'ober.

## Arc'had 1 : Staliañ Moses-SMT

```
 $ docker pull techiaith/moses-smt
```

Pelgargañ ha staliañ a raio ur reizhiad troidigezh emgefreek Moses war hoc'h endro Docker.

## Arc'had 2 : Loc'hañ ul lusker troidigezh emgefreek

Evit ar mare ez eus testennoù kembraek da dapout evit ar mekanik. Hizivaet e vo al lodenn-mañ pa vo kinniget testennoù brezhonek. Troet e vo al lodenn-mañ diwezhatoc'h.

Mae’r Uned Technolegau Iaith wedi creu peiriannau cyfieithu ar sail hyfforddi gyda data rydym wedi’i gasglu o ffynonellau agored a chyhoeddus, megis Cofnod y Cynulliad a’r Ddeddfwriaeth ar-lein.

Mae gan y peiriannau enwau a chyfeiriadau cyfieithu penodol. Yr enw ar y peiriant a hyfforddwyd gyda chofnodion y Cynulliad yw ‘CofnodYCynulliad’ a’r enw ar gyfer peiriant y corpws deddfwriaeth yw ‘Deddfwriaeth’.

Dyma’r ail orchymyn, gan ddewis peiriant ‘CofnodYCynulliad’ a’i osod i gyfieithu o’r Saesneg i’r Gymraeg :

```
 $ docker run --name moses-smt-cofnodycynulliad-en-cy -p 8080:8080 -p 8008:8008 techiaith/moses-smt start -e CofnodYCynulliad -s en -t cy
```

Bydd y system yn llwytho ffeil i lawr (tua 3Gb mewn maint yn achos peiriant CofnodYCynulliad) cyn iddo gadarnhau ei fod yn barod i dderbyn ceisiadau i’w cyfieithu.

Os agorwch chi eich porwr a mynd at [http://localhost:8008](http://localhost:8008), dylai ffurflen syml ymddangos er mwyn i chi wirio a yw’r peiriant yn gweithio ai peidio.

## Staliañ ha lañsañ adalek GitHub

Posupl eo pellgargañ al loazioù Docker-mañ war-eeun eus Github hag azasaat evit hoc'h ezhommoù:

```sh
 $ git clone https://github.com/porthtechnolegauiaith/moses-smt
 $ cd moses-smt/docker
 $ docker build --rm -t techiaith/moses-smt .
```

hag adarre:

```
 $ docker run --name moses-smt-cofnodycynulliad -p 8080:8080 techiaith/moses-smt start -e CofnodYCynulliad -s en -t cy
```

Ar servijer Docker a responto d'hoc'h azgoulennoù Docker war ar porzh 8008 hag e XMLRPC war ar porzh 8080.

## Skriptoù evit ar brezhoneg

Diorroet ez eus bet skriptoù evit tremen eus restroù .tmx da restroù gouest da vezañ lennet gant moses. Skrivet e vo amañ penaos implijout anezho diwezhatoc'h.


# Moses-SMT with Docker

If you have Docker installed on your computer [Get Started with Docker](https://docs.docker.com/windows/) then there is a very easy method by which you can install and use machine translation engines locally. There are only two commands involved.

## Command 1 : Installing Moses-SMT

```
 $ docker pull techiaith/moses-smt
```

This will download and install a Moses machine translation system within your Docker environment.


## Command 2 : Start a Machine Translation Engine of your Choice

The Language Technologies Unit have created machine translation engines that have been trained from bilingual data that we have collected from open and public sources, such as the Proceedings of the Welsh Assembly, the UK and Welsh Legislature website, as well as localisations of open source software. Each in turn provide domain specific machine translation capabilities. Each one is identified according to its Welsh name. Thus:

 - CofnodYCynulliad  : as trained from the Welsh Assembly Proceedings
 - Deddfwriaeth  : as trained from UK and Welsh legislature
 - Meddalwedd : as trained from localisations of various open source software projects.

These names can be used in the second Docker command that will start (and fetch is necessary from the Welsh National Language Technologies Portal) an engine for a desired source and target language pairing:

```
 $ docker run --name moses-smt-cofnodycynulliad-en-cy -p 8080:8080 -p 8008:8008 techiaith/moses-smt start -e CofnodYCynulliad -s en -t cy
```

In the case of CofnodYCynulliad, the engine may be a very large download - about 3Gb.

Open your browser and browse to [http://localhost:8008](http://localhost:8008), where you should see a simple demo form that will help you check if the engine is working or not.

## Installing and Running from GitHub

It is possible to download these Docker resources directly from GitHub and adapt for your scenario:

```sh
 $ git clone https://github.com/porthtechnolegauiaith/moses-smt
 $ cd moses-smt/docker
 $ docker build --rm -t techiaith/moses-smt .
```

and once again :

```
 $ docker run --name moses-smt-cofnodycynulliad -p 8080:8080 techiaith/moses-smt start -e CofnodYCynulliad -s en -t cy
```

The running Docker container will respond to JSON requests on port 8008 as well as XMLRPC on port 8080.

# Moses SMT
## Cyfieithu Peirianyddol Cymraeg <> Saesneg

[click here for English README](README_en.md)

## Cyflwyniad

Mae'r project yma yn cynnwys cod, sgriptiau a dogfennaeth i'ch galluogi i greu a defnyddio peiriannau cyfieithu Cymraeg<>Saesneg Moses-SMT eich hunain.

Mae'r sgriptiau yn hwyluso'n benodol :

 * gosod Moses-SMT o docker.com
 * gosod Moses-SMT yn uniongyrchol ar gyfrifiaduron/weinyddion Linux
 * llwytho i lawr a rhedeg peiriannau cyfieithu'r Uned Technolegau Iaith
 * creu peiriannau eich hunain ar sail casgliadau cyfieithiadau eich hunain, neu gorpora cyfochrog gan yr Uned Technolegau Iaith o ffynonellau cyhoeddus, megis Cofnod y Cynulliad a'r Ddeddfwriaeth.

Crëwyd y project yma diolch i nawdd gan Lywodraeth Cymru a CyfieithuCymru - rhaglen gyfieithu gyflawn "yn y cwmwl" ar gyfer cyfieithu rhwng y Gymraeg a’r Saesneg yw CyfieithuCymru a drwyddedir yn fasnachol gan Brifysgol Bangor.

Am ragor o wybodaeth ynghylch cyfieithu peirianyddol ac adnoddau eraill ewch i dudalennau cyfieithu Porth Technolegau Iaith Cenedlaethol Cymru - [techiaith.cymru/cyfieithu](http://techiaith.cymru/cyfieithu)

## Docker
Mae Docker yn dechnoleg pecynnu meddalwedd a hwyluso gosod ar gyfer Linux, Mac OS X a Windows.

Bydd y gorchymyn canlynol gyda Docker yn gosod Moses-SMT ar eich cyfrifiadur:

```sh
docker pull techiaith/moses-smt
```

Dyma enghraifft o sut mae defnyddio'r Moses-SMT o fewn Docker er mwyn rhedeg peiriant cyfieithu (ar sail corpws cyfochrog `CofnodYCynulliad`), sy'n cyfieithu o'r Saesneg i'r Gymraeg :

```sh
docker run --name moses-smt-cofnodycynulliad-en-cy -p 8008:8008 -p 8080:8080 techiaith/moses-smt start -e CofnodYCynulliad -s en -t cy
```

Yna, ewch i dudalen demo y peiriant er mwyn ei weld ar waith : http://localhost:8008



### Strwythur y Project

* **docs** - yn cynnwys dogfennaeth ar sut i ddefnyddio'r sgriptiau. Yn benodol:
  * sut mae gosod Moses-SMT o docker.com a llwytho peiriannau cyfieithu'r Uned Technolegau Iaith i lawr - [cliciwch yma...](docs/Docker.md)
  * sut mae gosod Moses-SMT ar gyfrifiadur arferol - [cliciwch yma...](docs/GosodiadArferol.md)
  * rhedeg Moses-SMT ar gyfrifiadur arferol - [cliciwch yma...](docs/RhedegMoses.md)
  * sut mae hyfforddi Moses-SMT a chreu eich peiriannau eich hunain - [cliciwch yma...](docs/Hyfforddi.md)

* **get** - yn cynnwys y sgriptiau a ddefnyddir i baratoi a gosod Moses-SMT yn hwylus ar gyfrifiaduron Linux
* **mtdk** - yn cynnwys sgriptiau sy'n hwyluso nodweddion hyfforddi Moses-SMT

### Ffeiliau'r Project

* **moses.py** - cod Python ar gyfer defnyddio holl nodweddion Moses-SMT ar gyfrifiaduron Linux.
* **python-server.py** - cod Python ar gyfer darparu gweinydd cyfieithu syml ar gyfer y we.
* **docker/Dockerfile** - y ffeil a ddefnyddir i adeiladu delweddau docker
* **docker/moses.py** - cod Python ar gyfer rhedeg Moses o fewn Docker
