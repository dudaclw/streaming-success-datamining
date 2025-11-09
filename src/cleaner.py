from pathlib import Path
from utils import safe_save_csv, validate_columns, ensure_folder

PROCESSED_PATH = Path("data/processed")


def basic_clean(df):
    df = df.copy()
    df.columns = df.columns.str.lower().str.strip()
    if "release_year" in df.columns:
        df = df.dropna(subset=["release_year"])
    return df


def clean_data(datasets: dict):
    ensure_folder(PROCESSED_PATH)
    cleaned = {}

    for name, df in datasets.items():
        if df is None:
            continue  # pula datasets que não foram carregados

        df_clean = basic_clean(df)

        validate_columns(df_clean, ["title", "release_year"], name=name)

        safe_save_csv(df_clean, PROCESSED_PATH / f"{name}_clean.csv")

        cleaned[name] = df_clean

    return cleaned
