from django import forms
from django.contrib.auth.models import User
from .models import Star


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder' : 'Tvoje Username'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder' : 'Tvoj Email'
        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder' : 'Tvoje Heslo'
        })


    class Meta:
        model = User
        fields=['username','email', 'password']
        
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tvoje Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Tvoje Heslo'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
                'class': 'form-control',
            })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
        })


VOTE_CHOICES= [
    (1, 'Slabé'),
    (2, 'Slabšie'),
    (3, 'Stredné'),
    (4, 'Výborné'),
    (5, 'Topka'),
    ]

class StarForm(forms.ModelForm):
    star = forms.CharField(label='Ohodnoť Film?', widget=forms.Select(choices=VOTE_CHOICES))

    
    class Meta:
        model = Star
        fields=["star"]
