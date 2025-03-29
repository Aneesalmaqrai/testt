import telebot
import requests
from telebot import types
#المطور [@zyad_alalmy]
#قناه المطور [@scr_py]
#تزويرك اللمصدر دليل فشلك
bot = telebot.TeleBot(token="5007211465:AAFY5pjiJALRWrMgc3U1ip3BcgQePFuheas")

@bot.message_handler(commands=["start"])
def start(message):
    key = types.InlineKeyboardMarkup()
    ch = types.InlineKeyboardButton(text="متابعه المطور",url="https://t.me/scr_py")
    key.add(ch)
    bot.send_photo(message.chat.id, "https://t.me/crypto_botw/14", caption=f"مرحبا عزيزي {message.from_user.first_name} في بوت معرفه سعر الدولار مقابل الجنيه المصري",reply_markup=key)

@bot.message_handler(func=lambda message: True)
def get_price(message):
    user = message.text.lower()
    url = "https://open.er-api.com/v6/latest"
    params = {"base": "USD"}
    res = requests.get(url, params=params)
    data = res.json()
    price = data.get("rates").get("EGP")
    if user.strip() == 'usd':
        bot.reply_to(message, f"سعر الدولار مقابل الجنيه هو {price}")

print("Bot Work ☑️")
bot.polling()
