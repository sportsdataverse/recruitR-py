from config import TFS_BASE_URL
from headers_gen import headers_gen
import re  # noqa: F401
import requests
import pandas as pd
import numpy as np

def tfs_positions(year: int, ranking_key = None, sport_key = None, headers = None):
    """tfs_positions

    Args:
        ranking_key (int): The Key of the Ranking to lookup
        sport_key (int): Sport Key (e.g. 1 for College Football and 2 for Men's College Basketball)
        year (int): Year
        headers (dict, optional): Headers. Defaults to `headers_gen()`.
    Returns:
        pd.DataFrame: Dataframe of positions.

    """
    params = {
        'rankingKey;': ranking_key,
        'sportKey': sport_key,
        'year': year
    }
    if headers is None:
        headers = headers_gen()

    url = TFS_BASE_URL + "positions"
    response = requests.get(url, params=params, headers = headers)
    resp_json = response.json()
    resp = pd.json_normalize(resp_json)
    resp = resp.replace({np.nan: 0})
    return resp
