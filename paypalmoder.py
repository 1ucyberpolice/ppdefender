import asyncio
import logging
import random
import time

import aioschedule

import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from filters import IsAdminFilter
import telebot

storage = MemoryStorage()

logging.basicConfig(level=logging.INFO)
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)

dp.filters_factory.bind(IsAdminFilter)


class AdminPanel(StatesGroup):
    paypal = State()


class AdminPanel1(StatesGroup):
    notification_admin_panel = State()


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

addedpp = """_Палки в процессе добавления, ожидайте админов❕️_
"""
added_notification = """
<i>Данные сохранены❕️🕰</i>
"""
disput = """
♠️Администрация проекта♠️
           ⚡𝐏𝐚𝐲𝐏𝐚𝐥 𝐒𝐪𝐮𝐚𝐝⚡
            предупреждает❕️
_ За диспуты будем штрафовать
и не выплачивать профиты!_
"""
disput2 = """
_1. Не говорите покупателю, что
отправите посылку через час, два.
2. После профита не раскрывайте 
себя.
3. Отвечайте им, держите их вплоть
до вывода.
4. Не допускайте банов аккаунтов._"""

kassaEuro = ['1']
euroFinder = ['€']
userFinder = ['@']
userSymbol = ['Не определен', '2']
euroNoSymbol = ['0']
euroN = [0]
profits = [0]
recordEuro = [2108]
euroResult = [0]
euroKassa = [0]
channelPost = ['1']

ppAnswer = [addedpp]
notificationAnswer = [disput2]

one_hour_cancel = [0]

publish_post_markup = types.InlineKeyboardMarkup()
topublish = types.InlineKeyboardButton('✅', callback_data='topublish')
tonopublish = types.InlineKeyboardButton('🚫', callback_data='tonopublish')
publish_post_markup.add(topublish, tonopublish)

markup_inline_choice = types.InlineKeyboardMarkup()
addPP = types.InlineKeyboardButton('Добавить PP', callback_data='add')
addNotiication = types.InlineKeyboardButton('Уведомление', callback_data='notification')
markup_inline_choice.add(addPP)
markup_inline_choice.add(addNotiication)

hour_inline_choice = types.InlineKeyboardMarkup()
switch_on = types.InlineKeyboardButton('Включить', callback_data='switch_on')
hour_inline_choice.add(switch_on)

markup_manuals = types.InlineKeyboardMarkup()
manual = types.InlineKeyboardButton('🎓Мануалы🎓', callback_data='manual')
markup_manuals.add(manual)

manual_markup = types.InlineKeyboardMarkup()
first = types.InlineKeyboardButton('📚Работа с PayPal|Vinted',
                                   url='https://telegra.ph/%F0%9D%90%8F%F0%9D%90%9A%F0%9D%90%B2%F0%9D%90%8F%F0%9D%90%9A%F0%9D%90%A5-%F0%9D%90%84%F0%9D%90%A6%F0%9D%90%A9%F0%9D%90%A2%F0%9D%90%AB%F0%9D%90%9E--Manual-10-07-01')
second = types.InlineKeyboardButton('📚Трек-код DNL', url='https://telegra.ph/%F0%9D%90%8F%F0%9D%90%9A%F0%9D%90%B2%F0%9D%90%8F%F0%9D%90%9A%F0%9D%90%A5-%F0%9D%90%84%F0%9D%90%A6%F0%9D%90%A9%F0%9D%90%A2%F0%9D%90%AB%F0%9D%90%9ETrek-kod-DNL-07-03')
third = types.InlineKeyboardButton('Обратно', callback_data='return')
manual_markup.add(first)
manual_markup.add(second)
manual_markup.add(third)

for_top_worker_markup = types.InlineKeyboardMarkup()
top_worker_panel1 = types.InlineKeyboardButton('👁Привилегии', callback_data='privilegii')
top_worker_panel2 = types.InlineKeyboardButton('🔰Парсер', url='https://t.me/paypalparcer_bot')
for_top_worker_markup.add(top_worker_panel1)
for_top_worker_markup.add(top_worker_panel2)

return_privilegii = types.InlineKeyboardMarkup()
return_privilegi1 = types.InlineKeyboardButton('Обратно🔙', callback_data='return3')
return_privilegii.add(return_privilegi1)

new_member_in_main = """
💠Новый топ-воркер!💠 
Профиль: @{0}

_Для участников данного 
чата действуют особые 
привилегии❕_

💷Удачного скама!
 """

