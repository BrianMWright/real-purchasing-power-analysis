# Real Purchasing Power Analysis of Gold and the DJIA

This repository contains a Python script that compares the historical purchasing power of gold and the Dow Jones Industrial Average (DJIA) over time, adjusted for inflation using the Consumer Price Index (CPI).

## Overview

The script downloads historical data for:
- **Gold futures (`GC=F`)** from Yahoo Finance
- **Dow Jones Industrial Average (`^DJI`)** from Yahoo Finance
- **Consumer Price Index (`CUUR0000SA0R`)** from the Federal Reserve Economic Data (FRED)

After retrieving the data, it:

1. Aligns and cleans the datasets by filling missing values.
2. Normalizes the CPI to serve as a baseline for calculating inflation-adjusted (real) values.
3. Computes the real purchasing power of both gold and the DJIA.
4. Generates plots to visualize how their purchasing power has evolved over various historical periods (e.g., from 10, 20, 30, 40, and 50 years ago to the present).

## Features

- **Automated Data Retrieval:** Uses `yfinance` and `pandas_datareader` to fetch financial and economic data.
- **Data Cleaning and Normalization:** Ensures all time series align properly and adjusts for inflation using CPI data.
- **Visualization:** Creates clear line plots depicting the real purchasing power of gold and DJIA over time.

## Requirements

- Python 3.7 or later
- [pandas](https://pandas.pydata.org/)
- [yfinance](https://pypi.org/project/yfinance/)
- [matplotlib](https://matplotlib.org/)
- [pandas_datareader](https://pandas-datareader.readthedocs.io/)

Install the required dependencies using:

```bash
pip install pandas yfinance matplotlib pandas_datareader
