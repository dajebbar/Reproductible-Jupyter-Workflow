import os
import pandas as pd
from urllib.request import urlretrieve

FREMONT_URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"


def check_fremont_data(filename="Fremont.csv", url=FREMONT_URL, force_download=False):
    """Check Data: Download and cache fremont data

    Parameters
    ----------
    filename: string (optional)
        location to save data

    url: string(optional)
        web location of the data

    force_download: bool (optional):
        if True, force of redownload the data

    returns
    -------
    data: pandas.DataFrame
        the Frimont Bridge Data

    -----

    """

    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)

    data = pd.read_csv("Fremont.csv", index_col="Date", parse_dates=True)

    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%Y %H:%M:%S %p')
    except TypeError:
        data.index = pd.to_datetime(data.index)

    data.columns = ['Total', 'East', 'West']

    return data