new_member = """
🍀К чату присоединился воркер!🍀   
Профиль: @{0}

_❕️Вся информация в закрепленных 
сообщениях._

🔫Хорошего дня и удачного скама! """
add_pp = """
_Введите доступные
палки❕️_
"""
pp_saved = """
<i>Палки сохранены❕️</i>
/available_pp
"""
coderAdmin = """
♣️<i>Админ:</i> @ucyberpolice7♣️
  <i>Статус:</i> Кодер
  <i>Выберите действие❕️</i>
"""
ownerAdmin = """
♣️<i>Админ:</i> @blackebayer♣️
  <i>Статус:</i> Владелец
  <i>Выберите действие❕️</i>
"""
nono = """
Тянешься к власти?
Ахуел ты, ладно, давай брат, обнял.
Нажмешь 'ОК' - бан"""
add_not = """
_Введите текст 
уведомления❕️_
"""
coder_panel = """
♣️<i>Кодер:</i> @ucyberpolice7♣️
  <i>Скрытый:</i> .docs/.re
  <i>Логи:</i> clear
  <i>Хост:</i> stably
"""
privilegii = """
⚡️𝐏𝐚𝐲𝐏𝐚𝐥 𝐄𝐦𝐩𝐢𝐫𝐞⚡️
Привилегии топ-воркерам:
   <i>- Ставка 60%,
     Личный парсер,
     Специальные
     возможности</i>
"""

adminID = [1695283624, 999503141]

@dp.message_handler(regexp='&')
async def personal(message: types.Message):
    if message.from_user.id == 1695283624:
        profits[0] -= 1
        await message.delete()


@dp.message_handler(content_types=['new_chat_members'])
async def users_joined(message: types.Message):
    if message.chat.id == -1001487558891:
        await message.delete()
        await message.answer(new_member_in_main.format(message.from_user.username), parse_mode="Markdown")
        await message.answer(text, parse_mode='Markdown', reply_markup=for_top_worker_markup)

    elif message.chat.id == -1001375668801:
        await message.delete()
        await message.answer(new_member.format(message.from_user.username), parse_mode="Markdown")
        await message.answer(text, parse_mode='Markdown', reply_markup=markup_manuals)


@dp.message_handler(is_admin=True, commands=["coderPanel"], state=None)
async def cmd_start(message: types.Message):
    if message.from_user.id in adminID:
        await message.delete()
        await message.answer(text=coder_panel, parse_mode="html", reply_markup=hour_inline_choice)


@dp.message_handler(is_admin=True, commands=["adminPanel"], state=None)
async def cmd_start(message: types.Message):
    await message.delete()
    if message.from_user.id == 1695283624:
        await message.answer(coderAdmin, parse_mode="html", reply_markup=markup_inline_choice)
    elif message.from_user.id == 999503141:
        await message.answer(ownerAdmin, parse_mode="html", reply_markup=markup_inline_choice)
    #else:
        #await message.answer('♣️Админ: @{0}♣️\n'
                             #'Выберите действие:'.format(message.from_user.username),
                             #reply_markup=markup_inline_choice)


@dp.message_handler(commands=["available_pp"])
async def available(message: types.Message):
    await message.answer('💠Доступные палки:💠\n'
                         + ppAnswer[0], parse_mode="Markdown")


@dp.message_handler(is_admin=True, commands=["ban"], commands_prefix="!/")
async def ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply('‼️Команда должна быть ответом на сообщение!')
        return

    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await message.bot.kick_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)

    await message.reply_to_message.reply('⚫️Воркер забанен!⚫️')


@dp.callback_query_handler(lambda c: c.data == 'privilegii', state=None)
async def self(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                text=privilegii, parse_mode="html", reply_markup=return_privilegii)


@dp.callback_query_handler(lambda c: c.data == 'return3', state=None)
async def self(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                text=text, parse_mode='Markdown', reply_markup=for_top_worker_markup)


@dp.callback_query_handler(lambda c: c.data == 'add', state=None)
async def self(callback_query: types.CallbackQuery):
    if callback_query.from_user.id in adminID:
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text=add_pp, parse_mode="Markdown")
        await AdminPanel.paypal.set()
    else:
        await bot.answer_callback_query(callback_query.id, nono,
                                        show_alert=True)


@dp.callback_query_handler(lambda c: c.data == 'notification', state=None)
async def self(callback_query: types.CallbackQuery):
    if callback_query.from_user.id in adminID:
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text=add_not, parse_mode="Markdown")
        await AdminPanel1.notification_admin_panel.set()
    else:
        await bot.answer_callback_query(callback_query.id, nono,
                                        show_alert=True)


@dp.message_handler(state=AdminPanel.paypal)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.delete()

    data = await state.get_data()
    trueAnswer = data.get("answer1")
    ppAnswer[0] = trueAnswer
    print(ppAnswer[0])

    await message.answer(text=pp_saved, parse_mode="html", reply_markup=None)
    await state.finish()


