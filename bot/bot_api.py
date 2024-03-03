import json

import requests

BASE_URL = "http://127.0.0.1:8000/api/v1"


# bu userlar
def get_user(chat_id):
    """
    BU USERLARNI TEKSHIRIB OLISH UCHUN
    """
    url = f"{BASE_URL}/users/{chat_id}/"
    response = requests.get(url).text
    data = json.loads(response)
    return data


# bu userlar yaratish
def create_user(chat_id, from_user_id, username, phone):
    """
    BU USERLARNI YARATISH UCHUN
    """
    url = f"{BASE_URL}/users/create/"
    post = requests.post(
        url=url,
        data={
            "chat_id": chat_id,
            "from_user_id": from_user_id,
            "username": username,
            "phone": phone,
        },
    )
    return post


# bu orqali categoriyalar ro'yxatini chiqaradi
def get_category_list():
    """
    BU YERDA CATEORIYALR RO'XATINI ALL QILIB OLYAPMIZ
    """
    url = f"{BASE_URL}/category/"
    response = requests.get(url=url).text
    data = json.loads(response)
    return data


def get_category(category_id):
    """
    BU YERDA categoriyaNI GET QILIB OLIB UNDAGI MALUMOTLARNI SAQLASH OLISH UCHUN
    """
    url = f"{BASE_URL}/category/{category_id}"
    response = requests.get(url=url).text
    data = json.loads(response)
    return data


def questionnaire_list(category_id):
    """
    BU YERDA questionLARNI all BUTTON QILIB CHIQARISH UCHUN
    """
    url = f"{BASE_URL}/question/{category_id}/"
    response = requests.get(url=url).text
    data = json.loads(response)
    return data


def questionnaire(id):
    """
        bu yerda questioni o'zini olamiz
    """
    url = f"{BASE_URL}/questionnaire/{id}"
    response = requests.get(url=url).text
    data = json.loads(response)
    return data


def get_questionnaire_user(category_id, user_id):
    url = f"{BASE_URL}/question-user/{category_id}/{user_id}"
    response = requests.get(url=url).text
    data = json.loads(response)
    return data
    # if 'detail' in data:
    #     return "siz ovoz"


def create_user_question(category_id, user_id, quest_id):
    res = f"{BASE_URL}/question-user/create/"
    a = requests.post(res, data={
        'user': user_id,
        'category': category_id,
        'questionnaire': quest_id,
    })
    return a


def get_channel():
    url = f"{BASE_URL}/channel/"
    response = requests.get(url).text
    data = json.loads(response)
    return data
