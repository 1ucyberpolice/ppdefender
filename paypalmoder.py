import asyncio
import io
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
    'долбаеб',
    'что за хуйню ты несешь...',
    'бред',
    'съебись от сюда нахуй',
    'школьник ебанный',
    'из нас двоих ботом кажешься ты',
    'не пиши сюда больше пж'
]
victimID = [
    '1'
]

addedpp = """_Палки в процессе добавления,
ожидайте админов❕️_
"""
added_notification = """
𝐃𝐄𝐅𝐄𝐍𝐃𝐄𝐑🐇 -v 3.1
<i>Данные сохранены!🕰</i>
[<a href="https://t.me/joinchat/Dw6y1ndupHc5YjEy">&#8204;.back</a>] - Вернуться
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
notificationAnswer = ['None']

one_hour_cancel = [0]

publish_post_markup = types.InlineKeyboardMarkup()
topublish = types.InlineKeyboardButton('✅', callback_data='topublish')
tonopublish = types.InlineKeyboardButton('🚫', callback_data='tonopublish')
publish_post_markup.add(topublish, tonopublish)

markup_inline_choice = types.InlineKeyboardMarkup()
addPP = types.InlineKeyboardButton('add PP📨', callback_data='add')
delete_PP = types.InlineKeyboardButton('del PP', callback_data='delete_paypal')
addNotiication = types.InlineKeyboardButton('adt📩', callback_data='notification')
markup_inline_choice.add(addPP, delete_PP)

paypal_command = types.InlineKeyboardMarkup()
equip = types.InlineKeyboardButton('Взять📥', callback_data='equip_paypal')
paypal_command.add(equip)

new_system_manual = types.InlineKeyboardMarkup()
man = types.InlineKeyboardButton('Получить PayPal', url='https://telegra.ph/%F0%9D%90%8F%F0%9D%90%9A%F0%9D%90%B2%F0%9D%90%8F%F0%9D%90%9A%F0%9D%90%A5-%F0%9D%90%84%F0%9D%90%A6%F0%9D%90%A9%F0%9D%90%A2%F0%9D%90%AB%F0%9D%90%9E-Novaya-sistema-07-19')
new_system_manual.add(man)

paypal_profit = types.InlineKeyboardMarkup()
profit = types.InlineKeyboardButton('Profit📩', callback_data='profit')
paypal_profit.add(profit)

hour_inline_choice = types.InlineKeyboardMarkup()
switch_on = types.InlineKeyboardButton('aio', callback_data='switch_on')
safe_mode = types.InlineKeyboardButton('SF💀', callback_data='safe_mode')
hour_inline_choice.add(switch_on, safe_mode)

payment_markup = types.InlineKeyboardMarkup()
paid_out = types.InlineKeyboardButton('paid out', callback_data='paid_out')
no_paid_out = types.InlineKeyboardButton('not paid', callback_data='no_paid_out')
payment_markup.add(paid_out, no_paid_out)

markup_manuals = types.InlineKeyboardMarkup()
manual = types.InlineKeyboardButton('🎓Мануалы🎓', callback_data='manual')
markup_manuals.add(manual)

markup_close = types.InlineKeyboardMarkup()
close = types.InlineKeyboardButton('✖️', callback_data='close')
markup_close.add(close)

markup_close1 = types.InlineKeyboardMarkup()
close = types.InlineKeyboardButton('✖️', callback_data='close1')
markup_close1.add(close)

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
🍀В проекте новый участник!🍀       
Профиль: @{0}

_❕️Вся информация в закрепленных 
сообщениях._

🔫Хорошего дня и удачного скама! """
add_pp = """
𝐃𝐄𝐅𝐄𝐍𝐃𝐄𝐑🐇 -v 3.1
_Введите доступные
PayPal❕️_
"""
pp_saved = """
𝐃𝐄𝐅𝐄𝐍𝐃𝐄𝐑🐇 -v 3.1
<i>PayPal сохранены❕️</i>
/available_pp
[<a href="https://t.me/joinchat/Dw6y1ndupHc5YjEy">&#8204;.back</a>] - Вернуться
"""
nono = """
Тебе сюда нельзя, долбаеб любопытный"""
add_not = """
𝐃𝐄𝐅𝐄𝐍𝐃𝐄𝐑🐇 -v 3.1
_Введите текст 
уведомления❕️_
"""
privilegii = """
⚡️𝐏𝐚𝐲𝐏𝐚𝐥 𝐄𝐦𝐩𝐢𝐫𝐞⚡️
Привилегии топ-воркерам:
   <i>- Ставка 60%,
     Личный парсер,
     Специальные
     возможности</i>
"""

