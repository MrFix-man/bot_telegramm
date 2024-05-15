import asyncio

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, Audio

from dwn import download

bot = Bot('7025822220:AAHSXZmFXOpp8B-eB2JE9OE1zcuP-K9MJWI')
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: Message):
    print(message)
    await message.answer(f'Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}, вставьте пожалуйста ссылку на  ролик с YouTube')


@dp.message(F.text)
async def dwl(message: Message):
    data = {
        'url': 'N/A'
    }
    entites = message.entities or []
    for entity in entites:
        if entity.type in data.keys():
            data[entity.type] = entity.extract_from(message.text)
    video_link = data['url']
    path_to_audio = download(video_link)
    await bot.send_audio(message.chat.id,FSInputFile(path_to_audio))


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
