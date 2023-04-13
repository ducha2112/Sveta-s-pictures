from django import  forms
from django.contrib.auth.models import User
from .models import Profile

# from django.contrib.auth.forms import UserCreationForm

# class UserRegisterForm(UserCreationForm):
class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(
        label='Введите логин',
        required=True,
        help_text='Обязательное поле. Не более 150 символов. Нельзя вводить символы @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})

    )
    email = forms.EmailField(
        label='Введите Email ',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    # some = forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        help_text='Пароль не должен быть похож на другую вашу личную информацию. <br> Ваш пароль должен содержать не менее 8 символов',
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Введите пароль'})

    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = [ 'username', 'email','password1', 'password2' ]
 # 'password1', 'password2','some'

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='Введите логин',
        required=True,
        help_text='Нельзя вводить символы @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})

    )
    email = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )

    class Meta:
        model = User
        fields = [ 'username', 'email' ]


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Загрузить фото',
        required=False,
        widget=forms.FileInput

    )
    class Meta:
        model = Profile
        fields = ['img']

