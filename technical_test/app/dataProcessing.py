import numpy as np
import pandas as pd

from sklearn.pipeline import Pipeline

from feature_engine.creation import CyclicalFeatures
from feature_engine.datetime import DatetimeFeatures
from feature_engine.imputation import DropMissingData
from feature_engine.selection import DropFeatures

from feature_engine.timeseries.forecasting import (
    LagFeatures,
    WindowFeatures,
)

def dataProcessing(data):
    # data['time'] = pd.to_datetime(data['time'])
    # data.index = data['time']
    # data = data.fillna(method='ffill').fillna(method='bfill')
    # data = data.resample('D').mean()
    cols_var = data.columns
    # Datetime features
    dtf = DatetimeFeatures(
        # the datetime variable
        variables="index",
        
        # the features we want to create
        features_to_extract=[
            "month",
            "week",
            "day_of_week",
            "day_of_month",
        ],
    )

    # Periodic features

    cyclicf = CyclicalFeatures(
        # The features we want to transform.
        variables=["month","week"],
        # Whether to drop the original features.
        drop_original=True,
    )

    # Drop missing data
    imputer = DropMissingData()
    # Drop original time series : preventing data leakage
    drop_ts = DropFeatures(features_to_drop=[i for i in cols_var])



    # Window features

    winf = WindowFeatures(
        variables=["WindSpeed","ReactivePower","ActivePower"],  # the input variables
        window=["1D", "3D", "7D", "15D","30D"],  # average of 3 previous days
        freq="1D",  # move 1 day forward
        missing_values="ignore",
    )

    # Lag features.

    lagf = LagFeatures(
        variables=["WindSpeed","ReactivePower","ActivePower"],  # the input variables
        freq=["1D", "3D", "7D", "15D","30D"],  # move 1 d and 3 d forward
        missing_values="ignore",
    )

    pipe = Pipeline(
    [
        ("datetime_features", dtf),
        ("lagf", lagf),
        ("winf", winf),
        ("Periodic", cyclicf),
        ("dropna", imputer),
        ("drop_ts", drop_ts),
    ]
    )

    return pipe.fit_transform(data)

