from config import TFS_BASE_URL
from headers_gen import headers_gen
import re  # noqa: F401
import requests
import pandas as pd
import numpy as np

def tfs_conferences(page_size: int, query=None, headers = None):
    """tfs_conferences

    Args:
        query (str): Query string
        page_size (int, optional): Page Size. Defaults to 500.
        headers (dict, optional): Headers. Defaults to `headers_gen()`.
    Returns:
        pd.DataFrame: Dataframe of transfer portal team rankings.

    """
    params = {
        'q;': query,
        'pageSize': page_size
    }
    if headers is None:
        headers = headers_gen()

    url = TFS_BASE_URL + "conferences"
    response = requests.get(url, params=params, headers = headers)
    resp_json = response.json()
    resp = pd.json_normalize(resp_json)
    resp = resp.replace({np.nan: 0})
    return resp

