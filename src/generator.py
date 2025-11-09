from pathlib import Path
import pandas as pd

OUTPUTS_PATH = Path("data/outputs")

def create_new_titles():
    novos_titulos = pd.DataFrame({
        "plataforma": [
            "Netflix", "Netflix",
            "Disney+", "Disney+",
            "Prime Video", "Prime Video"
        ],
        "tipo": ["Filme", "Série", "Filme", "Série", "Filme", "Série"],
        "nome": [
            "NOME FILME NETFLIX",
            "NOME SÉRIE NETFLIX",
            "NOME FILME DISNEY",
            "NOME SÉRIE DISNEY",
            "NOME FILME PRIME",
            "NOME SÉRIE PRIME"
        ],
        "genero": [
            "Drama", "Crime, Drama",
            "Animação, Família",
            "Aventura, Fantasia",
            "Ação, Suspense",
            "Ficção científica, Distopia"
        ],
        "sinopse_curta": [
            "Sinopse curta do filme da Netflix...",
            "Sinopse curta da série da Netflix...",
            "Sinopse curta do filme da Disney...",
            "Sinopse curta da série da Disney...",
            "Sinopse curta do filme do Prime...",
            "Sinopse curta da série do Prime..."
        ],
        "rating": [
            "TV-MA",
            "TV-14",
            "PG",
            "TV-PG",
            "R",
            "TV-14"
        ],
        "sucesso": [
            92.5,
            90.0,
            88.0,
            89.5,
            87.0,
            91.0
        ]
    })

    OUTPUTS_PATH.mkdir(parents=True, exist_ok=True)
    novos_titulos.to_csv(OUTPUTS_PATH / "new_titles.csv", index=False)

    return novos_titulos