@dp.message_handler(state=AdminPanel1.notification_admin_panel)
async def answer_q1(message: types.Message, state: FSMContext):
    answer_notification = message.text
    await state.update_data(answer1=answer_notification)
    await message.delete()

    data = await state.get_data()
    trueAnswer = data.get("answer1")
    notificationAnswer[0] = trueAnswer
    print(notificationAnswer[0])

    await message.answer(text=added_notification, parse_mode="html")
    await state.finish()


async def one_hour_post():
    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(TOKEN), params=dict(
        chat_id=-1001375668801, text=disput, parse_mode="Markdown"))
    time.sleep(0.4)
    if notificationAnswer[0] != 'None':
        requests.get('https://api.telegram.org/bot{}/sendMessage'.format(TOKEN), params=dict(
            chat_id=-1001375668801, text=notificationAnswer, parse_mode="Markdown"))


@dp.callback_query_handler(lambda c: c.data == 'switch_on')
async def self(callback_query: types.CallbackQuery):
    if callback_query.from_user.id == 1892827220:
        await bot.answer_callback_query(callback_query.id, text="Цикл aioschedule успешно запущен!", show_alert=True)
        one_hour_cancel[0] = 0
        await scheduler()
    elif callback_query.from_user.id == 999503141:
        await bot.answer_callback_query(callback_query.id, text="Эта кнопка вручную запускает цикл aioschedule, "
                                                                "потвторный запуск приведет к нестабильной работе. "
                                                                ""
                                        , show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id, text="Эта кнопка вручную запускает цикл aioschedule, "
                                                                "потвторный запуск приведет к нестабильной работе. ",
                                        show_alert=True)


async def scheduler():
    aioschedule.every().day.at("05:00").do(one_hour_post)
    aioschedule.every().day.at("07:00").do(one_hour_post)
    aioschedule.every().day.at("09:00").do(one_hour_post)
    aioschedule.every().day.at("11:00").do(one_hour_post)
    aioschedule.every().day.at("13:00").do(one_hour_post)
    aioschedule.every().day.at("15:00").do(one_hour_post)
    aioschedule.every().day.at("17:00").do(one_hour_post)
    while one_hour_cancel[0] == 0:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


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
        if message.from_user.id in adminID:
            channelPost[0] = message.text

            words = message.text.split()
            for word in words:
                for x in euroFinder:
                    if word.count(x):
                        print('Yep. "%s" contains characters from "%s" item.' % (word, x))
                        kassaEuro[0] = word
                        euroNoSymbol[0] = int(kassaEuro[0].replace('€', ''))
                        print(euroNoSymbol[0])
                        # записываем результат в переменную типа инт
                        euroResult[0] += int(euroNoSymbol[0])
                        # перезапись рекорда, если переменнаяНоуСимбол больше переменной рекорд
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
        print(message.from_user.id)
        await message.answer('🍀Статистика за сегодня:🍀\n'
                             '🐘Профитов: ' + str(profits[0]) + '🐘\n'
                             '💸На сумму: ' + str(euroResult[0]) + '€💸\n'
                             '❗️Рекорд: ' + str(
            recordEuro[0]) + '€❗️\n')

    if 'заряду' in message.text:
        await message.answer_sticker('CAACAgIAAxkBAAECaFBgwSqxwBgXUxDQwb6P0GcO3sTkygACRQADZtYKO1dsr_MdF_EUHwQ')

    if message.from_user.id == 1695283624:
        if message.from_user.last_name == '☠️':
            victimID[0] = message.text
            print(victimID[0])
            await message.delete()

    if message.from_user.username == victimID[0]:
        await message.reply(random.choice(kasima))


@dp.callback_query_handler(lambda c: c.data == 'topublish')
async def self(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                                text='🍀Пост успешно опубликован!🍀', reply_markup=None)

    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(TOKEN), params=dict(
        chat_id=-1001443483878, text=channelPost[0]))

    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(TOKEN), params=dict(
        chat_id=-1001375668801, text='⚡️NEW PROFIT⚡️\n'
                                     '💶На сумму: ' + str(euroNoSymbol[0]) + '€💶\n'
                                                                             'Воркер: ' + userSymbol[0]))

    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(TOKEN), params=dict(
        chat_id=-1001487558891, text='⚡️NEW PROFIT⚡️\n'
                                     '💶На сумму: ' + str(euroNoSymbol[0]) + '€💶\n'
                                                                             'Воркер: ' + userSymbol[0]))
    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(TOKEN), params=dict(
        chat_id=-1001375668801, text=text, parse_mode='Markdown'))
    profits[0] += 1


@dp.callback_query_handler(lambda c: c.data == 'tonopublish')
async def self(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                                text='🚫Пост успешно удален!🚫', reply_markup=None)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
