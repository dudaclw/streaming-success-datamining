from pathlib import Path
import pandas as pd
from utils import safe_save_csv, combine_dataframes

OUTPUTS_PATH = Path("data/outputs")


def add_success_score(df: pd.DataFrame, plataforma: str) -> pd.DataFrame:
    df = df.copy()

    if "release_year" not in df.columns:
        raise ValueError(f"DataFrame de {plataforma} não tem coluna 'release_year'.")

    max_year = df["release_year"].max()
    df["sucesso"] = (df["release_year"] / max_year) * 100
    df["sucesso"] = df["sucesso"].round(2)
    df["plataforma"] = plataforma.capitalize()

    return df


def analyze_and_score(datasets_clean: dict) -> pd.DataFrame:
    OUTPUTS_PATH.mkdir(parents=True, exist_ok=True)

    scored_list = []
    for name, df in datasets_clean.items():
        df_scored = add_success_score(df, name)
        scored_list.append(df_scored)

    combined = combine_dataframes({name: df for name, df in datasets_clean.items()})
    combined["sucesso"] = pd.concat(scored_list, ignore_index=True)["sucesso"]

    safe_save_csv(combined, OUTPUTS_PATH / "success_scores.csv")
    return combined
