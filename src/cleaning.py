import pandas as pd
import logging
from pathlib import Path

# --- Project paths ---
PROJECT_ROOT = Path(__file__).parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"

# File paths
CSV_FILES = {
    "ad_events": DATA_RAW / "ad_events.csv",
    "ads": DATA_RAW / "ads.csv",
    "campaigns": DATA_RAW / "campaigns.csv",
    "users": DATA_RAW / "users.csv",
}

# Function to import our CSVs


def import_csvs(filepaths):
    dataframes = {}
    for name, fp in filepaths.items():
        try:
            df = pd.read_csv(fp)
            dataframes[name] = df
            logging.info(f"Loaded {name} from {fp}")
        except Exception as e:
            logging.error(f"Failed to load {name} from {fp}: {e}")
            raise
    return dataframes


# Testing
# logging.basicConfig(level=logging.INFO)
dfs = import_csvs(CSV_FILES)

# Function to export cleaned CSVs into data/cleaned


def clean_ad_events(df):
    df = df.copy()

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df["user_id"] = df["user_id"].astype(str).str.strip()

    df["day_of_week"] = df["day_of_week"].astype("category")
    df["time_of_day"] = df["time_of_day"].astype("category")
    df["event_type"] = df["event_type"].astype("category")

    df = df.drop_duplicates()

    return df


def clean_ads(df):
    df = df.copy()

    # df["target_interests"] = df["target_interests"].str.split(",\s*") need to explode this to get one row per unique value / id. 
    # df["target_interests"] = df["target_interests"].astype("category") 


print(dfs["ads"].describe())


