# Averiguação Cadastral
Repositório para projeto conjunto no âmbito do Bootcamp em Machine Learning com o objetivo de desenvolver um algoritmo para identificação automática do público de averiguação cadastral do Cadastro Único para Programas Sociais

# ![Badge concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=GREEN&style=for-the-badge) ![Badge Outubro/2024](http://img.shields.io/static/v1?label=DATA&message=Outubro/2024&color=blue&style=for-the-badge)

## Nome do projeto
Algoritmo de classificação usando técnicas de Machine Learning (ML) para identificação do público para averiguação Cadastral

## Descrição do problema 
O Cadastro Único para Programas Sociais é o principal instrumento do Estado brasileiro para a caracterização socioeconômica das famílias de baixa renda que residem no território nacional, para permitir a seleção e a inclusão dessas famílias em programas federais, sendo usado para a concessão dos benefícios do Programa Bolsa Família, do Pé de Meia, da Tarifa Social de Energia Elétrica, do Auxílio Gás, do Programa Minha Casa Minha Vida, entre outros. 

Para reduzir erros de inclusão, constantemente é feito um processo de qualificação cadastral. Neste ano, por exemplo, até o momento foram convocadas 3,3 milhões de famílias para averiguação do cadastro, o qual consiste em verificar as famílias que apresentam algum indício de inconsistência, seja de renda, de declaração de vínculo empregatício, ou de composição familiar.

Considerando a referência de setembro/2024, existem mais de 40 milhões de famílias incluídas no Cadastro Único, e 93 milhões de pessoas. Para uma melhor focalização das políticas públicas sociais usuárias deste cadastro para seleção dos beneficiários é preciso automatizar o processo de averiguação cadastral.

Para tanto, a proposta do presente projeto é propor um algoritmo que, a partir das características das família, seja possível classificar cada família em uma faixa de renda mais provável. Destaca-se que, considerando que as bases utilizadas são de 2018, os valores utilizados para a definição das faixas de renda serão as vigentes em 2018, conforme segue abaixo:
* Pobreza: de 0 a 178,00, considerando a faixa de pobreza do Programa Bolsa Família em 2018;
* Baixa renda: de 178,01 a 1/2 salário-mínimo vigente em 2018, ou seja 477,00 considerando o salário-mínimo de 954,00;
* Acima de 1/2 salário-mínimo, ou seja, acima de 477,00.

No Cadastro Único a renda familiar mensal utilizada para o cálculo da renda média familiar é a soma dos rendimentos brutos, ou seja, sem descontos, auferidos por todos os integrantes da família. Nesse cálculo, não são incluídos os valores referentes aos seguintes programas:
* Benefícios e auxílios assistenciais de natureza eventual e temporária;
* Valores oriundos de programas assistenciais de transferência de renda, com exceção do Benefício de Prestação Continuada de que trata o art. 20 da Lei nº 8.742, de 1993;
* Rendas de natureza eventual ou sazonal, na forma estabelecida em ato do Ministro de Estado do MDS; e
* Outros rendimentos, na forma estabelecida em ato do Ministro de Estado do MDS.

O valor da renda familiar mensal é dividida então pelo número de pessoas que compõem a família, variável 'qtd_pessoas' da **Base de Família**.
  
O modelo objetiva auxiliar em uma maior focalização das políticas públicas sociais para as famílias que apresentam características relacionadas à maior vulnerabilidade de renda, identificando famílias que apresentam caracterísiticas não esperadas para a faixa de renda apresentada, guiando ações de qualificação do Cadastro Único.

## Benefícios do uso do algoritmo de ML para automatização do processo de averiguação cadastral
* É possível incluir toda a base do Cadastro Único na análise de definição do público de averiguação cadastral, sem a necessidade de definição de amostra, ao aplicar o modelo de ML no universo total;
* É possível identificar as variáveis que contribuem diretamente para a definição automática das famílias a serem incluídas no processo de averigação cadastral, evitando critérios subjetivos para a seleção das variáveis;
* É possível atualizar o algoritmo com os dados mais atuais, de modo a acompanhar as mudanças das famílias ao longo do tempo. 

# Bases de dados utilizadas
As bases de dados utilizadas estão disponibilizadas no <a href="https://dados.gov.br/dados/conjuntos-dados/microdados-amostrais-do-cadastro-unico">Portal de Dados abertos do Governo Federal do MDS</a>.

As bases são amostrais, desidentificadas, sendo que as mais recentes disponíveis no portal de dados abertos, acessado em outubro/2024, são da referêcia de 2018.

Uma base apresenta os dados de pessoas e a outra base os dados das famílias. É possível combinar as duas bases de dados por meio da variável 'id_familia': Identificador único da família para pareamento com a base de pessoas. No caso da **Base famílias**, os dados estão relacionados à família, sendo uma por linha. No caso da **Base pessoas** é uma pessoa por linha, sendo que a variável 'id_familia' está repetida para as pessoas que compõem a mesma família. 

Como as bases são muito grandes, tendo a base de famílias mais de 4,8 milhões de linhas e a de pessoas mais de 12,8 milhões, foi preparada uma base amostral da base de famílias de 100 mil linhas retirando as colunas "nom_estab_assist_saude_fam", "cod_eas_fam", "nom_centro_assist_fam" e "cod_centro_assist_fam" por não serem relevantes para a construção do modelo e por apresentarem muitos valores vazios conforme imagem abaixo.

![Percentual_ausentes_base_fam](Perc_ausentes_fam.jpg)

Também foram retiradas as colunas relacionadas diretamente à renda da família, pois o objetivo do projeto é identificar as características das famílias que estão mais diretamente relacionadas à faixa de renda. A inclusão dos valores recebidos estão muito diretamente relacionados à classificação da renda e não permitiriam a avaliação das demais variáveis. Desta forma, para a análise, a variável 'marc_pbf' foi retirada da **Base famílias**, assim como as variáveis 'val_remuner_emprego_memb', 'val_renda_bruta_12_meses_memb', 'val_renda_doacao_memb', 'val_renda_aposent_memb', 'val_renda_seguro_desemp_memb', 'val_renda_pensao_alimen_memb' e 'val_outras_rendas_memb' foram retiradas na **Base pessoas**. 
Além disso, os valores são variáveis derivadas, utilizadas para o cálculo da 'vlr_renda_media_fam', que foi a base para a produção da variável target. Assim, o uso dessas variáveis poderia comprometer a eficácia do modelo ao vazar informação.  

Além disso, foram incluídas, após a coluna cd_ibge, duas novas colunas, uf_ibge e regiao_ibge, de modo a permitir a análise se essas variáveis contribuem para a acurácia do modelo.

A partir da base amostral de famílias, foi feito um merge com a base pessoas, usando o id_familia. Para tanto, foram excluídas as colunas "cd_ibge", "estrato" e "classf" da base de pessoas, pois são colunas comuns à base de famílias e não foram usadas para o merge, já que apenas o valor id_familia é único na base de famílias.

Registra-se que na base de pessoas também foram encontrados valores vazio, conforme imagem abaixo. Isso se deve a regras de preenchimento do formulário do Cadastro Único, que para alguns campos o seu preenchimento é condicionado ao preenchimento de outro. Desta forma, o processo de limpeza dos valores NaN foi realizado com base nessas regras e será detalhado em campo específico.

![Percentual_ausentes_base_pessoa](Perc_ausentes_pessoa.jpg)

Na base final, foram mantidades aproximadamente 100 mil famílias incluídas na base amostral de famílias e as pessoas da base de pessoas relacionadas com o mesmo id_familia da base amostral, resultando em uma base amostral de famílias e pessoas com mais de 250 mil linhas. Destaca-se que foram preparadas duas bases amostrais distintas, randomizadas e aleatórias, para apoiar o processo de construção do modelo.

Abaixo segue o dicionário das bases utilizadas.

## Base famílias

