import os
import aiogram as aio
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random as rnd
from modules.RPS import RPS
from modules.YTS import SearchYT
from modules.MultiUse import multiUseMod

rock = RPS.GameItem('Камень', 0, 2, 1)
paper = RPS.GameItem('Бумага', 1, 0, 2)
scissors = RPS.GameItem('Ножницы', 2, 1, 0)

handGame = RPS.handItem(rock, scissors, paper)

phrase_tuple = ("Что бы это значило?", "Извини, такого я не понимаю...", "Это какой-то текст... Хотел бы я знать, что он значит :(", "Когда-то и меня вела дорога приключений...")

with open('privacy/youtube-key.txt', 'r') as apiKey_file:
    thisApiKey = apiKey_file.read()

with open('privacy/tokenBot.txt', 'r') as tokenBot_file:
    thisBotToken = tokenBot_file.read()

thisBot = aio.Bot(thisBotToken)
dp = aio.Dispatcher(thisBot)

BTN_ROCK = InlineKeyboardButton('Камень', callback_data='Rock')
BTN_SCISSORS = InlineKeyboardButton('Ножницы', callback_data='Scissors')
BTN_PAPER = InlineKeyboardButton('Бумага', callback_data='Paper')

RSP_KB = InlineKeyboardMarkup().add(BTN_ROCK, BTN_SCISSORS, BTN_PAPER)

@dp.message_handler(commands=["start"])
async def process_start_command(message: aio.types.Message):
    print(message.from_user.id)
    multiUseMod.dirUser(message.from_user.id)

    await message.reply("Привет!\nЯ на связи и жду команды!\nНапиши /help и я расскажу, что умею :)")

@dp.message_handler(commands=["help"])
async def process_help_command(message: aio.types.Message):
    await message.reply("/help - список команд \n/echo - эхо-бот \n/RSP - камень-ножницы-бумага \n/YTsearch - поиск видосов на ютубе")

@dp.message_handler(commands=["echo"])
async def echo_bot(message: aio.types.Message):
    await message.reply("Играем в эхо!\nНапиши /echostop, если захочешь закончить!")
    with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_echo.txt', 'w') as flagEcho_file:
        flagEcho_file.write('True')

@dp.message_handler(commands=["YT"])
async def echo_bot(message: aio.types.Message):
    if len(message.text) <= len("/YT "):
        await message.reply("Пиши /YT <Ключевое слово>, чтобы найти видео! Например: /YT котики")
    else:
        myKW = message.text[len("/YT "):len(message.text)]
        myIdList = SearchYT.yt_video_search(myKW, thisApiKey)
        myLinkList = SearchYT.yt_video_return(myIdList)
        for i in myLinkList:
            await thisBot.send_message(message.from_user.id, text=i)

@dp.message_handler(commands=["RSP"])
async def RSP_bot(message: aio.types.Message):
    await message.reply("Играем в камень-ножницы-бумага!\nНапиши /RSPstop, чтобы закончить!", reply_markup=RSP_KB)
    flagRSP = "True"
    with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_RSP.txt', 'w') as flagRSP_file:
        flagRSP_file.write('True')

@dp.message_handler(commands=["Rock"])
async def choose_rock(message: aio.types.Message):
    with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_RSP.txt', 'r') as flagRSP_file:
        if flagRSP_file.read() == 'True':
            playerTurn = handGame.choise(True, 1)
            PCTurn = handGame.choise(False, 1)
            result_msg = RPS.compareHand(playerTurn['Game_Item'], PCTurn['Game_Item'])
            await thisBot.send_message(
                message.from_user.id,
                text=f'{playerTurn["msg"]},\n{PCTurn["msg"]},\n{result_msg}',
                reply_markup=RSP_KB
            )

@dp.message_handler(commands=["Scissors"])
async def choose_scissors(message: aio.types.Message):
    with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_RSP.txt', 'r') as flagRSP_file:
        if flagRSP_file.read() == 'True':
            playerTurn = handGame.choise(True, 2)
            PCTurn = handGame.choise(False, 2)
            result_msg = RPS.compareHand(playerTurn['Game_Item'], PCTurn['Game_Item'])
            await thisBot.send_message(
                message.from_user.id,
                text=f'{playerTurn["msg"]},\n{PCTurn["msg"]},\n{result_msg}',
                reply_markup=RSP_KB
            )

