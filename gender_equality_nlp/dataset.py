from pathlib import Path
import re

from loguru import logger
import pandas as pd
import typer

from gender_equality_nlp.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


def clean_text(text: str) -> str:
    """Normalize PDF/OCR text while preserving readable sentence boundaries."""
    text = re.sub(r"-\s*\n\s*", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def load_text_corpus(input_path: Path) -> pd.DataFrame:
    """Load submissions from a CSV file or a directory of plain-text files."""
    if input_path.is_file():
        data = pd.read_csv(input_path)
        if "text" not in data.columns:
            raise ValueError("Input CSV must include a 'text' column.")
        data["text"] = data["text"].fillna("").map(clean_text)
        return data

    if not input_path.is_dir():
        raise FileNotFoundError(f"Input path does not exist: {input_path}")

    records = []
    for file_path in sorted(input_path.glob("*.txt")):
        records.append(
            {
                "document_id": file_path.stem,
                "source_path": str(file_path),
                "text": clean_text(file_path.read_text(encoding="utf-8", errors="ignore")),
            }
        )

    if not records:
        raise ValueError(f"No .txt files found in {input_path}")

    return pd.DataFrame.from_records(records)


@app.command()
def main(
    input_path: Path = RAW_DATA_DIR / "submissions",
    output_path: Path = PROCESSED_DATA_DIR / "submissions.csv",
):
    """Create a clean submissions table from raw text files or a source CSV."""
    logger.info(f"Loading corpus from {input_path}")
    data = load_text_corpus(input_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(output_path, index=False)
    logger.success(f"Wrote {len(data)} documents to {output_path}")


if __name__ == "__main__":
    app()
