#!/usr/bin/env python
# coding: utf-8

# -------------------------------------------------
# Inicio
# -------------------------------------------------

import os, sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import warnings 
warnings.filterwarnings("ignore")

import argparse
parser = argparse.ArgumentParser(description="Exibe um nome passado como argumento.")
parser.add_argument('path_file_entrada', type=str, help='Caminho e Nome do arquivo a ser carregado')
parser.add_argument('path_file_saida', type=str, help='Caminho e Nome do arquivo processado')
args = parser.parse_args()

vlr_salario_minimo_2018 = 954
vlr_lim_pobreza = 178.00

# -------------------------------------------------
# Funcoes
# -------------------------------------------------

def define_cod_faixa_renda(x):
    '''
    PBZ: pobreza
    BRD: baixa renda
    ASM: acima de 1/2 salario minimo
    '''
    meio_sm = vlr_salario_minimo_2018/2
    
    if x >=0 and x <= vlr_lim_pobreza: return 'PBZ'
    elif x > vlr_lim_pobreza and x <= meio_sm: return 'BRD'
    elif x > meio_sm: return 'ASM'
    else: return 'nao informado'

def define_nom_faixa_renda(x):
    '''
    PBZ: pobreza
    BRD: baixa renda
    ASM: acima de 1/2 salario minimo
    '''
    meio_sm = vlr_salario_minimo_2018/2
    
    if x >=0 and x <= vlr_lim_pobreza: return 'Pobreza'
    elif x > vlr_lim_pobreza and x <= meio_sm: return 'Baixa Renda'
    elif x > meio_sm: return 'Acima de 1/2 salario minimo'
    else: return 'nao informado'

def incluir_nomes(df, coluna, nova_coluna, mapa_nomes):
    df[nova_coluna] = df[coluna].map(mapa_nomes)


# -------------------------------------------------
# Ler dados
# -------------------------------------------------
#df_fam = pd.read_csv('./dados/df_familia_final.csv', sep=',', low_memory=False)

print('\nInicio do script...')

print('Lendo o arquivo de entrada...', args.path_file_entrada)
df_fam = pd.read_csv(args.path_file_entrada, sep=',', low_memory=False)

# -------------------------------------------------
# PRIMEIRA PARTE
# -------------------------------------------------
# Engenharia de atributos
print('\nPRIMEIRA PARTE: Realizando Engenharia de atributos...')
print('*'*70)

# -------------------------------------------------
# Converter tipos
# -------------------------------------------------
print('Convertendo atributos para inteiro ou string...')
l_col_str = ['cd_ibge','uf_ibge', 'regiao_ibge', 'id_familia']
l_col_int = [col for col in df_fam.columns if col.startswith('cod') 
                 or col.startswith('qtd') 
                 or col.startswith('dias')
                 or col.startswith('ind')]  
l_col_int = l_col_int + ['estrato','classf', 'classe_renda']
for c in l_col_int:
    df_fam[c] = df_fam[c].astype(int)
for c in l_col_str:
    df_fam[c] = df_fam[c].astype(str)


# -------------------------------------------------
# Criar campos para classe renda
# -------------------------------------------------
print('Criando campos de codigo e nome para vlr_renda_media_fam...')
df_fam['cod_faixa_renda'] = df_fam['vlr_renda_media_fam'].apply(lambda x: define_cod_faixa_renda(x))
df_fam['nom_faixa_renda'] = df_fam['vlr_renda_media_fam'].apply(lambda x: define_nom_faixa_renda(x))


# -------------------------------------------------
# Criar colunas de nomes para outros atributos
# -------------------------------------------------
print('Criando campos de nomes para outros atributos...')

# uf_ibge
# -------------------------------------------------
mapa_sigla_UF = {
    '12':'AC','27':'AL','13':'AM','16':'AP','29':'BA',
    '23':'CE','53':'DF','32':'ES','52':'GO','21':'MA',
    '31':'MG','50':'MS','51':'MT','15':'PA','25':'PB',
    '26':'PE','22':'PI','41':'PR','33':'RJ','24':'RN',
    '11':'RO','14':'RR','43':'RS','42':'SC','28':'SE',
    '35':'SP','17':'TO'}
incluir_nomes(df_fam, 'uf_ibge', 'nome_uf_ibge', mapa_sigla_UF)


# regiao_ibge
# -------------------------------------------------
mapa_regioes = {'1': 'Norte', '2': 'Nordeste', '3': 'Centro_Oeste','4': 'Sudeste', '5': 'Sul'}
incluir_nomes(df_fam, 'regiao_ibge', 'nome_regiao_ibge', mapa_regioes)


