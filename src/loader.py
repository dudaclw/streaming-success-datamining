from utils import safe_read_csv

def load_datasets():
    datasets = {
        "netflix": safe_read_csv("data/raw/netflix_titles.csv"),
        "disney": safe_read_csv("data/raw/disney_plus_titles.csv"),
        "prime": safe_read_csv("data/raw/amazon_prime_titles.csv")
    }
    return datasets