adminID = [1695283624, 999503141, 1086861029]
me_bayer = [1695283624, 999503141]
photo_alive = [1]
alive_message = [1]

notificationStatus = ['__Stop__']


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


@dp.message_handler(is_admin=True, commands=["adm"], commands_prefix="./",state=None)
async def cmd_start(message: types.Message):
    await message.delete()
    if message.from_user.id == 1695283624:
        photo_id = await bot.send_photo(message.chat.id, 'https://i.imgur.com/BORpJFa.jpg')
        photo_alive[0] = photo_id.message_id

    elif message.from_user.id == 999503141:
        photo_id = await bot.send_photo(message.chat.id,'https://i.imgur.com/XDGN51K.jpg')
        photo_alive[0] = photo_id.message_id

    elif message.from_user.id == 1086861029:
        photo_id = await bot.send_photo(message.chat.id,'https://i.imgur.com/ZMgD4VD.jpg')
        photo_alive[0] = photo_id.message_id

    msg = await message.answer(text='𝐃𝐄𝐅𝐄𝐍𝐃𝐄𝐑🐇 -v 3.1\n'
                              '╚ 𝐏𝐚𝐲𝐏𝐚𝐥 𝐄𝐦𝐩𝐢𝐫𝐞⚡️\n'
                                  '<i>Admin</i>: @{0}\n'
                                  '[<a href="https://t.me/joinchat/Dw6y1ndupHc5YjEy">&#8204;.u</a>] - '
                                  '<i>Additional Set</i>\n'
                              '[<a href="https://t.me/joinchat/Dw6y1ndupHc5YjEy">&#8204;.exit</a>] - '
                              '<i>Close</i>'
                         .format(message.from_user.username),
                             parse_mode="html", disable_web_page_preview=True, reply_markup=markup_inline_choice)
    alive_message[0] = msg.message_id


@dp.message_handler(commands=["back"], commands_prefix="./")
async def available(message: types.Message):
    await message.delete()
    await bot.edit_message_text(chat_id=message.chat.id, message_id=alive_message[0], text='𝐃𝐄𝐅𝐄𝐍𝐃𝐄𝐑🐇 -v 3.1\n'
                              '╚ 𝐏𝐚𝐲𝐏𝐚𝐥 𝐄𝐦𝐩𝐢𝐫𝐞⚡️\n'
                                  '<i>Admin</i>: @{0}\n'
                                  '[<a href="https://t.me/joinchat/Dw6y1ndupHc5YjEy">&#8204;.u</a>] - '
                                  '<i>Additional Set</i>\n'
                              '[<a href="https://t.me/joinchat/Dw6y1ndupHc5YjEy">&#8204;.exit</a>] - '
                              '<i>Close</i>'
                         .format(message.from_user.username),
                             parse_mode="html", disable_web_page_preview=True, reply_markup=markup_inline_choice)


@dp.message_handler(commands=["exit"], commands_prefix="./")
async def available(message: types.Message):
    await message.delete()
    await bot.delete_message(chat_id=message.chat.id, message_id=photo_alive[0])
    await bot.delete_message(chat_id=message.chat.id, message_id=alive_message[0])


@dp.message_handler(commands=["u"], commands_prefix="./")
async def available(message: types.Message):
    await message.delete()

    safe_mode = '<i>Off</i>'

    notification_status = '__Stop__'
    if notificationStatus[0] == '__Run__':
        notification_status = '<i>Run</i>'
    else:
        notification_status = '<i>Stop</i>'

    adt_status = 'Empty'
    if notificationAnswer[0] == 'None':
        adt_status = '<i>Empty</i>'
    else:
        adt_status = '<i>Full</i>'

    await bot.edit_message_text(chat_id=message.chat.id, message_id=alive_message[0],
                                text='𝐃𝐄𝐅𝐄𝐍𝐃𝐄𝐑🐇 -v 3.1\n'
                                '-id: {1}'.format(message.from_user.id, message.chat.id)+'\n'
                                '╔SafeMode: '+ safe_mode + '\n'
                                '╠Aio: ' + notification_status + '\n'
                                '╚adt📩: ' + adt_status + '\n'
                                '[<a href="https://t.me/joinchat/Dw6y1ndupHc5YjEy">&#8204;.tools</a>] - '
                                  '<i>Other</i>\n', parse_mode='html'
                                ,reply_markup=hour_inline_choice)


