from config import TFS_BASE_URL
from headers_gen import headers_gen
import re  # noqa: F401
import requests
import pandas as pd
import numpy as np

def tfs_recruits(sport_key: int, year: int, min_date = None, page = 1, page_size = 250, headers = None):
    """tfs_recruits

    Args:
        sport_key (int): Sport Key (e.g. 1 for College Football and 2 for Men's College Basketball)
        year (int): Year
        page_size (int, optional): Page Size. Defaults to 500.
        headers (dict, optional): Headers. Defaults to `headers_gen()`.

    Returns:
        pd.DataFrame: Dataframe of transfer portal player rankings data.

    """
    params = {
        'sportKey': sport_key,
        'year': year,
        'minDate': min_date,
        'page': page,
        'pageSize': page_size
    }
    if headers is None:
        headers = headers_gen()

    url = TFS_BASE_URL + "recruits"
    response = requests.get(url, params=params, headers = headers)
    resp_json = response.json()
    resp = pd.json_normalize(resp_json['players'] )
    resp = resp.replace({np.nan: 0})

    return {
        'players': resp.to_dict(orient='records'),
        'pagination': resp_json['pagination']
    }
