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
def text(message):
    try:
        output = message.text
        bot.send_message(
            message.chat.id,
            output,
            parse_mode='markdown'
            #parse_mode='html',
        )
        print("text", output)
    except:
        print("error", message)


@bot.message_handler(func=lambda message: message.forward_from_chat, content_types=["text", "photo", "video"])
def posts_from_channels(message):
    try:
        output = message.text
        bot.send_message(
            message.chat.id,
            output,
            parse_mode='markdown'
        )
        print('frwd', outout)
    except:
        print("error", message)


bot.polling(none_stop=True)