| Seq. | Nome da variável                 | Tipo   | Tamanho (Inteiro) | Tamanho (Decimal) | Descrição                                                                                                     |
|------|-----------------------------------|--------|-------------------|------------------|---------------------------------------------------------------------------------------------------------------|
| 1    | cd_ibge                          | String | 7                 |                  | Código IBGE do Município                                                                                       |
| 1a    | uf_ibge                          | Numeric | 2                 |              | Código IBGE da Unidade Federada: 12	- AC, 27 - AL, 13	- AM, 16 - AP, 29 -	BA, 23 - CE, 53 -	DF, 32	- ES, 52 - GO, 21 -	MA, 31 -	MG, 50 -	MS, 51	- MT, 15 - PA, 25 -	PB, 26 -	PE, 22	- PI, 41 -	PR, 33 -	RJ, 24	- RN, 11 - RO, 14 -	RR, 43 -	RS, 42 -	SC, 28 -	SE, 35 -	SP, 17 - TO  :exclamation::heavy_exclamation_mark: **(Coluna nova incluída na base amostral)** |
| 1b    | regiao_ibge                      | Numeric | 2                 |                  | Região da Unidade Federada: 1 - Norte, 2 - Nordeste, 3 - Sudeste, 4 - Sul, 5 - Centro-Oeste :exclamation::heavy_exclamation_mark: **(Coluna nova incluída na base amostral)**|
| 2    | dat_cadastramento_fam             | String | 8                 |                  | Data do cadastramento da família no formato YYYY-MM-DD  :exclamation::heavy_exclamation_mark:**(Coluna excluída na base amostral)**               |
| 3    | dat_alteracao_fam                 | Date   | 8                 |                  | Data da última alteração em qualquer campo da família no formato YYYY-MM-DD (Variável utilizada nos anos de 2014, 2015, 2016 e 2017)  :exclamation::heavy_exclamation_mark: **(Coluna excluída na base amostral)**    |
| 4    | vlr_renda_media_fam               | Numeric| 9                 |                  | Valor da renda média (per capita) da família, formato NNNNNNNNN (não tem a vírgula). Ex.: Uma renda de R$ 125,00 constará na base como 125   |
| 5    | dat_atualizacao_familia           | Date   | 8                 |                  | Data da última atualização da família dos dados considerados sensíveis à manutenção do cadastro no formato YYYY-MM-DD (2014-2017)    :exclamation::heavy_exclamation_mark:**(Coluna excluída na base amostral)**      |
| 6    | dat_atual_fam                     | Date   | 8                 |                  | Data da última alteração em qualquer campo da família no formato YYYY-MM-DD (variável utilizada nos anos de 2012 e 2013)         :exclamation::heavy_exclamation_mark: **(Coluna excluída na base amostral)**     |
| 7    | cod_local_domic_fam               | Numeric| 1                 |                  | Características do local onde está situado o domicílio: 1 - Urbanas, 2 - Rurais, 9 - Nenhuma das respostas anteriores   |
| 8    | cod_especie_domic_fam             | Numeric| 1                 |                  | Espécie do domicílio: 1 - Particular Permanente, 2 - Particular improvisado, 3 - Coletivo, 9 - Nenhuma das respostas anteriores    |
| 9    | qtd_comodos_domic_fam             | Numeric| 2                 |                  | Quantidade de cômodos do domicílio ou -1 quando o campo não se aplica                                          |
| 10   | qtd_comodos_dormitorio_fam        | Numeric| 2                 |                  | Quantidade de cômodos servindo como dormitório do domicílio ou -1 quando o campo não se aplica        |
| 11   | cod_material_piso_fam             | Numeric| 1                 |                  | Material predominante no piso do domicílio: 1 - Terra, 2 - Cimento, 3 - Madeira aproveitada, 4 - Madeira aparelhada, 5 - Cerâmica, lajota ou pedra, 6 - Carpete, 7 - Outro Material ou -1 quando o campo não se aplica   |
| 12   | cod_material_domic_fam            | Numeric| 1                 |                  | Material predominante nas paredes externas do domicílio: 1 - Alvenaria/tijolo com revestimento, 2 - Alvenaria/tijolo sem revestimento,  3 - Madeira aparelhada, 4 - Taipa revestida, 5 - Taipa não revestida, 6 - Madeira aproveitada, 7 - Palha, 8 - Outro Material ou -1 quando o campo não se aplica  |
| 13   | cod_agua_canalizada_fam           | Numeric| 1                 |                  | Se o domicílio tem água encanada: 1 - Sim, 2 - Não  ou -1 quando o campo não se aplica   |
| 14   | cod_abaste_agua_domic_fam         | Numeric| 1                 |                  | Forma de abastecimento de água: 1 - Rede geral de distribuição, 2 - Poço ou nascente, 3 - Cisternas, 4 - Outra forma ou -1 quando o campo não se aplica    |
| 15   | cod_banheiro_domic_fam            | Numeric| 1                 |                  | Existência de banheiro: 1 - Sim, 2 - Não   ou -1 quando o campo não se aplica            |
| 16   | cod_escoa_sanitario_domic_fam     | Numeric| 1                 |                  | Forma de escoamento sanitário: 1 - Rede coletora de esgoto ou pluvial, 2 - Fossa séptica,  3 - Fossa rudimentar, 4 - Vala a céu aberto, 5 - Direto para um rio, lago ou mar,   6 - Outra forma ou -1 quando o campo não se aplica     |
| 17   | cod_destino_lixo_domic_fam        | Numeric| 1                 |                  | Forma de coleta do lixo: 1 - É coletado diretamente, 2 - É coletado indiretamente, 3 - É queimado ou enterrado na propriedade,  4 - É jogado em terreno baldio ou logradouro (rua, avenida, etc.), 5 - É jogado em rio ou mar, 6 - Tem outro destino ou -1 quando o campo não se aplica     |
| 18   | cod_iluminacao_domic_fam          | Numeric| 1                 |                  | Tipo de iluminação: 1 - Elétrica com medidor próprio, 2 - Elétrica com medidor comunitário, 3 - Elétrica sem medidor, 4 - Óleo, querosene ou gás, 5 - Vela, 6 - Outra forma ou -1 quando o campo não se aplica   |
| 19   | cod_calcamento_domic_fam          | Numeric| 1                 |                  | Calçamento: 1 - Total, 2 - Parcial, 3 - Não existe ou -1 quando o campo não se aplica  |
| 20   | cod_familia_indigena_fam          | Numeric| 1                 |                  | Família indígena: 1 - Sim, 2 - Não                                                                             |
| 21   | ind_familia_quilombola_fam        | Numeric| 1                 |                  | Família quilombola: 1 - Sim, 2 - Não                                                                           |
| 22   | nom_estab_assist_saude_fam        | String | 70                |                  | Nome do estabelecimento EAS/MS   :exclamation::heavy_exclamation_mark: **(Coluna excluída na base amostral)**     |
| 23   | cod_eas_fam                       | String | 12                |                  | Código do estabelecimento EAS/MS  :exclamation::heavy_exclamation_mark:  **(Coluna excluída na base amostral)**    |
| 24   | nom_centro_assist_fam             | String | 70                |                  | Nome do CRAS/CREAS :exclamation::heavy_exclamation_mark: **(Coluna excluída na base amostral)**            |
| 25   | cod_centro_assist_fam             | String | 12                |                  | Código do CRAS/CREAS :exclamation::heavy_exclamation_mark:  **(Coluna excluída na base amostral)**     |
| 26   | ind_parc_mds_fam                  | Numeric| 3                 |                  | Grupos tradicionais e específicos: 101 Família Cigana, 201 Família Extrativista, 202 Família de Pescadores, 203 Família pertencente a Comunidade de Terreiro, 204 Família Ribeirinha, 205 Família de Agricultores Familiares, 301 Família Assentada da Reforma Agrária, 302 Família beneficiária do Programa Nacional de Crédito Fundiário, 303 Família Acampada, 304 Família Atingida por Empreendimentos de Infraestrutura, 305 Família de Preso do Sistema Carcerário, 306 Família de Catadores de Material Reciclável, 000 Nenhuma ou 9 - Nenhuma das respostas anteriores|
| 27   | peso_fam                          | Numeric| 1                 | 14               | Peso calculado da família                                                                                      |
| 28   | id_familia                        | Numeric| 8                 |                  | Identificador único da família para pareamento com a base de pessoas                                           |
| 29   | estrato                           | Numeric| 1                 |                  | Grandes grupos de municípios, de acordo com a quantidade de famílias cadastradas: 1 - GM1 (101 a 5.000 famílias) ou 2 - GM1 (5.001 ou mais famílias) |
| 30   | classf                            | Numeric| 1                 |                  | Subdivisão pela Unidade Federativa e divisão administrativa: 1 - Capital, 2 - Região Metropolitana (RM) ou Região Integrada de Desenvolvimento (RIDE), 3 - Outros          |
| 31   | qtd_pessoas                       | Numeric| 1                 |                  | Quantidade de pessoas utilizada no cálculo da renda per capita familiar – variável calculada pelo sistema        |
| 32   | marc_pbf                          | Numeric| 1                 |                  | Marcação se a família é beneficiária do Programa Bolsa Família: 0 – Não, 1 – Sim **(Coluna excluída na base amostral)**  |
| 33 | dias_cadastramento                  | Numeric | 1 a 4            |                  | Número de dias entre 31/12/2018 e a data dat_cadastramento_fam  :exclamation::heavy_exclamation_mark: **(Coluna nova incluída na base amostral)**|
| 34 | dias_atualizacao                   | Numeric | 1 a 4            |                  | Número de dias entre 31/12/2018 e a data dat_atualizacao_familia  :exclamation::heavy_exclamation_mark: **(Coluna nova incluída na base amostral)**|
| 35 | classe_renda                      | Numeric  | 1                |                   | Classificação da faixa de renda da família, calculada a partir do vlr_renda_media_fam: 0 - pobreza, 1 - baixa renda, 2 - acima de 1/2 S.M. :exclamation::heavy_exclamation_mark: **(Coluna nova incluída na base amostral)**|


## Base pessoas

| Seq. | Nome da variável                 | Tipo    | Tamanho (Inteiro) | Tamanho (Decimal) | Descrição                                                                                                                                           |
|------|-----------------------------------|---------|-------------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| 1    | cd_ibge                          | String  | 7                 |                   | Código IBGE do Município :exclamation::heavy_exclamation_mark:   **(Coluna excluída na base amostral)**        |
| 2    | cod_sexo_pessoa                  | Numeric | 1                 |                   | Sexo: 1 - Masculino, 2 - Feminino                                                                                                                    |
| 3    | idade                            | Numeric | 3                 |                   | Idade calculada a partir da diferença entre a data de nascimento da pessoa e a data de referência da base                                             |
| 4    | cod_parentesco_rf_pessoa          | Numeric | 2                 |                   | Relação de parentesco com o RF: 1 - Pessoa Responsável pela Unidade Familiar, 2 - Cônjuge ou companheiro(a), 3 - Filho(a), 4 - Enteado(a), 5 - Neto(a) ou bisneto(a), 6 - Pai ou mãe,  7 - Sogro(a), 8 - Irmão ou irmã,  9 - Genro ou nora, 10 - Outro parente, 11 - Não parente    |
| 5    | cod_raca_cor_pessoa              | Numeric | 1                 |                   | Cor ou raça: 1 - Branca, 2 - Preta, 3 - Amarela, 4 - Parda, 5 - Indígena                                                                             |
| 6    | cod_local_nascimento_pessoa      | Numeric | 1                 |                   | Local de nascimento: 1 - Neste município, 2 - Em outro município, 3 - Em outro país                                                                  |
| 7    | cod_certidao_registrada_pessoa   | Numeric | 1                 |                   | Pessoa registrada em cartório: 1 - Sim e tem Certidão de Nascimento, 2 - Sim, mas não tem Certidão, 3 - Não                                           |
| 8    | cod_deficiencia_memb             | Numeric | 1                 |                   | Pessoa tem deficiência: 1 - Sim, 2 - Não                                                                                                             |
| 9    | cod_sabe_ler_escrever_memb       | Numeric | 1                 |                   | Pessoa sabe ler e escrever: 1 - Sim, 2 - Não                                                                                                         |
| 10   | ind_frequenta_escola_memb        | Numeric | 1                 |                   | Pessoa frequenta escola: 1 - Sim, rede pública, 2 - Sim, rede particular, 3 - Não, já frequentou, 4 - Nunca frequentou                               |
| 11   | cod_escola_local_memb            | Numeric | 1                 |                   | Escola localizada no município: 1 - Sim, 2 - Não ou -1 quando o campo não se aplica                                                                  |
| 12   | cod_curso_frequenta_memb         | Numeric | 2                 |                   | Curso que a pessoa frequenta: 1 - Creche, 2 - Pré-escola (exceto CA), 3 - Classe de Alfabetização - CA, 4 - Ensino Fundamental regular (duração 8 anos),  5 - Ensino Fundamental regular (duração 9 anos), 6 - Ensino Fundamental especial, 7 - Ensino Médio regular, 8 - Ensino Médio especial, 9 - Ensino Fundamental EJA - séries iniciais (Supletivo - 1ª a 4ª),  10 - Ensino Fundamental EJA - séries finais (Supletivo - 5ª a 8ª), 11 - Ensino Médio EJA (Supletivo), 12 - Alfabetização para adultos (Mobral, etc.), 13 - Superior, Aperfeiçoamento, Especialização, Mestrado, Doutorado, 14 - Pré-vestibular ou -1 quando o campo não se aplica |
| 13   | cod_ano_serie_frequenta_memb     | Numeric | 2                 |                   | Ano e série que a pessoa frequenta: 1 - Primeiro, 2 - Segundo, 3 - Terceiro, 4 - Quarto(a), 5 - Quinto(a), 6 - Sexto(a), 7 - Sétimo(a), 8 - Oitavo(a), 9 - Nono(a), 10 - Curso não-seriado ou -1 quando o campo não se aplica |
| 14   | cod_curso_frequentou_pessoa_memb | Numeric | 2                 |                   | Curso mais elevado que a pessoa frequentou: 1 - Creche, 2 - Pré-escola (exceto CA), 3 - Classe de Alfabetização - CA, 4 - Ensino Fundamental 1ª a 4ª séries, Elementar (Primário), Primeira fase do 1º grau, 5 - Ensino Fundamental 5ª a 8ª séries, Médio 1º ciclo (Ginasial), Segunda fase do 1º grau, 6 - Ensino Fundamental (duração 9 anos), 7 - Ensino Fundamental Especial, 8 - Ensino Médio, 2º grau, Médio 2º ciclo (Científico, Clássico, Técnico, Normal), 9 - Ensino Médio Especial, 10 - Ensino Fundamental EJA - séries iniciais (Supletivo 1ª a 4ª), 11 - Ensino Fundamental EJA - séries finais (Supletivo 5ª a 8ª), 12 - Ensino Médio EJA (Supletivo), 13 - Superior, Aperfeiçoamento, Especialização, Mestrado, Doutorado, 14 - Alfabetização para Adultos (Mobral, etc.), 15 - Nenhum ou -1 quando o campo não se aplica  |
| 15   | cod_ano_serie_frequentou_memb    | Numeric | 2                 |                   | Último ano e série frequentado pela pessoa: 1 - Primeiro, 2 - Segundo, 3 - Terceiro, 4 - Quarto(a), 5 - Quinto(a), 6 - Sexto(a), 7 - Sétimo(a), 8 - Oitavo(a), 9 - Nono(a), 10 - Curso não-seriado ou -1 quando o campo não se aplica  |
| 16   | cod_concluiu_frequentou_memb     | Numeric | 1                 |                   | A pessoa concluiu o curso: 1 - Sim, 2 - Não  ou -1 quando o campo não se aplica                                    |
| 17   | cod_trabalhou_memb               | Numeric | 1                 |                   | Pessoa trabalhou na semana passada: 1 - Sim, 2 - Não  ou -1 quando o campo não se aplica                                           |
| 18   | cod_afastado_trab_memb           | Numeric | 1                 |                   | Pessoa afastada na semana passada: 1 - Sim, 2 - Não ou -1 quando o campo não se aplica                                                |
| 19   | cod_agricultura_trab_memb        | Numeric | 1                 |                   | É atividade extrativista: 1 - Sim, 2 - Não, -1 quando o campo não se aplica  ou 9 - para desconhecido                   |
| 20   | cod_principal_trab_memb          | Numeric | 2                 |                   | Função principal: 1 - Trabalhador por conta própria, 2 - Trabalhador temporário em área rural, 3 - Empregado sem carteira de trabalho assinada, 4 - Empregado com carteira de trabalho assinada, 5 - Trabalhador doméstico sem carteira de trabalho assinada, 6 - Trabalhador doméstico com carteira de trabalho assinada, 7 - Trabalhador não-remunerado, 8 - Militar ou servidor público, 9 - Empregador, 10 - Estagiário, 11 - Aprendiz ou -1 quando o campo não se aplica|
| 21   | val_remuner_emprego_memb         | Numeric | 5                 |                   | Valor da remuneração no formato NNNNN (sem casas decimais). Ex: uma remuneração de R$ 125,00 constará na base como 125         :exclamation::heavy_exclamation_mark: **(Coluna excluída na base amostral)** |
| 22   | cod_trabalho_12_meses_memb       | Numeric | 1                 |                   | Pessoa com trabalho remunerado em algum período nos últimos 12 meses: 1 - Sim, 2 - Não  ou -1 quando o campo não se aplica      |
| 23   | qtd_meses_12_meses_memb          | Numeric | 2                 |                   | Quantidade de meses trabalhados nos últimos 12 meses ou -1 quando o campo não se aplica                    |
| 24   | val_renda_bruta_12_meses_memb    | Numeric | 5                 |                   | Valor de remuneração bruta no formato NNNNN (sem casas decimais). Ex: uma remuneração de R$ 125,00 constará na base como 125   :exclamation::heavy_exclamation_mark: **(Coluna excluída na base amostral)**  |
| 25   | val_renda_doacao_memb            | Numeric | 5                 |                   | Valor recebido de doação no formato NNNNN (sem casas decimais). Ex: uma renda de R$ 125,00 constará na base como 125           :exclamation::heavy_exclamation_mark: **(Coluna excluída na base amostral)**  |
| 26   | val_renda_aposent_memb           | Numeric | 5                 |                   | Valor recebido de aposentadoria no formato NNNNN (sem casas decimais). Ex: uma remuneração de R$ 125,00 constará na base como 125  :exclamation::heavy_exclamation_mark: **(Coluna excluída na base amostral)**  |
| 27   | val_renda_seguro_desemp_memb     | Numeric | 5                 |                   | Valor recebido de seguro desemprego no formato NNNNN (sem casas decimais). Ex: um valor de R$ 125,00 constará na base como 125   :exclamation::heavy_exclamation_mark: **(Coluna excluída na base amostral)** |
| 28   | val_renda_pensao_alimen_memb     | Numeric | 5                 |                   | Valor recebido de pensão alimentícia no formato NNNNN (sem casas decimais). Ex: uma renda de R$ 125,00 constará na base como 125    :exclamation::heavy_exclamation_mark: **(Coluna excluída na base amostral)**  |
| 29   | val_outras_rendas_memb           | Numeric | 5                 |                   | Valor recebido de outras fontes no formato NNNNN (sem casas decimais). Ex: uma renda de R$ 125,00 constará na base como 125       :exclamation::heavy_exclamation_mark: **(Coluna excluída na base amostral)**  |
| 30   | peso.fam                        | Numeric | 1                 | 14                | Peso calculado da família                                                                                                         :exclamation::heavy_exclamation_mark: **(Coluna excluída na base amostral)**  |
| 31   | peso.pes                        | Numeric | 1                 | 14                | Peso calculado da pessoa                                                                                                                             |
| 32   | id_familia                      | Numeric | 8                 |                   | Identificador único da família de vinculação da pessoa para pareamento com a base de famílias                                                        |
| 33   | estrato                         | Numeric | 1                 |                   | São grandes grupos de municípios, de acordo com a quantidade de famílias cadastradas: 1 - GM1 (101 A 5.000 famílias), 2 - GM2 (5.001 ou mais famílias)  :exclamation::heavy_exclamation_mark: **(Coluna excluída na base amostral)**   |
| 34   | classf                          | Numeric | 1                 |                   | Subdivisão pela Unidade Federativa e divisão administrativa: 1 - Capital, 2 - Região Metropolitana (RM) ou Região Integrada de Desenvolvimento (RIDE) :exclamation::heavy_exclamation_mark:  **(Coluna excluída na base amostral)**   |

