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
    df = df.drop_duplicates()

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df["user_id"] = df["user_id"].astype(str).str.strip()

    df["day_of_week"] = df["day_of_week"].astype("category")
    df["time_of_day"] = df["time_of_day"].astype("category")
    df["event_type"] = df["event_type"].astype("category")

    

    return df


def clean_ads(df):
    df = df.copy()
    df = df.drop_duplicates()

    df["target_interests"] = df["target_interests"].str.split(",\s*").explode()
    df["target_interests"] = df["target_interests"].str.strip()

    df["target_interests"] = df["target_interests"].astype("string").str.strip() 
    df["ad_platform"] = df["ad_platform"].astype("string").str.strip()
    df["ad_type"] = df["ad_type"].astype("string").str.strip()
    df["target_gender"] = df["target_gender"].astype("string").str.strip()

    return df


def clean_campaigns(df):
    df = df.copy()
    df = df.drop_duplicates()

    df["name"] = df["name"].astype("string").str.strip()
    df["start_date"] = pd.to_datetime(df["start_date"]).dt.date
    df["end_date"] = pd.to_datetime(df["end_date"]).dt.date

    return df


def clean_users(df):
    df = df.copy()
    df = df.drop_duplicates()

    #convert user_gender, country, location, user_id to str
    df["user_id"] = df["user_id"].astype("string").str.strip()
    df["country"] = df["country"].astype("string").str.strip()
    df["user_gender"] = df["user_gender"].astype("string").str.strip()
    df["location"] = df["location"].astype("string").str.strip()

    #convert interests to str and explode
    df["interests"] = df["interests"].str.split(",\s*").explode()
    df["interests"] = df["interests"].str.strip()

    
    return df



# after this last function I dont think we'll need more for this file? Will look to export, but can maybe do that in a different file
testing = dfs["users"]
print(testing.describe)
print(testing.head(10))
