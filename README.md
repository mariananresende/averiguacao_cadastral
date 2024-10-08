# Averiguação Cadastral
Repositório para projeto conjunto no âmbito do Bootcamp em Machine Learning com o objetivo de desenvolver um algoritmo para identificação automática do público de averiguação cadastral do Cadastro Único para Programas Sociais

# ![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM_DESENVOLVIMENTO&color=GREEN&style=for-the-badge) ![Badge Outubro/2024](http://img.shields.io/static/v1?label=DATA&message=Outubro/2024&color=blue&style=for-the-badge)

## Nome do projeto
Algoritmo de classificação usando técnicas de Machine Learning (ML) para identificação do público para averiguação Cadastral

## Descrição do problema 
O Cadastro Único para Programas Sociais é o principal instrumento do Estado brasileiro para a seleção e a inclusão de famílias de baixa renda em programas federais, sendo usado para a concessão dos benefícios do Programa Bolsa Família, do Pé de Meia, da Tarifa Social de Energia Elétrica, do Auxílio Gás, do Programa Minha Casa Minha Vida, entre outros. 

Para reduzir erros de inclusão, constantemente é feito um processo de qualificação cadastral. Neste ano, por exemplo, até o momento foram convocadas 3,3 milhões de famílias para averiguação do cadastro, o qual consiste em verificar as famílias que apresentam algum indício de inconsistência, seja de renda, de declaração de vínculo empregatício, ou de composição familiar.

Considerando a referência de setembro/2024, existem mais de 40 milhões de famílias incluídas no Cadastro Único, e 93 milhões de pessoas. Para uma melhor focalização das políticas públicas sociais usuárias deste cadastro para seleção dos beneficiários é preciso automatizar o processo de averiguação cadastral.

Para tanto, a proposta do presente projeto é propor um algoritmo que, a partir das características das família, seja possível classificar cada família em uma faixa de renda mais provável:
* Pobreza: de 0 a 218,00;
* Baixa renda: de 218,01 a 1/2 salário-mínimo;
* Acima de 1/2 salário-mínimo.
  
O modelo objetiva auxiliar em uma maior focalização das políticas públicas sociais para as famílias que apresentam características relacionadas à maior vulnerabilidade de renda, identificando famílias que apresentam caracterísiticas não esperadas para a faixa de renda apresentada, guiando ações de qualificação do Cadastro Único.

## Benefícios do uso do algoritmo de ML para automatização do processo de averiguação cadastral
* É possível incluir toda a base do Cadastro Único na análise de definição do público de averiguação cadastral, sem a necessidade de definição de amostra;
* É possível identificar as variáveis que contribuem diretamente para a definição automática das famílias a serem incluídas no processo de averigação cadastral, evitando critérios subjetivos para a seleção das variáveis;
* É possível atualizar o algoritmo com os dados mais atuais, de modo a acompanhar as mudanças das famílias ao longo do tempo. 

## Bases de dados utilizadas
As bases de dados utilizadas estão disponibilizadas no <a href="https://dados.gov.br/dados/conjuntos-dados/microdados-amostrais-do-cadastro-unico)">Portal de Dados abertos do Governo Federal do MDS</a>.

As bases são amostrais, desidentificadas, e as últimas bases disponíveis no portal são de 2018, acessado em outubro/2024.

Uma base apresenta os dados de pessoas e a outra base os dados das famílias. É possível combinar as duas bases de dados por meio da variável id_familia: Identificador único da família para pareamento com a base de pessoas. No caso da Base famílias, os dados estão relacionados à família, sendo uma por linha. No caso da Base pessoas é uma pessoa por linha, sendo que a variável id_familia estará repetida para as pessoas que compõem a mesma família. Abaixo segue o dicionário das bases.

### Base famílias