## Limpeza das bases
Tanto na **Base famílias**, quanto na **Base pessoas** existe um número considerável de valores vazios considerando as regras de preenchimento do formulário do Cadastro Único. Assim, foi necessário olhar para as regras de preenchimento do formulário do Cadastro Único, com base no Manual do Entrevistador do Cadastro Único, de modo a identificar os valores vazios pelo fato de não serem de preenchimento obrigatório.
Assim foram realizadas as seguintes limpezas dos valores NaN:

### Base famílias
#### Campos relacionados às características do domicílio:
Os campos 'qtd_comodos_domic_fam', 'qtd_comodos_dormitorio_fam', 'cod_material_piso_fam', 'cod_material_domic_fam', 'cod_agua_canalizada_fam', 'cod_abaste_agua_domic_fam', 'cod_banheiro_domic_fam', 'cod_escoa_sanitario_domic_fam', 'cod_destino_lixo_domic_fam', 'cod_iluminacao_domic_fam', 'cod_calcamento_domic_fam' só são de preenchimento obrigatório no caso da resposta ter sido "1- Particular permamente" no campo 'cod_especie_domic_fam'. Sendo assim, quando o campo 'cod_especie_domic_fam' é diferente de 1, os valores dos campos relacionados às características do domicílio foi preenchido com **-1**.
#### Campo relacionado ao escoamento sanitário:
O campo 'cod_escoa_sanitario_domic_fam' só é de preenchimento obrigatório quando o campo 'cod_banheiro_domic_fam' é preenchido com "1 - Sim". Desta forma, quando o campo 'cod_banheiro_domic_fam' é igual a 2 (ou seja, não possui banheiro), o valor do campo 'cod_escoa_sanitario_domic_fam' foi preenchido com **-1**.
#### Campo relacionado à família quilombola:
O campo 'ind_familia_quilombola_fam' só deve ser preenchido caso o campo 'cod_familia_indigena_fam' for "2 - Não". Assim, quando o campo 'cod_familia_indigena_fam' é igual a 1 (ou seja, a família for indígena), o valor do campo 'ind_familia_quilombola_fam' foi marcado como **2**, ou seja, a família não é quilombola.
#### Campos relacionados ao local do domicílio e à espécie do domicílio:
Foi identificado que os valores vazios dos campos 'cod_especie_domic_fam' e 'cod_local_domic_fam' coincidem, ou seja, quando um valor é vazio na campo 'cod_especie_domic_fam' também é vazio no campo 'cod_local_domic_fam'. Na base de dados amostral de 2018 disponível no portal de dados abertos, não tem a marcação se a família vive em situação de rua. No Manual do entrevistador há a orientação de que, caso a família esteja em situação de rua, o bloco 2 - características do domicílio não deve ser preenchido, pois existe um cadastramento diferenciado. Desta forma, este caso de valores ausentes pode estar relacionado à situação de rua. De modo a tentar captar se essa condição interfere no modelo, os valores dos dois campos foram preenchidos com **9**, representando nenhuma das outras repostas.
#### Campos relacionadas à Grupos tradicionais e específicos
O campo 'ind_parc_mds_fam' está relacionado à marcação de grupos tradicionais e específicos para além de indígena, quilombola, situação de rua ou resgatados do trabalho análogo ao de escravo. Foi avaliado se os valores ausentes estavam relacionados à marcação de indígena ou quilombola, ou ao valor 9 para 'cod_especie_domic_fam' e 'cod_local_domic_fam' criado na tentativa de captar as famílias em situação de rua. Não foi identificado o motivo dos valores vazios. Assim, de modo a tentar captar se a ausência de marcação deste campo pode representar alguma situação que impacte no modelo, os valores vazios foram preenchidos com **9**, representando nenhuma das outras repostas.
#### Valores vazios remanescentes
Após todas as limpezas descritas acima, ficou um resquício insignificantes de linhas com valores vazios que foram excluídas da base:
* qtd_comodos_domic_fam         41
* qtd_comodos_dormitorio_fam    10
* classe_renda                   3

### Base pessoas
#### Campo frequenta escola
Os campos 'cod_escola_local_memb', 'cod_curso_frequenta_memb', 'cod_ano_serie_frequenta_memb' só são obrigatório se a pessoa respondeu "1 - Sim, rede pública", "2 - Sim, rede particular" no campo 'ind_frequenta_escola_memb'. Desta forma, quando o campo 'ind_frequenta_escola_memb' foi preenchido com valor diferente de 1 ou 2, os campos vazios relacionados foram preenchidos com **-1**.
#### Campo ano e série que a pessoa frequenta
O campo 'cod_ano_serie_frequenta_memb' só é obrigatório ser preenchido quando no campo 'cod_curso_frequenta_memb' (curso que a pessoa frequenta) a pessoa respondeu uma das opções: 4 - Ensino Fundamental regular (duração 8 anos), 5 - Ensino Fundamental regular (duração 9 anos), 6 - Ensino Fundamental especial, 7 - Ensino Médio regular ou 8 - Ensino Médio especial. Assim, quando o campo 'cod_curso_frequenta_memb' foi preenchido com valor difente de 4, 5, 6, 7 ou 8 os valores vazios de 'cod_ano_serie_frequenta_memb' foram preenchidos com **-1**.
#### Campo curso mais elevado que frequentou
O campo 'cod_curso_frequentou_pessoa_memb' só é obrigatório quando o campo 'ind_frequenta_escola_memb' (Pessoa frequenta escola?) for respondido com "3 - Não, já frequentou". Assim, quando o campo 'ind_frequenta_escola_memb' estava diferente de 3, os valores vazios do campo 'cod_curso_frequentou_pessoa_memb' foram preenchidos com **-1**.
#### Campos relacionados ao curso frequentado
Os campos 'cod_ano_serie_frequentou_memb' e 'cod_concluiu_frequentou_memb' só devem ser preenchidos caso a pessoa frequentou algum dos cursos 4 - Ensino Fundamental 1ª a 4ª séries, Elementar (Primário), Primeira fase do 1º grau, 5 - Ensino Fundamental 5ª a 8ª séries, Médio 1º ciclo (Ginasial), Segunda fase do 1º grau, 6 - Ensino Fundamental (duração 9 anos), 7 - Ensino Fundamental Especial, 8 - Ensino Médio, 2º grau, Médio 2º ciclo (Científico, Clássico, Técnico, Normal) ou 9 - Ensino Médio Especial no campo 'cod_curso_frequentou_pessoa_memb'. Desta forma, quando a resposta do campo 'cod_curso_frequentou_pessoa_memb' foi diferente de 4, 5, 6, 7, 8 e 9 os valores vazios dos campos 'cod_ano_serie_frequentou_memb' e 'cod_concluiu_frequentou_memb' foi preenchido com **-1**.
#### Campos relacionados ao trabalho
Os campos 'cod_trabalhou_memb', 'cod_afastado_trab_memb', 'cod_agricultura_trab_memb', 'cod_principal_trab_memb', 'cod_trabalho_12_meses_memb', 'qtd_meses_12_meses_memb' só devem ser preenchidos para pessoas com 14 anos ou mais. Assim, para o caso de pessoas com idade menor que 14 anos, no campo 'idade', os valores dos campos relacionados ao trabalho foram preenchidos com **-1**.
#### Campo relacionado ao afastamento do trabalho
O campo 'cod_afastado_trab_memb' só deve ser respondido se o campo 'cod_trabalhou_memb' (Pessoa trabalhou na semana passada?) for respondido como "2 - Não". Assim, para os casos de resposta diferente de 2, os valores vazios do campo 'cod_afastado_trab_memb' foram preenchidos com **-1**.
#### Campo relacionado à atividade extrativista e ao trabalho principal
O campo 'cod_agricultura_trab_memb' (É atividade extrativista? 1 - Sim e 2 - Não) e o campo 'cod_principal_trab_memb' só são obrigatórios se a pessoa respondeu 1 - Sim no campo 'cod_trabalhou_memb' (Pessoa trabalhou na semana passada?) ou no campo 'cod_afastado_trab_memb' (Pessoa afastada na semana passada?). Assim, para o caso em que os 'cod_trabalhou_memb' e 'cod_afastado_trab_memb' tiveram resposta diferente de 1, os valores vazios de 'cod_agricultura_trab_memb' e de 'cod_principal_trab_memb' foram substituídos por **-1**. 
Além disso, observou-se ainda alguns valores vazios remanescentes para o campo 'cod_agricultura_trab_memb'. Desta forma, foi avaliado o preenchimento do campo 'cod_principal_trab_memb'. Quando este estava marcado com "2 - Trabalhador temporário em área rural", o valor vazio do campo 'cod_agricultura_trab_memb' foi alterado para "**1** - Sim" e para os demais casos para **9** - Desconhecido.  
#### Campo relacionado à quantidade de meses trabalhados
O campo 'qtd_meses_12_meses_memb' (Quantidade de meses trabalhados nos últimos 12 meses) só é obrigatório se a pessoa tiver respondido "1 - Sim" no campo 'cod_trabalho_12_meses_memb' (Pessoa com trabalho remunerado em algum período nos último 12 meses). Desta forma, os valores vazios do campo 'qtd_meses_12_meses_memb' foi alterado para **-1** quando o campo 'cod_trabalho_12_meses_memb' for diferente de 1.
#### Valores vazios remanescentes
Foram feitas diversas análises adicionais para identificar possíveis ajustes nos valores vazios finais. Entretanto, não foi identificada outra situação de valor vazio que parece estar relacionado à regra de preenchimento do Cadastro Único. Desta forma, as linhas com valores vazios remanescentes foram excluídas, conforme segue abaixo. Destaca-se que esses valores são pouco representativos frente ao total de linhas da base amostral de pessoas, que possui mais de 260 mil linhas.
* cod_raca_cor_pessoa                  107
* cod_local_nascimento_pessoa         1118
* cod_sabe_ler_escrever_memb            45
* ind_frequenta_escola_memb             49
* cod_escola_local_memb                661
* cod_curso_frequenta_memb              13
* cod_curso_frequentou_pessoa_memb      13
* cod_ano_serie_frequentou_memb          2
* cod_trabalhou_memb                   643
* cod_trabalho_12_meses_memb           676

