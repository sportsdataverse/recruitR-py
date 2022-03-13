from config import TFS_BASE_URL
from headers_gen import headers_gen
import re  # noqa: F401
import requests
import pandas as pd
import numpy as np

def tfs_team_schedule(team_key: int, year: int, page=1, page_size = 100, headers = None):
    """tfs_team_schedule

    Args:
        team_key (int): Team Key (see `tfs_teams()`)
        year (int): Year
        page (int, optional): Page. Defaults to 1.
        page_size (int, optional): Page Size. Defaults to 500.
        headers (dict, optional): Headers. Defaults to `headers_gen()`.
    Returns:
        dict: Dictionary of team schedule and pagination information.
            {
                schedule: pd.DataFrame,
                pagination: dict
            }

    """
    params = {
        'page': page,
        'pageSize': page_size
    }
    if headers is None:
        headers = headers_gen()

    url = TFS_BASE_URL + "teams/{}/{}/schedule".format(team_key, year)
    response = requests.get(url, params=params, headers = headers)
    resp_json = response.json()
    resp = pd.json_normalize(resp_json['list'])
    resp = resp.replace({np.nan: 0})
    return {
        'schedule': resp.to_dict(orient='records'),
        'pagination': resp_json['pagination']
    }
