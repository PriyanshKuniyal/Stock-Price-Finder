# Stock Data Fetcher

This project fetches stock price data for a list of stock symbols from the Yahoo Finance API (`yfinance`) at various intervals.
The fetched data is saved into a JSON file where each stock symbol is the key, and the value contains data for each interval.

## Features

- **Stock Data**: Fetches stock price data (Open/Close) for various intervals such as 1-minute, 5-minute, 15-minute, 30-minute, hourly, daily, and weekly.
- **Intervals Supported**:
  - `1m`: 1-minute data (max period of 5 days)
  - `5m`: 5-minute data (max period of 1 month)
  - `15m`: 15-minute data (max period of 1 month)
  - `30m`: 30-minute data (max period of 1 month)
  - `60m`: Hourly data (max period of 1 year)
  - `1d`: Daily data (max period of 1 year)
  - `1wk`: Weekly data (max period of 1 year)
- **JSON Output**: Stores stock symbol data into a JSON file with the stock symbol as the key and interval data as the value.

## Project Structure

. ├── stock_data_fetcher.py # Main Python script to fetch and save stock data 
  ├── stock_data.json # JSON file where stock data is stored 
  └── .README.md # This README file
  └── .LICENSE# This LICENSE file(MIT)


## Prerequisites

- Python 3.10+
- Required Python packages:
  - `yfinance`

Install the required package using pip:
# pip install yfinance

Usage
Clone the repository:
''' bash
git clone https://github.com/yourusername/stock-data-fetcher.git
cd Stock-Price-Finder

Configure the stock list:
Update the symbol_list in the stock_data_fetcher.py file with your list of stock symbols.

Run the script:
Run the stock_data_fetcher.py script to fetch stock data and store it in a JSON file:

View the JSON output:
After the script runs successfully, you can find the fetched data in the stock_data.json file.

Example JSON Output
The stock_data.json will look like this:

{
    "AAPL": {
        "1m": 150.5,
        "5m": 151.3,
        "15m": 149.8,
        "30m": 150.2,
        "60m": 150.1,
        "1d": 152.3,
        "1wk": 153.0
    },
    "MSFT": {
        "1m": 280.7,
        "5m": 281.2,
        "15m": 279.9,
        "30m": 280.5,
        "60m": 281.1,
        "1d": 282.8,
        "1wk": 284.0
    }
}

Customization
Modify stock symbols: Update the symbol_list in the script with the stocks you're interested in.

Intervals: You can change or add more intervals based on Yahoo Finance's supported intervals by modifying the interval_to_period dictionary.

License:
This project is licensed under the MIT License. See the LICENSE file for details.

Contributions
Contributions, issues, and feature requests are welcome! Feel free to check out the issues page.