@dp.message_handler(commands=["available_pp"])
async def available(message: types.Message):
    with open('available_pp.txt') as f:
        line_count = 0
        for line in f:
            line_count += 1
    await message.answer('Работаем по новой системе!\n'
                         '\n'
                         '💠Доступных PayPal: {0}💠\n'
                         '\n'
                         '<i>📚Подробная информация\n'
                         'в мануале ниже.</i>'.format(line_count), parse_mode='html', reply_markup=new_system_manual)


@dp.message_handler(is_admin=True, commands=["ban"], commands_prefix="!/")
async def ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply('‼️Команда должна быть ответом на сообщение!')
        return

    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await message.bot.kick_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)

    await message.reply_to_message.reply('️Воркер забанен!')


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

    id_file = open("available_pp.txt", "a+")
    id_file.write(str(ppAnswer[0]) + '\n')
    id_file.close()

    await bot.edit_message_text(chat_id=message.chat.id, message_id=alive_message[0],
                                text=pp_saved, parse_mode="html", reply_markup=markup_close)
    await state.finish()


@dp.message_handler(state=AdminPanel1.notification_admin_panel)
async def answer_q1(message: types.Message, state: FSMContext):
    answer_notification = message.text
    await state.update_data(answer1=answer_notification)
    await message.delete()

    data = await state.get_data()
    trueAnswer = data.get("answer1")
    notificationAnswer[0] = trueAnswer

    await bot.edit_message_text(chat_id=message.chat.id, message_id=alive_message[0],
                                text=added_notification, parse_mode="html", reply_markup=markup_close)
    await state.finish()


async def one_hour_post():
    if notificationAnswer[0] != 'None':
        requests.get('https://api.telegram.org/bot{}/sendMessage'.format(TOKEN), params=dict(
            chat_id=-1001375668801, text=notificationAnswer[0], parse_mode="Markdown"))


@dp.callback_query_handler(lambda c: c.data == 'switch_on')
async def self(callback_query: types.CallbackQuery):
    if callback_query.from_user.id in adminID:
        await bot.answer_callback_query(callback_query.id, text="Цикл aioschedule успешно запущен!", show_alert=True)
        one_hour_cancel[0] = 0
        notificationStatus[0] = '__Run__'

        safe_mode = '<i>Off</i>'

        notification_status = '__Stop__'
        if notificationStatus[0] == '__Run__':
            notification_status = '<i>Run</i>'
        else:
            notification_status = '<i>Stop</i>'

        adt_status = 'Empty'
        if notificationAnswer[0] == 'None':
            adt_status = '<i>Empty</i>'
        else:
            adt_status = '<i>Full</i>'

        chat_id = callback_query.message.chat.id

        await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                                    text='𝐃𝐄𝐅𝐄𝐍𝐃𝐄𝐑🐇 -v 3.1\n'
                                          '-id: ' + str(chat_id) + '\n'
                                          '╔SafeMode: ' + safe_mode + '\n'
                                          '╠Aio: ' + notification_status + '\n'
                                          '╚adt📩: ' + adt_status + '\n'
                                          '[<a href="https://t.me/joinchat/Dw6y1ndupHc5YjEy">&#8204;.tools</a>] - '
                                           '<i>Other</i>\n', parse_mode='html', reply_markup=hour_inline_choice)
        await scheduler()
    else:
        await bot.answer_callback_query(callback_query.id, text="Эта кнопка вручную запускает цикл aioschedule, "
                                                                "потвторный запуск приведет к нестабильной работе. ",
                                        show_alert=True)


@dp.message_handler(is_admin=True, commands=["file"], commands_prefix="./")
async def available(message: types.Message):
    await message.delete()
    pp_file = open("available_pp.txt", "a+")

    with io.open('available_pp.txt') as file:
        info = file.read().rstrip('\n')

    pp_file.close()
    await bot.send_message(message.chat.id, text="📑Содержимое файла:\n"+ info, reply_markup=markup_close1)


