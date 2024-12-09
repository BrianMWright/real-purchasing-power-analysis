import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import pandas_datareader.data as web

# Define the date range
start = "1900-01-01"
end = datetime.now().strftime("%Y-%m-%d")

# Fetch historical data using yfinance
gold_data = yf.download('GC=F', start=start, end=end)  # Gold futures
djia_data = yf.download('^DJI', start=start, end=end)  # Dow Jones Industrial Average
cpi_data = web.DataReader('CUUR0000SA0R', 'fred', start, end)  # Consumer Price Index for All Urban Consumers

# Fill missing data by forward fill method
gold_data = gold_data['Adj Close'].ffill()
djia_data = djia_data['Adj Close'].ffill()
cpi_data = cpi_data.ffill()

# Reindex the gold and DJIA data to match CPI dates
gold_data = gold_data.reindex(cpi_data.index, method='ffill')
djia_data = djia_data.reindex(cpi_data.index, method='ffill')

# Ensure that all NaNs are handled after reindexing
gold_data = gold_data.ffill().bfill()
djia_data = djia_data.ffill().bfill()

# Check if data alignment was successful
if gold_data.isnull().any() or djia_data.isnull().any():
    print("Data alignment issue detected.")
else:
    print("Data aligned successfully.")

# Normalize CPI to start at 1 for the base year
cpi_normalized = cpi_data / cpi_data.iloc[0]

# Calculate inflation-adjusted (real) values for gold and DJIA
gold_real = gold_data * (cpi_normalized.iloc[0] / cpi_normalized).values.flatten()
djia_real = djia_data * (cpi_normalized.iloc[0] / cpi_normalized).values.flatten()

def plot_purchasing_power(start_year):
    start_date = f'{start_year}-01-01'
    plt.figure(figsize=(14, 8))
    plt.plot(gold_real[start_date:], label='Gold (Real Purchasing Power)', color='gold')
    plt.plot(djia_real[start_date:], label='DJIA (Real Purchasing Power)', color='blue')
    plt.title(f'Purchasing Power from {start_year} to Present')
    plt.xlabel('Year')
    plt.ylabel('Purchasing Power')
    plt.legend()
    plt.grid(True)
    plt.show()

# Plot the data with different starting points
for start_year in [datetime.now().year - 10, datetime.now().year - 20, datetime.now().year - 30, datetime.now().year - 40, datetime.now().year - 50]:
    plot_purchasing_power(start_year)
