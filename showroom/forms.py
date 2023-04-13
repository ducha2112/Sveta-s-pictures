from django import forms

from .models import Comment, Pictures, Message


class AddPicture(forms.ModelForm):

    slug = forms.SlugField(label='Введи уникальное имя картины',required=True, widget=forms.TextInput(attrs={'class': ' form-control','placeholder':'Уникальное имя картины'}))
    title = forms.CharField(label='Введи название картины',widget=forms.TextInput(attrs={'class': ' form-control','placeholder':'Название картины'}))
    desc=forms.CharField(label='Напиши что-нибудь о картине',required=True, widget=forms.Textarea(attrs={'class': 'md-textarea form-control','placeholder':'Описание картины'}))
    image = forms.ImageField(label='Выберите изображение',
        required=False,
        widget=forms.FileInput
)

    class Meta:
        model = Pictures
        fields = ('slug','title','desc','image')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'



class CommentForm(forms.ModelForm):

    text = forms.CharField(label='',required=True, widget=forms.Textarea(attrs={'class': 'md-textarea form-control','placeholder':'Оставьте ваш комментарий'}))

    # user = forms.CharField(widget=forms.HiddenInput)
    # lesson = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Comment
        fields = ('text',)
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class']='form-control'

class MessageFromUser(forms.ModelForm):
    theme = forms.CharField(
        label='Тема сообщения',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите тему сообщения'})

    )
    email = forms.EmailField(
        label='Введите Ваш Email и мы обязательно ответим Вам ',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    text = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст сообщения здесь'}), required=True)

    class Meta:
        model = Message
        fields = ['theme','email','text']
