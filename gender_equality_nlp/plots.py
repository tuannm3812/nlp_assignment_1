from pathlib import Path

from loguru import logger
import matplotlib.pyplot as plt
import pandas as pd
import typer

from gender_equality_nlp.config import FIGURES_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


def top_terms(features: pd.DataFrame, n_terms: int = 20) -> pd.Series:
    """Rank TF-IDF terms by their average document score."""
    terms = features.drop(columns=["document_id"], errors="ignore")
    return terms.mean(axis=0).sort_values(ascending=False).head(n_terms)


@app.command()
def main(
    input_path: Path = PROCESSED_DATA_DIR / "features.csv",
    output_path: Path = FIGURES_DIR / "top_terms.png",
    n_terms: int = 20,
):
    """Plot the most influential terms in the TF-IDF matrix."""
    logger.info(f"Reading features from {input_path}")
    features = pd.read_csv(input_path)
    ranked_terms = top_terms(features, n_terms)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    ranked_terms.sort_values().plot.barh(ax=ax, color="#2f6f73")
    ax.set_xlabel("Mean TF-IDF score")
    ax.set_ylabel("")
    ax.set_title("Top Terms Across Policy Submissions")
    fig.tight_layout()
    fig.savefig(output_path, dpi=200)
    plt.close(fig)
    logger.success(f"Wrote figure to {output_path}")


if __name__ == "__main__":
    app()
