import streamlit as st
from app.db import Database
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import numpy as np



def write():
    st.title("Data Analysis")

    st.markdown(
        """
        # Introdução

        O projeto **MrMovies** apresenta uma solução que possa prever o sucesso de um filme de forma automatizada, para melhor apoiar as **decisões dos investidores dos filmes**.

        Investir na indústria do cinema é uma grande oportunidade porém complexa e de alto risco, além de se conectar com os melhores talentos para o projeto, acompanhar os custos e o processo de produção e distribuição o mais díficil é lidar com o lado pessoal de um filme. O que os críticos de cinema e o público alvo esperam de um filme é sempre algo muito pessoal, e achar a fórmula de sucesso é um trabalho arduo, tando para os investidores experientes quanto para os que recém entraram no negócio.

        Podemos dividir a formula de sucesso de um filme em três pilares: o da **equipe**, o da **história** e o das **finanças**. Assim, é importante possuir um balanço entre a equipe e os talentos necessários para executar a produção do filme, um roteiro que seja cativante e engajado com o público e por último e um balanço de contas que permita que o negócio seja sustentável do início ao fim.

        ![Os Três Pilares](/images/pilares.png)

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

        ### Dado uma série de avaliações de um filme, qual o seu score?

        Com avaliações textuais de filmes realizados por espectadores e críticos é possivel utilizar ferramentas de análise de sentimento para determinar a performance de um filme. Combinando dados históricos em conjunto com avaliações realizadas por uma equipe de críticos especialistas e pesquisas de mercado é possível determinar a crítica de um filme que ainda está em processo de produção.

        ### Dado um filme qual o potencial de audiência dele (score)?

        Utilizando os gêneros e temáticas abordadas pelo filme e a audiência alvo é possível determinar o potencial de audiência do filme, e o potencial que ele tem comparado com dados históricos.


        ## Finanças

        As perguntas executivas abaixo servem para analizar o potencial de sucesso do projeto do ponto de vista dos seus aspectos financeiros.

        ### Qual é a taxa de risco de um filme baseada nas suas projeções financeiras?

        Analizando o valor do custo inicial do projeto junto com os valores projetados de arrecadação é possível determinar se a relação de lucro sobre investimento (ROI) determinam se o projeto é de alto ou baixo risco.

        ### Qual será a performance de filme baseado nas suas expectativas de mercado?

        Expectativas de mercado podem incluir, por exemplo, os gêneros e temáticas abordadas, o segmento demográfico que se busca atingir, a data e a região de lançamento prevista. Essas informações ajudam a determinar a performance e popularidade de um filme no segmento de mercado que ele busca atingir baseando-se em dados históricos.

        ### Qual o score financeiro de um filme?

        Utilizando as pontuações financeiras o sistema calcula um *score* para o último pilar de sucesso do filme, os usuários do sistema utilizam esse *score* como um dos fatores de decisão.

        ## Geral

        ### Qual o score global de um filme?

        Baseando-se em todos os scores calculados nos três pilares de análise do projeto o sistema produz um score global que é utilizado pelos usuários para determinar o potencial de investimento do filme.
        """
    )
