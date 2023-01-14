from django import forms
from django.forms import ModelForm
from .models import rev
# class Review_Form(forms.Form):
#     user_name=forms.CharField(max_length=10)
#     rating=forms.IntegerField()


class Review_Form(ModelForm):
    class Meta:
        model=rev
        fields='__all__'

        labels={
            'user_name':'UserName',
            'rating':'Rating',
        }
        error_messages={
            "user_name":{
                "required ": "Your User MUst Required",
                "max_length":"Please enter a short Name"
            }
        }
#     user_name=forms.CharField(max_length=10)
#     rating=forms.IntegerField()