| Seq. | Nome da variável                 | Tipo   | Tamanho (Inteiro) | Tamanho (Decimal) | Descrição                                                                                                     |
|------|-----------------------------------|--------|-------------------|------------------|---------------------------------------------------------------------------------------------------------------|
| 1    | cd_ibge                          | String | 7                 |                  | Código IBGE do Município                                                                                       |
| 2    | dat_cadastramento_fam             | String | 8                 |                  | Data do cadastramento da família no formato YYYY-MM-DD                                                         |
| 3    | dat_alteracao_fam                 | Date   | 8                 |                  | Data da última alteração em qualquer campo da família no formato YYYY-MM-DD (Variável utilizada nos anos de 2014, 2015, 2016 e 2017)                 |
| 4    | vlr_renda_media_fam               | Numeric| 9                 |                  | Valor da renda média (per capita) da família, formato NNNNNNNNN (não tem a vírgula). Ex.: Uma renda de R$ 125,00 constará na base como 125            |
| 5    | dat_atualizacao_familia           | Date   | 8                 |                  | Data da última atualização da família dos dados considerados sensíveis à manutenção do cadastro no formato YYYY-MM-DD (2014-2017)                     |
| 6    | dat_atual_fam                     | Date   | 8                 |                  | Data da última alteração em qualquer campo da família no formato YYYY-MM-DD (variável utilizada nos anos de 2012 e 2013)                              |
| 7    | cod_local_domic_fam               | Numeric| 1                 |                  | Características do local onde está situado o domicílio: 1 - Urbanas, 2 - Rurais                                |
| 8    | cod_especie_domic_fam             | Numeric| 1                 |                  | Espécie do domicílio: 1 - Particular Permanente, 2 - Particular improvisado, 3 - Coletivo                       |
| 9    | qtd_comodos_domic_fam             | Numeric| 2                 |                  | Quantidade de cômodos do domicílio                                                                             |
| 10   | qtd_comodos_dormitorio_fam        | Numeric| 2                 |                  | Quantidade de cômodos servindo como dormitório do domicílio                                                    |
| 11   | cod_material_piso_fam             | Numeric| 1                 |                  | Material predominante no piso do domicílio: 1 - Terra, 2 - Cimento, 3 - Madeira aproveitada, etc.              |
| 12   | cod_material_domic_fam            | Numeric| 1                 |                  | Material predominante nas paredes externas do domicílio: 1 - Alvenaria/tijolo com revestimento, etc.           |
| 13   | cod_agua_canalizada_fam           | Numeric| 1                 |                  | Se o domicílio tem água encanada: 1 - Sim, 2 - Não                                                             |
| 14   | cod_abaste_agua_domic_fam         | Numeric| 1                 |                  | Forma de abastecimento de água: 1 - Rede geral de distribuição, 2 - Poço ou nascente, etc.                     |
| 15   | cod_banheiro_domic_fam            | Numeric| 1                 |                  | Existência de banheiro: 1 - Sim, 2 - Não                                                                       |
| 16   | cod_escoa_sanitario_domic_fam     | Numeric| 1                 |                  | Forma de escoamento sanitário: 1 - Rede coletora de esgoto ou pluvial, etc.                                    |
| 17   | cod_destino_lixo_domic_fam        | Numeric| 1                 |                  | Forma de coleta do lixo: 1 - É coletado diretamente, 2 - É coletado indiretamente, etc.                        |
| 18   | cod_iluminacao_domic_fam          | Numeric| 1                 |                  | Tipo de iluminação: 1 - Elétrica com medidor próprio, 2 - Elétrica com medidor comunitário, etc.               |
| 19   | cod_calcamento_domic_fam          | Numeric| 1                 |                  | Calçamento: 1 - Total, 2 - Parcial, 3 - Não existe                                                             |
| 20   | cod_familia_indigena_fam          | Numeric| 1                 |                  | Família indígena: 1 - Sim, 2 - Não                                                                             |
| 21   | ind_familia_quilombola_fam        | Numeric| 1                 |                  | Família quilombola: 1 - Sim, 2 - Não                                                                           |
| 22   | nom_estab_assist_saude_fam        | String | 70                |                  | Nome do estabelecimento EAS/MS                                                                                 |
| 23   | cod_eas_fam                       | String | 12                |                  | Código do estabelecimento EAS/MS                                                                               |
| 24   | nom_centro_assist_fam             | String | 70                |                  | Nome do CRAS/CREAS                                                                                            |
| 25   | cod_centro_assist_fam             | String | 12                |                  | Código do CRAS/CREAS                                                                                           |
| 26   | ind_parc_mds_fam                  | Numeric| 3                 |                  | Grupos tradicionais e específicos: 101 Família Cigana, 201 Família Extrativista, 202 Família de Pescadores, etc.|
| 27   | peso_fam                          | Numeric| 1                 | 14               | Peso calculado da família                                                                                      |
| 28   | id_familia                        | Numeric| 8                 |                  | Identificador único da família para pareamento com a base de pessoas                                           |
| 29   | estrato                           | Numeric| 1                 |                  | Grandes grupos de municípios, de acordo com a quantidade de famílias cadastradas: 1 - GM1 (101 a 5.000 famílias), etc. |
| 30   | classf                            | Numeric| 1                 |                  | Subdivisão pela Unidade Federativa e divisão administrativa: 1 - Capital, 2 - Região Metropolitana (RM) ou Região Integrada de Desenvolvimento (RIDE), etc. |
| 31   | qtd_pessoas                       | Numeric| 1                 |                  | Quantidade de pessoas utilizada no cálculo da renda per capita familiar – variável calculada pelo sistema        |
| 32   | marc_pbf                          | Numeric| 1                 |                  | Marcação se a família é beneficiária do Programa Bolsa Família: 0 – Não, 1 – Sim                               |

