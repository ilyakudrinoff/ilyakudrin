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


class Author(TimeStampedModel):
    title = models.CharField('Название', max_length=200)
    text = models.TextField('Текст')

    class Meta:
        verbose_name = _('Авторские записки')
        verbose_name_plural = _('Авторские записки')
        ordering = ['-created_at', 'title']

    def __str__(self):
        return self.title + " " + str(self.created_at)


class News(TimeStampedModel):
    image = models.ImageField('Изображение', upload_to='static/imgnews', default='default.jpg')
    title = models.CharField('Название', max_length=200)
    text = models.TextField('Текст')
    link = models.CharField('ССылка', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = _('Новости')
        verbose_name_plural = _('Новости')
        ordering = ['-created_at', 'title']

    def __str__(self):
        return self.title + " " + str(self.created_at)


class Store(TimeStampedModel):
    image = models.ImageField('Изображение', upload_to='static/imgstores', default='default.jpg')
    name = models.CharField('Название', max_length=100)
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
    image = models.ImageField('Изображение', upload_to='static/imgbooks', default='default.jpg')
    description = models.TextField('Описание')
    count = models.IntegerField('Количество книг у автора', default=0)
    name_1 = models.CharField('Имя ссылки 1', blank=True, max_length=20)
    link_1 = models.CharField('Ссылка 1', blank=True, max_length=200)
    name_2 = models.CharField('Имя ссылки 2', blank=True, max_length=20)
    link_2 = models.CharField('Ссылка 2', blank=True, max_length=200)
    name_3 = models.CharField('Имя ссылки 3', blank=True, max_length=20)
    link_3 = models.CharField('Ссылка 3', blank=True, max_length=200)

    class Meta:
        verbose_name = _('Книжная полка')
        verbose_name_plural = _('Книжная полка')
        ordering = ['-created_at', 'name']

    def __str__(self):
        return self.name + " " + str(self.created_at)


class Review(TimeStampedModel):
    name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    text = models.TextField('Текст')
    book = models.ForeignKey(BookShelf, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Книга')

    class Meta:
        verbose_name = _('Отзывы')
        verbose_name_plural = _('Отзывы')
        ordering = ['-created_at',]

    def __str__(self):
        return self.last_name + " " + str(self.created_at)


class BuyQuery(TimeStampedModel):
    name = models.CharField('Имя', max_length=50)
    phone = models.CharField('Phone', max_length=11)
    mail = models.CharField('Почта', max_length=100)
    book = models.ForeignKey(BookShelf, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Книга')
    shirt = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Мерч')

    class Meta:
        verbose_name = _('Заявка на покупку')
        verbose_name_plural = _('Заявки на покупку')
        ordering = ['-created_at',]

    def __str__(self):
        return self.name + " " + str(self.created_at)
