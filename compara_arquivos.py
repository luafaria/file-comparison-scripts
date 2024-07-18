import os
import pandas as pd

# Diretórios de entrada e saída
input_dir = 'input'
output_dir = 'output'

# Verificar se os diretórios existem, caso contrário, criá-los
os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# Caminhos dos arquivos Excel comuns (dados fictícios)
arquivo1_comum = os.path.join(output_dir, 'dados1_comum.xlsx')
arquivo2_comum = os.path.join(output_dir, 'dados2_comum.xlsx')

# Carregar os arquivos Excel para DataFrames do pandas
df_dados1 = pd.read_excel(arquivo1_comum)
df_dados2 = pd.read_excel(arquivo2_comum)

# Filtrar dados2_comum pelas linhas que têm ID_TRANSACAO presente em dados1_comum
transacoes_dados1 = df_dados1['ID_TRANSACAO'].unique()
df_dados2_filtrado = df_dados2[df_dados2['ID_TRANSACAO'].isin(transacoes_dados1)]

# Filtrar dados2_comum pelas linhas que não têm STATUS_TRANSACAO igual a 'Aprovada'
df_dados2_filtrado = df_dados2_filtrado[df_dados2_filtrado['STATUS_TRANSACAO'] != 'Aprovada']

# Adicionar coluna para marcar a origem
df_dados1['TIPO'] = 'DADOS1'
df_dados2_filtrado['TIPO'] = 'DADOS2'

# Concatenar os DataFrames
resultado_comparacao = pd.concat([df_dados1, df_dados2_filtrado], ignore_index=True)

# Caminho para salvar o DataFrame resultante em um novo arquivo Excel com cabeçalho
arquivo_resultado = os.path.join(output_dir, 'resultado_comparacao_dados_comum.xlsx')

# Salvar o DataFrame resultante no arquivo especificado
resultado_comparacao.to_excel(arquivo_resultado, index=False, header=True)

# Exemplo de exibição do DataFrame resultante
print("Linhas correspondentes encontradas:")
print(resultado_comparacao.head())

print(f"Resultado da comparação salvo em: {arquivo_resultado}")