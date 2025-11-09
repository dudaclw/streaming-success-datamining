import logging
from pathlib import Path
import pandas as pd

# ==========================
# Funções utilitárias gerais
# ==========================

def ensure_folder(path: str):
    folder = Path(path)
    folder.mkdir(parents=True, exist_ok=True)
    logging.debug(f"📁 Pasta verificada/criada: {path}")


def summarize_df(df: pd.DataFrame, name: str = "DataFrame", lines: int = 5):
    logging.info(f"Resumo de {name}: {len(df)} linhas e {len(df.columns)} colunas")
    logging.debug(f"Primeiras {lines} linhas de {name}:\n{df.head(lines)}")


def safe_read_csv(filepath: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(filepath)
        logging.info(f"✅ Arquivo lido com sucesso: {filepath}")
        return df
    except FileNotFoundError:
        logging.error(f"❌ Arquivo não encontrado: {filepath}")
        return None
    except Exception as e:
        logging.error(f"⚠️ Erro ao ler o CSV {filepath}: {e}", exc_info=True)
        return None


def safe_save_csv(df: pd.DataFrame, filepath: str):
    try:
        ensure_folder(Path(filepath).parent)
        df.to_csv(filepath, index=False)
        logging.info(f"💾 Arquivo salvo com sucesso: {filepath}")
    except Exception as e:
        logging.error(f"⚠️ Erro ao salvar {filepath}: {e}", exc_info=True)


def validate_columns(df: pd.DataFrame, required_columns: list, name: str = "DataFrame") -> bool:
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        logging.warning(f"⚠️ {name} está faltando as colunas: {missing}")
        return False
    logging.debug(f"✅ {name} contém todas as colunas obrigatórias.")
    return True


def combine_dataframes(dfs: dict) -> pd.DataFrame:
    combined_list = []
    for name, df in dfs.items():
        df = df.copy()
        df["plataforma"] = name.capitalize()
        combined_list.append(df)
        logging.debug(f"📦 Adicionando {len(df)} linhas de {name} ao DataFrame.")

    combined = pd.concat(combined_list, ignore_index=True)
    logging.info(f"DataFrames combinados: {len(combined)} linhas no total.")
    return combined
