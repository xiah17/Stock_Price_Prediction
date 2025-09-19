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