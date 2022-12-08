#!/usr/bin/env python3

# SVTV daily telegram-bot
# @svtvnews_daily_bot
# t.me/svtvnews_daily_bot

from telebot import TeleBot, types


token_file = open('/Users/narek/.pass/.svtvnews_bot.token')
token = token_file.read().rstrip('\n')
bot = TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    output = "Привет! Раз в день я буду пересылать тебе посты из @svtvnews "
    output += "резюмирующие события, произошедшие за день.\n\n"
    output += "Hello! Once a day I will forward you messages from @svtvnews "
    output += "summarizing the main events of the day."
    bot.send_message(
        message.chat.id,
        output,
        parse_mode='html',
    )


@bot.message_handler(commands=['help'])
def help(message):
    start(message)


#@bot.message_handler(func=lambda message: message.forward_from_chat, content_types=["text", "photo", "video"])
@bot.message_handler(content_types=["text"])
def text(message):
    output = message.text
    bot.send_message(
        message.chat.id,
        output,
        parse_mode='html',
    )


@bot.message_handler(content_types=["photo"])
def photo(message):
    bot.forward_message(
        message.chat.id, 
        message_id=message.id,
        from_chat_id=message.chat.id
    )

bot.polling(none_stop=True)
