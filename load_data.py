"""Load and clean the Chicago Strategic Subject List (historical) dataset.

Usage:
    from load_data import load_ssl
    df = load_ssl()
"""
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent
RAW_CSV = DATA_DIR / "Strategic_Subject_List_-_Historical_20261104.csv"

AGE_ORDER = ["less than 20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80"]

RACE_LABELS = {
    "BLK": "Black",
    "WWH": "White Hispanic",
    "WHI": "White",
    "API": "Asian/Pacific Islander",
    "WBH": "Black Hispanic",
    "I": "American Indian/Alaska Native",
    "U": "Unknown",
}

SEX_LABELS = {"M": "Male", "F": "Female", "X": "Unknown"}

# Exact copies of other columns (SSL SCORE / RAW SSL SCORE) or constant values
REDUNDANT_COLS = ["HEAT SCORE", "RAW_HEAT_SCORE", "PRE RAW HEAT SCORE", "STATUS I"]

FLAG_COLS = ["WEAPON I", "DRUG I", "CPD ARREST I", "PAROLEE I"]


def _snake(name: str) -> str:
    return name.strip().lower().replace(" ", "_")


def load_ssl(path: Path = RAW_CSV, drop_duplicates: bool = False) -> pd.DataFrame:
    df = pd.read_csv(path, low_memory=False)
    df = df.drop(columns=REDUNDANT_COLS)

    # Y/N indicators -> bool (PAROLEE I is only ever "Y" or blank)
    for col in FLAG_COLS:
        df[col] = df[col].eq("Y")

    df["COMMUNITY AREA"] = df["COMMUNITY AREA"].str.strip().replace("", pd.NA)

    age_type = pd.CategoricalDtype(AGE_ORDER, ordered=True)
    for col in ["AGE CURR", "AGE GROUP", "AGE TO", "PREDICTOR RAT AGE AT LATEST ARREST"]:
        df[col] = df[col].astype(age_type)

    df["RACE"] = df["RACE CODE CD"].map(RACE_LABELS).astype("category")
    df["SEX"] = df["SEX CODE CD"].map(SEX_LABELS).astype("category")

    # Rows have no person ID, so identical rows may be different people; keep by default
    if drop_duplicates:
        df = df.drop_duplicates()

    df.columns = [_snake(c) for c in df.columns]
    return df.reset_index(drop=True)


if __name__ == "__main__":
    df = load_ssl()
    print(df.shape)
    df.info()
