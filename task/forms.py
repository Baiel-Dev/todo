from  django import forms
from task.models import Task,Easy

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class EasyForm(forms.ModelForm):
    class Meta:
        model = Easy
        fields = '__all__'
