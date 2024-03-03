from rest_framework import serializers

from .models import BotUser, Category, Questionnaire, QuestionnaireUser, State, Channel


class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = ("pk", "chat_id", "from_user_id", "username", "phone")


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = (
            "title",
        )


class CategorySerializer(serializers.ModelSerializer):
    state = StateSerializer()

    class Meta:
        model = Category
        fields = ("pk", "title", "slug", "state")


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = (
            "pk",
            "title",
            "category",
        )


class QuestionnaireUserSerializer(serializers.ModelSerializer):
    # user = BotUserSerializers()
    user = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    questionnaire = serializers.StringRelatedField()

    class Meta:
        model = QuestionnaireUser
        fields = ("category", "questionnaire", "user", "number_votes")


class QuestionnaireUserCreateSerializer(serializers.ModelSerializer):
    # user = BotUserSerializers()
    # category = CategorySerializers()
    # questionnaire = QuestionnaireSerializers()

    class Meta:
        model = QuestionnaireUser
        fields = ('user', 'category', 'questionnaire')


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('channel_id', "channel_url")
