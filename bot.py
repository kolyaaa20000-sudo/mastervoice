import os
import random
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

# Токен берется из закрытых настроек хостинга (безопасно от ботов-краков)
TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

user_codes = {}

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    code = str(random.randint(1000, 9999))
    user_codes[user_id] = code
    
    await message.answer(
        f"🚗 **Добро пожаловать в MasterVoice!**\n\n"
        f"🎁 Вам успешно начислен эксклюзивный анимированный **золотой Rolls-Royce** с подписью от MasterVoice!\n\n"
        f"🔐 Ваш код подтверждения для входа в приложение:\n"
        f"👉 `{code}`",
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
