from django.utils.translation import gettext_lazy as _
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Team(TimeStampedModel):
    name = models.CharField('Название команды', max_length=50)
    company = models.CharField('Организация', max_length=50)

    class Meta:
        verbose_name = _('команда')
        verbose_name_plural = _('команды')
        ordering = ['-created_at', 'name']

    def __str__(self):
        return self.name

class Speaker(TimeStampedModel):
    name = models.CharField('Имя', max_length=50)
    lastName = models.CharField('Фамилия', max_length=50)
    serName = models.CharField('Отчество', max_length=50, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True, verbose_name='команда')
    
    class Meta:
        verbose_name = _('спикер')
        verbose_name_plural = _('спикеры')
        ordering = ['-created_at', 'lastName']

    def __str__(self):
        return self.lastName + " " + str(self.created_at)


class ResultsSpeaker(TimeStampedModel):
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE, blank=True, null=True, verbose_name='спикер')
    result = models.IntegerField('Баллы за игру')

    class Meta:
        verbose_name = _('результат спикера')
        verbose_name_plural = _('результаты спикера')
        ordering = ['result',]

    def __str__(self):
        return self.speaker + " " + str(self.result)


class ResultsTeam(TimeStampedModel):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True, verbose_name='команда')
    result = models.IntegerField('Баллы за игру')

    class Meta:
        verbose_name = _('результат команды')
        verbose_name_plural = _('результаты команды')
        ordering = ['result',]

    def __str__(self):
        return self.team + " " + str(self.result)


class News(TimeStampedModel):
    image = models.ImageField('Изображение', upload_to='static/imgnews', default='default.jpg')
    title = models.CharField('Название', max_length=200)
    text = models.TextField('Текст')

    class Meta:
        verbose_name = _('Новости')
        verbose_name_plural = _('Новости')
        ordering = ['-created_at', 'title']

    def __str__(self):
        return self.title + " " + str(self.created_at)
