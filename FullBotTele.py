import telebot
# isi token bot 
bot_token = [TOKEN_BOT]

# Baris 6 isi dengan id kontak yang mau di target
id_kontak_tertentu = [...] 
# untuk yang ini bisa di matiin kalau mau 1 kontak ar
id_kontak_tertentu1 = [...] 
# isi id chat pribadi
id_anda = [...]

bot = telebot.TeleBot(bot_token)

@bot.message_handler(func=lambda message: message.from_user.id == int(id_anda))
def handle_message(message):
    message_text = message.text
    bot.send_message(id_kontak_tertentu, message_text)
    bot.send_message(id_kontak_tertentu1, message_text)

bot.polling()
