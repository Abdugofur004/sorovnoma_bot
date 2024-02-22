from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BotUser(BaseModel):
    chat_id = models.CharField(max_length=128, unique=True)
    from_user_id = models.CharField(max_length=128)
    username = models.CharField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.chat_id


class State(BaseModel):
    title = models.CharField(max_length=100)  # sector bosqichi


class Category(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='state')

    def __str__(self):
        return self.title


class Questionnaire(BaseModel):
    title = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class QuestionnaireUser(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name="question")
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE, related_name='user')
    number_votes = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return f"{self.questionnaire} {self.number_votes}"
