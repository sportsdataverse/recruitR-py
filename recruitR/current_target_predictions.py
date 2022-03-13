from config import TFS_BASE_URL
from headers_gen import headers_gen
import re  # noqa: F401
import requests
import pandas as pd
import numpy as np

def tfs_current_target_predictions(site_key: int, sport_key: int, year: int,
                             page = 1, page_size = 500, headers = None):
    """tfs_current_target_predictions

    Args:
        site_key (int): Site key
        sport_key (int): Sport Key (e.g. 1 for College Football and 2 for Men's College Basketball)
        year (int): Year
        page (int, optional): Page. Defaults to 1.
        page_size (int, optional): Page Size. Defaults to 50.
        headers (dict, optional): Headers. Defaults to `headers_gen()`.
    Returns:
        pd.DataFrame: Dataframe of institution rankings.

    """
    params = {
        'page': page,
        'pagesize': page_size
    }
    if headers is None:
        headers = headers_gen()
    url = TFS_BASE_URL + "sites/{}/years/{}/sports/{}/currentTargetPredictions".format(site_key, year, sport_key)
    response = requests.get(url, params=params, headers = headers)
    resp_json = response.json()
    resp = pd.json_normalize(resp_json)
    resp = resp.replace({np.nan: 0})
    return resp

