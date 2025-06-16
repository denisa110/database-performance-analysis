from pathlib import Path

# === Calea de bază: rădăcina proiectului ===
BASE_DIR = Path("D:/Disertatie/1.database_performance_analysis")

# === Structura de directoare ===
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
METADATA_DIR = DATA_DIR / "metadata"

RESULTS_DIR = BASE_DIR / "results"
TABLES_DIR = RESULTS_DIR / "tables"
PLOTS_DIR = RESULTS_DIR / "plots"

# === Fișiere CSV brute ===
RAW_FILES = {
    "no_index": RAW_DIR / "queries_no_index.csv",
    "with_index": RAW_DIR / "queries_with_index.csv",
    "no_shards": RAW_DIR / "queries_no_shards.csv",
    "with_shards": RAW_DIR / "queries_with_shards.csv"
}

# === Funcție: Creează directoarele dacă nu există ===
def ensure_directories():
    for path in [TABLES_DIR, PLOTS_DIR, PROCESSED_DIR, METADATA_DIR]:
        path.mkdir(parents=True, exist_ok=True)
    print("[OK] Directoare verificate/creat automat.")

# === Funcție: Validează existența fișierelor brute ===
def validate_raw_files():
    missing = [str(f) for f in RAW_FILES.values() if not f.exists()]
    if missing:
        print("[WARN] Lipsesc fișierele următoare:")
        for f in missing:
            print(f"  - {f}")
    else:
        print("[OK] Toate fișierele brute sunt prezente.")
