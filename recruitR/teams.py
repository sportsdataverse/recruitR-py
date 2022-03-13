from config import TFS_BASE_URL
from headers_gen import headers_gen
import re  # noqa: F401
import requests
import pandas as pd
import numpy as np

def tfs_teams(sport_key: int, year: int,institution_type=None, headers = None):
    """tfs_teams

    Args:
        sport_key (int): Sport Key (e.g. 1 for College Football and 2 for Men's College Basketball)
        year (int): Year
        headers (dict, optional): Headers. Defaults to `headers_gen()`.
    Returns:
        pd.DataFrame: Dataframe of transfer portal team rankings.

    """
    params = {
        'sportKey': sport_key,
        'year': year,
        'institutionType': institution_type
    }
    if headers is None:
        headers = headers_gen()

    url = TFS_BASE_URL + "teams"
    response = requests.get(url, params=params, headers = headers)
    resp_json = response.json()
    resp = pd.json_normalize(resp_json)
    resp = resp.replace({np.nan: 0})
    return resp

