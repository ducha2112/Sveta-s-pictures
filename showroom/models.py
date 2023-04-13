from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse




class Pictures(models.Model):
    slug = models.SlugField('Уникальное название картины', unique=True)
    title = models.CharField('Название картины', max_length=120)
    desc = models.TextField('Описание картины')
    image = models.ImageField('Изображение', default='default.png', upload_to='showroom_images')

    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = 'Рисунок'
        verbose_name_plural = 'Рисунки'

    def get_absolute_url(self):
        return reverse('picture-detail', kwargs={'slug': self.slug})

class Comment(models.Model):
    text = models.TextField(verbose_name='Текст комментария')
    user = models.ForeignKey(User, verbose_name='Автор комментария', on_delete=models.CASCADE, blank=True,
                             null=True)
    picture = models.ForeignKey(Pictures, related_name='comments_image', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Комментарий к картине{self.picture}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Message(models.Model):
    theme = models.CharField('Тема сообщения', max_length=100, unique=True)
    email = models.EmailField('Адрес электронной почты', max_length=254)
    text = models.TextField('Текст сообщения')



    def __str__(self):
        return f'{self.theme}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

