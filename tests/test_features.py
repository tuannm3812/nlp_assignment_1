import pandas as pd

from gender_equality_nlp.features import build_tfidf_features


def test_build_tfidf_features_preserves_document_ids() -> None:
    data = pd.DataFrame(
        {
            "document_id": ["a", "b"],
            "text": ["gender equality targets", "pay gap reporting"],
        }
    )

    features = build_tfidf_features(data, max_features=5, ngram_max=1)

    assert features["document_id"].tolist() == ["a", "b"]
    assert features.shape[0] == 2
    assert features.shape[1] > 1
