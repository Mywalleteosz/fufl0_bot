import requests

def eth_usdt_bybit():
    r = requests.get(
        "https://api.bybit.com/v5/market/tickers",
        params={"category": "spot", "symbol": "ETHUSDT"}
    ).json()
    return float(r["result"]["list"][0]["lastPrice"])

def eth_usdt_okx():
    r = requests.get(
        "https://www.okx.com/api/v5/market/ticker",
        params={"instId": "ETH-USDT"}
    ).json()
    return float(r["data"][0]["last"])
