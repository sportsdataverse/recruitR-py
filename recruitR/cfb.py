import pyarrow.parquet as pq
import pandas as pd
import urllib3
import certifi
import json
import time
from typing import List, Callable, Iterator, Union, Optional
from recruitR.library.http import APIHTTP
from recruitR.config import *
from recruitR.errors import SeasonNotFoundError
from recruitR.dl_utils import download

file_name = 'recruits.json'
CURRENT_SEASON = 2022
# Initialize Functions
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())

def get_cfb_recruit_rankings(season: int = None,  pages: int = None) -> pd.DataFrame:
    """
    Get recruiting rankings from a given college football recruiting class.
    """
    MIN_SEASON = 2002
    if season is None:
        season = CURRENT_SEASON
    if season < MIN_SEASON:
        raise SeasonNotFoundError(season)
    if pages is None:
        pages = 30
    if type(pages) is int:
        pages = [pages]
    recruits_df = pd.DataFrame()
    for page in pages:
        url = RANKINGS_URL.format(year=season,items=100, page= page+1)
        df = json.loads(download(url))
        data = pd.json_normalize(df)
        recruits_df = pd.concat([recruits_df,data],axis=0)
    return recruits_df

def get_cfb_recruitment(recruitment: int) -> pd.DataFrame:
    """
    Get summary information on a college football recruitment.
    """

    if type(recruitment) is int:
        recruitment = [recruitment]
    recruits_df = pd.DataFrame()

    for recruit in recruitment:
        url = RECRUITMENT_URL.format(recruitment=recruit)
        df = json.loads(download(url))
        data = pd.json_normalize(df)
        recruits_df = pd.concat([recruits_df,data],axis=0)
    return recruits_df

def get_cfb_recruitment_interests(recruitment: int) -> pd.DataFrame:
    """
    Get recruit interests for a college football recruitment.
    """

    if type(recruitment) is int:
        recruitment = [recruitment]
    recruits_df = pd.DataFrame()

    for recruit in recruitment:
        url = RECRUITMENT_INTERESTS_URL.format(recruitment=recruit)
        df = json.loads(download(url))
        data = pd.json_normalize(df)
        recruits_df = pd.concat([recruits_df,data],axis=0)
    return recruits_df

def get_cfb_recruitment_events(recruitment: int) -> pd.DataFrame:
    """
    Get recruit interest events from a college football recruitment.
    """

    if type(recruitment) is int:
        recruitment = [recruitment]
    recruits_df = pd.DataFrame()

    for recruit in recruitment:
        url = RECRUITMENT_INTEREST_EVENTS_URL.format(recruitment=recruit)
        df = json.loads(download(url))
        data = pd.json_normalize(df)
        recruits_df = pd.concat([recruits_df,data],axis=0)
    return recruits_df

def get_cfb_recruitment_events_detailed(recruitment: int) -> pd.DataFrame:
    """
    Get recruit interest events (detailed) from a college football recruitment.
    """

    if type(recruitment) is int:
        recruitment = [recruitment]
    recruits_df = pd.DataFrame()

    for recruit in recruitment:
        url = RECRUITMENT_INTEREST_DEPTH_DETAIL_URL.format(recruitment=recruit)
        df = json.loads(download(url))
        data = pd.json_normalize(df)
        recruits_df = pd.concat([recruits_df,data],axis=0)
    return recruits_df

def get_cfb_recruitment_offers(recruitment: int) -> pd.DataFrame:
    """
    Get recruit offers for a college football recruitment.
    """

    if type(recruitment) is int:
        recruitment = [recruitment]
    recruits_df = pd.DataFrame()

    for recruit in recruitment:
        url = RECRUITMENT_OFFERS_URL.format(recruitment=recruit)
        df = json.loads(download(url))
        data = pd.json_normalize(df)
        recruits_df = pd.concat([recruits_df,data],axis=0)
    return recruits_df

def get_cfb_committed_recruitment_interests(recruitment: int) -> pd.DataFrame:
    """
    Get all recruits from a given season.
    """

    if type(recruitment) is int:
        recruitment = [recruitment]
    recruits_df = pd.DataFrame()

    for recruit in recruitment:
        url = RECRUITMENT_COMMITTED_RECRUIT_INTEREST_URL.format(recruitment=recruit)
        df = json.loads(download(url))
        data = pd.json_normalize(df)
        recruits_df = pd.concat([recruits_df,data],axis=0)
    return recruits_df

def get_cfb_institution(institution: int) -> pd.DataFrame:
    """
    Get institution information.
    """

    if type(institution) is int:
        institution = [institution]
    institution_df = pd.DataFrame()

    for institution in institution:
        url = INSTITUTION_URL.format(institution=institution)
        df = json.loads(download(url))
        data = pd.json_normalize(df)
        institution_df = pd.concat([institution_df,data],axis=0)
    return institution_df

def get_cfb_institution_location(institution: int) -> pd.DataFrame:
    """
    Get institution location
    """

    if type(institution) is int:
        institution = [institution]
    institution_df = pd.DataFrame()

    for institution in institution:
        url = INSTITUTION_LOCATION_URL.format(institution=institution)
        df = json.loads(download(url))
        data = pd.json_normalize(df)
        institution_df = pd.concat([institution_df,data],axis=0)
    return institution_df



