import pandas as pd

def test_no_missing_values():
    df = pd.read_csv("data/cleaned_data.csv")  # or output from notebook
    assert df.isnull().sum().sum() == 0

def test_expected_columns():
    df = pd.read_csv("data/cleaned_data.csv")
    expected_cols = ["feature1", "feature2", "target"]
    assert all(col in df.columns for col in expected_cols)
