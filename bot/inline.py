from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot_api import get_category_list, questionnaire_list


def category_inline():
    """
        BU KATEGORIYALARNI LIST BUTTON QILIB CHIQARADI
    """
    markup = InlineKeyboardMarkup(row_width=1)
    for i in get_category_list():
        btn = InlineKeyboardButton(i['title'], callback_data=f"category|{i['pk']}")
        markup.add(btn)
    return markup


def questionnaire_inline(category_id):
    """
        BU QUESIONLARNI BUTTON QILIB CHIQARDI
    """
    markup = InlineKeyboardMarkup(row_width=1)
    for i in questionnaire_list(category_id):
        btn = InlineKeyboardButton(i['title'], callback_data=f"questionnaire|{category_id}")
        markup.add(btn)
    return markup
