from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import TaskCustomUser  # Импорт модели TaskCustomUser
from task.models import Task  # Импорт модели Task


# Форма для задач
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'category', 'priority']  # Указать нужные поля


# Форма для регистрации пользователей
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Поле для ввода email

    class Meta:
        model = TaskCustomUser
        fields = ('username', 'email', 'password1', 'password2')  # Поля для регистрации

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']  # Сохранение email
        if commit:
            user.save()  # Сохранение пользователя
        return user


from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']  # Поля, которые пользователь может редактировать
