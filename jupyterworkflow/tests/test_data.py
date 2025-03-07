from jupyterworkflow.data import check_fremont_data
import pandas as pd
import numpy as np


def test_fremont_data():
    data = check_fremont_data()
    assert all(data.columns == ['Total', 'East', 'West'])
    assert isinstance(data.index, pd.DatetimeIndex)
    assert len(np.unique(data.index.time) == 24)
