import yfinance as yf
import matplotlib.pyplot as plt
import seaborn

msft = yf.Ticker("MSFT")

# get stock info
#print(msft.info)

# get historical market data
hist = msft.history(period="5d")

print(type(hist))

# msft.actions
print(hist['Close'])

# Plot everything by leveraging the very powerful matplotlib package
hist['Close'].plot(figsize=(16, 9))

# Download stock data then export as CSV
data_df = yf.download("AAPL", start="2020-02-01", end="2020-03-20")
data_df.to_csv('aapl.csv')
