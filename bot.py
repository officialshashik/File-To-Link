import telebot
import time
import pyshorteners
import os

bot = telebot.TeleBot(token=os.getenv('TG_BOT_TOKEN'))

def short(url):
    return pyshorteners.Shortener().tinyurl.short(url)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '𝐇𝐞𝐲𝐚! 𝐈 𝐚𝐦 𝐚 𝙰𝙻 𝚔𝚞𝚙𝚙𝚒𝚢𝚊 𝙵 𝚝𝚘 𝙻𝙸𝙽𝙺 𝙱𝙾𝚃 𝐜𝐫𝐞𝐚𝐭𝐞𝐝 𝐛𝐲 <a href="https://t.me/apealkuppiya">ᗩ/し ᏦᑌᑭᑭᏆᎩᗩᵀᴹ 🐣</a>.𝐒𝐞𝐧𝐝 𝐦𝐞 𝐚𝐧𝐲 𝐟𝐢𝐥𝐞 (𝐕𝐢𝐝𝐞𝐨, 𝐀𝐮𝐝𝐢𝐨, 𝐏𝐡𝐨𝐭𝐨, 𝐃𝐨𝐜𝐮𝐦𝐞𝐧𝐭)🐣🏻')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, '𝐒𝐞𝐧𝐝 𝐦𝐞 𝐚𝐧𝐲 𝐭𝐲𝐩𝐞 𝐨𝐟 𝐚 𝐟𝐢𝐥𝐞 & 𝐈 𝐰𝐢𝐥𝐥 𝐬𝐞𝐧𝐝 𝐲𝐨𝐮 𝐭𝐡𝐞 𝐬𝐡𝐨𝐫𝐭𝐞𝐧 𝐥𝐢𝐧𝐤 𝐨𝐟 𝐢𝐭 💁🏻‍♂️🎈')    

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

