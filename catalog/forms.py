from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.


User = get_user_model()


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        #Проверка того, что дата не выходит за "нижнюю" границу (не в прошлом).
        if data < datetime.date.today():
            raise ValidationError('Invalid date - renewal in past')

        #Проверка того, то дата не выходит за "верхнюю" границу (+4 недели).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError('Invalid date - renewal more than 4 weeks ahead')

        # Помните, что всегда надо возвращать "очищенные" данные.
        return data


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    age = forms.IntegerField()

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "age", "email", "password1", "password2"]

