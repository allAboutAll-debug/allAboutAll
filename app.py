import telebot
import requests

bot = telebot.TeleBot('913705823:AAFYXv4SlObaP4J0r8ni3Je_Fc9d6t2mQfo')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать! Это система подписок.')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '/menu':
        # url = 'http://aboutbetweenall.000webhostapp.com/api/user/read.php'
        # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        # result = requests.get(url, headers=headers)
        # print(result.content.decode())

        url = 'http://aboutbetweenall.000webhostapp.com/api/user/create.php'
        payload = {
            'telegram_id': message.from_user.id,
            'first_name': message.from_user.first_name
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'Content-Type':'application/json',
            "Accept": "application/json"
        }
        s = requests.Session()
        s.post(url, json=payload, headers=headers)

        text = 'Чтобы начать получать уведомления нужно сделать подписку. Здесь же вы можете управлять существующими подписками. (Потребуется подтвердить переход по ссылке)'
        keyboard = telebot.types.InlineKeyboardMarkup()
        key_create = telebot.types.InlineKeyboardButton(text='Добавить подписку', callback_data='create', url= 'https://google.com')
        keyboard.add(key_create)
        key_manage = telebot.types.InlineKeyboardButton(text='Управление подписками', callback_data='manage', url= 'https://google.com')
        keyboard.add(key_manage)
        bot.send_message(message.from_user.id, text=text, reply_markup=keyboard)

bot.polling()
