import telebot
import requests

bot = telebot.TeleBot('913705823:AAFYXv4SlObaP4J0r8ni3Je_Fc9d6t2mQfo')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать! Это система подписок.')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '/menu':
        url = 'http://aboutbetweenall.000webhostapp.com/api/user/create.php'
        payload = {
            'telegram_id': message.from_user.id,
            'first_name': message.from_user.first_name
        }
        requests.post(url, json=payload)

        text = 'Чтобы начать получать уведомления нужно сделать подписку. Здесь же вы можете управлять существующими подписками. (Потребуется подтвердить переход по ссылке)'
        keyboard = telebot.types.InlineKeyboardMarkup()
        key_create = telebot.types.InlineKeyboardButton(text='Добавить подписку', callback_data='create', url= 'https://google.com')
        keyboard.add(key_create)
        key_manage = telebot.types.InlineKeyboardButton(text='Управление подписками', callback_data='manage', url= 'http://aboutbetweenall.000webhostapp.com/?t_id=' + str(message.from_user.id))
        keyboard.add(key_manage)
        bot.send_message(message.from_user.id, text=text, reply_markup=keyboard)

bot.polling()
