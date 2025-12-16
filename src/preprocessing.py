import pandas as pd


def load_raw_data(transaction_path: str, identity_path: str) -> pd.DataFrame:
    """
    Load transaction and identity datasets and merge on TransactionID.
    """
    tx = pd.read_csv(transaction_path)
    identity = pd.read_csv(identity_path)

    df = tx.merge(identity, on="TransactionID", how="left")
    return df


def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic cleaning steps suitable for compliance analytics.
    """
    df = df.copy()

    # Ensure target is integer
    if "isFraud" in df.columns:
        df["isFraud"] = df["isFraud"].astype(int)

    # Drop identifier-style columns
    id_cols = [c for c in df.columns if c.lower().endswith("id")]
    df = df.drop(columns=id_cols, errors="ignore")

    return df