from pickle import NONE
from config import TFS_BASE_URL
from headers_gen import headers_gen
import re  # noqa: F401
import requests
import pandas as pd
import numpy as np

def tfs_composite_team_rankings(sport_key: int, year: int, page_size = 500, headers = None):
    """tfs_composite_team_rankings

    Args:
        sport_key (int): Sport Key (e.g. 1 for College Football and 2 for Men's College Basketball)
        year (int): Year
        page_size (int, optional): Page Size. Defaults to 500.
        headers (dict, optional): Headers. Defaults to `headers_gen()`.
    Returns:
        pd.DataFrame: Composite Team Rankings data

    """
    params = {
        'pageSize': page_size
    }
    if headers is None:
        headers = headers_gen()
    url = TFS_BASE_URL + "rankings/{}/{}/compositeTeamRankingFeed".format(sport_key, year)
    response = requests.get(url, params=params, headers = headers)
    resp_json = response.json()
    resp = pd.json_normalize(resp_json )
    resp = resp.replace({np.nan: 0})
    return resp

