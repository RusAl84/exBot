import telebot;

bot = telebot.TeleBot('5982175377:AAGn4Gkx9ONHMckazUG1pXqh-a0UJuNkI88');


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    name = bot.get_me()
    with open("log.txt", "a", encoding="utf8") as file:
        file.write(f"{name} {message.from_user.id}  {str(message.text)} \n")
    if str(message.text).lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif str(message.text).lower() == "/help":
        bot.send_message(message.from_user.id, "Здесь можно написать команду. Например напиши: привет!")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)