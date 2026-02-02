import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, period="2y"):
    """
    Fetches historical stock data from yfinance.
    
    Args:
        ticker (str): Stock ticker symbol (e.g., AAPL).
        period (str): Data period to download (default: "2y").
        
    Returns:
        pd.DataFrame: Cleaned dataframe with Date index.
    """
    print(f"Fetching data for {ticker} over {period}...")
    try:
        data = yf.download(ticker, period=period, progress=False)
        
        if data.empty:
            raise ValueError(f"No data found for ticker {ticker}.")
            
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)
            
        data.dropna(inplace=True)
        
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
