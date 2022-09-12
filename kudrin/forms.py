from django import forms

from .models import Review, BuyQuery


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'last_name', 'text',)
        labels = {'name': 'Ваше имя', 'last_name': 'Ваша фамилия', 'text': 'Ваша рецензия (отзыв)', }


class BuyQueryForm(forms.ModelForm):
    class Meta:
        model = BuyQuery
        fields = ('name', 'phone', 'mail',)
        labels = {'name': 'Имя', 'phone': 'Номер телефона', 'mail': 'Электронная почта', }
