from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

class BinanceClient:
    def __init__(self):
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")
        print("API KEY:", api_key)
        print("API SECRET:", api_secret)

        self.client = Client(api_key, api_secret)

        # ✅ Futures Testnet endpoint
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

    def get_client(self):
        return self.client