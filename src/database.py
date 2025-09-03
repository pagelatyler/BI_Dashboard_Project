import pandas as pd
import logging
from pathlib import Path

# --- Project Paths ---

PROJECT_ROOT = Path(__file__).parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"

dict = {
    "ad_events": DATA_RAW / "ad_events.csv",
    "ads": DATA_RAW / "ads.csv",
    "campaigns": DATA_RAW / "campaigns.csv",
    "users": DATA_RAW / "users.csv"
}


def clean_csvs(filepath):
    dataframes = {}
    try:
        for name, fp in filepath.items():
            df = pd.read_csv(fp)
            dataframes[name] = df
            logging.info(f"Loaded {name} from {fp}")
    except Exception as e:
        logging.error(f"Failed to load {name} from {fp}: {e}")
        raise

    return dataframes


logging.basicConfig(level=logging.INFO)
dfs = clean_csvs(dict)
print(dfs.values())
