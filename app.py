import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import load_model
from flask import Flask, render_template, request, send_file
import datetime as dt
import yfinance as yf
import sklearn.preprocessing import MinMaxScaler
import os
plt.style.use('fivethirtyeight')

app = Flask(__name__)

# Load the model (make sure your model is in the correct path)
model = load_model('stock_dl_model.h5')

@app.route('/', methods=['GET', 'POST'])
def index ():
    if request.method == 'POST':
        stock = request.form.get('stock')
        if not stock:
            stock = 'POWERGRID.NS' # Default stock if none is entered
        
        # Define the start and end dates for stock data
        start = dt.datetime(2000, 1, 1)
        end = dt.datetime(2024, 10, 1)
        
        # Download stock data
        df = yf.download(stock, start=start, end=end)
        
        # Descriptive Data
        data_desc = df.describe()
        
        # Exponential Moving Averages
        