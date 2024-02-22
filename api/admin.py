from django.contrib import admin
from django.apps import apps
from .models import Category
post_models = apps.get_app_config('api').get_models()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    prepopulated_fields = {'slug': ('title',)}


for model in post_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass