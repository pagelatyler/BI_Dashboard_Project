import pandas as pd
import logging
import re
from pathlib import Path

ad_events_fp = Path(r"data/raw/ad_events.csv")
ads_fp = Path(r"data/raw/ads.csv")
campaigns_fp = Path(r"data/raw/campaigns.csv")
users_fp = Path(r"data/raw/users.csv")

read_ad_events = pd.read_csv(ad_events_fp)
read_ads_fp = pd.read_csv(ads_fp)
read_campaigns_fp = pd.read_csv(campaigns_fp)
read_users_fp = pd.read_csv(users_fp)

# print(read_ad_events.head())
# print(read_ads_fp.head())
# print(read_campaigns_fp.head())
# print(read_users_fp.head())
 
print('The current working directory is ' + str((Path.cwd())))
# Function to import our CSVs

# One function for each CSV to clean it

# Function to export cleaned CSVs into data/cleaned

# Use logging to track the cleaning process


# def import_csv(file_path):
