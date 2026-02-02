
# Stock Market Trends Analysis

A Python-based tool to analyze stock market trends using technical indicators (MA, RSI, MACD, Bollinger Bands) and Machine Learning (Random Forest) to predict future prices.

## Prerequisities
- Python 3.8+

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script and enter a ticker symbol when prompted.

```bash
python main.py
```

Or pass the ticker as an argument:
```bash
python main.py AAPL
python main.py RELIANCE.NS
```

## Features
- **Data Fetching**: Real-time data from Yahoo Finance (`yfinance`).
- **Technical Analysis**: 
    - Moving Averages (20, 50, 200)
    - RSI (Relative Strength Index)
    - MACD (Moving Average Convergence Divergence)
    - Bollinger Bands
- **Trend Detection**: AUTOMATIC classification of Uptrend/Downtrend/Sideways.
- **Prediction**: Random Forest Regressor predicts the next day's closing price.
- **Visualization**: Interactive plots of price and indicators.
=======
# stock_market_trend_analysis
ml project