Após a limpeza da base amostral de pessoas, foi feito um merge com a base amostral de famílias, de modo a retirar as famílias que tiveram pessoas excluídas, gerando uma base final com mais de 96 mil famílias e com mais de 250 mil pessoas.

# Variável dependente (target)
A variavél dependente do projeto é classe_renda:
* Classe 0 (pobreza);
* Classe 1 (baixa renda);
* Classe 2 (acima 1/2 S.M.).

# Variáveis independentes (features)
Para a seleção das variáveis independentes, serão aplicadas técnicas de Machine Learning para definição das que contribuem diretamente para a classificação mais adequada das famílias nas classes de renda. Além disso, será realizada engenharia de features para a construção de novas variáveis, a partir das existentes, que podem contribuir para a maior acurácia do modelo. 
De modo a ouvir a área de negócio, foram realizadas reuniões com a Coordenadora-Geral de Acompanhamento e Qualificação do Cadastro, do Departamento de Operação do Cadastro Único (CGAQC/DECAU). 
A partir das contribuições da área de negócio e com o objetivo de possibilitar o exercício por todos os autores do projeto no âmbito do Bootcamp, as análises foram dividdas em grupos temáticos, conforme se segue:

## Características do Responsável Familiar - Mariana:
---
O Responsável pela Unidadde Familiar (RUF) é a pessoa responsável por prestar as informações ao Cadastro Único em nome da família, que pode ser: 
* Responsável Familiar (RF) - deve ser um dos componentes da família e morador do domicílio, com idade mínima de 16 (dezesseis) anos, preferencialmente mulher;
* Representante Legal (RL) - indivíduo não membro da família e que não seja morador do domicílio, legalmente responsável por pessoas menores de dezesseis anos ou incapazes e responsável por prestar as informações ao Cadastro Único, quando não houver morador caracterizado como Responsável Familiar. Nas situações em que a família tiver o RL, este a representará e atuará em nome da família que está sendo cadastrada. Sendo assim, o RL
que será entrevistado para prestar as informações da família e de seus integrantes. No momento da entrevista, as informações de todas as pessoas da família devem ser prestadas pelo RUF.

De modo a avaliar se as características do RF contribuem para a acurácia do modelo, serão incluídas as seguintes variáveis no modelo da **Base Pessoas** para 'cod_parentesco_rf_pessoa' igual a 1, ou seja, "Pessoa Responsável pela Unidade Familiar":
* cod_sexo_pessoa;
* idade;
* cod_raca_cor_pessoa;
* cod_local_nascimento_pessoa;
* cod_certidao_registrada_pessoa;
* cod_deficiencia_memb;
* cod_sabe_ler_escrever_memb;
* ind_frequenta_escola_memb;
* cod_escola_local_memb;
* cod_curso_frequenta_memb;
* cod_ano_serie_frequenta_memb;
* cod_curso_frequentou_pessoa_memb;
* cod_ano_serie_frequentou_memb;
* cod_concluiu_frequentou_memb;
* cod_trabalhou_memb;
* cod_afastado_trab_memb;
* cod_agricultura_trab_memb;
* cod_principal_trab_memb;
* cod_trabalho_12_meses_memb;
* qtd_meses_12_meses_memb.

