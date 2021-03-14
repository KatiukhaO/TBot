import telebot

bot = telebot.TeleBot('1652980479:AAHZ4v2Nbi_HiztCeqOVfYxlHamQR-mWIUk')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я Бот. {message.from_user.first_name}, я допоможу тобі вивчити англійську!')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    vocabulary = {'i': 'я',
                  'true': 'правда',
                  'you': 'ти',
                  'food': 'їжа',
                  'cat': 'кіт',
                  'weakly':'слабко',
                  'flow': 'потік',
                  'probably': 'мабуть',
                  'dimension': 'розмірність',
                  'compliant': 'сумісний',
                  'solve': 'рішення',
                  'convert': 'перетворити',
                  'implement': 'впровадити',
                  'relatively': 'відносно',
                  'exist': 'існувати'}

    if message.text.lower() == 'привіт':
        bot.send_message(message.from_user.id, f'Привіт, {message.from_user.first_name}')
    elif message.text.lower() in vocabulary.keys():
        bot.send_message(message.from_user.id, vocabulary[message.text.lower()])
    elif message.text.lower() in vocabulary.values():
        for k, v in vocabulary.items():
            if message.text.lower() == v:
                bot.send_message(message.from_user.id, k)


bot.polling(none_stop=True)

if __name__ == '__main__':
    bot.polling(none_stop=True)
