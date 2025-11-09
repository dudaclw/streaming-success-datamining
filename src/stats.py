from pathlib import Path
import pandas as pd

OUTPUTS_PATH = Path("data/outputs")

def _explode_genres(df: pd.DataFrame) -> pd.Series:
    s = df["listed_in"].dropna().str.split(",")
    genres = []
    for lst in s:
        genres.extend([g.strip() for g in lst])
    return pd.Series(genres)


def genre_stats(datasets_clean: dict, top_n: int = 10) -> pd.DataFrame:
    rows = []

    for name, df in datasets_clean.items():
        genres = _explode_genres(df)
        counts = genres.value_counts().head(top_n)

        for genre, count in counts.items():
            rows.append({
                "plataforma": name.capitalize(),
                "genero": genre,
                "quantidade": count
            })

    stats_df = pd.DataFrame(rows)
    OUTPUTS_PATH.mkdir(parents=True, exist_ok=True)
    stats_df.to_csv(OUTPUTS_PATH / "genre_stats.csv", index=False)
    return stats_df


def rating_stats(datasets_clean: dict, top_n: int = 10) -> pd.DataFrame:
    rows = []

    for name, df in datasets_clean.items():
        counts = df["rating"].value_counts().head(top_n)

        for rating, count in counts.items():
            rows.append({
                "plataforma": name.capitalize(),
                "rating": str(rating),
                "quantidade": count
            })

    stats_df = pd.DataFrame(rows)
    OUTPUTS_PATH.mkdir(parents=True, exist_ok=True)
    stats_df.to_csv(OUTPUTS_PATH / "rating_stats.csv", index=False)
    return stats_df
