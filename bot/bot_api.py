import requests
import json

BASE_URL = 'http://127.0.0.1:8000/api/v1'


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
    post = requests.post(url=url, data={
        'chat_id': chat_id,
        'from_user_id': from_user_id,
        'username': username,
        'phone': phone
    })
    return post


# bu orqali categoriyalar ro'yxatini chiqaradi
def get_category_list():
    """
         BU YERDA CATEORIYALR TO'XATINI ALL QILIB OLYAPMIZ
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
        BU YERDA questionLARNI BUTTON QILIB CHIQARISH UCHUN
    """
    url = f"{BASE_URL}/question/{category_id}/"
    response = requests.get(url=url).text
    data = json.loads(response)
    return data