@dp.message_handler(commands=["paypal"], commands_prefix="./")
async def available(message: types.Message):
    import random
    line = random.choice(open('available_pp.txt').readlines())

    if message.chat.type == types.ChatType.PRIVATE:
        await bot.send_photo(message.chat.id, 'https://i.imgur.com/O0K6MlN.jpg')
        await bot.send_message(message.chat.id, text='𝐃𝐄𝐅𝐄𝐍𝐃𝐄𝐑🐇 -v 3.1 \n'
                                                     'Доступный PayPal:\n '
                                                     + line,
                               parse_mode='html', reply_markup=paypal_command)


@dp.callback_query_handler(lambda c: c.data == 'equip_paypal')
async def self(callback_query: types.CallbackQuery):
    msg = callback_query.message.text
    paypal = msg.split(" ")
    thisPayPal = 'False'

    for i in paypal:
        if i.count('@'):
            pp = i

    with io.open('available_pp.txt') as file:
        for line in file:
            if pp in line:
                thisPayPal = 'True'

    if thisPayPal == 'True':
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text='𝐃𝐄𝐅𝐄𝐍𝐃𝐄𝐑🐇 -v 3.1 \n'
                                         '<i>Ты</i>: @{0}\n'
                                         '<i>Твой активный PayPal</i>: \n'
                                    .format(callback_query.message.chat.id) + pp, parse_mode="html"
                                    , reply_markup=paypal_profit)
        for id in me_bayer:
            await bot.send_message(id, text='<i>Воркер:</i> @{0}\n'
                                            '<i>Взял PayPal:</i> '.format(
                callback_query.message.chat.username) + pp,
                                   parse_mode="html")

    elif thisPayPal == 'False':
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="𝐃𝐄𝐅𝐄𝐍𝐃𝐄𝐑🐇 -v 3.1 \n"
                                         "<i>Кто-то успел забрать\n"
                                         "PayPal раньше тебя!</i>", parse_mode="html", reply_markup=markup_close1)

    with open("available_pp.txt", "r") as f:
        lines = f.readlines()
    with open("available_pp.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != pp:
                f.write(line)


@dp.callback_query_handler(lambda c: c.data == 'delete_paypal')
async def self(callback_query: types.CallbackQuery):
    if callback_query.from_user.id in adminID:
        with open('available_pp.txt', 'w'):
            pass
        await bot.answer_callback_query(callback_query.id, text='Данные успешно стерты!',
                                        show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id, nono,
                                        show_alert=True)


@dp.callback_query_handler(lambda c: c.data == 'profit')
async def self(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                                text='𝐃𝐄𝐅𝐄𝐍𝐃𝐄𝐑🐇 -v 3.1 \n'
                                     '<i>Ты</i>: @{0}\n'
                                     '<i>Администрация оповещена о\n'
                                     'твоем профите!</i>'.format(callback_query.message.chat.id), parse_mode="html"
                                , reply_markup=None)
    for id in me_bayer:
        await bot.send_message(id, text='<i>📩Воркер:</i> @{0}\n'
                                        '<i>Уведомляет об успешном профите!</i>'
                                 .format(callback_query.message.chat.username),
                               parse_mode="html")


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


@dp.callback_query_handler(lambda c: c.data == 'close')
async def self(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=photo_alive[0])
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=alive_message[0])


@dp.callback_query_handler(lambda c: c.data == 'close1')
async def self(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)


@dp.callback_query_handler(lambda c: c.data == 'manual')
async def self(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                                text='🎓Выберите мануал:🎓', reply_markup=manual_markup)


@dp.callback_query_handler(lambda c: c.data == 'return')
async def self(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                                text=text, parse_mode='Markdown', reply_markup=markup_manuals)


@dp.message_handler(regexp='❕')
async def personal(message: types.Message):
    if message.from_user.id == 1892827220:
        recordEuro[0] = message.text
        print(recordEuro[0])
        await message.delete()


@dp.message_handler()
async def cassa(message: types.Message):
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
        print(message.from_user.id)
        await message.answer('💼Статистика за сегодня:💼\n'
                             '🐑<i>Профитов</i>: ' + str(profits[0]) + '\n'
                             '💸<i>На сумму</i>: ' + str(euroResult[0]) + '€💸\n'
                             '❕<i>Рекорд</i>: ' + str(
            recordEuro[0]) + '€\n', parse_mode='html')

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
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