# classf
# -------------------------------------------------
mapa_classf = {1: 'Capital', 2: 'Regiao_Metrop', 3: 'Outros'}
incluir_nomes(df_fam, 'classf', 'nome_classf', mapa_classf)


# cod_local_domic_fam
# -------------------------------------------------
mapa_local_domic = {1: 'Urbanas', 2: 'Rurais', 9: 'Nao_se_aplica'}
incluir_nomes(df_fam, 'cod_local_domic_fam', 'nome_local_domic_fam', mapa_local_domic)	


# cod_especie_domic_fam
# -------------------------------------------------
mapa_especie_domic = {
    1: 'Particular_Permanente',
    2: 'Particular_improvisado',
    3: 'Coletivo',
    9: 'Nao_se_aplica'}
incluir_nomes(df_fam, 'cod_especie_domic_fam', 'nome_especie_domic_fam', mapa_especie_domic)	


# cod_material_piso_fam
# -------------------------------------------------
mapa_material_piso = {
   -1: 'Nao_se_aplica',
    1: 'Terra',
    2: 'Cimento',
    3: 'Madeira_aprov',
    4: 'Madeira_apar',
    5: 'Ceram_laj_pedra',
    6: 'Carpete',
    7: 'Outro'}
incluir_nomes(df_fam, 'cod_material_piso_fam', 'nome_material_piso_fam', mapa_material_piso)


# cod_material_domic_fam
# -------------------------------------------------
mapa_material_domic = {
   -1: 'Nao_se_aplica',
    1: 'Alvenaria_ou_tijolo_com_revestimento',
    2: 'Alvenaria_ou_tijolo_sem_revestimento',
    3: 'Madeira_apar',
    4: 'Taipa_revestida',
    5: 'Taipa_nao_revestida',
    6: 'Madeira_aprov',
    7: 'Palha',
    8: 'Outro_Material'}
incluir_nomes(df_fam, 'cod_material_domic_fam', 'nome_material_domic_fam',  mapa_material_domic)


# cod_agua_canalizada_fam
# -------------------------------------------------
mapa_agua_canaliz = {
    1: 'Tem_agua_canalizada',
    2: 'Nao_tem_agua_canalizada',
    -1: 'Nao_se_aplica'}
incluir_nomes(df_fam, 'cod_agua_canalizada_fam', 'nome_agua_canalizada_fam', mapa_agua_canaliz)	


# cod_abaste_agua_domic_fam
# -------------------------------------------------
mapa_abastec_agua = {
    1: 'Rede_distribuicao',
    2: 'Poco_ou_Nascente',
    3: 'Cisterna',
    4: 'Outros',
   -1: 'Nao_se_aplica'}
incluir_nomes(df_fam, 'cod_abaste_agua_domic_fam', 'nome_abaste_agua_domic_fam', mapa_abastec_agua)	


# cod_banheiro_domic_fam
# -------------------------------------------------
mapa_banheiro_domic = {1: 'Com_banheiro', 2: 'Sem_banheiro', -1: 'Nao_se_aplica'}
incluir_nomes(df_fam, 'cod_banheiro_domic_fam', 'nome_banheiro_domic_fam', mapa_banheiro_domic)	


# cod_escoa_sanitario_domic_fam
# -------------------------------------------------
mapa_escoa_sanitario = {
    1: 'Rede_coletora de esgoto/ pluvial',
    2: 'Fossa_septica',
    3: 'Fossa_rudimentar',
    4: 'Vala_ceu_aberto',
    5: 'Direto_para_rio_mar',
    6: 'Outro',
   -1: 'Nao_se_aplica'}
incluir_nomes(df_fam, 'cod_escoa_sanitario_domic_fam', 'nome_escoa_sanitario_domic_fam', mapa_escoa_sanitario)	


# cod_destino_lixo_domic_fam
# -------------------------------------------------
mapa_destino_lixo = {
    1: 'Coletado_diretamente',
    2: 'Coletado_indiretamente',
    3: 'Queimado_ou_enterrado_propriedade',
    4: 'Jogado_em_terreno_baldio_ou_logradouro',
    5: 'Jogado_rio_mar',
    6: 'Outro_destino',
   -1: 'Nao_se_aplica'}
incluir_nomes(df_fam, 'cod_destino_lixo_domic_fam', 'nome_destino_lixo_domic_fam', mapa_destino_lixo)	