### Resultado da análise
Foi realizada a análise das variáveis relacionadas ao responsável familiar a partir da base amostral de pessoas, filtrando 'cod_parentesco_rf_pessoa' igual a 1. Para tanto, foi gerada uma matriz de correlação das variáveis, conforme figura abaixo.
![Matriz_correlacao](https://github.com/user-attachments/assets/0096bd1b-da05-4507-8911-4429fc256914)

A partir da análise da matriz, foram retiradas as variáveis com correlação maior que 0.8, por terem uma forte relação linear entre si, sendo retiradas do dataframe as variáveis: 'cod_afastado_trab_memb', 'qtd_meses_12_meses_memb' e 'cod_trabalho_12_meses_memb'.

Após essa etapa, foram testados quatro modelos preditivos que são indicados para modelos com variáveis numéricas categóricas e quantitativas. Após o treinamento dos modelos e busca de hiperparâmetros, foram indentificados os seguites resultados para cada um dos modelos:
* Melhores hiperparâmetros para DecisionTree: {'classifier__max_depth': 7, 'classifier__min_samples_split': 10}
* Melhores hiperparâmetros para RandomForest: {'classifier__max_depth': 10, 'classifier__n_estimators': 100}
* Melhores hiperparâmetros para XGBoost: {'classifier__learning_rate': 0.1, 'classifier__max_depth': 5, 'classifier__n_estimators': 300}
* Melhores hiperparâmetros para CatBoost: {'classifier__depth': 5, 'classifier__iterations': 500, 'classifier__learning_rate': 0.1}

| DecisionTree | RandomForest | XGBoost | CatBoost |
| ----- | ------ | ------- | ------- |
|  F1 Score: 0.58 |  F1 Score: 0.57 | F1 Score: 0.58 | F1 Score: 0.58 |
 | Acurácia: 0.71 | Acurácia: 0.71 | Acurácia: 0.72 |   Acurácia: 0.72 |

Posteriormente foram identificadas as variáveis independentes que mais contribuíram para cada um dos modelos estudados, conforme listagem abaixo das 5 features mais importantes:
* As 5 Features mais importantes para o modelo DecisionTree e a sua importância:
  * idade - 0.134895;
  * cod_principal_trab_memb - 0.067074;
  * cod_trabalhou_memb - 0.022994;
  * cod_deficiencia_memb - 0.019315;
  * cod_curso_frequenta_memb -  0.005036.
* As 5 Features mais importantes para o modelo RandomForest e a sua importância:
  * idade - 0.132884;
  * cod_principal_trab_memb - 0.049982;
  * cod_deficiencia_memb - 0.010507;
  * cod_agricultura_trab_memb - 0.008699;
  * cod_sexo_pessoa - 0.006098.
* As 5 Features mais importantes para o modelo XGBoost:
  * idade - 0.145930;
  * cod_principal_trab_memb - 0.060059;
  * cod_deficiencia_memb - 0.012771;
  * cod_agricultura_trab_memb - 0.010870;
  * cod_curso_frequentou_pessoa_memb - 0.005735.
* As 5 Features mais importantes para o modelo CatBoost:
  * idade - 0.149101;
  * cod_principal_trab_memb - 0.059360;
  * cod_deficiencia_memb - 0.013621;
  * cod_agricultura_trab_memb - 0.010150;
  * cod_sexo_pessoa - 0.005751.

Abaixo, segue gráfico com a análise da importância de todas as features para o modelo CatBoost.

![Importancia_features](https://github.com/user-attachments/assets/1ec7761a-0b6f-4ac8-91b2-90458404f11d)

Posteriormente, considerando que a variável target está desbalanceada, tendo 58% de famílias da amostra na classe 0, 21% na classe 1 e 20% na classe 2, foi feito um balanceamento aumentando a amostra para as classes 1 e 2, usando a estratégia de criar amostras sintéticas, e a redução de amostras da classe 0. Após o balanceamento, observou-se os seguintes resultados de cada modelo.
* Melhores hiperparâmetros para DecisionTree (usando dados balanceados): {'classifier__max_depth': 7, 'classifier__min_samples_split': 5}
* Melhores hiperparâmetros para RandomForest (usando dados balanceados): {'classifier__max_depth': 20, 'classifier__n_estimators': 200}
* Melhores hiperparâmetros para XGBoost (usando dados balanceados): {'classifier__learning_rate': 0.1, 'classifier__max_depth': 5, 'classifier__n_estimators': 300}
* Melhores hiperparâmetros para CatBoost (usando dados balanceados): {'classifier__depth': 5, 'classifier__iterations': 500, 'classifier__learning_rate': 0.1}
  
| DecisionTree - balanceado | RandomForest - balanceado | XGBoost - balanceado | CatBoost - balanceado |
| ------ | ----- | ----- | ----- |
|  F1 Score: 0.59 | F1 Score: 0.65 | F1 Score: 0.62 | F1 Score: 0.61 |
 | Acurácia: 0.62 |  Acurácia: 0.66 | Acurácia: 0.63 | F1 Score: 0.61 |

Em relação às features mais importantes, após o balanceamento, segue o resumo do que foi observado:
* Features que estão entre as cinco mais importantes em todos os modelos, antes e depois do balanceamento:
  * idade
  * cod_principal_trab_memb
  * cod_deficiencia_memb
* Demais features:
  * cod_sexo_pessoa:
    * Entre as 5 mais importantes antes do balanceamento para os modelos RandomForest e CatBoost;
    * Entre as 5 mais importantes depois do balanceamento para os modelos DecisionTree, RandomForest, XGBoost e CatBoost.
  * cod_agricultura_trab_memb:
    * Entre as 5 mais importantes antes do balanceamento para os modelos RandomForest e CatBoost;
    * Entre as 5 mais importantes depois do balanceamento para os modelos DecisionTree e XGBoost.
  * cod_trabalhou_memb:
    * Entre as 5 mais importantes antes do balanceamento para o modelo DecisionTree;
    * Entre as 5 mais importantes depois do balanceamento para o modelo CatBoost.
  * cod_curso_frequentou_pessoa_memb:
    * Entre as 5 mais importantes antes do balanceamento para o modelo XGBoost;
    * Não está entre as 5 mais importantes depois do balanceamento para nenhum modelo.
  * cod_raca_cor_pessoa
    * Não está entre as 5 mais importantes antes do balancemaento para nenhum modelo;
    * Entre as 5 mais importantes após balancemaento para o modelo RandomForest.
  
Desta forma, de modo a construir um dataframe final, com as variáveis que serão utilizadas no modelo preditivo, serão usadas todas as veriáveis que figuram dentre as 5 mais importantes antes e/ou após o balancamento, relacionadas ao **Responsável familiar**: 
* idade
* cod_principal_trab_memb
* cod_deficiencia_memb
* cod_sexo_pessoa  
* cod_agricultura_trab_memb
* cod_trabalhou_memb
* cod_curso_frequentou_pessoa_memb
* cod_raca_cor_pessoa 
  
## Características do domicílio - Renata:
---
Para analisar se as características do domicílio contribuem para a acurácia do modelo, serão avaliadas, pelo menos, as variáveis abaixo da **Base de famílias**:
* uf_ibge;
* regiao_ibge;
* cod_local_domic_fam;
* cod_especie_domic_fam;
* qtd_comodos_domic_fam;
* qtd_comodos_dormitorio_fam;
* cod_material_piso_fam;
* cod_material_domic_fam
* cod_agua_canalizada_fam;
* cod_abaste_agua_domic_fam;
* cod_banheiro_domic_fam;
* cod_escoa_sanitario_domic_fam;
* cod_destino_lixo_domic_fam;
* cod_iluminacao_domic_fam;
* cod_calcamento_domic_fam;
* classf;
* Outros indicadores que sejam atualizadas de maneira recorrente, ao menos anualmente, que ajudem a caracterizar o perfil socioeconomico dos municípios brasileiros, de maneira a avaliar se contrbuem para uma maior acurácia do modelo.

### Resultado da análise exploratória
---

Em primeiro lugar, foi realizada uma extensa análise exploratória dos dados de domicílios. Algumas das principais constatações podem ser resumidas abaixo:

1. O histograma dos valores das rendas mostra uma distribuição assimétrica concentrada à esquerda (maior concentração de valores de renda na faixa de 0 a 200).
   Conforme cálculos realizados, **61% das famílias recebem até R$ 200**.
   
![01_Analise_inicial_domicilios_167_0](https://github.com/user-attachments/assets/fc62041c-84a2-4845-b93e-bd1ca9c66943)

2. Nas **regiões Norte e Nordeste, 50% das rendas familiares tendem a ser mais baixas**, inclusive abaixo da renda média nacional, não sendo relevante a classificação da divisão administrativa. 
    
![01_Analise_inicial_domicilios_173_0](https://github.com/user-attachments/assets/cc370156-0113-46fe-8308-52ed3a35abd1)

4. Famílias com uma **grande quantidade de pessoas** (caixas verdes) tendem a ter **renda familiar abaixo da renda familiar média**, principalmente quando das regiões Norte e Nordeste. Isso pode indicar um certo grau de importância da variável quantidade de pessoas em problemas de classificação da classe de renda.

![01_Analise_inicial_domicilios_186_0](https://github.com/user-attachments/assets/076f884f-97ec-4129-a4b8-5738c66edb99)

No entanto, a análise exploratória evidencia que não há variáveis de domicílio que possam auxiliar, de forma isolada e em grau elevado, na identificação da classe de renda.
Apenas a variável **quantidade de pessoas** possui correlação acima de 0.3 com a **classe de renda**.

![01_Analise_inicial_domicilios_206_0](https://github.com/user-attachments/assets/3315676e-f999-4c7a-a370-f1c7d4045e8e)


Mais detalhes podem ser vistos no caderno: Analises_Renata/01_Analise_inicial_domicilios.html    

### Resultado da análise das variáveis de domicílios 
---

Conforme a matriz de correlação abaixo (variáveis independentes relacionadas com domicílios), recomenda-se excluir as seguintes variáveis (correlação acima de 0.8) :
* regiao_ibge
* qtd_comodos_dormitorio_fam
* cod_banheiro_domic_fam

Abaixo são listadas as variáveis de correlação acima de 0.7:
* Colunas: uf_ibge e regiao_ibge - Correlação: 0.97
* Colunas: qtd_comodos_domic_fam e qtd_comodos_dormitorio_fam - Correlação: 0.81
* Colunas: cod_agua_canalizada_fam e cod_banheiro_domic_fam - Correlação: 0.83
* Colunas: cod_local_domic_fam e cod_especie_domic_fam - Correlação: 0.73
* Colunas: cod_agua_canalizada_fam e cod_abaste_agua_domic_fam - Correlação: 0.74

![10_Modelos_padrao_24_0](https://github.com/user-attachments/assets/7218bf2d-732a-44e0-b9d8-ded0d53dc9a0)


### Geração inicial de modelos de classificação 
---
Foram testados alguns modelos para prever a classe de renda (variavel target) considerando-se somente as variáveis de domicílios:
* CatBoost Classifier
* XGBoost Classifier
* Random Forest
* Decision Tree
* Logistic Regression
* KNeighbors Classifier 

Em um primeiro momento, sem utilização de busca de hiperparâmetros ou de balanceamento de classes, foi possível obter os seguintes resultados:

![metricas_dom](https://github.com/user-attachments/assets/2c565532-21bc-4ff5-8374-3e9b5c44879c)

Mais detalhes podem ser vistos no caderno: averiguacao_cadastral/Analises_Renata/02_Testando_Modelos.html

### Variáveis preditoras mais relevantes:
* qtde_pessoas 
* uf_ibge 
* qtd_comodos_domic_fam 
* dias_cadastramento 
* dias_atualizacao 
* cod_material_piso_fam 
* classf 
* ind_parc_mds_fam 
* cod_iluminacao_domic_fam 
* cod_local_domic_fam


## Características da família e Composição familiar - Grinaldo: 
---
Para analisar se as características da família e a composição familiar contribuem para a acurácia do modelo, serão avaliadas, pelo menos, as variáveis abaixo da **Base de famílias** e da **Base de pessoas**:
* dat_cadastramento_fam - Número de dias entre 31/12/2018 e a data de cadastramento;
* dat_atualizacao_familia - Número de dias entre 31/12/2018 e a data de atualização cadastral;
* cod_familia_indigena_fam; 
* ind_familia_quilombola_fam;
* ind_parc_mds_fam: 0 no caso de não pertencer a nenhum grupo tradicional e específico, 1 no caso de pertencer a pelo menos 1;
* qtd_pessoas: Quantidade de pessoas utilizada no cálculo da renda per capita familiar;
No caso da composição familiar será necessário avaliar se as diferentes formas de cálculo interferem na acurácia do modelo, avaliando se o resultado categórico, quando existe ou não a situação, se o resultado absoluto, ou seja, o número abosluto daquele caso, ou o percentual, ou seja, o número absoluto divido pelo total de pessoas da familia, interferem na acurácia.
* 1_infancia: nova variável construída a partir da variável "idade", de modo a identificar a situação da família em relação a ter ou não uma pessoa que esteja na 1ª infância, ou seja de 0 a 6 anos de idade;
* crianca_adolescente: nova variável construída a partir da variável "idade", de modo a identificar a situação da família em relação a ter ou não uma pessoa com mais de 6 anos e até 17 anos de idade;
* adultos: nova variável construída a partir da variável "idade", de modo a identificar a situação da família em relação a ter ou não uma pessoa entre 18 e 59 anos de idade;
* idoso: nova variável construída a partir da variável "idade", de modo a identificar a situação da família em relação a ter ou não uma pessoa com 60 anos ou mais; 
* deficiencia: nova variável construída a partir da variável "cod_deficiencia_memb" de modo a identificar a situação da família em relação a ter ou não em sua composição uma pessoa com deficiência;
* Poderão ser testadas outras faixas etárias para avaliar se alguma parece contribuir mais para a acurácia do modelo. As faixas podem ser trabalhadas de acordo com a documentação do indicador <a href="https://wiki-sagi.cidadania.gov.br/home/DS/Cad/I/IN030">Pessoas cadastradas por faixa etária</a> disponível na ferramenta de metadados Documenta Wiki.

### Resultado da Análise

Foram realizados 4 (quatro) cenários de análise de variáveis relacionadas às características da família e composição familiar.

Para fins de análise prévia, segue quadro resumo de acurácia nos cenários analisados:

![Figura 1](https://github.com/mariananresende/averiguacao_cadastral/blob/5812433b25893c54767e17b695a1b817b76a20f8/Analises_Grinaldo/Figura%201.png)

Visto que o cenário de análise sem a presença de dados booleanos foi o de melhor resultado, será apresentado somente este no presente documento.

### CENÁRIO - RETIRADA DE VARIÁVEIS BOOLEANAS

A primeira delas envolveu todas as variáveis envolvidas nesta categoria. Para analisar a correlação entre elas, foi gerada uma matriz de correlação de variáveis, representada na figura a seguir.

![figura6](https://github.com/mariananresende/averiguacao_cadastral/blob/65295ae1434a4f670abc22417ad710d43d048546/Analises_Grinaldo/figura6.png)

A partir da análise da matriz, foram retiradas as variáveis com correlação maior que 0.8, por terem uma forte relação linear entre si. Assim, foram retiradas do dataframe as variáveis: 

'qtd_1_infancia','qtd_crianca_adolescente','qtd_idosos','qtd_deficientes'

Após essa etapa, foram testados quatro modelos preditivos que são indicados para modelos com variáveis numéricas categóricas e quantitativas. Após o treinamento dos modelos e busca de hiperparâmetros, foram indentificados os seguites resultados para cada um dos modelos:

*	Melhores hiperparâmetros para DecisionTree: {'classifier__max_depth': 3, 'classifier__min_samples_split': 2}
*	Melhores hiperparâmetros para RandomForest: {'classifier__max_depth': 10, 'classifier__n_estimators': 200}
*	Melhores hiperparâmetros para XGBoost: {'classifier__learning_rate': 0.1, 'classifier__max_depth': 3, 'classifier__n_estimators': 250}
*	Melhores hiperparâmetros para CatBoost: {'classifier__depth': 3, 'classifier__iterations': 500, 'classifier__learning_rate': 0.1}

Os resultados de acurácia e F1 score foram os seguintes:

![figura7](https://github.com/mariananresende/averiguacao_cadastral/blob/b63f11e3d81cc1a486c80c906a69fc840913c302/Analises_Grinaldo/figura7.png)

Posteriormente foram identificadas as variáveis independentes que mais contribuíram para cada um dos modelos estudados, conforme listagem abaixo das features mais importantes:

10 Features mais importantes para o modelo DecisionTree:

                   Feature  Importância
* 0               pct_idosos       0.1346
* 1          pct_deficientes       0.0703
* 2         ind_parc_mds_fam       0.0000
* 3       qtd_crianca_adulto       0.0000
* 4               qtd_homens       0.0000
* 5             qtd_mulheres       0.0000
* 6       pct_crianca_adulto       0.0000
* 7  pct_crianca_adolescente       0.0000
* 8           pct_1_infancia       0.0000
* 9               pct_homens       0.0000

10 Features mais importantes para o modelo RandomForest:
                   Feature  Importância
* 0               pct_idosos      0.11015
* 1          pct_deficientes      0.04240
* 2       qtd_crianca_adulto      0.01370
* 3       dias_cadastramento      0.01335
* 4           pct_1_infancia      0.01220
* 5         dias_atualizacao      0.00590
* 6             qtde_pessoas      0.00455
* 7       pct_crianca_adulto      0.00425
* 8  pct_crianca_adolescente      0.00330
* 9         ind_parc_mds_fam      0.00255

10 Features mais importantes para o modelo XGBoost:
              Feature  Importância
* 0          pct_idosos      0.10595
* 1     pct_deficientes      0.04305
* 2        qtde_pessoas      0.01560
* 3  dias_cadastramento      0.01475
* 4      pct_1_infancia      0.01430
* 5  pct_crianca_adulto      0.00610
* 6  qtd_crianca_adulto      0.00465
* 7    dias_atualizacao      0.00425
* 8        pct_mulheres      0.00125
* 9    ind_parc_mds_fam      0.00100

10 Features mais importantes para o modelo CatBoost:
                    Feature  Importância
* 0                pct_idosos      0.10615
* 1           pct_deficientes      0.04460
* 2        dias_cadastramento      0.01890
* 3            pct_1_infancia      0.01500
* 4              qtde_pessoas      0.01000
* 5          dias_atualizacao      0.00570
* 6        pct_crianca_adulto      0.00380
* 7          ind_parc_mds_fam      0.00225
* 8        qtd_crianca_adulto      0.00215
* 9  cod_familia_indigena_fam      0.00005

Abaixo, segue gráfico com a análise da importância de todas as features para o modelo CatBoost.

![figura8](https://github.com/mariananresende/averiguacao_cadastral/blob/293b0bffa7d4df178c219f5b64a4dcdb21eb8706/Analises_Grinaldo/figura8.png)

Posteriormente, considerando que a variável target está desbalanceada, tendo 58% de famílias da amostra na classe 0, 21% na classe 1 e 20% na classe 2, foi feito um balanceamento aumentando a amostra para as classes 1 e 2, usando a estratégia de criar amostras sintéticas, e a redução de amostras da classe 0. Após o balanceamento, observou-se os seguintes resultados de cada modelo.

*	Melhores hiperparâmetros para DecisionTree (usando dados balanceados): {'classifier__max_depth': 7, 'classifier__min_samples_split': 2}
*	Melhores hiperparâmetros para RandomForest (usando dados balanceados): {'classifier__max_depth': 20, 'classifier__n_estimators': 200}
*	Melhores hiperparâmetros para XGBoost (usando dados balanceados): {'classifier__learning_rate': 0.1, 'classifier__max_depth': 5, 'classifier__n_estimators': 300}
*	Melhores hiperparâmetros para CatBoost (usando dados balanceados): {'classifier__depth': 5, 'classifier__iterations': 500, 'classifier__learning_rate': 0.1}

Modelo (usando dados balanceados): DecisionTree
  
*  F1 Score: 0.72
*  Acurácia: 0.73
  
Modelo (usando dados balanceados): RandomForest
  
*  F1 Score: 0.79
*  Acurácia: 0.79

Modelo (usando dados balanceados): XGBoost

*  F1 Score: 0.80
*  Acurácia: 0.80

Modelo (usando dados balanceados): CatBoost

*  F1 Score: 0.79
*  Acurácia: 0.79

Em relação às features mais importantes, após o balanceamento, segue o resumo do que foi observado:

![figura9](https://github.com/mariananresende/averiguacao_cadastral/blob/90b8a64022740660c1ad767bee2362963307f05c/Analises_Grinaldo/figura9.png)

## Escolaridade - Risla:
---
Para analisar se a escolaridade dos membros da familia contribuem para a acurácia do modelo, serão avaliadas, pelo menos, as variáveis abaixo da **Base de pessoas**. Neste caso, também deverá ser avaliado se as diferentes formas de cálculo interferem na acurácia do modelo, avaliando se o resultado categórico, quando existe ou não a situação, se o resultado absoluto, ou seja, o número absoluto daquele caso, ou o percentual, ou seja, o número absoluto divido pelo total de pessoas da familia, interferem na acurácia do modelo:
* alfabetizado: nova variável combinando as variáveis "cod_sabe_ler_escrever_memb" e "idade" de modo a identificar a situação da família em relação à pessoa com mais de 10 anos sem saber ler ou escrever;
* frequenta_escola: nova variável combinando as variáveis "ind_frequenta_escola_memb" e "idade" de modo a identificar a situação da família em relação à pessoa de 4 anos a 17 anos que não está na escola;
* frequenta_escola_publica: nova variável combinando as variáveis "ind_frequenta_escola_memb" e "idade" de modo a identificar a situação da família em relação à pessoa de 4 anos a 17 anos que está na escola pública;
* frequenta_escola_privada: nova variável combinando as variáveis "ind_frequenta_escola_memb" e "idade" de modo a identificar a situação da família em relação à pessoa de 4 anos a 17 anos que está na escola privada;
* frequenta_escola_nunca: nova variável combinando as variáveis "ind_frequenta_escola_memb" e "idade" de modo a identificar a situação da família em relação à pessoa de 4 anos a 17 anos que nunca frequentou escola;
* frequanta_creche: nova variável combinando as variáveis "cod_curso_frequentou_pessoa_memb" e "idade" de modo a identificar a situação da família em relação à pessoa de menos de 4 anos que não está na creche; 
* frequenta_escola_nunca_adulto: nova variável combinando as variáveis "ind_frequenta_escola_memb" e "idade" de modo a identificar a situação da família em relação à pessoa com 18 anos ou mais que nunca frequentou escola;
* cod_escola_local_memb;
* Poderão ser pensadas e testadas variáveis a serem construídas por meio da engenharia de features, utilizando as varáveis "cod_curso_frequentou_pessoa_memb", "cod_ano_serie_frequentou_memb" e "cod_concluiu_frequentou_memb".  Para tanto, serão estudadas as variáveis que compõem as dimensões de vulnerabilidade do Índice de Vulnerabilidade das Famílias do Cadastro Único (IVCAD), "Desenvolvimento de Crianças e Adolescentes" e "Desenvolvimento na Primeira Infância" conforme documentação dos indicadores do Cadastro Único apresentada na ferramenta de metadados <a href="https://wiki-sagi.cidadania.gov.br/en/home/DS/Cad/I">Documenta Wiki</a>.
* Além disso poderão ser incluídos indicadores escolares do município como o Ideb, por exemplo.

Após análise de quais variáveis referentes a cada família seriam possíveis de calcular e inserir no modelo, chegou-se à seguinte lista:

- Variável alfabetizado: percentual de pessoas maiores de 10 anos que não sabem ler ou escrever (**pct_nao_alfabetizados**)
- Variável frequenta_escola: percentual de pessoas entre 4 e 17 anos que não frequentam a escola (**pct_n_freq_escola**)
- Variável frequenta_escola_publica: percentual de pessoas entre 4 e 17 anos que frequentam a escola pública (**pct_freq_publica**)
- Variável frequenta_escola_particular: percentual de pessoas entre 4 e 17 anos que frequentam a escola particular (**pct_freq_particular**)
- Variável frequenta_escola_nunca: percentual de pessoas entre 4 e 17 anos que nunca frequentaram a escola (**pct_nunca_freq_escola**)
- Variável frequenta_creche: percentual de crianças menores de 4 anos que não está na creche (**pct_n_freq_creche**)
- Variável frequenta_escola_nunca_adulto: percentual de pessoas maiores de 18 anos que nunca frequentaram a escola (**pct_adultos_nunca_freq_escola**)
- Variável frequenta_escola_municipio: percentual de pessoas entre 4 e 17 anos que frequentam a escola no município (**pct_freq_escola_municipio**)
- Variável **ideb_2017_municipio** com os valores do IDEB de 2017 da rede pública para cada município

Com a criação das variáveis acima, foi possível criar uma matriz de correlação para retirar uma das variáveis que possuía alta correlação (acima de 0.80), conforme figura a seguir:

![Gráfico de correlação das variáveis de escolaridade](matriz_corr_variaveis.png)

Como a variável pct_freq_escola_municipio apresentou correlação de 0.9 com a variável pct_freq_publica, decidiu-se retirar a variável pct_freq_escola_municipio por considerar que a variável relacionada ao percentual de pessoas que frequentam a escola pública teria mais aderência ao problema de negócio.

A partir dos dados normalizados, foi criada uma instância de Pipeline para treinar quatro modelos (Árvore de Decisão, Random Forest, XGBoost e CatBoost) com o objetivo de analisar a importância das variáveis de escolaridade para o modelo. Como o modelo CatBoost estava apresentando os melhores resultados na equipe, esse algoritmo foi escolhido para selecionar as variáveis mais importantes que serão adicionadas à base de dados completa para o modelo final. Através do seguinte gráfico é possível conferir quais variáveis foram consideradas mais importantes para o CatBoost:

![Gráfico de importância de features de escolaridade](import_features_catboost.png)

A título de curiosidade segue lista das 10 variáveis mais importantes de acordo com o modelo:


```
Top 10 Features para o modelo DecisionTree balanceado:

                  Feature  Importância
adultos_nunca_freq_escola     0.031791
         pct_freq_publica     0.017144
      ideb_2017_municipio     0.004254
        pct_n_freq_escola     0.001523
    pct_nao_alfabetizados     0.000637
          pct_freq_creche     0.000523
      pct_freq_particular     0.000078

Top 10 Features para o modelo RandomForest balanceado:

                  Feature  Importância
         pct_freq_publica     0.053930
      ideb_2017_municipio     0.034506
adultos_nunca_freq_escola     0.016833
    pct_nao_alfabetizados     0.012948
          pct_freq_creche     0.005627
        pct_n_freq_escola     0.003192
      pct_freq_particular     0.001829
    pct_nunca_freq_escola     0.001591

Top 10 Features para o modelo XGBoost balanceado:

                  Feature  Importância
         pct_freq_publica     0.050800
      ideb_2017_municipio     0.035034
adultos_nunca_freq_escola     0.014326
    pct_nao_alfabetizados     0.010025
          pct_freq_creche     0.005792
        pct_n_freq_escola     0.004419
    pct_nunca_freq_escola     0.002435
      pct_freq_particular     0.002150

Top 10 Features para o modelo CatBoost balanceado:

                  Feature  Importância
         pct_freq_publica     0.048396
      ideb_2017_municipio     0.033817
adultos_nunca_freq_escola     0.011984
    pct_nao_alfabetizados     0.009046
          pct_freq_creche     0.006134
        pct_n_freq_escola     0.004435
      pct_freq_particular     0.002202
    pct_nunca_freq_escola     0.002161
             ideb_ausente     0.000026
```

Assim, segue a lista das variáveis selecionadas a partir dos resultados de feature_importance do CatBoost:

1. pct_freq_publica
2. ideb_2017_municipio
3. adultos_nunca_freq_escola
4. pct_nao_alfabetizados
5. pct_freq_creche
6. pct_n_freq_escola
7. pct_freq_particular
8.  pct_nunca_freq_escola

## Trabalho - Michela:
---
Para analisar se a condição de trabalho dos membros da familia contribuem para a acurácia do modelo, serão avaliadas, pelo menos, as variáveis abaixo da **Base de pessoas**. Neste caso, também deverá ser avaliado se as diferentes formas de cálculo interferem na acurácia do modelo, avaliando se o resultado categórico, quando existe ou não a situação, se o resultado absoluto, ou seja, o número absoluto daquele caso, ou o percentual, ou seja, o número absoluto divido pelo total de pessoas da familia, interferem na acurácia do modelo:
* trabalho_semana_adulto: nova variável combinando as variáveis "cod_trabalhou_memb" e "idade" de modo a identificar a situação da família em relação à pessoa entre 18 e 59 anos que trabalhou na semana passada;
* trabalho_semana_idoso: nova variável combinando as variáveis "cod_trabalhou_memb" e "idade" de modo a identificar a situação da família em relação à pessoa com 60 anos ou mais que trabalhou na semana passada;
* trabalho_semana_criança: nova variável combinando as variáveis "cod_trabalhou_memb" e "idade" de modo a identificar a situação da família em relação à pessoa menor de 18 anos que trabalhou na semana passada;
* afastado_trabalho: nova variável combinando as variáveis "cod_afastado_trab_memb" e "idade" de modo a identificar a situação da família em relação à pessoa entre 18 e 59 anos que ficou afastada do trabalho na semana passada;
* atividade extrativista: nova variável combinando as variáveis "cod_agricultura_trab_memb" e "idade" de modo a identificar a situação da família em relação à pessoa entre 18 e 59 anos que trabalha em atividade agrícola ou extrativista;
* trabalho_principal: nova variável combinando as variáveis "cod_principal_trab_memb" e "idade" de modo a identificar a situação da família em relação à pessoa entre 18 e 59 anos e o seu trabalho principal;
* trabalho_12meses_adulto: nova variável combinando as variáveis "cod_trabalho_12_meses_memb" e "idade" de modo a identificar a situação da família em relação à pessoa entre 18 e 59 anos com trabalho remunerado em algum período nos último 12 meses;
* trabalho_12meses_idoso: nova variável combinando as variáveis "cod_trabalho_12_meses_memb" e "idade" de modo a identificar a situação da família em relação à pessoa com 60 anos ou mais com trabalho remunerado em algum período nos último 12 meses;
* trabalho_12meses_criança: nova variável combinando as variáveis "cod_trabalho_12_meses_memb" e "idade" de modo a identificar a situação da família em relação à pessoa menor de 18 anos com trabalho remunerado em algum período nos último 12 meses;
* meses_trabalho: nova variável combinando as variáveis "qtd_meses_12_meses_memb" e "idade" de modo a identificar a situação da família em relação ao número de meses trabalhado nos últimos 12 meses para pessoa a partir de 18 anos.

  Com a criação das variáveis acima, foi possível criar uma matriz de correlação para retirar uma das variáveis que possuía alta correlação (acima de 0.80). No caso das variáveis de trabalho, as variáveis de trabalho semana e trabalho ano mostraram correlação de 0,9, conforme figura a seguir:

![Gráfico de correlação das variáveis de trabalho](Analises_Michela/corr_trabalho.png)

Muitos modelos foram testados para verificar a relação de importância entre as variáveis de trabalho e a classe renda. Os resultados são apresentados em seguida:

![Gráfico de features importance das variáveis de trabalho](Analises_Michela/features_importance_trabalho_decision_tree.png)

![Gráfico de features importance das variáveis de trabalho](Analises_Michela/features_importance_trabalho_random_forest.png)

![Gráfico de features importance das variáveis de trabalho](Analises_Michela/features_importance_trabalho_xgboost.png)

![Gráfico de features importance das variáveis de trabalho](Analises_Michela/features_importance_trabalho_catboost.png)

Por fim, a figura abaixo apresenta uma análise mais ampla a respeito da relação entre as variáveis do tema trabalho e a classe de renda. A partir dessa figura, é possível notar que as variáveis de percentual de adultos e idosos que tiveram algum trabalho no período de 12 meses e a ocupação de servidor ou militar parece mais associado às classes de renda 1 e 2. As pessoas da classe de renda zero, parecem estar mais associadas às ocupações de conta própria e atividades agrícolas e extrativistas.

![Radviz das variáveis de trabalho](Analises_Michela/radviz_trabalho.png)

# Modelo de classificação em Classe de renda 0, 1 e 2

## Base de dados final
Após a seleção das features mais importantes dentro de cada temática, foi preparada uma base conjugando as features selecionadas, a qual foi usada para treinamento do modelo. O dicionário da base preaprada segue abaixo:
| Variável | Descrição |
| ------- | -------|
| id_familia  |  Identificador único da família para pareamento com a base de pessoas |
| rf_idade  | Idade do responsável familiar, calculado a partir do cruzamento do campo 'cod_parentesco_rf_pessoa' == 1, conforme dicionário da **base pessoas**, e da variável 'idade' |
| rf_trab_principal |  Função principal do responsável familiar, calculado a partir do cruzamento do campo 'cod_parentesco_rf_pessoa' == 1 e do campo 'cod_principal_trab_memb', conforme dicionário da **base pessoas** |    
| rf_com_deficiencia |   Marcação se responsável familiar tem deficiência, calculado a partir do cruzamento do campo 'cod_parentesco_rf_pessoa' == 1 e do campo 'cod_deficiencia_memb', conforme dicionário da **base pessoas** |
| rf_trab_agricultura  | Marcação se responsável familiar atua em atividade extrativista, calculado a partir do cruzamento do campo 'cod_parentesco_rf_pessoa' == 1 e do campo 'cod_agricultura_trab_memb', conforme dicionário da **base pessoas** |
|   rf_sexo  | Sexo do responsável familiar, calculado a partir do cruzamento do campo 'cod_parentesco_rf_pessoa' == 1 e do campo 'cod_sexo_pessoa', conforme dicionário da **base pessoas** |
|  rf_curso_frequentou | Identificação do curso mais elevado que o responsável familiar frequentou, calculado a partir do cruzamento do campo 'cod_parentesco_rf_pessoa' == 1 e do campo 'cod_curso_frequentou_pessoa_memb', conforme dicionário da **base pessoas** |        | rf_curso_frequenta  |  Identificação do curso que o responsável familiar frequenta, calculado a partir do cruzamento do campo 'cod_parentesco_rf_pessoa' == 1 e do campo 'cod_curso_frequenta_memb', conforme dicionário da **base pessoas** |
|   rf_trabalhou_semana  | Identificação se o responsável familiar trabalhou na semana passada, calculado a partir do cruzamento do campo 'cod_parentesco_rf_pessoa' == 1 e do campo 'cod_trabalhou_memb', conforme dicionário da **base pessoas** |
|   rf_cor_raca   | Cor ou raça do responsável familiar, calculado a partir do cruzamento do campo 'cod_parentesco_rf_pessoa' == 1 e do campo 'cod_raca_cor_pessoa', conforme dicionário da **base pessoas** |      
|  rf_concluiu_curso |  Marcação se responsável familiar concluiu o curso mais elevado que frequentou, calculado a partir do cruzamento do campo 'cod_parentesco_rf_pessoa' == 1 e do campo 'cod_concluiu_frequentou_memb', conforme dicionário da **base pessoas** |
|  pct_extrativista  | Percentual dos adultos que atuam em atividade extrativista, calculado por meio do campo 'cod_agricultura_trab_memb' == 1, com o filtro de 'idade' >= 18 e <= 59, dividido pela 'qtde_pessoas' |
| pct_conta_propria | Percentual de adultos que trabalham por conta própria, calculado por meio do campo 'cod_principal_trab_memb'] == 1, com filtro de 'idade' >= 18 e <= 59, dividido pela 'qtde_pessoas' |
|    pct_trab_rural_temporario | Percentual de adultos que atuam como trabalhador temporário em área rual, calculado por meio do campo 'cod_principal_trab_memb' == 2, com filtro de 'idade' >= 18 e <= 59, dividido pela 'qtde_pessoas' |
| pct_empregado_sem_carteira | Percentual de adultos empregados sem carteira assinada, calculado por meio do campo 'cod_principal_trab_memb' == 3, com filtro  de 'idade' >= 18 e <= 59, dividido pela 'qtde_pessoas' |
 |  pct_empregado_com_carteira |Percentual de adultos empregados com carteira assinada, calculado por meio do campo 'cod_principal_trab_memb' == 4, com filtro  de 'idade' >= 18 e <= 59, dividido pela 'qtde_pessoas' |
 | pct_trab_domestico_sem_carteira | Percentual de adultos trabalhadores domésticos sem carteira assinada, calculado por meio do campo 'cod_principal_trab_memb' == 5, com filtro  de 'idade' >= 18 e <= 59, dividido pela 'qtde_pessoas' |
 | pct_militar_servidor | Percentual de adultos militares ou servidores públicos, calculado por meio do campo 'cod_principal_trab_memb' == 8, com filtro  de 'idade' >= 18 e <= 59), dividido pela 'qtde_pessoas' |
 | pct_trabalho_12meses_adulto | Percentual de adultos com trabalho em algum período nos últimos 12 meses, calculado por meio do campo 'cod_trabalho_12_meses_memb' == 1, com filtro  de 'idade' >= 18 e <= 59, dividido pela 'qtde_pessoas' |
| pct_trabalho_12meses_idoso | Percentual de idosos com trabalho em algum período nos últimos 12 meses, calculado por meio do campo 'cod_trabalho_12_meses_memb' == 1, com filtro  de 'idade' >= 60, dividido pela 'qtde_pessoas' |
| pct_trabalho_12meses_crianca | Percentual de idosos com trabalho em algum período nos últimos 12 meses, calculado por meio do campo 'cod_trabalho_12_meses_memb' == 1, com filtro  de 'idade' <18 dividido pela 'qtde_pessoas'. Lembrando que neste caso, conforme registrado no tópico referente à limpeza de dados, os campos de trabalho só foram considerado para idade >= 14 |           
| pct_nao_alfabetizados  | Percentual de pessoas não alfabetizadas, calculado por meio do campo 'cod_sabe_ler_escrever_memb' == 2, com filtro de 'idade' >= 10, divido  pela 'qtde_pessoas' |
|  pct_n_freq_escola  | Percentual de pessoas em idade escolar que não frequentam a escola, calculado por meio do campo 'ind_frequenta_escola_memb' == 3, com filtro de 'idade' >= 4 e <= 17, dividido pela 'qtde_pessoas' |
 | pct_freq_publica   | Percentual de pessoas em idade escolar que frequentam escola pública, calculada por meio do campo 'ind_frequenta_escola_memb' == 1, com filtro de 'idade' >= 4 e <= 17, dividido pela 'qtde_pessoas' |
 |  pct_freq_particular  | Percentual de pessoas em idade escolar que frequentam escola particular, calculada por meio do campo 'ind_frequenta_escola_memb' == 2, com filtro de 'idade' >= 4 e <= 17, dividido pela 'qtde_pessoas' |
 |  pct_adulto_nunca_freq_escola  | Percentual de adultos que nunca frequentaram escola, calculada por meio do campo 'ind_frequenta_escola_memb' == 4, com filtro de 'idade' >= 18, dividido pela 'qtde_pessoas' |
 |  pct_escolar_nunca_freq_escola | Percentual de pessoas em idade escolar que nunca frequentaram escola, calculada por meio do campo 'ind_frequenta_escola_memb' == 4, com filtro de 'idade' >= 4 e <= 17, dividido pela 'qtde_pessoas' |
|  pct_freq_creche | Percentual de pessoas da primeira infância que frequentam creche, calculada por meio do campo 'cod_curso_frequenta_memb' == 1, com filtro de 'idade' <4, dividido pela 'qtde_pessoas' |     
|  pct_idosos  | Pecentual de idosos que compõem a família, calculado por meio do filtro 'idade' >= 60, dividido pela 'qtde_pessoas'|
|  pct_deficientes  | Percentual de pessoas com deficiência que compõem a família, calculado por meio do campo 'cod_deficiencia_memb' == 1, dividido pela 'qtde_pessoas' |     
|  pct_1_infancia |  Percentual de pessoas da primeira infância que compõem a família, calculado por meio do filtro 'idade' <=6, dividido pela 'qtde_pessoas' |
|  pct_adulto |  Percentual de adultos que compõem a família, calculado por meio do filtro 'idade' >= 18, dividido pela 'qtde_pessoas' |
 |  pct_crianca_adolescente  | Percentual de crianças e adolscentes que compõem a família, calculado por meio do filtro 'idade' >6 e <= 17, dividido pela 'qtde_pessoas' |  
 |  fam_gpte  | Marcação se a família compõem algum Grupo populacional,  tradicional e específico (GPTE), calculado por meio dos filtros 'ind_parc_mds_fam' != 0 ou 'cod_familia_indigena_fam'] == 1 ou 'ind_familia_quilombola_fam'] == 1 |
|  ideb_2017_municipio | Índice de Desenvolvimento da Educação Básica (Ideb) de 2017 |
|  uf_ibge | Nova variável criada com o código das Unidades Federativas (UF), conforme dicionário da **base familia** |  
|  classf | Subdivisão pela Unidade Federativa e divisão administrativa, conforme dicionário da **base familia** | 
|  cod_local_domic_fam  | Características do local onde está situado o domicílio, conforme dicionário da **base familia** | 
|  qtd_comodos_domic_fam | Quantidade de comodos do domicilio |
|  cod_material_piso_fam | Material predominante no piso do domicílio, conforme dicionário da **base familia** | 
|  cod_iluminacao_domic_fam  | Tipo de iluminação do domicílio, conforme dicionário da **base familia** | 
|  cod_familia_indigena_fam | Marcação se a família é indígena | 
|  ind_familia_quilombola_fam | Marcação se a família é quilombola | 
|  ind_parc_mds_fam | Marcação se a família pertence a algum dos Grupos tradicionais e específicos | 
|  qtde_pessoas  | Quantidade de pessoas que compõem a família e são utilizadas no cálculo da renda per capita familiar, conforme dicionário da **base familia** | 
|  dias_cadastramento | Variável nova calculada por meio da diferença entre a data de referência da base de dados, 31/12/2018, e o campo 'dat_cadastramento_fam', conforme dicionário da **base familia** |
|  dias_atualizacao | Variável nova calculada por meio da diferença entre a data de referência da base de dados, 31/12/2018, e o campo 'dat_atualizacao_familia', conforme dicionário da **base familia** |
|  classe_renda | Variável nova com as 3 classes de renda a serem preditas pelo modelo, conforme dicionário da **base familia** |

Foram preparados dois dataframes com as features acima descritas, o df_modelo, o qual foi construído a partir do balanceamento da classe_renda original, e o df_modelo_balanceado, construído a partir de uma amostra que levou em conta o balanceamento das calsses, de modo a ter um número semelhante de dados relacionados às três classes. Os dataframes constam na pasta Data_modelo.

Essa estratégia permitiu comparar a performance dos modelos em uma base desbalanceada, em uma base balanceada com posterior estratégias de balanceamento e a partir de uma base balanceada com dados originais.

## Pré-processamento
Após a preparação das bases, foi ralizado o pré-processamento das features, utilizando diferentes estratégias que permitiram comparar quais trouxeram melhores desempenho para o modelo.

### Processamento One-Hot Encoding
Mesmo para variáveis categóricas que já são representadas numericamente, adotar essa técnica de processamento ajuda a:
* Preservar o Significado Categórico: variáveis categóricas podem ser representadas numericamente, mas esses números não indicam uma ordem ou magnitude. Se usarmos essas variáveis diretamente em um modelo, ele pode interpretar os números como quantitativos, o que levaria a conclusões incorretas sobre a relação entre os valores. O One-Hot Encoding evita isso, transformando cada categoria em uma variável binária independente, preservando o caráter categórico da variável.
* Evitar Relações Espúrias entre Categorias: variáveis categóricas numéricas podem ser erroneamente tratadas como variáveis ordinais (onde a ordem importa). Isso significa que os modelos podem criar relações que não existem entre os números atribuídos às categorias.
O One-Hot Encoding trata cada categoria como uma entidade independente, eliminando essas relações artificiais.
* Melhor Desempenho do Modelo: Alguns algoritmos de machine learning, como árvores de decisão e redes neurais, tendem a ter um melhor desempenho quando recebem variáveis binárias (0/1) para cada categoria. O One-Hot Encoding facilita a identificação de padrões entre categorias de forma mais eficaz nesses modelos.
* Compatibilidade com Algoritmos de Machine Learning: Certos algoritmos, como regressão logística e K-means, assumem que as variáveis de entrada são numéricas e podem ser influenciados por magnitude. Nesse contexto, variáveis categóricas numéricas sem transformação podem distorcer os resultados. O One-Hot Encoding converte essas variáveis em uma forma que mantém a integridade dos dados categóricos.
Desta forma, os modelos treinados foram testados com e sem o processamento utilizando o one-hot encoding, ou utilizando o one-hot encoding para algunas variáveis categóricas, de modo a identificar a estratégia que apresentou os melhores resultados.

### Normalização
Outro pré-processamento realizado diz respeito à normalização dos dados, de maneira a colocar todas as variáveis em uma escala comum, reduzindo o tempo de treinamento e melhorando a estabilidade do modelo. Quando as variáveis possuem escalas muito diferentes, os valores de maior magnitude podem dominar o aprendizado do modelo.

Além disso, após converter variáveis categóricas para forma numérica, normalizar os valores pode ser útil dependendo do algoritmo, pricipalmente em situações onde as variáveis resultantes de codificação podem ter magnitude diferente (por exemplo, variáveis de contagem ou de presença de características). Em alguns casos, mesmo variáveis categóricas numéricas que indicam uma ordem podem se beneficiar de normalização, pois coloca os valores em uma escala similar às demais variáveis do modelo.

Da mesma forma, foram treinados modelos com e sem a normalização, ou com a normalização de parte das features, de modo a identificar a estratégia que apresentou os melhores resultados. 

O modelo selecionado, que apresentou as melhores métricas, tiveram os dados quantitativos normalizados, ou seja, as variáveis 'qtd_comodos_domic_fam', 'qtde_pessoas', 'dias_cadastramento', 'dias_atualizacao', 'ideb_2017_municipio', usando o StandardScaler, ou seja, ajustando os valores para que tenham média igual a 0 e desvio padrão igual a 1.

### Seleção de features
No pré-processamento também foram identificadas as features com correlações altas, com limiar acima de 0.75, de modo a evitar a:
* Multicolinearidade, que ocorre quando duas ou mais variáveis independentes em um modelo têm uma correlação forte entre si. Quando isso acontece, torna-se difícil para o modelo determinar o impacto individual de cada variável nas previsões, pois elas trazem informações muito semelhantes. Isso pode inflar os coeficientes de regressão em modelos lineares, tornando as estimativas menos confiáveis. O modelo se torna sensível a pequenas mudanças nos dados, resultando em coeficientes instáveis, que podem variar bastante se o conjunto de dados for alterado, comprometendo a interpretabilidade e a precisão do modelo.
* Redundância de Informação, pois incluir variáveis redundantes não acrescenta novas informações ao modelo e pode, inclusive, aumentar o ruído. Em vez de contribuir para a previsão, elas podem apenas aumentar a complexidade do modelo sem melhorar seu desempenho, podendo levar a um ajuste excessivo (overfitting), onde o modelo se adapta muito bem aos dados de treino, mas não generaliza bem para novos dados.
* Complexidade do Modelo, ao usar um número excessivo de variáveis para descrever o comportamento do target, tornando o modelo difícel de interpretar. Um modelo mais simples é preferível, pois facilita a interpretação e o entendimento dos fatores que influenciam as previsões. Remover variáveis com alta correlação contribui para uma análise mais clara e objetiva.
* Impacto no Tempo de Treinamento, pois cada variável utilizada em um modelo afeta o tempo necessário para treinamento. Assim, variáveis redundantes aumentam o número de cálculos e a complexidade computacional, tornando o processo de treinamento mais lento. Eliminar variáveis com alta correlação reduz o tempo de processamento e otimiza o desempenho do modelo, sem perder significativamente a capacidade de previsão.

## Tipos de modelos treinados
Considerando que o objetivo do projeto é preparar um modelo preditivo que classique as famílias do Cadastro Único, em 3 classes de renda, por meio das características das famílias apresentadas em varáveis numéricas categóricas, quantitativas e percentuais, foram treinados e comparados os seguintes modelos:
* Random Forest Classifier - baseado em um conjunto de árvores de decisão, cada uma treinada em diferentes subconjuntos dos dados, é muito adequado para um problema de 3 classes, pois as árvores de decisão internas geram divisões que podem capturar a complexidade das diferentes classes;
* XGBoost - combina várias árvores de decisão de forma sequencial, corrigindo erros das árvores anteriores, é uma boa escolha para problemas de classificação com múltiplas classes devido ao seu desempenho e flexibilidade, especialmente quando os dados apresentam relações complexas entre variáveis;
* CatBoost Classifier - lida com variáveis categóricas de forma mais eficiente, sendo ideal para problemas que incluem variáveis categóricas numéricas e quantitativas, sendo uma boa escolha quando se deseja maximizar a performance sem a necessidade de muito pré-processamento;
* Regressão Logística Multinomial - método linear que pode ser adaptado para problemas de classificação com mais de duas classes, pode ser uma opção viável para problemas de classificação multiclasse, mas pode ter desempenho inferior em dados com relações complexas, a menos que se utilizem técnicas de feature engineering para melhorar o ajuste;
*  K-Nearest Neighbors (KNN) - método baseado em distância que classifica as amostras com base nos K vizinhos mais próximos, pode funcionar bem para problemas de 3 classes em conjuntos de dados menores, mas seu desempenho pode cair em conjuntos maiores ou mais complexos.

## Modelo selecionado
Após diversas análises e compração do resultado, o modelo que apresentou a melhor conjugação de resultado de diversos fatores foi o **Modelo de classificação Catboost, treinado a partir da base balanceada na sua origem, pré-processada usando o one-hot encoding em todas as variáveis categóricas, preservando os valores -1 imputados quando da limpeza dos dados e com as variáveis numéricas normalizadas**. 
O modelo foi selecionado a partir das características indicadas pela área de negócio esperadas para o modelo:
*  Uma acurácia razoável, de modo a evitar falsos positivos;
*  Uma alto recall, especialmente para a classe 2, de modo a evitar falsos negativos. Como o objetivo é identificar as famílias a serem convocada para uma qualificação cadastral, é importante que as famílias que tenham características de serem classificadas como classe 2 sejam identificadas, mesmo que para isso tenha um risco um pouco mais elevado de que famílias da classe 0 ou 1 sejam classificadas como 2.
Além disso, foram considerados também, para a seleção do modelo, um equilíbrio entre essas duas métricas, e para tanto comparados os valores do F1-Score dos modelos, além da análise do AUC, que avalia a capacidade do modelo de separar as classes.
Assim, o modelo selecionado apresentou os seguintes resultados:

| Classe |  Precisão | Recall | F1-Score | AUC |
|----|-----|-----|------------| ------ |
| Classe 0 | 0.7683 | 0.807884 |  0.7876 | 0.9199 |
| Classe 1 | 0.6819 |  0.6483 | 0.6647 | 0.8467 |
| Classe 2 | 0.7926 | 0.7906 | 0.7916 | 0.9300 |

Considerando o modelo como um todo, pode-se destacar:
* O modelo apresentou uma acurácia de 0.7494, significando que o modelo acertou cerca de 74,94% das previsões. Embora a acurácia não seja sempre a melhor métrica em problemas de classes desbalanceadas, ela é complementada pelas outras métricas para uma visão mais detalhada.
* Uma alta Capacidade de Discriminação (AUC Elevado), com um AUC superior a 0.9 para duas das classes, a 0 e a 1, e um AUC geral de 0.8989, mostra uma forte habilidade do modelo para diferenciar as classes corretamente.
* Um bom Equilíbrio entre Precision e Recall, pois o F1-score é relativamente alto para todas as classes, especialmente para a classe 2.
* O modelo apresentou um desempenho consistente entre as classes, indicando que não está focado em uma classe específica, mas está tentando capturar bem todas elas.

As etapas para a construção do modelo e os resultados obtidos podem ser acessados e replicados por meio do notebook [Final_Modelo_df_balanceado_onehotencoder_Catboost.ipynb](https://github.com/mariananresende/averiguacao_cadastral/blob/main/Final_Modelo_df_balanceado_onehotencoder_Catboost.ipynb).


## Utilização do modelo
Para a utilização do modelo [CatBoostClassifier_balanceado.pkl](https://github.com/mariananresende/averiguacao_cadastral/blob/main/CatBoostClassifier_balanceado.pkl) e predição das classes é preciso fazer a limpeza das bases, de modo a retirar o valores NaN. Sugere-se usar as regras descritas na seção "Limpeza das bases", a qual segue as regras de preenchimento do formulário do Cadastro Único.

Após esta etapa é preciso criar uma base de dados final com as features selecionadas no modelo, o que pode ser feito por meio do notebook [Gerando_df_modelo_final.ipynb](https://github.com/mariananresende/averiguacao_cadastral/blob/main/Gerando_df_modelo_final.ipynb)

Por fim, o df produzido deverá ser dividido em um dataframe X, com as features, e outro com a variável target classe_renda, para posterior comparação. Para tanto, o caminho está detalhado no notebook [Testando_modelo.ipynb](https://github.com/mariananresende/averiguacao_cadastral/blob/main/Testando_modelo.ipynb)

# Autores do projeto (ordem alfabética)
Grinaldo Oliveira - IBGE - SES/BA-SSI - grinaldo.oliveira@ibge.gov.br 

Mariana Nogueira de Resende Sousa - MDS-SAGICAD-DMA-CGPI - mariananresende@gmail.com

Michela Barreto Camboim Gonçalves Feitosa - Agência Nacional de Saúde Suplementar - mcamboim@gmail.com

Renata Guanaes - Departamento de Estudos Econômicos/CADE - rguanaes@gmail.com

Risla Miranda - SEGES/MGI - rislamiranda@gmail.com

## Agradecimento especial
Tutor Ricardo de Lima - MGI-SGD-DEDAD-CGIAR-CPRIA - ricdelima@gmail.com 

