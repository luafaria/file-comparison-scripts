import pandas as pd

# Caminhos dos arquivos Excel (dados fictícios)
arquivo_dados1 = 'dados1_original.xlsx'
arquivo_dados2 = 'dados2_original.xlsx'

# Novos nomes para os arquivos de saída
novo_arquivo_dados1 = 'dados1_comum.xlsx'
novo_arquivo_dados2 = 'dados2_comum.xlsx'

# Carregar os arquivos Excel para DataFrames do pandas
df_dados1 = pd.read_excel(arquivo_dados1)
df_dados2 = pd.read_excel(arquivo_dados2)

# Obter os nomes das colunas de cada DataFrame
colunas_dados1 = set(df_dados1.columns)
colunas_dados2 = set(df_dados2.columns)

# Encontrar a interseção dos nomes das colunas (colunas em comum)
colunas_comuns = list(colunas_dados1.intersection(colunas_dados2))

# Selecionar apenas as colunas comuns em cada DataFrame
df_dados1_comuns = df_dados1[colunas_comuns]
df_dados2_comuns = df_dados2[colunas_comuns]

# Ordenar as colunas do df_dados2_comuns seguindo a ordem das colunas de df_dados1
df_dados2_comuns = df_dados2_comuns[df_dados1_comuns.columns]

# Salvar os DataFrames com todas as colunas em comum e ordenadas nos novos arquivos
df_dados1_comuns.to_excel(novo_arquivo_dados1, index=False)
df_dados2_comuns.to_excel(novo_arquivo_dados2, index=False)

print(f"Novos arquivos atualizados e salvos com sucesso: {novo_arquivo_dados1} e {novo_arquivo_dados2}.")