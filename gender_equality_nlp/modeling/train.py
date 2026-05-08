from pathlib import Path

import joblib
from loguru import logger
import pandas as pd
from sklearn.cluster import KMeans
import typer

from gender_equality_nlp.config import MODELS_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    features_path: Path = PROCESSED_DATA_DIR / "features.csv",
    model_path: Path = MODELS_DIR / "kmeans_model.joblib",
    labels_path: Path = PROCESSED_DATA_DIR / "cluster_labels.csv",
    n_clusters: int = 5,
    random_state: int = 42,
):
    """Train a K-Means clustering model on TF-IDF features."""
    logger.info(f"Reading features from {features_path}")
    features = pd.read_csv(features_path)
    document_ids = (
        features.pop("document_id") if "document_id" in features else pd.Series(features.index)
    )

    model = KMeans(n_clusters=n_clusters, random_state=random_state, n_init="auto")
    labels = model.fit_predict(features)

    model_path.parent.mkdir(parents=True, exist_ok=True)
    labels_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    pd.DataFrame({"document_id": document_ids, "cluster": labels}).to_csv(labels_path, index=False)
    logger.success(f"Saved model to {model_path} and labels to {labels_path}")


if __name__ == "__main__":
    app()
