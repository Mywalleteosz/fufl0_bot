from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from web3 import Web3

# Подключаемся к Ethereum через Infura или другой RPC узел
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/your-infura-api-key"))

# Функция для получения баланса ETH
def get_balance(address):
    if not w3.isAddress(address):
        return "Некорректный адрес кошелька."
    
    # Получаем баланс
    balance = w3.eth.get_balance(address)
    eth_balance = w3.fromWei(balance, 'ether')
    return f"Баланс ETH для {address}: {eth_balance} ETH"

# Обработчик команды /balance
def balance(update: Update, context: CallbackContext):
    # Получаем адрес кошелька от пользователя
    if len(context.args) == 0:
        update.message.reply_text("Пожалуйста, введите адрес кошелька после команды. Пример: /balance 0xE7F211567Ef2186F3ADA151e0fC69F04B3406597")
        return
    
    wallet_address = context.args[0]
    response = get_balance(wallet_address)
    update.message.reply_text(response)

# Главная функция, которая запускает бота
def main():
    # Токен для твоего бота (получишь у BotFather в Telegram)
    TOKEN = "8449123073:AAGyVW4bnjGl2MrNjJBtdPCdpf-H--I3wPU"
    
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    
    # Обработчик команды /balance
    dispatcher.add_handler(CommandHandler("balance", balance))
    
    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
