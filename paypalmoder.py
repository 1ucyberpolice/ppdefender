import logging
import random

import requests
from aiogram import Bot, Dispatcher, executor, types

from filters import IsAdminFilter
import telebot

logging.basicConfig(level=logging.INFO)

from config_pp import TOKEN
bot = Bot(TOKEN)
dp = Dispatcher(bot)
GROUP_ID = 564021126

dp.filters_factory.bind(IsAdminFilter)

text = '[💸Канал выплат💸](https://t.me/joinchat/ZJWZj5mCEog4NmQy)'
toolID = [
    'None',
    'None',
    '3'
]
kasima = [
    'Чепуха',
    'Лучше бы молчал...',
    'Ну и бред',
    'Лучше бы воркал...',
    'Ничего умнее от тебя не ожидал услышать...',
    'Из нас двоих ботом кажешься ты',
    'Не пиши сюда больше пж'
]
victimID = [
    '1'
]

kassaEuro = ['1']

euroFinder = ['€']
userFinder = ['@']
userSymbol = ['1', '2']

euroNoSymbol = ['0']
euroN = [0]
profits = [0]
recordEuro = [2108]
euroResult = [0]
euroKassa = [0]


ppmoderAdd = ['Палки в процессе добавления! Ожидайте админов.']
channelPost = ['1']

publish_post_markup = types.InlineKeyboardMarkup()
topublish = types.InlineKeyboardButton('✅', callback_data='topublish')
tonopublish = types.InlineKeyboardButton('🚫', callback_data='tonopublish')
publish_post_markup.add(topublish, tonopublish)

markup_inline_choice = types.InlineKeyboardMarkup()
addPP = types.InlineKeyboardButton('Добавить PP', callback_data='add')
markup_inline_choice.add(addPP)

markup_pp = types.InlineKeyboardMarkup()
added = types.InlineKeyboardButton('PP добавлены', callback_data='added')
markup_pp.add(added)

markup_manuals = types.InlineKeyboardMarkup()
manual = types.InlineKeyboardButton('🎓Мануалы🎓', callback_data='manual')
markup_manuals.add(manual)

manual_markup = types.InlineKeyboardMarkup()
first = types.InlineKeyboardButton('📚Работа с PayPal | Vinted', url='https://telegra.ph/Status-proekta---VORK-06-05')
second = types.InlineKeyboardButton('📚Какой товар выставлять?', url='https://telegra.ph/Kakoj-tovar-vystavlyat-06-05')
third = types.InlineKeyboardButton('Обратно', callback_data='return')
manual_markup.add(first)
manual_markup.add(second)
manual_markup.add(third)


@dp.message_handler(content_types=['new_chat_members'])
async def users_joined(message: types.Message):
    await message.delete()
    await message.answer('🍀К чату присоединился воркер!🍀'
                         '\nПрофиль: @{0}\n'
                         '\n'
                         '❗️Вся информация в закрепленных \nсообщениях.\n'
                         '\n'
                         '🔫Хорошего дня и удачного скама!'.format(message.from_user.username))
    await message.answer(text, parse_mode='Markdown', reply_markup=markup_manuals)


@dp.message_handler(is_admin=True, commands=["adminPanel"])
async def cmd_start(message: types.Message):
    await message.delete()
    await message.answer('♣️Админ: @{0}♣️\n'
                         '      Выберите действие:'.format(message.from_user.username),
                         reply_markup=markup_inline_choice)

@dp.message_handler(commands=["available_pp"])
async def avaliable(message: types.Message):
    await message.answer('🍀Доступные палки:🍀\n'
                         +ppmoderAdd[0])

@dp.message_handler(is_admin=True, commands=["ban"], commands_prefix="!/")
async def ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply('‼️Команда должна быть ответом на сообщение!')
        return

    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await message.bot.kick_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)

    await message.reply_to_message.reply('⚫️Воркер забанен!⚫️')


@dp.callback_query_handler(lambda c: c.data == 'add')
async def self(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                              text='🍀Введите доступные🍀\n'
                                   '      палки!\n', reply_markup=markup_pp)



@dp.callback_query_handler(lambda c: c.data == 'manual')
async def self(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                              text='🎓Выберите мануал:🎓', reply_markup=manual_markup)


@dp.callback_query_handler(lambda c: c.data == 'return')
async def self(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                              text=text, parse_mode='Markdown', reply_markup=markup_manuals)

@dp.message_handler(regexp='❗️')
async def personal(message: types.Message):
    if message.from_user.id == 1892827220:
        recordEuro[0] = message.text
        print(recordEuro[0])
        await message.delete()