# cod_iluminacao_domic_fam
# -------------------------------------------------
mapa_ilum = {
    1: 'Eletrica_med_proprio',
    2: 'Eletrica_med_comunitario',
    3: 'Eletrica_sem med',
    4: 'Oleo_querosene_gas',
    5: 'Vela',
    6: 'Outra_forma',
   -1: 'Nao_se_aplica'}
incluir_nomes(df_fam, 'cod_iluminacao_domic_fam', 'nome_iluminacao_domic_fam', mapa_ilum)	


# cod_calcamento_domic_fam
# -------------------------------------------------
mapa_calc = {
    1: 'Total',
    2: 'Parcial',
    3: 'Nao_existe',
   -1: 'Nao_se_aplica'}
incluir_nomes(df_fam, 'cod_calcamento_domic_fam', 'nome_calcamento_domic_fam', mapa_calc)	


# -------------------------------------------------
# Criar indicador de grupo especial
# -------------------------------------------------
print('Criando campos simplificados para grupos específicos...')

df_fam['ind_grp_especifico'] = np.where(df_fam['ind_parc_mds_fam']==0, 'Nao', 'Sim')

df_fam['ind_grp_especial'] = np.where(
                                (df_fam['ind_grp_especifico'] == 'Sim') | 
                                ((df_fam['ind_grp_especifico'] == 'Nao') & (df_fam['cod_familia_indigena_fam'] == 1)) |
                                ((df_fam['ind_grp_especifico'] == 'Nao') & (df_fam['ind_familia_quilombola_fam'] == 1)), 
                                'Sim', 'Nao')

# -------------------------------------------------
# Simplificar listas
# -------------------------------------------------
print('Criando campos simplificados para outros atributos...')

# qtd_comodos_domic_fam
# -------------------------------------------------
bins = [0, 2, 3, 4, 5, 16]
labels = ['menor_igual_2', '3', '4', '5', 'maior_igual_6']
df_fam['faixa_comodos_domic_fam'] = pd.cut(df_fam['qtd_comodos_domic_fam'], 
                                           bins=bins, 
                                           labels=labels, 
                                           include_lowest=True)
df_fam['faixa_comodos_domic_fam'] = np.where(df_fam['qtd_comodos_domic_fam'] == -1, 'Nao_se_aplica', 
                                             df_fam['faixa_comodos_domic_fam'])


# qtd_comodos_dormitorio_fam
# -------------------------------------------------
bins = [-1, 0, 1, 2, 12]
labels = ['Nenhum', 'Apenas_1', 'Apenas_2', 'maior_igual_3']
df_fam['faixa_comodos_dormitorio_fam'] = pd.cut(df_fam['qtd_comodos_dormitorio_fam'], 
                                                bins=bins, labels=labels, include_lowest=True)
df_fam['faixa_comodos_dormitorio_fam'] = np.where(df_fam['qtd_comodos_dormitorio_fam'] == -1, 'Nao_se_aplica', 
                                             df_fam['faixa_comodos_dormitorio_fam'])
df_fam['faixa_comodos_dormitorio_fam'] = np.where(df_fam['qtd_comodos_dormitorio_fam'] >12, 'maior_igual_3', 
                                             df_fam['faixa_comodos_dormitorio_fam'])


# qtde_pessoas
# -------------------------------------------------
bins = [0, 1, 2, 3, 13]
labels = ['1_pessoa', '2_pessoas', '3_pessoas', 'maior_igual_4 pessoas']

df_fam['faixa_qtde_pessoas'] = pd.cut(df_fam['qtde_pessoas'], 
                                      bins=bins, labels=labels, include_lowest=True)
df_fam['faixa_qtde_pessoas'] = np.where(df_fam['qtde_pessoas'] == -1, 'Nao_se_aplica', 
                                             df_fam['faixa_qtde_pessoas'])


# cod_banheiro_domic_fam/ cod_escoa_sanitario_domic_fam
# -------------------------------------------------
condicoes = [
  (df_fam['cod_banheiro_domic_fam'] == -1) & (df_fam['cod_escoa_sanitario_domic_fam'] == -1), 
  (df_fam['cod_banheiro_domic_fam'] ==  2) & (df_fam['cod_escoa_sanitario_domic_fam'] == -1), 
  (df_fam['cod_banheiro_domic_fam'] ==  1) & (df_fam['cod_escoa_sanitario_domic_fam'] ==  1 ),
  (df_fam['cod_banheiro_domic_fam'] ==  1) & (df_fam['cod_escoa_sanitario_domic_fam'].isin([2])),
  (df_fam['cod_banheiro_domic_fam'] ==  1) & (df_fam['cod_escoa_sanitario_domic_fam'].isin([3])),  
  (df_fam['cod_banheiro_domic_fam'] ==  1) & (df_fam['cod_escoa_sanitario_domic_fam'].isin([4,5,6]) )
  ]
