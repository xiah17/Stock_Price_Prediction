# Stock_Price_Prediction
A simple end-to-end stock price prediction project using a Long Short-Term Memory (LSTM) neural network implemented in Python (TensorFlow/Keras). 
The project exposes a Flask REST API that serves predictions and model metadata and includes an optional lightweight frontend for visualization. 
Intended for educational use and experimentation not production financial.

# 🧠Features
- LSTM-based prediction of stock closing prices.
- Data preprocessing: scaling, sequence generation, splitting.
- Model training pipeline with callbacks (EarlyStopping, ModelCheckpoint).
- Smoothing Techniques: MA, EMA.
- Interactive plots: actual vs predicted prices.
- Flask REST API for serving predictions in real time.

# 📊Visualization
- Training loss curves.
- Actual vs Predicted price charts.
- Comparison across multiple stock symbols.

# 📦Python Dependencies
- maplotlib.pyplot
- numpy
- scipy
- pandas
- yfinance

