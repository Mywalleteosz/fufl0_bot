import requests

def get_balance(wallet):
    # 2Miners API пример для Ethereum
    url = f"https://eth.2miners.com/api/accounts/{wallet}"
    r = requests.get(url).json()
    # делим на 1e18 для нормального отображения ETH
    unpaid = r["stats"]["balance"] / 1e18
    paid = r["stats"]["paid"] / 1e18
    return unpaid, paid
