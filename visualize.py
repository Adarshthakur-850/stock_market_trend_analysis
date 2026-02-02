import matplotlib.pyplot as plt
import seaborn as sns

def plot_analysis(df, ticker):
    """
    Plots Price, Moving Averages, RSI, and MACD.
    """
    sns.set_style("darkgrid")
    
    fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True, gridspec_kw={'height_ratios': [2, 1, 1]})
    
    axes[0].plot(df.index, df['Close'], label='Close Price', color='black', alpha=0.6)
    axes[0].plot(df.index, df['MA20'], label='MA20', color='blue', linewidth=1)
    axes[0].plot(df.index, df['MA50'], label='MA50', color='orange', linewidth=1)
    axes[0].plot(df.index, df['MA200'], label='MA200', color='red', linewidth=1)
    axes[0].fill_between(df.index, df['BB_High'], df['BB_Low'], color='gray', alpha=0.1, label='Bollinger Bands')
    axes[0].set_title(f"{ticker} Price Analysis")
    axes[0].legend()
    
    axes[1].plot(df.index, df['RSI'], color='purple', label='RSI')
    axes[1].axhline(70, color='red', linestyle='--', alpha=0.5)
    axes[1].axhline(30, color='green', linestyle='--', alpha=0.5)
    axes[1].set_title("Relative Strength Index (RSI)")
    axes[1].legend()
    
    axes[2].plot(df.index, df['MACD'], label='MACD', color='blue')
    axes[2].plot(df.index, df['MACD_Signal'], label='Signal', color='orange')
    axes[2].bar(df.index, df['MACD'] - df['MACD_Signal'], color='grey', alpha=0.3)
    axes[2].set_title("MACD")
    axes[2].legend()
    
    plt.tight_layout()
    plt.show()
