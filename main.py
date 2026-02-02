import data_fetch
import indicators
import trend_logic
import model
import visualize
import sys

def main():
    print("=== Stock Market Trends Analysis ===")
    
    if len(sys.argv) > 1:
        ticker = sys.argv[1]
    else:
        ticker = input("Enter Stock Ticker (e.g., AAPL, TSLA, RELIANCE.NS): ").strip().upper()
    
    df = data_fetch.fetch_stock_data(ticker)
    if df is None:
        return
    
    print(f"Data fetched successfully. Rows: {len(df)}")
    
    print("Calculating technical indicators...")
    df = indicators.add_indicators(df)
    
    trend = trend_logic.analyze_trend(df)
    print(f"\n>>> CURRENT TREND: {trend} <<<\n")
    
    print("Training prediction model...")
    next_price = model.train_predict_model(df)
    print(f"\n>>> PREDICTED NEXT DAY CLOSE: ${next_price:.2f} <<<\n")
    
    print("Generating plots...")
    visualize.plot_analysis(df, ticker)

if __name__ == "__main__":
    main()
