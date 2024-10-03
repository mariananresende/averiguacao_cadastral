# Averiguação Cadastral
Repositório para projeto conjunto no âmbito do Bootcamp em Machine Learning com o objetivo de desenvolver um algoritmo para identificação automática do público de averiguação cadastral do Cadastro Único para Programas Sociais

# ![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM_DESENVOLVIMENTO&color=GREEN&style=for-the-badge) ![Badge Outubro/2024](http://img.shields.io/static/v1?label=DATA&message=Outubro/2024&color=blue&style=for-the-badge)

## Nome do projeto
Algoritmo para identificação do público para averiguação Cadastral

## Descrição do problema 
O Cadastro Único para Programas Sociais é o principal instrumento do Estado brasileiro para a seleção e a inclusão de famílias de baixa renda em programas federais, sendo usado para a concessão dos benefícios do Programa Bolsa Família, do Pé de Meia, da Tarifa Social de Energia Elétrica, do Auxílio Gás, do Programa Minha Casa Minha Vida, entre outros. 

Para reduzir erros de inclusão, constantemente é feito um processo de qualificação cadastral. Neste ano, por exemplo, até o momento foram convocadas 3,3 milhões de famílias para averiguação do cadastro, por divergências de de renda e de composição familiar.

Aualmente existem mais de 40 milhões de famílias incluídas no Cadastro Único, e 93 milhões de pessoas. Para uma melhor focalização das políticas públicas sociais usuárias deste cadastro para seleção dos beneficiários é preciso automatizar o processo de averiguação cadastral.

Para tanto, a proposta do presente projeto é propor um algoritmo que, a partir das características das família, seja possível classificar cada família em uma faixa de renda mais provável:
* Pobreza: de 0 a 218,00;
* Baixa renda: de 218,01 a 1/2 salário-mínimo;
* Acima de 1/2 salário-mínimo.
  
O modelo objetiva auxiliar em uma maior focalização das políticas públicas sociais para as famílias que apresentam características relacionadas à maior vulnerabilidade de renda, identificando famílias que apresentam caracterísiticas não esperadas para a faixa de renda apresentada, guiando ações de qualificação do Cadastro Único.

## Bases de dados utilizadas
As bases de dados utilizadas estão disponibilizadas no <a href="https://dados.gov.br/dados/conjuntos-dados/microdados-amostrais-do-cadastro-unico)">Portal de Dados abertos do Governo Federal do MDS</a>.

As bases são amostrais, desidentificadas, e as últimas bases disponíveis no portal são de 2018.

Uma base apresenta os dados de pessoas e a outra base os dados das famílias. É possível combinar as duas bases de dados por meio da variável id_familia: Identificador único da família para pareamento com a base de pessoas.

O dicionário das bases está salvo nos arquivos do projeto.

## Variável dependente
A variavél dependente do projeto é a vlr_renda_media_fam: Valor da renda média (per capita) da família.

## Variáveis independentes
Podem ser selecionadas diversas variáveis que podem estar relacionadas à condição de pobreza. Durante treinamento será possível identificar quais as variáveis parecem ser mais relevantes para o modelo.

### Base famílias

* dat_cadastramento_fam: Data do cadastramento da família
* cod_local_domic_fam: Características do local onde está situado o domicílio
* cod_agua_canalizada_fam: Se o domicílio tem água encanada
* cod_escoa_sanitario_domic_fam: Forma de escoamento sanitário
* ind_parc_mds_fam: Pertencente a Grupos tradicionais e específicos
* qtd_pessoas: Quantidade de pessoas utilizada no cálculo da renda per capita familiar

### Base pessoas

* cod_sexo_pessoa: sexo (do Responsável familiar)
* idade (de modo a selecionar famílias com crianças, idosos)
* cod_parentesco_rf_pessoa: Relação de parentesco com o RF (resposta 1 -  Pessoa Responsável pela Unidade Familiar - RF)
* cod_raca_cor_pessoa: Cor ou raça (do Responsável familiar)
* cod_deficiencia_memb: Pessoa tem deficiência? (ao menos 1 pessoa na família com deficiência)
* cod_sabe_ler_escrever_memb: Pessoa sabe ler e escrever? (ao menos uma pessoa com mais de 10 anos sem saber ler ou escrever)
* ind_frequenta_escola_memb: Pessoa frequenta escola? (ao menos 1 pessoa com menos de 17 anos que não está na escola)
* cod_trabalhou_memb: Pessoa trabalhou na semana passada? (responsável familiar não trabalhou na semana passada)
* cod_trabalhou_memb: Pessoa trabalhou na semana passada? (ao menos 1 pessoa com 15 anos ou mais que não trabalhou na semana passada e não estuda)
* qtd_meses_12_meses_memb: Quantidade de meses trabalhados nos últimos 12 meses

## Autores do projeto (ordem alfabética)
Grinaldo Oliveira

Mariana Nogueira de Resende Sousa

Renata

Risla

