import os
import pandas as pd

# Carregar o arquivo grande
file_path = 'data/tweets.csv'
chunk_size = 50000  # Número de linhas por parte

# Ler o arquivo em partes menores
for i, chunk in enumerate(pd.read_csv(file_path, chunksize=chunk_size, encoding='ISO-8859-1')):
    chunk.to_csv(f'data/tweets_part_{i}.csv', index=False)

# Remover o arquivo original
os.remove(file_path)
