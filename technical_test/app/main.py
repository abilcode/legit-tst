from fastapi import FastAPI
import pandas as pd
import numpy as np

import pickle

from app import app as forecast

app = FastAPI()



@app.get("/")
async def welcome():
    return f"welcome, go to url/predict/ for the forecast"

@app.get("/predict/")
async def predict():
    tmp = forecast()
    return f"data : {tmp}"