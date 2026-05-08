from pathlib import Path

import pandas as pd
import pytest

from gender_equality_nlp.dataset import clean_text, load_text_corpus


def test_clean_text_repairs_hyphenated_line_breaks() -> None:
    text = "gender equal-\n ity   targets\n\nmatter"

    assert clean_text(text) == "gender equality targets matter"


def test_load_text_corpus_reads_directory(tmp_path: Path) -> None:
    (tmp_path / "submission-one.txt").write_text("Pay gap\nreporting", encoding="utf-8")

    data = load_text_corpus(tmp_path)

    assert data.to_dict("records") == [
        {
            "document_id": "submission-one",
            "source_path": str(tmp_path / "submission-one.txt"),
            "text": "Pay gap reporting",
        }
    ]


def test_load_text_corpus_requires_text_column(tmp_path: Path) -> None:
    csv_path = tmp_path / "submissions.csv"
    pd.DataFrame({"title": ["Submission 1"]}).to_csv(csv_path, index=False)

    with pytest.raises(ValueError, match="text"):
        load_text_corpus(csv_path)
