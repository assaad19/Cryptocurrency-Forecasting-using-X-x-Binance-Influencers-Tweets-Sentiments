import pandas as pd
import os

csvs=['240115_binance_1002.csv','240115_SOL_3357.csv','240116_binance_1076.csv','240116_SOL_2148.csv',
    '240117_binance_1117.csv','240117_SOL_2423.csv','240118_binance_742.csv','240118_SOL_2336.csv',
    '240119_binance_746.csv','240119_SOL_1517.csv','240120_binance_1454.csv','240120_SOL_2807.csv',
    '240122_binance_1285.csv','240122_SOL_2810.csv','240124_binance_787.csv','240124_SOL_2152.csv',
    '240201_binance_1006.csv','240201_SOL_3030.csv','240205_binance_657.csv','240205_SOL_1777.csv',
    '240207_binance_689.csv','240207_SOL_2008.csv','240208_binance_599.csv','240208_SOL_1829.csv',
    '240209_binance_561.csv','240209_SOL_1777.csv','240211_binance_524.csv','240211_SOL_1333.csv',
    '240212_binance_510.csv','240212_SOL_1464.csv','240214_binance_423.csv','240214_SOL_1500.csv',
    '240215_binance_586.csv','240215_SOL_1662.csv','240217_binance_563.csv','240217_SOL_1622.csv',
    '240218_binance_613.csv','240218_SOL_1621.csv','240219_binance_615.csv','240219_SOL_1723.csv',
    '240220_binance_515.csv','240220_SOL_1577.csv']

def process_csv(file_path):
    df = pd.read_csv(file_path)  # Read CSV file
    df = df.iloc[1:]  # Remove column names (assuming they are in the first row)
    return df

# Iterate through CSV files, process them, and concatenate vertically
dfs = [process_csv(file) for file in csvs]
combined_df = pd.concat(dfs, ignore_index=True)

# Add column names to the combined dataframe
column_names = [
    "username", "tweet_text", "tweet_raw", "date",
    "happy", "angry", "surprise", "sad", "fear",
    "afinn", "bing", "sid", "bertweet", "bertweet_confidence"
]
combined_df.columns = column_names

# csv combined dataframe
output_path = "aggregated_data_f.csv"
combined_df.to_csv(output_path, index=False)

print(f"Combined data saved to: {output_path}")