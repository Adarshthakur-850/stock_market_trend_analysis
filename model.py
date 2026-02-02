import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

def train_predict_model(df):
    """
    Trains a Random Forest model to predict next day's Close price.
    
    Args:
        df (pd.DataFrame): Dataframe with indicators.
        
    Returns:
        float: Predicted next day closing price.
    """
    df = df.copy()
    df['Target'] = df['Close'].shift(-1)
    
    data = df.dropna()
    
    features = ['Close', 'Open', 'High', 'Low', 'Volume', 'MA20', 'MA50', 'MA200', 'RSI', 'MACD', 'BB_High', 'BB_Low']
    X = data[features]
    y = data['Target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    print(f"Model RMSE: {rmse:.2f}")
    
    joblib.dump(model, "model.pkl")
    
    last_row = df.iloc[[-1]][features]
    next_close = model.predict(last_row)[0]
    
    return next_close
