from telebot import TeleBot
from telebot.types import Message, CallbackQuery
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
from default import send_contact
from inline import category_inline, questionnaire_inline
from bot_api import create_user, get_user, get_category


class UserState(StatesGroup):
    user = State()


state_storage = StateMemoryStorage()
TOKEN = "5838680373:AAG5tgPeIB4_Zw9YAjclIltETwQOVQEuTtA"
bot = TeleBot(token=TOKEN, parse_mode='html')
bot.add_custom_filter(custom_filter=custom_filters.StateFilter(bot))


@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    if len(get_user(chat_id)) > 0:
        bot.send_message(chat_id, 'Ovoz berish', reply_markup=category_inline())
    else:
        msg = bot.send_message(chat_id, "Ботдан фойдаланиш учун пастдаги \"Рақамни юбориш\" тугмасини босинг 👇",
                               reply_markup=send_contact())
        bot.register_next_step_handler(msg, save_contact)


def save_contact(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    username = message.from_user.username
    contact = message.contact.phone_number

    create_user(chat_id=chat_id, from_user_id=from_user_id, username=username, phone=contact)
    bot.send_message(chat_id, 'Ovoz berish', reply_markup=category_inline())


@bot.callback_query_handler(func=lambda call: 'category' in call.data)
def category(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    category_id = int(call.data.split('|')[1])
    category = get_category(category_id)
    print(category)
    bot.delete_message(chat_id, call.message.message_id)

    bot.set_state(chat_id, UserState.user, from_user_id)
    with bot.retrieve_data(from_user_id, chat_id) as data:
        data['card'] = {
            'category_id': category_id,
            'category_title': category['title'],
            'category_slug': category['slug'],
            'sektor': category['state']
        }
        bot.send_message(chat_id, f"<b>'ENG {data['card']['category_title']}' TANLOVINING START BERILDI.</b>",
                         reply_markup=questionnaire_inline(category_id))


#
# @bot.callback_query_handler(func=lambda call: "questionnaire|" in call.data)
# def questionnaire(call: CallbackQuery):
#     chat_id = call.message.chat.id
#     from_user_id = call.from_user.id
#     ques_id = int(call.data.split('|')[1])
#     questionnaire = questionnaire_list(ques_id)
#     print(questionnaire)
#     with bot.retrieve_data(from_user_id, chat_id) as data:
#         # slug = data['card']['slug']
#         # data['card']['questionnaire'] = questionnaire_title['title']
#         # data['card']['chat_id'] = chat_id
#         print(data)


if __name__ == "__main__":
    bot.polling(none_stop=True)
