#!/usr/bin/env python3


from telebot import TeleBot, types


token_file = open('/Users/narek/.pass/.svtv_bot.token')
token = token_file.read().rstrip('\n')
bot = TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    output = "Привет! Раз в день я буду пересылать тебе посты из @svtv_news "
    output += "резюмирующие события, произошедшие за день.\n\n"
    output += "Hello! Once a day I will forward you messages from @svtv_news "
    output += "summarizing day's events."

    bot.send_message(
        message.chat.id,
        output,
        parse_mode='html',
    )


@bot.message_handler(commands=['help'])
def help(message):
    start(message)


@bot.message_handler(content_types=['text'])
def mess(message):
    output = message.text
    bot.send_message(
        message.chat.id,
        output,
        parse_mode='html',
    )
    print("text", output)


@bot.message_handler(func=lambda message: message.forward_from_chat, content_types=["text", "photo", "video"])
def posts_from_channels(message):
    output = message
    bot.send_message(
        message.chat.id,
        output,
        parse_mode='html',
    )
    print('frwd', message.text)


bot.polling(none_stop=True)
