import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with missing arrival delay."""
    df_clean = df.dropna(subset=["ARR_DELAY"])
    print(f"Dataset shape after cleaning: {df_clean.shape}")
    return df_clean