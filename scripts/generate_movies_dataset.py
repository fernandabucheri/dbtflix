from faker import Faker
import random
import pandas as pd
import numpy as np

print("Iniciando a geração dos dados aleatórios, aguarde...")

# Inicializa o gerador de dados falsos
fake = Faker('en_US')

# Lista dos gêneros de filme que vamos usar
movie_genres = ['Drama', 'Crime', 'Action', 'Fantasy', 'Sci-Fi', 'Animation', 'Comedy', 'Thriller', 'Musical']

# Aqui definimos a chance de cada gênero aparecer. 
# Por exemplo, 'Drama' tem 20% de chance, 'Sci-Fi' só 5%, etc.
# Isso ajuda a simular que alguns gêneros são mais comuns que outros na nossa base.
genre_probs = [0.20, 0.10, 0.15, 0.10, 0.05, 0.10, 0.15, 0.10, 0.05]

# Definimos as características da nota média (rating) para cada gênero:
# Cada gênero tem uma média e um desvio padrão, que usamos para criar variação realista.
rating_params = {
    'Drama':      (7.0, 1.0),
    'Crime':      (6.5, 1.2),
    'Action':     (6.8, 1.1),
    'Fantasy':    (7.2, 0.9),
    'Sci-Fi':     (7.3, 0.8),
    'Animation':  (7.5, 0.7),
    'Comedy':     (6.9, 1.0),
    'Thriller':   (6.7, 1.1),
    'Musical':    (7.1, 0.9),
}

# Lista vazia para armazenar todas as linhas (filmes) que vamos criar
data = []

for i in range(1, 100001):
    # Cria um título fake com 3 palavras (exemplo: "Lost stars shine")
    # Remove o ponto final que vem no final da sentença
    title = fake.sentence(nb_words=3).replace('.', '')
    
    # Escolhe um gênero para o filme, usando as probabilidades definidas antes
    # Assim a distribuição dos gêneros fica realista, não uniforme
    genre = random.choices(movie_genres, weights=genre_probs, k=1)[0]
    
    # Define um ano de lançamento aleatório entre 1940 e 2024
    year = random.randint(1940, 2024)
    
    # Pega a média e o desvio padrão de rating para o gênero escolhido
    mean, std = rating_params[genre]
    
    # Gera uma nota aleatória para o filme, seguindo uma distribuição normal
    # com aquela média e desvio, simulando avaliações reais que se concentram
    # em torno de uma média, mas com variação natural
    # Depois, limitamos o valor para ficar entre 0 e 10 (não tem nota negativa ou acima de 10)
    rating = np.clip(np.random.normal(mean, std), 0, 10)
    
    # Arredonda a nota para duas casas decimais, para ficar mais realista
    rating = round(rating, 2)
    
    # Adiciona a linha criada à lista, com id, título, gênero, ano e nota
    data.append([i, title, genre, year, rating])

# Transforma a lista de listas em um DataFrame do pandas, com colunas nomeadas
df = pd.DataFrame(data, columns=['id', 'title', 'genre', 'release_year', 'rating'])

# Salva o DataFrame em um arquivo CSV, sem o índice e com codificação UTF-8
df.to_csv('data/movies.csv', index=False, encoding='utf-8')

print("Dados gerados com sucesso!")