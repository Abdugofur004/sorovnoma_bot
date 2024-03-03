from bot_api import create_user, get_category, get_user, questionnaire, get_questionnaire_user, create_user_question, \
    get_channel
from default import send_contact
from inline import category_inline, questionnaire_inline, channel_inline
from telebot import TeleBot, custom_filters
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
from telebot.types import CallbackQuery, Message


class UserState(StatesGroup):
    user = State()


state_storage = StateMemoryStorage()
TOKEN = "5838680373:AAG5tgPeIB4_Zw9YAjclIltETwQOVQEuTtA"
bot = TeleBot(token=TOKEN, parse_mode="html")
bot.add_custom_filter(custom_filter=custom_filters.StateFilter(bot))


@bot.message_handler(commands=["start"])
def start(message: Message):
    chat_id = message.chat.id
    for i in get_channel():
        # print(i['channel_id'])
        channel_id = int(i['channel_id'])
        check_sub_channel = bot.get_chat_member(chat_id=channel_id, user_id=chat_id)

    if check_sub_channel in ['mumber', 'creator', 'administrator']:
        try:
            if len(get_user(chat_id)) > 0:
                bot.send_message(chat_id, "Овоз бериш учун қуйидаги категориялардан бирини танланг 👇", reply_markup=category_inline())
            else:
                msg = bot.send_message(
                    chat_id,
                    'Ботдан фойдаланиш учун пастдаги "Рақамни юбориш" тугмасини босинг 👇',
                    reply_markup=send_contact(),
                )
                bot.register_next_step_handler(msg, save_contact)
        except Exception as e:
            bot.send_message(chat_id, "Бот да хандайдир хатолик бор ботни қайта ишга тушуринг. /start")
    elif check_sub_channel != 'left':
        bot.send_message(chat_id, "Овоз бериш учун олдин каналларга обуна бўлинг", reply_markup=channel_inline())


@bot.callback_query_handler(func=lambda call: call.data == 'check')
def check(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.message.from_user.id
    bot.delete_message(chat_id, message_id=call.message.message_id)
    for i in get_channel():
        channel_id = int(i['channel_id'])
    check_sub_channel = bot.get_chat_member(chat_id=channel_id, user_id=call.message.from_user.id).status

    if check_sub_channel == 'member' or check_sub_channel == 'creator' or check_sub_channel == 'administrator':
        if len(get_user(chat_id)) > 0:
            bot.send_message(chat_id, "Овоз бериш учун қуйидаги категориялардан бирини танланг 👇",
                             reply_markup=category_inline())
        else:
            msg = bot.send_message(
                chat_id,
                'Ботдан фойдаланиш учун пастдаги "Рақамни юбориш" тугмасини босинг 👇',
                reply_markup=send_contact(),
            )
            bot.register_next_step_handler(msg, save_contact)
    elif check_sub_channel != 'left':
        bot.send_message(chat_id, "Овоз бериш учун олдин каналларга обуна бўлинг❗️", reply_markup=channel_inline())


def save_contact(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    username = message.from_user.username
    contact = message.contact.phone_number
    try:
        create_user(
            chat_id=chat_id, from_user_id=from_user_id, username=username, phone=contact
        )
        bot.send_message(chat_id, "Овоз бериш учун қуйидаги категориялардан бирини танланг 👇",
                         reply_markup=category_inline())
    except Exception as e:
        bot.send_message(chat_id, "Бот да хандайдир хатолик бор ботни қайта ишга тушуринг./start")


@bot.callback_query_handler(func=lambda call: "category" in call.data)
def category(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    try:
        category_id = int(call.data.split("|")[1])
        category = get_category(category_id)
        bot.delete_message(chat_id, call.message.message_id)

        bot.set_state(chat_id, UserState.user, from_user_id)
        with bot.retrieve_data(from_user_id, chat_id) as data:
            data["card"] = {
                "category_id": category_id,
                "category_title": category["title"],
                "category_slug": category["slug"],
                "sektor": category["state"],
            }
            bot.send_message(
                chat_id,
                f"<b>'Энг {data['card']['category_title']}' танловига старт берилди</b>",
                reply_markup=questionnaire_inline(category_id),
            )
    except Exception as e:
        bot.send_message(chat_id, "Бот да хандайдир хатолик бор ботни қайта ишга тушуринг. /start")


@bot.callback_query_handler(func=lambda call: "questionnaire" in call.data)
def questionnaire_get(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id

    try:
        bot.delete_message(chat_id, call.message.message_id)
        questionnaire_id = int(call.data.split("|")[1])
        questionnaire_base_title = questionnaire(questionnaire_id)
        b = get_user(chat_id)
        with bot.retrieve_data(from_user_id, chat_id) as data:
            category_id = data['card']['category_id']
            category_title = data['card']['category_title']
            questionnaire_title = questionnaire_base_title['title']
            sector = data['card']['sektor']['title']
            user_id = b['pk']
            a = get_questionnaire_user(category_id, chat_id)
            if 'detail' in a:
                create_user_question(category_id, user_id, questionnaire_id)
                text = f"✅Табриклайман сиз<b>{sector}</b>да <b>{category_title}</b> " \
                       f"бўйича <b>{questionnaire_title}</b>га овоз бердингиз!"
                bot.send_message(chat_id, text)
            else:
                text = f"❌Кечирасиз сиз <b>{sector}</b>да <b>{category_title}</b>бўйича " \
                       f"<b>{questionnaire_title}</b>га овоз бергансиз!"
                bot.send_message(chat_id, text)

    except Exception as e:
        bot.send_message(chat_id, "Бот да хандайдир хатолик бор ботни қайта ишга тушуринг. /start")


if __name__ == "__main__":
    bot.polling(none_stop=True)
