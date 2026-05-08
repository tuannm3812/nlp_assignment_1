from pathlib import Path

import joblib
from loguru import logger
import pandas as pd
import typer

from gender_equality_nlp.config import MODELS_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    features_path: Path = PROCESSED_DATA_DIR / "features.csv",
    model_path: Path = MODELS_DIR / "kmeans_model.joblib",
    predictions_path: Path = PROCESSED_DATA_DIR / "predictions.csv",
):
    """Assign documents to clusters using a trained K-Means model."""
    logger.info(f"Loading model from {model_path}")
    model = joblib.load(model_path)
    features = pd.read_csv(features_path)
    document_ids = (
        features.pop("document_id") if "document_id" in features else pd.Series(features.index)
    )
    predictions = model.predict(features)

    predictions_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame({"document_id": document_ids, "cluster": predictions}).to_csv(
        predictions_path,
        index=False,
    )
    logger.success(f"Wrote predictions to {predictions_path}")


if __name__ == "__main__":
    app()
