from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from decouple import config
import logging
import random


TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
ADMIN = 711881147

@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"Privet itishnik {message.from_user.full_name}")

@dp.message_handler(commands=['quiz'])
async def victorina_1(message: types.Message):
    question = "Сколько областьей в Кыргызстане?"
    answers = ['1', '3', '5', '7']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=3
                        )

@dp.message_handler(commands=['quiz1'])
async def victorina_2(message: types.Message):
     question = "Столица Канады?"
     answers = ['Онтарио', 'Ванкувер', 'Оттава', 'Кубек']
     await bot.send_poll(message.chat.id,
                         question=question,
                         options=answers,
                         is_anonymous=False,
                         type='quiz',
                         correct_option_id=2
                         )

@dp.message_handler(commands=['mem1'])
async def mem(message: types.Message):
    murkup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_1"
    )
    murkup.add(button_call_1)

    photo = open("media/output1.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)

    question = "Output:"
    answers = ["[2, 4]", '[2, 4, 6]', '[2]', '[4]', '[0]', "Error"]
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0,
                        open_period=10,
                        reply_markup=murkup
                        )

@dp.message_handler(commands=['mem1'])
async def mem(message: types.Message):
    murkup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_1"
    )
    murkup.add(button_call_1)

    photo = open("media/output2.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)

    question = "Output:"
    answers = ['[20]', '[10]', "Error"]
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        open_period=10,

                        )
@dp.callback_query_handler(lambda func: func.data == 'button_call_1')
async def mem2(call:types.CallbackQuery):
    photo = open("media/output1.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo)

    question = "Output:"
    answers = ["[2, 4]", '[2, 4, 6]', "Error"]
    await bot.send_poll(call.message.chat.id,

                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0,
                        open_period=10,
                        )
    #pin


@dp.message_handler(commands=["pin"], commands_prefix="!/")
async def pin(message: types.Message):
    if message.from_user.id != ADMIN:
        await message.reply("Хозяин другой!")
    if message.text.startswith('!pin'):

        if not message.reply_to_message:
            await message.reply('Команда должна быть ответом на сообщение!')

my_bot = Bot(TOKEN)
def pinMsg(update, context):

        my_bot.pin_chat_message(chat_id=update.message.chat.id, message_id=update.message.message_id,
                                disable_notification=None, timeout=None)
        #game


@dp.message_handler()
async def game(message: types.Message):
    emodji = '🎱, 🥏, ⛳,️🏐'.split()
    a = random.choice(emodji)
    if message.text == 'Game to start':
        await bot.send_dice(message.from_user.id, emoji=a),

@dp.message_handler()
async def echo(message:types.Message):
     text=f'hi there:{message.text}'
     await bot.send_message(chat_id=message.from_user.id,text=text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)