import re
import csv
from pathlib import Path

def clean_query_csv(input_file: str, output_file: str):
    input_path = Path(input_file)  # FĂRĂ VIRGULĂ
    output_path = Path(output_file)

    # Verifică dacă fișierul de input există
    if not input_path.exists():
        print(f"[ERROR] Fișierul de input nu există: {input_path}")
        return

    # Creează directorul de output dacă nu există
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with input_path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines:
        print("[ERROR] Fișierul de input este gol")
        return

    header = lines[0].strip().split(",")
    clean_rows = [header]

    pattern = re.compile(
        r'^(?P<query_id>\d+),["]?(?P<query_text>.+?)["]?,' +
        r'(?P<execution_time_ms>\d+),(?P<status>\w+),' +
        r'(?P<documents_returned>\d+),(?P<timestamp>[^,]+)$'
    )

    processed_lines = 0
    ignored_lines = 0

    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        processed_lines += 1
        line = line.replace('"""""""', '"').replace('""""""', '"').replace('"""""', '"')
        line = line.replace('""""', '"').replace('"""', '"').replace('""', '"')

        match = pattern.match(line)
        if match:
            clean_rows.append([
                match.group("query_id"),
                match.group("query_text"),
                match.group("execution_time_ms"),
                match.group("status"),
                match.group("documents_returned"),
                match.group("timestamp")
            ])
        else:
            ignored_lines += 1
            if ignored_lines <= 3:
                print(f"[WARN] Linie ignorată {processed_lines}: {line[:80]}...")

    with output_path.open("w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(clean_rows)

    print(f"[OK] Procesat {processed_lines} linii")
    print(f"[OK] Curățat cu succes {len(clean_rows)-1} rânduri")
    print(f"[WARN] Ignorat {ignored_lines} linii malformate")
    print(f"[OK] Fișierul curățat a fost salvat: {output_path.resolve()}")

# Executare
if __name__ == "__main__":
    clean_query_csv(
        input_file=r"D:\Disertatie\1.database_performance_analysis\data\raw\queries_with_shards.csv",
        output_file=r"D:\Disertatie\1.database_performance_analysis\data\raw\queries_with_shards_clean.csv"
    )
