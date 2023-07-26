# Добавляем таблицу в админку сайта
from django.contrib import admin
from .models import Artiles

admin.site.register(Artiles)

