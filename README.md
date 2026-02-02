
# 📈 Stock Market Trend Analysis

A Python-based tool for analyzing stock market trends using technical indicators and machine learning.  
This project fetches historical stock data, computes key technical indicators, detects trend patterns, predicts future prices, and visualizes results with intuitive charts.



<img width="1919" height="1025" alt="Screenshot 2026-01-31 193955" src="https://github.com/user-attachments/assets/1c48018a-ca88-4c45-a5a4-4f1e9f03e498" />


---

# 🔍 Features

- **Data Fetching**  
  Retrieves historical stock data using `yfinance`.

- **Technical Analysis**  
  Computes commonly used indicators:
  - Moving Averages (e.g., SMA)
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence)
  - Bollinger Bands  
  *(These indicators help reveal trend direction and momentum.)* :contentReference[oaicite:0]{index=0}

- **Trend Detection**  
  Automatically identifies whether the stock is in an uptrend, downtrend, or sideways movement.

- **Machine Learning Prediction**  
  Uses a **Random Forest Regressor** to forecast the next day’s closing price.

- **Visualization**  
  Plots price and indicators for visual inspection of patterns and trends.

---

# 🛠️ Getting Started

## 📦 Prerequisites

- Python 3.8+
- Install required packages:

```bash
pip install -r requirements.txt
````

---

## 🚀 Usage

### Run interactively

Start the analysis tool and follow the prompts:

```bash
python main.py
```

### Provide ticker symbol directly

```bash
python main.py AAPL
python main.py RELIANCE.NS
```

Replace the tickers above with any valid symbol supported by Yahoo Finance.

---

## 📁 Repository Structure

```
.
├── data_fetch.py         # Fetches stock market data

├── indicators.py         # Computes technical indicators

├── trend_logic.py        # Logic for classifying trend direction

├── model.py              # Machine learning model for prediction

├── visualize.py          # Chart generation and plotting

├── main.py               # Entry point

├── requirements.txt      # Libraries and dependencies

└── README.md             # Project documentation

```

---

## 🧠 How It Works

1. **Fetch Data:**
   Pull historical stock prices with `yfinance`.

2. **Compute Indicators:**
   Calculate technical measures that help characterize price movement and trends.

3. **Trend Classification:**
   Apply logic to label the trend (e.g., uptrend, downtrend, sideways).

4. **Prediction:**
   Train and apply a Random Forest model to predict the following trading day’s price.

5. **Visualization:**
   Render plots showing price with indicators for exploratory analysis.

---

## 📊 Example Output

*(Screenshot in your repo displays visual results of trend analysis and prediction.)*

---

## 🧩 Contributing

Contributions are welcome. Please open an issue or submit a pull request with improvements.

---

## 📄 License

This repository does not currently specify a license. You can add one depending on how you want to share this code (e.g., MIT, Apache-2.0).

---

## 📬 Contact

Opened by **Adarsh Thakur**.
