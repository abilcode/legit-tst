import pandas as pd
import numpy as np
from dataProcessing import dataProcessing



def forecast(date_start,model,X_test):
    data_start = pd.Timestamp(date_start)
    data_end = data_start + pd.offsets.Day(29)
    forecasting_points = pd.date_range(start=data_start, end=data_end, freq="1D")
    print(len(forecasting_points))
    #print(forecasting_points)
    # List to collect the RMSE for
    # each 24 hour forecast examined.

    rmse_ls = []

    # For every forecast start point:

    for forecast_point in forecasting_points:

        ###### Create forecasting horizon #####

        forecast_end = forecast_point + pd.offsets.Day(29)

        # The timestamps of the horizon
        index = pd.date_range(
            start=forecast_point,
            end=forecast_end,
            freq="1D",
        )

        # the forecasting horizon dataframe
        f_horizon = pd.DataFrame(columns=["ActivePower"], index=index)
            ##################################

        ###### the input data #############

        # 90 days before the first forecasting point
        start_point = forecast_point - pd.offsets.Day(90)

        # We create input data to obtain the first prediction value.
        input_data = X_test[(X_test.index >= start_point) &
                            (X_test.index < forecast_point)]
        input_data.loc[forecast_point] = np.nan
        ##################################

        # predictions
        pred = model.predict(dataProcessing(input_data))[0]
        # Add the prediction to the horizon
        # and to the input data
        print(forecast_point,pred)
        # Add the prediction to the horizon
        # and to the input data

        f_horizon.loc[forecast_point] = pred
        input_data.loc[forecast_point] = pred

        # repeat for additional points in horizon

        for i in range(30):

            # Re-slice the input data
            start_point = start_point + pd.offsets.Day(1)
            forecast_point = forecast_point + pd.offsets.Day(1)

            input_data = input_data[(input_data.index >= start_point)]
            input_data.loc[forecast_point] = np.nan

            # Obtain the prediction
            pred = model.predict(dataProcessing(input_data))[0]

            # Add prediction to horizon and input data
            f_horizon.loc[forecast_point] = pred
            input_data.loc[forecast_point] = pred

            # join predictions and grand truth
            tmp = pd.DataFrame(f_horizon["ActivePower"]).join(
                X_test["ActivePower"], lsuffix="_left", rsuffix="_right")
            tmp.columns = ["predicted", "actual"]
        #tmp.plot()
        #plt.ylabel("ActivePower concentration")
        #plt.show()
        # Determine the RMSE.
    return tmp

