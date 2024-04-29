from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile, Comment

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Primeiro Nome'
        self.fields['first_name'].widget.attrs['autocomplete'] = 'given-name'

        self.fields['username'].widget.attrs['placeholder'] = 'Nome de Usuário'
        self.fields['username'].widget.attrs['autocomplete'] = 'username'

        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['autocomplete'] = 'email'
        
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme sua Senha'

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
             raise forms.ValidationError('As senhas não coincidem.')
        return password2


class UserLoginForm(forms.Form):
    username = forms.CharField(
        label='Nome de Usuário',
        # widget=forms.TextInput(attrs={'placeholder': 'Nome de Usuário'})
    )
    password = forms.CharField(
        label='Senha',
        # widget=forms.PasswordInput(attrs={'placeholder': 'Senha'})
    )


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control w-100', 'id':'contentsBox', 'rows':'3', 'placeholder':'O que está acontecendo?', 'maxlength': '140'}))

    class Meta:
        model = Post
        fields = ['content']

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'username']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image', 'bio']


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control w-100', 'id':'contentsBox', 'rows':'3', 'placeholder':'O que está acontecendo?', 'maxlength': '140'}))

    class Meta:
        model = Comment
        fields = ['content']
