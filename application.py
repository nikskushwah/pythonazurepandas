from flask import Flask, request
import pandas as pd
import numpy as np
#from PlanBFlask import planb
#from PlanBFlask.application import application
app = Flask(__name__)

@app.route('/')
def home():
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
#    dates = pd.date_range('20130101', periods=6)
    return "hello"