### Base pessoas

| Seq. | Nome da variável                 | Tipo    | Tamanho (Inteiro) | Tamanho (Decimal) | Descrição                                                                                                                                           |
|------|-----------------------------------|---------|-------------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| 1    | cd_ibge                          | String  | 7                 |                   | Código IBGE do Município                                                                                                                             |
| 2    | cod_sexo_pessoa                  | Numeric | 1                 |                   | Sexo: 1 - Masculino, 2 - Feminino                                                                                                                    |
| 3    | idade                            | Numeric | 3                 |                   | Idade calculada a partir da diferença entre a data de nascimento da pessoa e a data de referência da base                                             |
| 4    | cod_parentesco_rf_pessoa          | Numeric | 2                 |                   | Relação de parentesco com o RF: 1 - Pessoa Responsável pela Unidade Familiar, 2 - Cônjuge ou companheiro(a), ...                                      |
| 5    | cod_raca_cor_pessoa              | Numeric | 1                 |                   | Cor ou raça: 1 - Branca, 2 - Preta, 3 - Amarela, 4 - Parda, 5 - Indígena                                                                             |
| 6    | cod_local_nascimento_pessoa      | Numeric | 1                 |                   | Local de nascimento: 1 - Neste município, 2 - Em outro município, 3 - Em outro país                                                                  |
| 7    | cod_certidao_registrada_pessoa   | Numeric | 1                 |                   | Pessoa registrada em cartório: 1 - Sim e tem Certidão de Nascimento, 2 - Sim, mas não tem Certidão, 3 - Não                                           |
| 8    | cod_deficiencia_memb             | Numeric | 1                 |                   | Pessoa tem deficiência: 1 - Sim, 2 - Não                                                                                                             |
| 9    | cod_sabe_ler_escrever_memb       | Numeric | 1                 |                   | Pessoa sabe ler e escrever: 1 - Sim, 2 - Não                                                                                                         |
| 10   | ind_frequenta_escola_memb        | Numeric | 1                 |                   | Pessoa frequenta escola: 1 - Sim, rede pública, 2 - Sim, rede particular, 3 - Não, já frequentou, 4 - Nunca frequentou                               |
| 11   | cod_escola_local_memb            | Numeric | 1                 |                   | Escola localizada no município: 1 - Sim, 2 - Não                                                                                                     |
| 12   | cod_curso_frequenta_memb         | Numeric | 2                 |                   | Curso que a pessoa frequenta: 1 - Creche, 2 - Pré-escola (exceto CA), 3 - Classe de Alfabetização - CA, 4 - Ensino Fundamental, ...                    |
| 13   | cod_ano_serie_frequenta_memb     | Numeric | 2                 |                   | Ano e série que a pessoa frequenta: 1 - Primeiro, 2 - Segundo, 3 - Terceiro, ...                                                                     |
| 14   | cod_curso_frequentou_pessoa_memb | Numeric | 2                 |                   | Curso mais elevado que a pessoa frequentou: 1 - Creche, 2 - Pré-escola, 3 - Classe de Alfabetização - CA, 4 - Ensino Fundamental, ...                 |
| 15   | cod_ano_serie_frequentou_memb    | Numeric | 2                 |                   | Último ano e série frequentado pela pessoa: 1 - Primeiro, 2 - Segundo, 3 - Terceiro, ...                                                             |
| 16   | cod_concluiu_frequentou_memb     | Numeric | 1                 |                   | A pessoa concluiu o curso: 1 - Sim, 2 - Não                                                                                                          |
| 17   | cod_trabalhou_memb               | Numeric | 1                 |                   | Pessoa trabalhou na semana passada: 1 - Sim, 2 - Não                                                                                                 |
| 18   | cod_afastado_trab_memb           | Numeric | 1                 |                   | Pessoa afastada na semana passada: 1 - Sim, 2 - Não                                                                                                  |
| 19   | cod_agricultura_trab_memb        | Numeric | 1                 |                   | É atividade extrativista: 1 - Sim, 2 - Não                                                                                                           |
| 20   | cod_principal_trab_memb          | Numeric | 2                 |                   | Função principal: 1 - Trabalhador por conta própria, 2 - Trabalhador temporário em área rural, 3 - Empregado sem carteira de trabalho assinada, ...   |
| 21   | val_remuner_emprego_memb         | Numeric | 5                 |                   | Valor da remuneração no formato NNNNN (sem casas decimais). Ex: uma remuneração de R$ 125,00 constará na base como 125                                |
| 22   | cod_trabalho_12_meses_memb       | Numeric | 1                 |                   | Pessoa com trabalho remunerado em algum período nos últimos 12 meses: 1 - Sim, 2 - Não                                                               |
| 23   | qtd_meses_12_meses_memb          | Numeric | 2                 |                   | Quantidade de meses trabalhados nos últimos 12 meses                                                                                                 |
| 24   | val_renda_bruta_12_meses_memb    | Numeric | 5                 |                   | Valor de remuneração bruta no formato NNNNN (sem casas decimais). Ex: uma remuneração de R$ 125,00 constará na base como 125                          |
| 25   | val_renda_doacao_memb            | Numeric | 5                 |                   | Valor recebido de doação no formato NNNNN (sem casas decimais). Ex: uma renda de R$ 125,00 constará na base como 125                                  |
| 26   | val_renda_aposent_memb           | Numeric | 5                 |                   | Valor recebido de aposentadoria no formato NNNNN (sem casas decimais). Ex: uma remuneração de R$ 125,00 constará na base como 125                     |
| 27   | val_renda_seguro_desemp_memb     | Numeric | 5                 |                   | Valor recebido de seguro desemprego no formato NNNNN (sem casas decimais). Ex: um valor de R$ 125,00 constará na base como 125                        |
| 28   | val_renda_pensao_alimen_memb     | Numeric | 5                 |                   | Valor recebido de pensão alimentícia no formato NNNNN (sem casas decimais). Ex: uma renda de R$ 125,00 constará na base como 125                      |
| 29   | val_outras_rendas_memb           | Numeric | 5                 |                   | Valor recebido de outras fontes no formato NNNNN (sem casas decimais). Ex: uma renda de R$ 125,00 constará na base como 125                           |
| 30   | peso.fam                        | Numeric | 1                 | 14                | Peso calculado da família                                                                                                                            |
| 31   | peso.pes                        | Numeric | 1                 | 14                | Peso calculado da pessoa                                                                                                                             |
| 32   | id_familia                      | Numeric | 8                 |                   | Identificador único da família de vinculação da pessoa para pareamento com a base de famílias                                                        |
| 33   | estrato                         | Numeric | 1                 |                   | São grandes grupos de municípios, de acordo com a quantidade de famílias cadastradas: 1 - GM1 (101 A 5.000 famílias), 2 - GM2 (5.001 ou mais famílias) |
| 34   | classf                          | Numeric | 1                 |                   | Subdivisão pela Unidade Federativa e divisão administrativa: 1 - Capital, 2 - Região Metropolitana (RM) ou Região Integrada de Desenvolvimento (RIDE) |



