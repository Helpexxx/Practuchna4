import telebot

token='7532661351:AAH7qIRZWG84_t9artsLkDqo82mYdVO5j4A'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ ==  '__main__':
    bot.polling()