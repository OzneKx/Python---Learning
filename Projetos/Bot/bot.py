import telebot # pyTelegramAPI

bot = telebot.Telebot('')


@bot.message_handler(commands=['start'])
def meu_start(message):
  bot.send_message(message.chat.id, 'Oi, estou aqui!')


@bot.message_handler(commands=['open'])
def abre_porta(message):
  bot.send_message(message.chat.id, 'Porta aberta!')


@bot.message_handler(commands=['close'])
def fecha_porta(message):
  bot.send_message(message.chat.id, 'Porta fechada!')


if __name__ == '__main__':
  bot.polling()
