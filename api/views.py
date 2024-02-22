from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import BotUser, Category, Questionnaire, QuestionnaireUser
from .serializers import BotUserSerializers, CategorySerializers, QuestionnaireSerializers, \
    QuestionnaireUserSerializers


# userlar ro'yxatdan o'tgan yoki o'tmaganligini tekshirish
class UserListAPIView(ListAPIView):
    serializer_class = BotUserSerializers

    def get_queryset(self):
        queryset = BotUser.objects.filter(chat_id=self.kwargs['chat_id'])
        return queryset


# userlar yaratish uchun
class UsersCreateAPIView(CreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializers


# bu kategoriyalarni button qilib chiqarish uchun
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


# bu categoriyaga bo'glangan postlarni olish uchun
class GetCategoryAPIView(RetrieveAPIView):
    """
        BU YERDA CATEGORIYDAGI MALUMOTLARNI GET QILIB bot.py DA dataGA SAQLAYAPMIZ
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class QuestionnaireListAPIView(ListAPIView):
    """
        BU YERDA CATEGORIYAGA BOG'LANGAN questionLARNI CHIQARISH
    """
    serializer_class = QuestionnaireSerializers

    def get_queryset(self):
        obj = Questionnaire.objects.filter(category=self.kwargs['pk'])
        return obj


class QuestionFilterAPIView(ListAPIView):
    queryset = QuestionnaireUser.objects.all()
    serializer_class = QuestionnaireUserSerializers

    # def get_queryset(self):
    #     obj = QuestionnaireUser.objects.filter(
    #         Q(chat_id=self.kwargs['chat_id']) & Q(category=self.kwargs['category'])
    #     )
    #     return obj
