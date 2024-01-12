import db

night = False
@bot.message_handler(commands=['kick'])
def kick(message):
    username = ' '.join(message.text.split(' ')[1:])
    usernames = db.get_all_alive()
    if not night:
        if not username in usernames:
            bot.send_message(message.chat.id, 'Такого имени нет')
            return
    voted = db.vote('citizen_vote', username, message.from_user.id)
    if voted:
        bot.send_message(message.chat.id, 'Ваш голос учитан')
        return
    bot.send_message(
        message.chat.id, 'Сейчас ночь вы не можете нткого выгнать')