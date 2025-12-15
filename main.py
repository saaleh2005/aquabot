import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers.start import start_router
from handlers.articles import articles_router
from handlers.search import search_router
from handlers.quiz import quiz_router

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(articles_router)
    dp.include_router(search_router)
    dp.include_router(quiz_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
