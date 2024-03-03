from telebot.types import KeyboardButton, ReplyKeyboardMarkup


def send_contact():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = KeyboardButton("Рақамни юбориш", request_contact=True)
    markup.add(keyboard)
    return markup
