from config import TFS_BASE_URL
from headers_gen import headers_gen
import re  # noqa: F401
import requests
import pandas as pd
import numpy as np

def tfs_institution_rankings(sport_key: int, year: int, institution_key = None, institutions = None,
                             conference_abbreviation = None, use_composite = True, ranking_type = 2,
                             page = 1, page_size = 300, headers = None):
    """tfs_institution_groups

    Args:
        sport_key (int): Sport Key (e.g. 1 for College Football and 2 for Men's College Basketball)
        year (int): Year
        institution_key (int, optional): Institution key associated with the institution rankings request
        institutions (str, optional): Comma separated list of institutions to return
        conference_abbreviation (str, optional): Conference to filter by
        use_composite (bool, optional): Use composite ranking. Defaults to False
        ranking_type (int, optional): Type of Ranking being requested. Defaults to 2 (Team)
            1 - Player
            2 - Team
            3 - Coach
            5 - EnrolledTeam
            6 - TeamTalent
            7 - Transfer
            8 - TransferTeam
            9 - CombinedTeam
        page (int, optional): Page. Defaults to 1.
        page_size (int, optional): Page Size. Defaults to 50.
        headers (dict, optional): Headers. Defaults to `headers_gen()`.
    Returns:
        dict: Dictionary of institution rankings and pagination information.
            {
                results: pd.DataFrame,
                pagination: dict
            }

    """
    params = {
        'institutionKey': institution_key,
        'institutions': institutions,
        'conferenceAbbreviation': conference_abbreviation,
        'useComposite': use_composite,
        'rankingType' : ranking_type,
        'page': page,
        'pagesize': page_size,
    }
    if headers is None:
        headers = headers_gen()
    url = TFS_BASE_URL + "rankings/{}/{}/institutionrankings".format(sport_key,year)
    response = requests.get(url, params = params, headers = headers)
    resp_json = response.json()
    resp = pd.json_normalize(resp_json['list'] )
    resp = resp.replace({np.nan: 0})

    return {
        'results': resp.to_dict(orient='records'),
        'pagination': resp_json['pagination']
    }

print(tfs_institution_rankings(sport_key=1, year=2022, page = 1, page_size = 100))