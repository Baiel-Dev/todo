from  django import forms
from task.models import Task,Easy,Hard

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class EasyForm(forms.ModelForm):
    class Meta:
        model = Easy
        fields = '__all__'

class HardForm(forms.ModelForm):
    class Meta:
        model = Hard
        fields = '__all__'
        widgets = {
            'category': forms.Select()  # Явно указываем, что это выпадающий список
        }