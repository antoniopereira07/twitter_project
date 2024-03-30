from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Primeiro Nome'
        self.fields['username'].widget.attrs['placeholder'] = 'Nome de Usuário'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme sua Senha'

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control w-100', 'id':'cotentsBox', 'rows':'3', 'placeholder':'O que está acontecendo?'}))

    class Meta:
        model = Post
        fields = ['content']



# class UserLoginForm(forms.Form):
#     username = forms.CharField(label='Nome de Usuário', widget=forms.TextInput(attrs={'placeholder': 'Nome de Usuário'}))
#     password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))


# class UserUpdateForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs['placeholder'] = 'Nome de Usuário'
#         self.fields['password'].widget.attrs['placeholder'] = 'Senha'

#     class Meta:
#         model = User
#         fields = ['username', 'password']