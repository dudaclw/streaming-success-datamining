import logging
import time
import shutil
from pathlib import Path

from loader import load_datasets
from cleaner import clean_data
from analyzer import analyze_and_score
from generator import create_new_titles
from stats import genre_stats, rating_stats

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S"
)

REQUIRED_FILES = [
    Path("data/raw/netflix_titles.csv"),
    Path("data/raw/disney_plus_titles.csv"),
    Path("data/raw/amazon_prime_titles.csv"),
]


def check_required_files() -> bool:
    missing = [str(f) for f in REQUIRED_FILES if not f.exists()]

    if missing:
        logging.error("❌ Arquivos obrigatórios não encontrados em 'data/raw/':")
        for f in missing:
            logging.error(f"   - {f}")
        logging.error("Finalize o programa, coloque os CSVs na pasta correta e tente novamente.")
        return False

    logging.info("📂 Todos os arquivos obrigatórios foram encontrados em 'data/raw/'.")
    return True


def clean_previous_outputs():
    for folder in ["data/processed", "data/outputs"]:
        path = Path(folder)
        if path.exists():
            shutil.rmtree(path, ignore_errors=True)
        path.mkdir(parents=True, exist_ok=True)

    logging.info("🧹 Pastas 'data/processed/' e 'data/outputs/' foram limpas e recriadas.")


def main():
    start_time = time.time()

    try:
        logging.info("🚀 Iniciando pipeline de análise de streaming data mining...")

        if not check_required_files():
            return

        clean_previous_outputs()

        logging.info("Carregando datasets brutos...")
        datasets_raw = load_datasets()
        logging.info(f"Datasets carregados: {', '.join(datasets_raw.keys())}")

        logging.info("Limpando e padronizando colunas...")
        datasets_clean = clean_data(datasets_raw)
        logging.info("✅ Limpeza concluída. Arquivos salvos em 'data/processed/'.")

        logging.info("Gerando estatísticas de gêneros por plataforma...")
        genre_df = genre_stats(datasets_clean)
        logging.info(
            f"✅ Estatísticas de gêneros salvas em 'data/outputs/genre_stats.csv' "
            f"({len(genre_df)} linhas)."
        )

        logging.info("Gerando estatísticas de ratings por plataforma...")
        rating_df = rating_stats(datasets_clean)
        logging.info(
            f"✅ Estatísticas de ratings salvas em 'data/outputs/rating_stats.csv' "
            f"({len(rating_df)} linhas)."
        )

        logging.info("Calculando coluna de sucesso baseada na recência...")
        combined_scores = analyze_and_score(datasets_clean)
        logging.info(
            f"✅ Coluna 'sucesso' gerada com {len(combined_scores)} registros combinados "
            f"(arquivo em 'data/outputs/success_scores.csv')."
        )

        logging.info("Gerando novos filmes e séries para cada plataforma...")
        novos_titulos = create_new_titles()
        logging.info(
            f"🎬 {len(novos_titulos)} novos títulos criados e salvos em "
            f"'data/outputs/new_titles.csv'."
        )

        elapsed = time.time() - start_time
        logging.info(f"⏱️ Pipeline concluída com sucesso em {elapsed:.2f} segundos.")

    except Exception as e:
        logging.error(f"❌ Erro durante a execução: {e}", exc_info=True)


if __name__ == "__main__":
    main()
