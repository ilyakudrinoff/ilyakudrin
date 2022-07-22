from django.utils.translation import gettext_lazy as _
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


Gender = (
    ('Man', 'Мужской'),
    ('Woman', 'Женский'),
    ('Unisex', 'Unisex'),
)


class News(TimeStampedModel):
    image = models.ImageField('Изображение')
    title = models.CharField('Название', max_length=200)
    text = models.TextField('Текст')
    link_1 = models.TextField('Ссылка 1', blank=True, max_length=200)
    link_2 = models.TextField('Ссылка 2', blank=True, max_length=200)
    link_3 = models.TextField('Ссылка 3', blank=True, max_length=200)

    class Meta:
        verbose_name = _('Новости')
        verbose_name_plural = _('Новости')
        ordering = ['-created_at', 'title']

    def __str__(self):
        return self.title + " " + str(self.created_at)


class Store(TimeStampedModel):
    image = models.ImageField('Изображение')
    name = models.TextField('Название', max_length=200)
    gender = models.CharField('Гендорный признак', choices=Gender, max_length=20, default=Gender[2])
    price = models.IntegerField()

    class Meta:
        verbose_name = _('Мерч')
        verbose_name_plural = _('Мерч')
        ordering = ['-created_at', 'name']

    def __str__(self):
        return self.name + " " + str(self.created_at)


class BookShelf(TimeStampedModel):
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    link_1 = models.CharField('Ссылка 1', blank=True, max_length=200)
    link_2 = models.CharField('Ссылка 2', blank=True, max_length=200)
    link_3 = models.CharField('Ссылка 3', blank=True, max_length=200)

    class Meta:
        verbose_name = _('Книжная полка')
        verbose_name_plural = _('Книжная полка')
        ordering = ['-created_at', 'name']

    def __str__(self):
        return self.name + " " + str(self.created_at)
