import yfinance as yf
import json

# Define the interval-to-period mapping
interval_to_period = {
    '1m': '5d',  # Maximum allowed for 1-minute interval
    '5m': '1mo', # Maximum allowed for 5-minute interval
    '15m': '1mo',# Maximum allowed for 15-minute interval
    '30m': '1mo',# Maximum allowed for 30-minute interval
    '60m': '1y',
    '1d': '1y',
    '1wk': '1y'
}

# List of stock names (example list)
symbol_list = ['AAPL', 'MSFT', 'GOOG', 'AMZN']  # Replace with your own list of stocks

# Function to fetch stock data for the symbol and interval
def get_stock_data(symbol, interval):
    period = interval_to_period[interval]  # Get the period for the interval

    # Fetch data using yfinance
    stock_data = yf.download(tickers=symbol, period=period, interval=interval)
    
    # Check the interval and return the correct price ( Close)
    #Change the 'Close' to 'Open' if you want the openng prices
    #Change the index in 'iloc[] to get the first or any other closing price if you want 
    if interval == '1d':
        if not stock_data.empty:
            return float(stock_data['Close'].iloc[-1])  # Get the last close price
        else:
            return 'NA'  # Return 'NA' if no data is found
    else:
        if not stock_data.empty:
            return float(stock_data['Close'].iloc[-1])  # Get the last closing price
        else:
            return 'NA'  # Return 'NA' if no data is found

# Function to write data to a JSON file
def write_to_json(file_path: str, data: dict):
    """
    Writes stock data to a JSON file.

    :param file_path: Path to the JSON file.
    :param data: Dictionary containing the stock data.
    """
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Collect stock data for each symbol and interval
stock_data_dict = {}  # Dictionary to hold all stock data

for symbol in symbol_list:
    print(f'Getting data for {symbol}')
    stock_data_dict[symbol] = {}  # Initialize dictionary for this stock
    
    # Loop through each interval and fetch the data
    for interval in interval_to_period.keys():
        stock_data_dict[symbol][interval] = get_stock_data(symbol, interval)

# Write the collected data to a JSON file
json_file_path = 'stock_data.json'#Enter the path of the json file
write_to_json(json_file_path, stock_data_dict)
