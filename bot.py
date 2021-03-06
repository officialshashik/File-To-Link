import telebot
import time
import pyshorteners
import os

bot = telebot.TeleBot(token=os.getenv('TG_BOT_TOKEN'))

def short(url):
    return pyshorteners.Shortener().tinyurl.short(url)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '๐๐๐ฒ๐! ๐ ๐๐ฆ ๐ ๐ฐ๐ป ๐๐๐๐๐๐ข๐ ๐ต ๐๐ ๐ป๐ธ๐ฝ๐บ ๐ฑ๐พ๐ ๐๐ซ๐๐๐ญ๐๐ ๐๐ฒ <a href="https://t.me/apealkuppiya">แฉ/ใ แฆแแญแญแแฉแฉแตแดน ๐ฃ</a>.๐๐๐ง๐ ๐ฆ๐ ๐๐ง๐ฒ ๐๐ข๐ฅ๐ (๐๐ข๐๐๐จ, ๐๐ฎ๐๐ข๐จ, ๐๐ก๐จ๐ญ๐จ, ๐๐จ๐๐ฎ๐ฆ๐๐ง๐ญ)๐ฃ๐ป')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, '๐๐๐ง๐ ๐ฆ๐ ๐๐ง๐ฒ ๐ญ๐ฒ๐ฉ๐ ๐จ๐ ๐ ๐๐ข๐ฅ๐ & ๐ ๐ฐ๐ข๐ฅ๐ฅ ๐ฌ๐๐ง๐ ๐ฒ๐จ๐ฎ ๐ญ๐ก๐ ๐ฌ๐ก๐จ๐ซ๐ญ๐๐ง ๐ฅ๐ข๐ง๐ค ๐จ๐ ๐ข๐ญ ๐๐ปโโ๏ธ๐')    

@bot.message_handler(content_types=['photo', 'video', 'audio', 'document'])
def file_sent(message):
    try:
        bot.send_message(message.chat.id, short(bot.get_file_url(message.document.file_id)))
    except AttributeError:
        try:
            bot.send_message(message.chat.id, short(bot.get_file_url(message.photo[0].file_id)))
        except AttributeError:
            try:
                bot.send_message(message.chat.id, short(bot.get_file_url(message.audio.file_id)))
            except AttributeError:
                try:
                    bot.send_message(message.chat.id, short(bot.get_file_url(message.video.file_id)))
                except AttributeError:
                    pass


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)