valores = ['Sem_banheiro',#'Nao_se_aplica', 
           'Sem_banheiro', 
           'Com_banheiro_rede_coletora', 
           'Com_banheiro_fossa_septica',
           'Com_banheiro_fossa_rudimentar',
           'Com_banheiro_escoamento_inadequado']

df_fam['nome_banh_escoa'] = np.select(condicoes, valores, default='Outros')


# cod_agua_canalizada_fam / cod_abaste_agua_domic_fam
# -------------------------------------------------
condicoes = [
  (df_fam['cod_agua_canalizada_fam'] == -1) & (df_fam['cod_abaste_agua_domic_fam'] == -1), 
  (df_fam['cod_agua_canalizada_fam'] ==  1) & (df_fam['cod_abaste_agua_domic_fam'] == 1), 
  (df_fam['cod_agua_canalizada_fam'] ==  1) & (df_fam['cod_abaste_agua_domic_fam'].isin([2,3,4])),
  (df_fam['cod_agua_canalizada_fam'] ==  2) & (df_fam['cod_abaste_agua_domic_fam']== 1),
  (df_fam['cod_agua_canalizada_fam'] ==  2) & (df_fam['cod_abaste_agua_domic_fam'].isin([2,3,4]))]
valores = ['Nao_se_aplica', 
           'Com_agua_canalizada_rede_distrib', 
           'Com_agua_canalizada_Poco_cisterna_outros', 
           'Sem_agua_canalizada_rede_distrib',
           'Sem_agua_canalizada_Poco_cisterna_outros']
df_fam['nome_agua_abaste'] = np.select(condicoes, valores, default='Outros')	


# cod_destino_lixo_domic_fam
# -------------------------------------------------
condicoes = [
  (df_fam['cod_destino_lixo_domic_fam'] == -1) , 
  (df_fam['cod_destino_lixo_domic_fam'] ==  1) , 
  (df_fam['cod_destino_lixo_domic_fam'] ==  2) ,
  (df_fam['cod_destino_lixo_domic_fam'].isin([3,4,5,6]))]
valores = ['Nao_se_aplica', 
           'Coletado_diretamente', 
           'Coletado_indiretamente', 
           'Sem_Coleta_adequada']
df_fam['nome_dest_lixo_simpl'] = np.select(condicoes, valores, default='Outros')	


# cod_iluminacao_domic_fam
# -------------------------------------------------
condicoes = [
  (df_fam['cod_iluminacao_domic_fam'] == -1), 
  (df_fam['cod_iluminacao_domic_fam'] ==  1), 
  (df_fam['cod_iluminacao_domic_fam'] ==  2),
  (df_fam['cod_iluminacao_domic_fam'] ==  3),
  (df_fam['cod_iluminacao_domic_fam'].isin([4,5,6]))]
valores = ['Nao_se_aplica', 
           'Eletrica_med_proprio', 
           'Eletrica_med_comunitario', 
           'Eletrica_sem_med',
           'Sem_eletricidade']
df_fam['nome_iluminacao_simpl'] = np.select(condicoes, valores, default='Outros')	


# cod_material_piso_fam
# -------------------------------------------------
df_fam['nome_material_piso_simpl'] = np.where(df_fam['cod_material_piso_fam'].isin([3,4,6,7]), 
                                              'Outro', 
                                              df_fam['nome_material_piso_fam'])

# cod_material_domic_fam
# -------------------------------------------------
df_fam['nome_material_domic_simpl'] = np.where(df_fam['cod_material_domic_fam'].isin([4,5,6,7,8]), 
                                              'Outro Material', 
                                              df_fam['nome_material_domic_fam'])



# -------------------------------------------------
# SEGUNDA PARTE
# -------------------------------------------------
# Preprocessamento dos dados para os algoritmos
print('\nSEGUNDA PARTE: Realizando preparação dos dados para algoritmos...')
print('*'*70)


# -------------------------------------------------
# Criação de listas de colunas para facilitar 
# -------------------------------------------------
l_col_id = ['id_familia']
l_col_target_num = ['vlr_renda_media_fam']
l_col_target_cat = ['classe_renda', 'cod_faixa_renda', 'nom_faixa_renda']

