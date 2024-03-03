from rest_framework import generics
from django.db.models import Q
from api import models, serializers
from django.shortcuts import get_object_or_404


# userlar ro'yxatdan o'tgan yoki o'tmaganligini tekshirish
class UserListAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.BotUserSerializer

    def get_object(self):
        obj = get_object_or_404(models.BotUser, chat_id=self.kwargs["chat_id"])
        return obj


# userlar yaratish uchun
class UsersCreateAPIView(generics.CreateAPIView):
    queryset = models.BotUser.objects.all()
    serializer_class = serializers.BotUserSerializer


# bu kategoriyalarni button qilib chiqarish uchun
class CategoryListAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all().select_related('state')
    serializer_class = serializers.CategorySerializer


# bu categoriyaga bo'glangan postlarni olish uchun
class GetCategoryAPIView(generics.RetrieveAPIView):
    """
    BU YERDA CATEGORIYDAGI MALUMOTLARNI GET QILIB bot.py DA dataGA SAQLAYAPMIZ
    """

    queryset = models.Category.objects.all().select_related('state')
    serializer_class = serializers.CategorySerializer


class QuestionnaireListAPIView(generics.ListAPIView):
    """
    BU YERDA CATEGORIYAGA BOG'LANGAN questionLARNI CHIQARISH
    """

    serializer_class = serializers.QuestionnaireSerializer

    def get_queryset(self):
        obj = models.Questionnaire.objects.filter(category=self.kwargs["pk"])
        return obj.select_related('category')


class QuestionnaireRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.QuestionnaireSerializer

    def get_queryset(self):
        obj = models.Questionnaire.objects.filter(pk=self.kwargs['pk'])
        return obj


class QuestionFilterAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.QuestionnaireUserSerializer

    def get_object(self):
        obj = get_object_or_404(models.QuestionnaireUser, category=self.kwargs['id'],
                                user__chat_id=self.kwargs['chat_id'])

        return obj


class QuestionCreateAPIView(generics.CreateAPIView):
    queryset = models.QuestionnaireUser.objects.all()
    serializer_class = serializers.QuestionnaireUserCreateSerializer


class ChannelListAPIView(generics.ListAPIView):
    queryset = models.Channel.objects.all()
    serializer_class = serializers.ChannelSerializer
