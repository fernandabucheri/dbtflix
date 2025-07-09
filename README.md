# dbtflix

dbtflix é um projeto que utiliza o dbt (ferramenta de transformação de dados que permite criar, testar e documentar pipelines analíticos de forma modular e versionada) para construir pipelines de dados para filmes e séries. Usando um dataset CSV e o DuckDB como data warehouse local, ele cobre desde a ingestão e transformação dos dados até análises mais detalhadas dos dados.

O projeto inclui um script para gerar dados sintéticos com a biblioteca Faker, permitindo ampliar o volume dos dados para testes, além de notebooks Jupyter para visualização e análise interativa dos resultados.

Principais pontos:

- Pipeline organizado com dbt (raw → staging → marts)

- Banco leve DuckDB, sem necessidade de servidor

- Geração de dados sintéticos para testes

- Testes automatizados e documentação

- Visualização de dados com notebooks Jupyter

## Estrutura do Projeto

- `data/`: Contém o dataset CSV de filmes de exemplo.
- `models/staging/`: Modelos de staging que selecionam e renomeiam colunas do dataset raw.
- `models/marts/`: Modelos analíticos que agregam e transformam os dados staged.
- `scripts/`: Scripts auxiliares, incluindo o gerador de dados sintéticos para o dataset de filmes.
- `notebooks/`: Notebooks Jupyter para análise e visualização dos dados gerados e transformados.


## Configuração

### Pré-requisitos

- Python 3.x
- pip
- dbt-core e dbt-duckdb
- Biblioteca `faker` para geração de dados sintéticos:
  ```bash
   pip install faker
   ```


### Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/fernandabucheri/dbtflix.git
   cd dbt_movies_project
   ```

2. Instale as dependências do dbt:
   ```bash
   pip install dbt-core dbt-duckdb
   ```

3. Configure seu perfil dbt:
   O dbt precisa de um arquivo  `profiles.yml` que fica, por padrão:

   - No Linux/macOS: `~/.dbt/profiles.yml`
   - No Windows: `C:\Users\SeuUsuario\.dbt\profiles.yml`

   Se a pasta `.dbt` não existir, crie manualmente.

   Exemplo de conteúdo para `profiles.yml` (ajuste o caminho conforme o seu projeto):

   ```yaml
   dbt_movies_project:
     target: dev
     outputs:
       dev:
         type: duckdb
         path: ":memory:"  # Para um banco de dados em memória (não persistente)
         # Ou, para um arquivo persistente (ex: no diretório do projeto):
         # path: "/caminho/para/seu/projeto/dbt_movies.duckdb"
         schema: dbt_movies
   ```
   O `schema` `dbt_movies` será criado pelo dbt. Para o `path`, você pode usar `:memory:` para um banco de dados temporário que é apagado após cada sessão, ou especificar um caminho de arquivo para um banco de dados persistente (recomendado para manter seus dados transformados).

   Importante: o nome `dbt_movies_project` deve ser igual ao campo `profile`: que está no seu `dbt_project.yml`.

4. Teste a configuração:

   ```bash
   dbt debug
   ```
   
   Se tudo estiver correto, você verá que todos os checks passaram e a conexão estará OK.

## Como Rodar

1. Carregue os dados de exemplo no seu banco de dados:
   ```bash
   dbt seed
   ```

2. Execute os modelos dbt:
   ```bash
   dbt run
   ```

3. Teste os modelos (opcional):
   ```bash
   dbt test
   ```

4. Gere a documentação do projeto (opcional):
   ```bash
   dbt docs generate
   dbt docs serve
   ```
   Isso iniciará um servidor web local ([http://localhost:8000](http://localhost:8000)) com a documentação do seu projeto dbt.
   
## Modelos

### Staging

- `stg_movies.sql`: Seleciona e renomeia as colunas do dataset `movies.csv`.

### Marts

- `agg_genre_ratings.sql`: Agrega os filmes por gênero e calcula a contagem total de filmes e a média de ratings por gênero.

## Gerador de Dados Sintéticos
   Para facilitar testes com um dataset maior e mais variado, o projeto inclui um script Python que gera dados sintéticos realistas para filmes usando a biblioteca faker.

   Local do script: `scripts/generate_movies_dataset.py`

   O script gera um arquivo CSV em `data/movies.csv` com milhares de registros.

   Isso permite simular um cenário mais próximo da produção e testar as transformações dbt com maior volume de dados.

   Exemplo básico de execução:

   ```bash
   python scripts/generate_movies_dataset.py
   ```
   Após rodar o script, basta voltar ao passo da seção [Como Rodar](#como-rodar)

## Análises
   Para análises exploratórias e visualização dos dados resultantes, utilize o notebook Jupyter:

   - Local do notebook: `notebooks/demo_dbt_duckdb.ipynb`
   - Nele, há gráficos e tabelas que mostram o funcionamento das transformações e os insights do dataset.
   