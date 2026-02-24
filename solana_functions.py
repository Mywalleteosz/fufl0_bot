from solana.rpc.api import Client

solana_client = Client("https://api.mainnet-beta.solana.com")
SOLANA_ADDRESS = "8pM1DN3RiT8vbom5u1sNryaNT1nyL8CTTW3b5PwWXRBH"

async def get_solana_balance():
    """Получаем баланс Solana-аккаунта"""
    response = solana_client.get_balance(SOLANA_ADDRESS)
    if response['result']:
        balance = response['result']['value'] / 10**9  # баланс в SOL
        return f"Баланс: {balance} SOL"
    else:
        return "Не удалось получить баланс."
