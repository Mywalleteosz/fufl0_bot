from aiogram import types

async def balance_command(message: types.Message):
    balance = await get_solana_balance()
    await message.reply(balance)
