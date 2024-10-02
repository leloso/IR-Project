import pandas as pd
from preprocessing import primary_preprocess

chunk_size = 10
chunks = pd.read_csv('data/Greek_Parliament_Proceedings_1989_2020.csv', chunksize=chunk_size, encoding='utf-8')

for chunk in chunks:
    chunk['processed_speech'] = chunk['speech'].apply(primary_preprocess)
    print(chunk[['speech', 'processed_speech']].head())
    break