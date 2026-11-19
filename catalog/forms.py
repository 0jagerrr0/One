import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(
        help_text="Укажите дату от сегодняшнего дня до четырёх недель вперёд."
    )

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError(_('Неккоректный ввод даты.'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Нельзя продлить книгу более чем на четыре недели.'))

        return data

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username',)
