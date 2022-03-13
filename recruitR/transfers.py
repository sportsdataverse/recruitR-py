from config import TFS_BASE_URL
from headers_gen import headers_gen
import re  # noqa: F401
import requests
import pandas as pd
import numpy as np

def tfs_transfers(sport_key: int, year: int, list_type: int,
                  position_group_key = None,
                  position_key = None,
                  eligibility = None,
                  institution_key = None,
                  status = None,
                  page = 1, page_size = 250, headers = None):
    """tfs_transfers

    Args:
        sport_key (int): Sport Key (e.g. 1 for College Football and 2 for Men's College Basketball)
        year (int): Year
        list_type (int): The type of list we are wanting to retrieve
            Defined Values:
                1 - Latest
                2 - Position
                3 - Overall
        eligibility (int): The eligibility to filter by
            Available values : 0, 1, 2, 3, 4
        position_group_key (int): The position group to filter by
        position_key (int): The position to filter by
        institution_key (int): The institution to filter by
        status (str): The status to filter by
        page_size (int, optional): Page Size. Defaults to 250.
        headers (dict, optional): Headers. Defaults to `headers_gen()`.

    Returns:
        pd.DataFrame: Dataframe of transfer portal player rankings data.

    """
    params = {
        'sportKey': sport_key,
        'year': year,
        'listType': list_type,
        'eligibility': eligibility,
        'positionGroupKey': position_group_key,
        'positionKey': position_key,
        'institutionKey': institution_key,
        'status': status,
        'page': page,
        'pageSize': page_size
    }
    if headers is None:
        headers = headers_gen()

    url = TFS_BASE_URL + "transfers"
    response = requests.get(url, params=params, headers = headers)
    resp_json = response.json()
    resp = pd.json_normalize(resp_json['players'] )
    resp = resp.replace({np.nan: 0})

    return {
        'players': resp.to_dict(orient='records'),
        'pagination': resp_json['pagination']
    }
print(tfs_transfers(sport_key=1, year=2019, list_type=1, page_size=250))