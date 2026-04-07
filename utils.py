import json
import pandas as pd


def safe_json_parse(text: str):
    try:
        return json.loads(text)
    except:
        return {}


def reviews_to_dataframe(marketing, brand, compliance):
    return pd.DataFrame([
        {"Type": "Marketing", **marketing.dict()},
        {"Type": "Brand", **brand.dict()},
        {"Type": "Compliance", **compliance.dict()},
    ])