@dp.message_handler(commands=["Paper"])
async def choose_paper(message: aio.types.Message):
    with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_RSP.txt', 'r') as flagRSP_file:
        if flagRSP_file.read() == 'True':
            playerTurn = handGame.choise(True, 3)
            PCTurn = handGame.choise(False, 3)
            result_msg = RPS.compareHand(playerTurn['Game_Item'], PCTurn['Game_Item'])
            await thisBot.send_message(
                message.from_user.id,
                text=f'{playerTurn["msg"]},\n{PCTurn["msg"]},\n{result_msg}',
                reply_markup=RSP_KB
            )

@dp.callback_query_handler(text='Rock')
async def process_callback_rock(callback_query: aio.types.CallbackQuery):
    with open(f'cache/multiUse/Users/{str(callback_query.from_user.id)}/cache/flag_RSP.txt', 'r') as flagRSP_file:
        if flagRSP_file.read() == 'True':
            playerTurn = handGame.choise(True, 1)
            PCTurn = handGame.choise(False, 1)
            result_msg = RPS.compareHand(playerTurn['Game_Item'], PCTurn['Game_Item'])
            await thisBot.answer_callback_query(callback_query.id)
            await thisBot.send_message(
                callback_query.from_user.id,
                text=f'{playerTurn["msg"]},\n{PCTurn["msg"]},\n{result_msg}',
                reply_markup=RSP_KB
            )

@dp.callback_query_handler(text='Scissors')
async def process_callback_rock(callback_query: aio.types.CallbackQuery):
    with open(f'cache/multiUse/Users/{str(callback_query.from_user.id)}/cache/flag_RSP.txt', 'r') as flagRSP_file:
        if flagRSP_file.read() == 'True':
            playerTurn = handGame.choise(True, 2)
            PCTurn = handGame.choise(False, 2)
            result_msg = RPS.compareHand(playerTurn['Game_Item'], PCTurn['Game_Item'])
            await thisBot.answer_callback_query(callback_query.id)
            await thisBot.send_message(
                callback_query.from_user.id,
                text=f'{playerTurn["msg"]},\n{PCTurn["msg"]},\n{result_msg}',
                reply_markup=RSP_KB
            )

@dp.callback_query_handler(text='Paper')
async def process_callback_rock(callback_query: aio.types.CallbackQuery):
    with open(f'cache/multiUse/Users/{str(callback_query.from_user.id)}/cache/flag_RSP.txt', 'r') as flagRSP_file:
        flagRSP = flagRSP_file.read()
        if flagRSP == 'True':
            playerTurn = handGame.choise(True, 3)
            PCTurn = handGame.choise(False, 3)
            result_msg = RPS.compareHand(playerTurn['Game_Item'], PCTurn['Game_Item'])
            await thisBot.answer_callback_query(callback_query.id)
            await thisBot.send_message(
                callback_query.from_user.id,
                text=f'{playerTurn["msg"]},\n{PCTurn["msg"]},\n{result_msg}',
                reply_markup=RSP_KB
            )

@dp.message_handler()
async def get_text_from_messages(message: aio.types.Message):
    with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_echo.txt', 'r') as flagEcho_file:
        with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_RSP.txt', 'r') as flagRSP_file:
            if flagRSP_file.read() == "False":
                if flagEcho_file.read() == "True":
                    if message.text != '/echostop':
                        await thisBot.send_message(message.from_user.id, f'Все говорят "{message.text}", а ты купи слона')
                    elif message.text == '/echostop':
                        await thisBot.send_message(message.from_user.id, 'Не играем в эхо!')
                        with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_echo.txt', 'w') as flagEcho_file:
                            flagEcho_file.write('False')
                else:
                    await message.reply(rnd.choice(phrase_tuple))
            else:
                if message.text == '/RSPstop':
                    await thisBot.send_message(message.from_user.id, 'Не играем в камень-ножницы-бумага!')
                    with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_RSP.txt', 'w') as flagRSP_file:
                        flagRSP_file.write('False')

aio.executor.start_polling(dp)
