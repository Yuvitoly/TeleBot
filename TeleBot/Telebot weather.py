# Тelebot для погоды


import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils.config import get_default_config
from telebot import types
owm = OWM("97dcde...3e3ef5")
bot = telebot.TeleBot("5621851805...CrSxDW8")
config_dict = get_default_config()
config_dict['language'] = 'ru'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    row = types.KeyboardButton(" /start ")
    markup.add(row)
    bot.reply_to(message, "Здравствуйте! Введите название города, в котором хотите узнать погоду: ", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def weather_text(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    wind = w.wind()["speed"]
    answer = 'В городе ' + message.text + ' сейчас ' + w.detailed_status + '\n'
    answer += 'Температура воздуха в среднем ' + str(temp) + ' градусов Цельсия' + '\n'
    answer += 'Скорость ветра достигает ' + str(wind) + ' м/c' + '\n'

    if temp < -10:
          answer += "Пи**ц как холодно, одевайся как танк!"
    elif temp < 10:
        answer += 'Холодно, оденься потеплее))'
    elif temp < 17:
        answer += 'Прохладно, лучше оденься)'
    elif temp < 25:
          answer += 'Жарень, хоть в шортах иди))'
    elif temp < 30:
          answer += 'Жарень, напечет, нужно кепка))'
    else:
        answer += 'На улице вроде норм!)'


    bot.send_message(message.chat.id, answer)


if __name__ == "__main__":
    bot.polling(none_stop=True)
