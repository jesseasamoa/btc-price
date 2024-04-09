import pandas as pd
from sqlalchemy import create_engine
from binance.client import Client
from binance import BinanceSocketManager
import asyncio
import logging

# Configure logging
logging.basicConfig(filename='socket_log.log', level=logging.INFO)

async def main():
    client = Client()
    bsm = BinanceSocketManager(client)
    socket = bsm.kline_socket('BTCUSDT')
    async with socket as s:
        while True:  # Added an infinite loop to continuously receive messages
            msg = await s.recv()
            logging.info(f"Received message: {msg}")  # Log the received message
            print(msg)
            df = datatransfo(msg)  # Call the data transformation function
            save_to_database(df)  # Call the function to save data to the database

def datatransfo(msg):
    df = pd.DataFrame({'Time': msg['E'], 'Price': msg['k']['c']}, index=[0])
    df['Price'] = df['Price'].astype(float)
    df['Time'] = pd.to_datetime(df['Time'], unit='ms')
    return df

def save_to_database(df):
    engine = create_engine('sqlite:///BTCUSDTstream.db')
    df.to_sql('BTCUSDT', engine, if_exists='append', index=False)

# Run the main function
asyncio.run(main())
