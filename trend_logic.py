def analyze_trend(df):
    latest = df.iloc[-1]
    price = latest['Close']
    ma50 = latest['MA50']
    ma200 = latest['MA200']
    rsi = latest['RSI']
    trend = "Sideways"
    if price > ma50 and ma50 > ma200:
        trend = "Uptrend"
    elif price < ma50 and ma50 < ma200:
        trend = "Downtrend"
    if rsi > 70:
        trend += " (Overbought - Potential Reversal)"
    elif rsi < 30:
        trend += " (Oversold - Potential Bounce)"
    return trend