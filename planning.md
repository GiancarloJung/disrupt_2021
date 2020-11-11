
# Introdução

O projeto **MrMovies** apresenta uma solução que possa prever o sucesso de um filme de forma automatizada, para melhor apoiar as **decisões dos investidores dos filmes**.

Investir na indústria do cinema é uma grande oportunidade porém complexa e de alto risco, além de se conectar com os melhores talentos para o projeto, acompanhar os custos e o processo de produção e distribuição o mais díficil é lidar com o lado pessoal de um filme. O que os críticos de cinema e o público alvo esperam de um filme é sempre algo muito pessoal, e achar a fórmula de sucesso é um trabalho arduo, tando para os investidores experientes quanto para os que recém entraram no negócio.

Podemos dividir a formula de sucesso de um filme em três pilares: o da **equipe**, o da **história** e o das **finanças**. Assim, é importante possuir um balanço entre a equipe e os talentos necessários para executar a produção do filme, um roteiro que seja cativante e engajado com o público e por último e um balanço de contas que permita que o negócio seja sustentável do início ao fim.  

![Os Três Pilares](link_pilares)

O **MrMovies** foi concebido como uma ferramenta que auxilia investidores a encontrar o projeto ideal para aplicar os seus recursos e esforços, oferecendo *insights* para uma tomada de decisão acertiva. Ela foi idealizada para atuar dentro de um ecossistema *data-driven* complementando outras ferramentas e algoritmos que possam existir.

Dessa forma, em posse do **MrMovies** um investidor é capaz de responder as seguintes perguntas executivas que o irão auxiliar a tomar a sua decisão, utilizando pontuações e fórmulas presentes no sistema (calculadas baseando-se em conjuntos de dados e em algoritmos de machine learning).


## Equipe

Do ponto de vista das pessoas envolvidas na produção de um projeto de cinema, a solução oferecerá insumos para as seguintes perguntas executivas:

### Qual a pontuação de um Produtor?

Um produtor de cinema é uma pessoa que supervisiona a produção de filmes, sejam eles contratados por uma produtora ou trabalhando de forma independente, os produtores planejam e coordenam vários aspectos da produção do filme, como a seleção do roteiro, coordenação da redação, direção e edição e obtenção de financiamento.

### Qual a pontuação da Equipe de Talentos?

A equipe de talentos de um filme (comumente chamada de *cast and crew*) é composta pelos atores, atrizes, diretores e outros profissionais que atuam atrás das cameras e trabalham no filme. A medida que o projeto vai tomando forma e essas pessoas começam a compor parte do time o sucesso ou fracasso do filme começa a ser definido.

### Qual o score de um filme baseado no time que trabalha nele?

Utilizando a pontuação do produtor e dos talentos envolvidos no projeto o sistema calcula um *score* para o primeiro pilar de sucesso do filme, a equipe. Os usuários do sistema utilizam esse *score* como um dos fatores de decisão.


## História

Produzir um filme é contar uma história, as perguntas executivas abaixo buscam determinar se essa história será responsável pelo sucesso da produção.

- *\[Teórico] [Modelo]* Dada a sinopse de um filme, qual o seu score?
- *\[Teórico] [Modelo]* Dado uma série de avaliações de um filme, qual o seu score?
- *\[Modelo]* Dado um filme qual o potencial de audiência dele (score)?



## Scores

### Team score

`| Movie | Producer | Actors/Actresses/Directors | Score |`

Reputação do Produtor
Experiência do Produtor
Qualidade do talento envolvido (Cast and Crew)

#### Perguntas

- Qual a pontuação/classificação/score de um Produtor?
- Qual a pontuação/classificação/score de um Ator/Atriz?
- Qual o score de um filme dado o time que trabalha nele?

#### Modelos

Modelo de Score da Pessoa
Média do Filme


### Script score

Qualidade do Script

`| Movie | Script |`

#### Perguntas

- *\[Teórico] [Modelo]* Dada a sinopse de um filme, qual o seu score?
- *\[Teórico] [Modelo]* Dado uma série de avaliações de um filme, qual o seu score?

#### Modelos (Teórico)

- Análise de Sentimento da Sinopse
- Análise de Sentimento da Review

`| Movie | Genre | Target Audience | Audience Score | Critic Score | Número de Oscars |`

#### Perguntas

- *\[Modelo]* Dado um filme qual o potencial de audiência dele (score)?

#### Modelos

Modelo de Regressão da Audiência


### Financial score

`| Movie | Budget | Gross/Profit |`

#### Perguntas

- *\[Modelo]* Qual é a taxa de risco de um filme baseada nas suas projeções financeiras?

#### Algoritmos

Modelo de Regressão Financeira

`| Movie | Genre | Country | Release Date |`

- *\[Modelo]* Qual será a performance de filme baseado nas suas expectativas de mercado?
- *\[Fórmula]* Qual o score financeiro de um filme?


## O desafio

4 Modelos
3 Fórumulas de Score