## Variável dependente
A variavél dependente do projeto é a vlr_renda_media_fam: Valor da renda média (per capita) da família. Será criada uma nova variável, com a classe da faixa de renda da família, conforme se segue:
* Classe 1: Pobreza (de 0 a 218,00);
* Classe 2: Baixa renda (de 218,01 a 1/2 salário-mínimo);
* Classe 3: Acima de 1/2 salário-mínimo.

## Variáveis independentes
Para a seleção das variáveis independentes, serão aplicadas técnicas de Machine Learning para definição das que contribuem diretamente para a classificação mais adequada das famílias nas classes de renda. Além disso, será realizada engenharia de features para a construção de novas variáveis, a partir das existentes, que podem contribuir para a maior acurácia do modelo. 
De modo a ouvir a área de negócio, será realizada uma reunião com a Coordenação-Geral de Acompanhamento e Qualificação do Cadastro, do Departamento de Operação do Cadastro Único (CGAQC/DECAU). 
A partir das contribuições da área de negócio e com o objetivo de possibilitar o exercício por todos os autores do projeto no âmbito do Bootcamp, as análises serão divididas conforme se segue:

### Análise 1: 
* 1_infancia: nova variável construída a partir da variável "idade", de modo a identificar se na família tem ao menos 1 pessoa na 1ª infância, ou seja de 0 a 6 anos de idade, sendo 0 se não tem e 1 se existe na família ao menos 1 pessoa;
* crianca_adolescente: nova variável construída a partir da variável "idade", de modo a identificar se na família tem ao menos 1 pessoa que tenha mais de 6 anos e até 17 anos de idade, sendo 0 se não tem e 1 se existe na família ao menos 1 pessoa;
* idoso: nova variável construída a partir da variável "idade" de modo a identificar se na família tem ao menos 1 pessoa com 60 anos ou mais; 
* deficiencia: nova variável construída a partir da variável "cod_deficiencia_memb" de modo a identificar se na família há pelo menos 1 pessoa com deficiência, sendo 0 se não tem e 1 se existe na família pelo menos 1 pessoa com deficiência;
* alfabetizado: nova variável combinando as variáveis "cod_sabe_ler_escrever_memb" e "idade" de  Pessoa sabe ler e escrever de modo a identificar se na família a pelo menos uma pessoa com mais de 10 anos sem saber ler ou escrever, sendo 0 para quando não houver e 1 para quando houver;
* frequenta_escola: nova variávbel comninando as variáveis "ind_frequenta_escola_memb" e "idade" de modo a identificar se na família há pelo menos 1 pessoa com menos de 17 anos que não está na escola;
* memb_trabalhou_estudou: nova variável combinando as variáveis "cod_trabalhou_memb", "idade", "ind_frequenta_escola_memb" e "cod_parentesco_rf_pessoa", quando "cod_parentesco_rf_pessoa" for diferente de 1, de modo a identificar se na família existe outra pessoa, que não seja o responsável familiar, com 15 anos ou mais, que não trabalhou na semana passada ("cod_trabalhou_memb"=2) e que não estuda ("ind_frequenta_escola_memb"=3 ou 4), sendo 0 se não existir pessoa com essas características e 1 se existir.

