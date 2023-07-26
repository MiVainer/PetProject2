from django.db import models

# Создаём тблицу в БД

class Artiles(models.Model):
    # Создаём столбцы в таблице
    skill = models.CharField('Название скила', max_length=50, default='Не заполнено')
    opisanie = models.CharField('Краткое описание', max_length=250, default='Не заполнено')
    full_text = models.TextField('Примеры реализации')

    def __str__(self):
        return self.skill

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = "Навыки DevOps"
        verbose_name_plural = "Навыки DevOps"
