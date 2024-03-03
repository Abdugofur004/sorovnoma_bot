from bot_api import get_category_list, questionnaire_list, get_channel
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def category_inline():
    """
    BU KATEGORIYALARNI LIST BUTTON QILIB CHIQARADI
    """
    markup = InlineKeyboardMarkup(row_width=1)
    for i in get_category_list():
        btn = InlineKeyboardButton(i["title"], callback_data=f"category|{i['pk']}")
        markup.add(btn)
    return markup


def questionnaire_inline(category_id):
    """
    BU QUESIONLARNI BUTTON QILIB CHIQARDI
    """
    markup = InlineKeyboardMarkup(row_width=1)
    for i in questionnaire_list(category_id):
        btn = InlineKeyboardButton(
            i["title"], callback_data=f"questionnaire|{i['pk']}"
        )
        markup.add(btn)
    return markup


def channel_inline():
    markup = InlineKeyboardMarkup(row_width=1)
    a = 0
    for i in get_channel():
        a += 1
        btn = InlineKeyboardButton(

            f"{a}-kanal", url=f"{i['channel_url']}"
        )
        markup.add(btn)
    check = InlineKeyboardButton("✅Obunani tasdiqlash", callback_data="check")
    markup.add(check)
    return markup
