from rest_framework.serializers import ModelSerializer
from .models import BotUser, Category, Questionnaire, QuestionnaireUser, State


class BotUserSerializers(ModelSerializer):
    class Meta:
        model = BotUser
        fields = ('chat_id', 'from_user_id', 'username', 'phone')


class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = ('pk', 'title',)


class CategorySerializers(ModelSerializer):
    state = StateSerializer()

    class Meta:
        model = Category
        fields = ('pk', 'title', 'slug', 'state')


class QuestionnaireSerializers(ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('pk', 'title', 'category',)


class QuestionnaireUserSerializers(ModelSerializer):
    user = BotUserSerializers()
    category = CategorySerializers()
    questionnaire = QuestionnaireSerializers()

    class Meta:
        model = QuestionnaireUser
        fields = ('category', 'questionnaire', 'user.chat_id')
