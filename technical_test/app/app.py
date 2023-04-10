
import pandas as pd
import pickle
from dataProcessing import dataProcessing
from forecast import forecast



def app():
    ### importing 
    pickle_in = open("/Users/abilfad/Desktop/legit/technical_test/code/iter2/xgb_forecast.pkl",'rb')
    xgb = pickle.load(pickle_in)
    data = pd.read_csv('/Users/abilfad/Desktop/legit/technical_test/data/Turbine_Data.csv')
    data['time'] = pd.to_datetime(data['time'])
    data.index = data['time']
    data = data.fillna(method='ffill').fillna(method='bfill')
    data = data.resample('D').mean()
    data.index = pd.to_datetime(data.index.date)
    print(data.shape)




    # slicing
    # train
    X_train = data[data.index < "2020-01-01"]
    X_test = data[data.index >= pd.Timestamp("2020-01-01") - pd.offsets.Day(30)]

    # target
    y_train = data[data.index < "2020-01-01"][["ActivePower"]]
    y_test = data[data.index >= pd.Timestamp("2020-01-01") - pd.offsets.Day(30)][[
        "ActivePower",
    ]]
    X_train_t = dataProcessing(X_train)
    y_train_t = y_train.loc[X_train_t.index]

    tmp = forecast("2020-03-01",xgb,X_test)
    print(f"Predicted : {tmp.predicted} Actual Data : {tmp.actual}")

    return tmp.predicted
    



