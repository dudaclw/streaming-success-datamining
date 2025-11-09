
# streaming-success-datamining

Projeto de Data Mining aplicado a catálogos de plataformas de streaming (Netflix, Disney+ e Amazon Prime Video).

O objetivo é:
- Analisar os dados de cada plataforma;
- Identificar campos relevantes para prever o “sucesso” de um título;
- Criar uma coluna `sucesso` (em %) baseada principalmente na recência (`release_year`);
- Propor **3 filmes** e **3 séries** (1 par por plataforma), com justificativas baseadas nos dados.

---

## 🧱 Estrutura do Projeto

```
streaming-success-datamining/
├── data/
│   ├── raw/          # CSVs originais (entrada)
│   │   ├── netflix_titles.csv
│   │   ├── disney_plus_titles.csv
│   │   └── amazon_prime_titles.csv
│   ├── processed/    # CSVs limpos e padronizados (gerados pelo código)
│   └── outputs/      # Resultados finais (gerados pelo código)
│       ├── genre_stats.csv       # Estatísticas de gêneros por plataforma
│       ├── rating_stats.csv      # Estatísticas de ratings por plataforma
│       ├── success_scores.csv    # Todos os títulos com coluna `sucesso`
│       └── new_titles.csv        # 3 filmes + 3 séries propostos
│
├── src/
│   ├── main.py       # Ponto de entrada da pipeline
│   ├── loader.py     # Leitura dos CSVs de data/raw/
│   ├── cleaner.py    # Limpeza e validação dos dados
│   ├── analyzer.py   # Cálculo da coluna `sucesso`
│   ├── stats.py      # Estatísticas de gêneros e ratings
│   ├── generator.py  # Criação dos novos títulos (3 filmes + 3 séries)
│   └── utils.py      # Funções auxiliares (leitura, salvamento, logs etc.)
│
├── reports/          # Relatórios finais 
│   └── ...
│
├── requirements.txt  # Dependências do projeto
└── README.md
```

---

## 📥 Como clonar o repositório

```bash
git clone https://github.com/dudaclw/streaming-success-datamining.git
cd streaming-success-datamining
```

---

## 🐍 Requisitos

- **Python 3.9+** (recomendado)
- Pip atualizado

Instale as dependências com:

```bash
pip install -r requirements.txt
```

Exemplo de conteúdo de `requirements.txt`:

```
pandas
```

(Caso tenha adicionado mais libs, inclua aqui.)

---

## 📂 Preparando os dados

Coloque os arquivos CSV originais na pasta `data/raw/` com estes nomes:

- `data/raw/netflix_titles.csv`
- `data/raw/disney_plus_titles.csv`
- `data/raw/amazon_prime_titles.csv`

> Os nomes dos arquivos são importantes: o código espera exatamente esses nomes.

---

## ▶️ Como rodar o projeto

Dentro da pasta raiz do repositório:

```bash
python src/main.py
```

O que o script faz:

1. Verifica se os CSVs obrigatórios existem em `data/raw/`;
2. Limpa e recria as pastas `data/processed/` e `data/outputs/`;
3. Carrega os dados brutos (Netflix, Disney+, Prime);
4. Limpa e padroniza os dados (colunas, nulos, etc.);
5. Gera estatísticas de:
   - gêneros (`genre_stats.csv`)
   - ratings (`rating_stats.csv`)
6. Calcula a coluna `sucesso` com base na recência (`success_scores.csv`);
7. Cria **3 filmes e 3 séries** propostos (`new_titles.csv`).

Durante a execução, mensagens de log são exibidas no terminal indicando o progresso da pipeline.

---

## 📊 Resultados gerados

Após rodar `python src/main.py`, você terá:

- `data/processed/`  
  - Arquivos *_clean.csv* com as versões limpas dos catálogos.

- `data/outputs/`
  - `genre_stats.csv` – gêneros mais frequentes por plataforma;
  - `rating_stats.csv` – ratings mais comuns por plataforma;
  - `success_scores.csv` – todos os títulos com a coluna `sucesso` (em %);
  - `new_titles.csv` – 3 filmes e 3 séries criados com:
    - `plataforma`
    - `tipo` (Filme ou Série)
    - `nome`
    - `genero`
    - `sinopse_curta`
    - `rating`
    - `sucesso` (% estimada de sucesso).

---

## 🧠 Lógica da coluna `sucesso`

A coluna `sucesso` é uma estimativa de probabilidade de sucesso baseada principalmente na **recência**:

```
sucesso = (release_year / ano_mais_recente) × 100
```

- Títulos mais novos (próximos ao ano mais recente da base) recebem valores mais altos.
- Essa coluna foi usada como base para escolher as porcentagens atribuídas aos novos filmes e séries propostos.

---

## 📌 Personalização

Você pode:

- Ajustar a lógica da função de sucesso em `src/analyzer.py` (ex.: incluir pesos por gênero ou rating);
- Editar ou estender as regras de criação dos novos títulos em `src/generator.py`;
- Adicionar gráficos ou relatórios adicionais a partir dos CSVs em `data/outputs/`.

---

Se tiver dúvidas ou quiser evoluir o projeto (ex.: adicionar regressão, clustering ou recomendação automática de títulos), sinta-se à vontade para abrir issues ou forks no repositório.
