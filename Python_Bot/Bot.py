from telebot import TeleBot,types
from datetime import datetime
from RequestLink import Convert,keys
token="1549538704:AAH_1J-2-SxqdoAKXCYvMROjrOewhdR3oJ0"
bot = TeleBot(token=token)
@bot.message_handler(commands=['start'])
def start(message):
	bot.reply_to(message, "Howdy, how are you doing?")
@bot.message_handler(commands=['time'])
def time_command(message):
    timenow=datetime.now()
    current_time=timenow.strftime("%H:%M:%S");
    bot.reply_to(message,"Toshkent vaqti bilan soat:"+current_time)
@bot.message_handler(commands=['usd'])
def usd_command(message):
    bot.reply_to(message,text=(f"1 USD ga {Convert('uzs')} uzs to'g'ri keladi"))
@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(message,"How i can help you?")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message,message.text)
bot.polling(none_stop=True)