import pandas as pd

# Caminhos dos arquivos Excel comuns (dados fictícios)
arquivo1_comum = 'dados1_comum.xlsx'
arquivo2_comum = 'dados2_comum.xlsx'

# Carregar os arquivos Excel para DataFrames do pandas
df_dados1 = pd.read_excel(arquivo1_comum)
df_dados2 = pd.read_excel(arquivo2_comum)

# Obter os CLUSTER_CLIENTE únicos de dados1_comum
clusters_dados1 = df_dados1['CLUSTER_CLIENTE'].unique()

# Filtrar dados2_comum pelas linhas que têm CLUSTER_CLIENTE presente em dados1_comum
df_dados2_filtrado = df_dados2[df_dados2['CLUSTER_CLIENTE'].isin(clusters_dados1)]

# Filtrar dados2_comum pelas linhas que não têm GRUPO_TESTE igual a 'Controle'
df_dados2_filtrado = df_dados2_filtrado[df_dados2_filtrado['GRUPO_TESTE'] != 'Controle']

# Adicionar coluna para marcar a origem
df_dados1['Tipo'] = 'DADOS1'
df_dados2_filtrado['Tipo'] = 'DADOS2'

# Concatenar os DataFrames
resultado_comparacao = pd.concat([df_dados1, df_dados2_filtrado], ignore_index=True)

# Salvar o DataFrame resultante em um novo arquivo Excel com cabeçalho
resultado_comparacao.to_excel('resultado_comparacao_dados_comum.xlsx', index=False, header=True)

# Exemplo de exibição do DataFrame resultante
print("Linhas correspondentes encontradas:")
print(resultado_comparacao.head())