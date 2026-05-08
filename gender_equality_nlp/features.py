from pathlib import Path

from loguru import logger
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import typer

from gender_equality_nlp.config import PROCESSED_DATA_DIR

app = typer.Typer()


def build_tfidf_features(
    data: pd.DataFrame,
    text_column: str = "text",
    max_features: int = 2_000,
    ngram_max: int = 2,
) -> pd.DataFrame:
    """Return a document-term matrix with stable document identifiers."""
    if text_column not in data.columns:
        raise ValueError(f"Missing text column: {text_column}")

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=max_features,
        ngram_range=(1, ngram_max),
        min_df=1,
    )
    matrix = vectorizer.fit_transform(data[text_column].fillna(""))
    features = pd.DataFrame.sparse.from_spmatrix(
        matrix,
        columns=vectorizer.get_feature_names_out(),
        index=data.get("document_id", data.index),
    )
    features.index.name = "document_id"
    return features.reset_index()


@app.command()
def main(
    input_path: Path = PROCESSED_DATA_DIR / "submissions.csv",
    output_path: Path = PROCESSED_DATA_DIR / "features.csv",
    text_column: str = "text",
    max_features: int = 2_000,
    ngram_max: int = 2,
):
    """Build TF-IDF features for downstream clustering or inspection."""
    logger.info(f"Reading processed corpus from {input_path}")
    data = pd.read_csv(input_path)
    features = build_tfidf_features(data, text_column, max_features, ngram_max)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    features.to_csv(output_path, index=False)
    logger.success(f"Wrote TF-IDF matrix with {features.shape[1] - 1} terms to {output_path}")


if __name__ == "__main__":
    app()
