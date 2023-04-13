from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class Profile(models.Model):
    user = models.OneToOneField(User,verbose_name ='Пользователь', on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователя', default ='default.jpg', upload_to='user_images')




    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 350 or image.width > 256:
            resize = (350,256)
            image.thumbnail(resize)
            image.save(self.img.path)


    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'

