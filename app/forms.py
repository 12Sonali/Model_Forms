from django import forms

from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=WebPage
        fields='__all__'
        labels={'topic_name':'TN'}#It will change the name in form
        widgets={'email':forms.PasswordInput}#it will change the data type

class AccessrecordForm(forms.ModelForm):
    class Meta:
        model=AccessRecord 
        fields='__all__'
        