@dp.message_handler()
async def kassa(message: types.Message):
    if message.chat.type == types.ChatType.PRIVATE:
        if message.from_user.id == 1892827220:
            channelPost[0] = message.text

            words = message.text.split()
            for word in words:
                for x in euroFinder:
                    if word.count(x):
                        print('Yep. "%s" contains characters from "%s" item.' % (word, x))
                        kassaEuro[0] = word
                        euroNoSymbol[0] = int(kassaEuro[0].replace('€',''))
                        print(euroNoSymbol[0])
                        #записываем результат в переменную типа инт
                        euroResult[0] += int(euroNoSymbol[0])
                        #перезапись рекорда, если переменнаяНоуСимбол больше переменной рекорд
                        if int(euroResult[0]) > int(recordEuro[0]):
                            recordEuro[0] = int(euroResult[0])

            for word in words:
                for x in userFinder:
                    if word.count(x):
                        print('Yep. "%s" contains characters from "%s" item.' % (word, x))
                        userSymbol[0] = word
                        print(userSymbol[0])

            await message.delete()

            if channelPost != '1':
                await message.answer(channelPost[0], reply_markup=publish_post_markup)

    if message.chat.type == types.ChatType.PRIVATE:
        if message.from_user.username == 'blackebayer':
            channelPost[0] = message.text

            words = message.text.split()
            for word in words:
                for x in euroFinder:
                    if word.count(x):
                        print('Yep. "%s" contains characters from "%s" item.' % (word, x))
                        kassaEuro[0] = word
                        euroNoSymbol[0] = int(kassaEuro[0].replace('€',''))
                        print(euroNoSymbol[0])
                        #записываем результат в переменную типа инт
                        euroResult[0] += int(euroNoSymbol[0])
                        #перезапись рекорда, если переменнаяНоуСимбол больше переменной рекорд
                        if int(euroResult[0]) > int(recordEuro[0]):
                            recordEuro[0] = int(euroResult[0])

            for word in words:
                for x in userFinder:
                    if word.count(x):
                        print('Yep. "%s" contains characters from "%s" item.' % (word, x))
                        userSymbol[0] = word
                        print(userSymbol[0])

            await message.delete()

            if channelPost != '1':
                await message.answer(channelPost[0], reply_markup=publish_post_markup)

    if 'касса' in message.text:
        print(message.chat.id)
        await message.answer('🍀Статистика за сегодня:🍀\n'
                             '🐘Профитов: '+str(profits[0])+'🐘\n'
                             '💸На сумму: '+str(euroResult[0])+'€💸\n'
                             '❗️Рекорд: '+str(recordEuro[0])+'€❗️\n')

    if 'заряду' in message.text:
        await message.answer_sticker('CAACAgIAAxkBAAECaFBgwSqxwBgXUxDQwb6P0GcO3sTkygACRQADZtYKO1dsr_MdF_EUHwQ')

    if message.from_user.id == 1892827220:
        if message.from_user.last_name == 'Українаа':
            victimID[0] = message.text
            print(victimID[0])
            await message.delete()

    if message.from_user.username == victimID[0]:
        await message.reply(random.choice(kasima))

    if message.from_user.username == '09370007390':
        if '‼️' in message.text:
            ppmoderAdd[0] = message.text
            await message.delete()

    if message.from_user.username == 'ucyberpolice':
        if '‼️' in message.text:
            ppmoderAdd[0] = message.text
            await message.delete()

    if message.from_user.username == 'blackebayer':
        if '‼️' in message.text:
            ppmoderAdd[0] = message.text
            await message.delete()


@dp.callback_query_handler(lambda c: c.data == 'added')
async def self(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                              text='🍀Палки сохранены!🍀\n'
                                   '       /available_pp',reply_markup=None)


@dp.callback_query_handler(lambda c: c.data == 'topublish')
async def self(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                              text='🍀Пост успешно опубликован!🍀',reply_markup=None)

    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(TOKEN), params=dict(
        chat_id=-1001443483878, text=channelPost[0]))

    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(TOKEN), params=dict(
        chat_id=-1001375668801, text='⚡️NEW PROFIT⚡️\n'
                             '💶На сумму: '+str(euroNoSymbol[0])+'€💶\n'
                             'Воркер: '+userSymbol[0]))
    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(TOKEN), params=dict(
        chat_id=-587107060, text=text, parse_mode='Markdown'))
    profits[0] += 1


@dp.callback_query_handler(lambda c: c.data == 'tonopublish')
async def self(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                              text='🚫Пост успешно удален!🚫',reply_markup=None)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