l_col_num = ['qtd_comodos_domic_fam', 'qtd_comodos_dormitorio_fam',
             'dias_cadastramento', 'dias_atualizacao', 'qtde_pessoas']
l_col_num_scaled = ['qtd_comodos_domic_fam_scaled', 'qtd_comodos_dormitorio_fam_scaled',
                    'dias_cadastramento_scaled', 'dias_atualizacao_scaled',
                    'qtde_pessoas_scaled']

l_col_cat_num = ['uf_ibge', 'regiao_ibge', 'classf', 
             'cod_local_domic_fam', 'cod_especie_domic_fam',
             'cod_material_piso_fam', 'cod_material_domic_fam',
             'cod_agua_canalizada_fam', 'cod_abaste_agua_domic_fam',
             'cod_banheiro_domic_fam', 'cod_escoa_sanitario_domic_fam',
             'cod_destino_lixo_domic_fam', 'cod_iluminacao_domic_fam',
             'cod_calcamento_domic_fam'] 

l_col_cat_nomes = ['nome_uf_ibge','nome_regiao_ibge', 'nome_classf', 
                   'nome_local_domic_fam', 'nome_especie_domic_fam', 
                   'nome_material_piso_fam', 'nome_material_domic_fam', 
                   'nome_agua_canalizada_fam', 'nome_abaste_agua_domic_fam', 
                   'nome_banheiro_domic_fam', 'nome_escoa_sanitario_domic_fam', 
                   'nome_destino_lixo_domic_fam', 'nome_iluminacao_domic_fam', 
                   'nome_calcamento_domic_fam']

l_col_cat_num_outras = ['estrato',
                    'cod_familia_indigena_fam',
                    'ind_familia_quilombola_fam',
                    'ind_parc_mds_fam']

l_col_cat_nomes_simpl = ['nome_banh_escoa', 'nome_agua_abaste', 
                         'nome_dest_lixo_simpl', 'nome_iluminacao_simpl',
                         'nome_material_piso_simpl', 'nome_material_domic_simpl',
                         'ind_grp_especifico', 'ind_grp_especial']

l_col_cat_faixas = ['faixa_comodos_domic_fam', 'faixa_comodos_dormitorio_fam', 'faixa_qtde_pessoas']


# -------------------------------------------------
# Converter atributos num_categoricos para string
# -------------------------------------------------
print('Converter atributos num_categoricos para string...')
for c in l_col_cat_num:
    df_fam[c] = df_fam[c].astype(str)

for c in l_col_cat_num_outras:
    df_fam[c] = df_fam[c].astype(str)


# -------------------------------------------------
# Normalizar atributos numéricos
# -------------------------------------------------
print('Normalizar atributos numéricos...')
scaler = StandardScaler()
df_fam_scaled = pd.DataFrame(scaler.fit_transform(df_fam[l_col_num]),
                             columns=[f'{col}_scaled' for col in l_col_num])

df_fam = pd.concat([df_fam, df_fam_scaled], axis=1)
print('Atributos normalizados:\n', df_fam_scaled.columns.values)



# -------------------------------------------------
# Criar colunas One Hot Encoding
# -------------------------------------------------
print('\nCriar colunas One Hot Encoding...')

lista_nomes = l_col_cat_nomes + l_col_cat_num_outras + l_col_cat_nomes_simpl + l_col_cat_faixas
lista_nomes_encoded = [nome + '_encoded' for nome in lista_nomes]

label_encoders = {}
label_mappings = {}

encoder = OneHotEncoder(sparse=False)

for col in lista_nomes:
    one_hot_encoded = encoder.fit_transform(df_fam[[col]])
    one_hot_encoded_df = pd.DataFrame(one_hot_encoded, columns=[f'{col}_{category}' for category in encoder.categories_[0]])
    df_fam = pd.concat([df_fam, one_hot_encoded_df], axis=1)
    label_encoders[col] = encoder
    label_mappings[col] = dict(zip(encoder.categories_[0], range(len(encoder.categories_[0]))))


# -------------------------------------------------
# Salvar dados preparados
# -------------------------------------------------
#df_fam.to_csv('./dados/df_familia_final_preparado.csv', encoding='UTF-8', sep='|', index=False) 


print('\nExecução do script finalizada com sucesso!!!!')
print('Arquivo gerado com novos atributos/ atributos encoded de domicilios: ', args.path_file_saida)
df_fam.to_csv(args.path_file_saida, encoding='UTF-8', sep='|', index=False) 


