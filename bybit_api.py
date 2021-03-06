import ccxt
import os
from pprint import pprint

from dotenv import load_dotenv
load_dotenv(verbose=True)

# .envファイルからそれぞれの値を取得
API_KEY = os.getenv("API_KEY")
SECRET = os.getenv("SECRET")

class BybitApi:
    def __init__(self):
        self.bybit_api = ccxt.bybit(
            {
                "apiKey": API_KEY,
                "secret": SECRET,
                # "urls": {
                #     "api": "https://api-testnet.bybit.com/" # testnet（デモ版）を使用する場合はこの記述が必要なのでコメントアウトを外す
                # }
            }
        )
    
    # 保有中のポジションを取得
    def get_position(self, symbol):
        self.bybit_api.load_markets()
        market = self.bybit_api.market(symbol)

        return self.bybit_api.v2_private_get_position_list({ "symbol": market["id"] })["result"]
    
    # 注文を作成
    def create_order(self, symbol, order_type, side, amount):
        order = self.bybit_api.create_order(
            symbol,     # 通貨ペア
            order_type, # 成行注文か指値注文か（market: 成行注文、limit: 指値注文）
            side,       # 買いか売りか（buy: 買い、sell: 売り）
            amount,     # 注文量（USD）
            { 
              "qty": amount
            }
        )

        return order
