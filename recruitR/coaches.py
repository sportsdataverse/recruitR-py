from config import TFS_BASE_URL
from headers_gen import headers_gen
import re  # noqa: F401
import requests
import pandas as pd
import numpy as np

def tfs_coaches(sport_key: int, year: int, page = 1, page_size = 50, headers = None):
    """tfs_coaches

    Args:
        sport_key (int): Sport Key (e.g. 1 for College Football and 2 for Men's College Basketball)
        year (int): Year
        page (int, optional): Page. Defaults to 1.
        page_size (int, optional): Page Size. Defaults to 50.
        headers (dict, optional): Headers. Defaults to `headers_gen()`.
    Returns:
        dict: Dictionary of coaches and pagination information.
            {
                results: pd.DataFrame,
                pagination: dict
            }
            ## results:

                | Variable                  | Type    |
                |---------------------------|---------|
                | key                       | int64   |
                | cbsKey                    | int64   |
                | firstName                 | object  |
                | lastName                  | object  |
                | profileUrl                | object  |
                | defaultAssetUrl           | object  |
                | compositeRating           | float64 |
                | averageCompositeRating    | float64 |
                | overallRank               | int32   |
                | divisionRank              | int32   |
                | conferenceRank            | int32   |
                | currentJob.institutionKey | int32   |
                | currentJob.teamKey        | int32   |
                | currentJob.cbsKey         | int32   |
                | currentJob.name           | object  |
                | currentJob.abbreviation   | object  |
                | currentJob.fullName       | object  |
                | currentJob                | float64 |

            ## pagination:
                {
                    'currentPage': int32,
                    'itemsPerPage': int32,
                    'count': int32,
                    'pageCount': int32
                }

    """
    params = {
        'sportKey': sport_key,
        'year': year,
        'page': page,
        'pageSize': page_size
    }
    if headers is None:
        headers = headers_gen()

    url = TFS_BASE_URL + "coaches"
    response = requests.get(url, params=params, headers = headers)
    resp_json = response.json()
    resp = pd.json_normalize(resp_json['results'] )
    resp = resp.replace({np.nan: 0})
    resp[['overallRank','divisionRank','conferenceRank','currentJob.institutionKey','currentJob.teamKey','currentJob.cbsKey']] = resp[['overallRank','divisionRank','conferenceRank','currentJob.institutionKey','currentJob.teamKey','currentJob.cbsKey']].astype(int)

    return {
        'results': resp.to_dict(orient='records'),
        'pagination': resp_json['pagination']
    }