### Análise 2:


### Análise 3:


### Análise 4:


### Variáveis comuns a todas as análises:
#### Base famílias
* dat_cadastramento_fam - Número de dias entre 31/12/2018 e a data de cadastramento;
* dat_atualizacao_familia - Número de dias entre 31/12/2018 e a data de atualização cadastral;
* cod_local_domic_fam;
* cod_agua_canalizada_fam;
* cod_escoa_sanitario_domic_fam;
* cod_familia_indigena_fam; ind_familia_quilombola_fam; ind_parc_mds_fam: 0 no caso de não pertencer a nenhum Grupo populacional tradicional e específico, 1 no caso de pertencer a pelo menos 1;
* qtd_pessoas: Quantidade de pessoas utilizada no cálculo da renda per capita familiar;

#### Base pessoas
* rf_mulher - Nova variável cruzando as variáveis "cod_sexo_pessoa" e "cod_parentesco_rf_pessoa", para o caso de resposta 1 para a variável "cod_parentesco_rf_pessoa", sendo 0 para o caso do RF não ser mulher e 1 para o caso de ser mulher;
* rf_branca - Nova variável cruzando as variáveis "cod_raca_cor_pessoa" e "cod_parentesco_rf_pessoa", para o caso de resposta 1 para a variável "cod_raca_cor_pessoa" e 1 para a variável "cod_parentesco_rf_pessoa", sendo 0 para o caso do RF não ser Branca e 1 para o caso de ser branca;
* rf_preta - Nova variável cruzando as variáveis "cod_raca_cor_pessoa" e "cod_parentesco_rf_pessoa", para o caso de resposta 2 para a variável "cod_raca_cor_pessoa" e 1 para a variável "cod_parentesco_rf_pessoa", sendo 0 para o caso do RF não ser Preta e 1 para o caso de ser Preta;
* rf_amarela - Nova variável cruzando as variáveis "cod_raca_cor_pessoa" e "cod_parentesco_rf_pessoa", para o caso de resposta 3 para a variável "cod_raca_cor_pessoa" e 1 para a variável "cod_parentesco_rf_pessoa", sendo 0 para o caso do RF não ser Amarela e 1 para o caso de ser Amarela;
* rf_parda - Nova variável cruzando as variáveis "cod_raca_cor_pessoa" e "cod_parentesco_rf_pessoa", para o caso de resposta 4 para a variável "cod_raca_cor_pessoa" e 1 para a variável "cod_parentesco_rf_pessoa", sendo 0 para o caso do RF não ser Parda e 1 para o caso de ser Parda;
* rf_indigena - Nova variável cruzando as variáveis "cod_raca_cor_pessoa" e "cod_parentesco_rf_pessoa", para o caso de resposta 5 para a variável "cod_raca_cor_pessoa" e 1 para a variável "cod_parentesco_rf_pessoa", sendo 0 para o caso do RF não ser Indígena e 1 para o caso de ser Indígena;
* rf_trabalhou - Nova variável cruzando as variáveis "cod_trabalhou_memb" e "cod_parentesco_rf_pessoa", para o caso de resposta 1 para a variável "cod_parentesco_rf_pessoa", sendo 0 para o caso do RF não ter trabalhado na semana passada e 1 para o caso de ter trabalhado;
* rf_qtd_meses_12_meses_memb - Nova variável cruzando as variáveis "qtd_meses_12_meses_memb" e "cod_parentesco_rf_pessoa", para o caso de resposta 1 para a variável "cod_parentesco_rf_pessoa", sendo a resposta o número de meses que o RF trabalhou nos últimos 12 meses.

## Autores do projeto (ordem alfabética)
Grinaldo Oliveira

Mariana Nogueira de Resende Sousa

Renata

Risla

