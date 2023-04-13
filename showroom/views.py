import json
import time
from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .forms import CommentForm, AddPicture
from .models import Pictures, Comment
from cloudipsp import Api, Checkout
from django.core.mail import send_mail
from django.contrib import messages
from .forms import MessageFromUser

secret_key = 'test'



class HomePage(ListView):
    model = Pictures
    template_name = 'showroom/home.html'
    context_object_name = 'pictures'
    ordering = ['-id']

    def get_context_data(self, **kwards):
        ctx = super(HomePage, self).get_context_data(**kwards)
        ctx['title'] = 'Главная страница'
        return ctx

class PictureShow(ListView):
    model = Pictures
    template_name = 'showroom/picture-show.html'
    context_object_name = 'pictures'

    def get_context_data(self, **kwards):
        ctx = super(PictureShow, self).get_context_data(**kwards)
        ctx['zag'] = 'Для просмотра просто кликни по иконке рисунка :)'
        return ctx



class PictureDetailPage(DetailView):
    model = Pictures
    template_name = 'showroom/picture-detail.html'
    form_class = CommentForm
    success_msg = 'Комментарий успешно создан'


    def get_context_data(self, **kwargs):
        ctx = super(PictureDetailPage, self).get_context_data(**kwargs)
        pictures= Pictures.objects.filter(slug=self.kwargs['slug'])
        comments = Comment.objects.filter(picture=pictures[0])
        picture = pictures[0]
        form = CommentForm
        ctx['comments'] = comments
        ctx['form']=form
        ctx['picture'] = picture
        return ctx

    def post(self, request, *args, **kwargs):
        slug = request.path.split("/")[2]
        picture = Pictures.objects.filter(slug=slug)
        post = request.POST.copy()
        post['user'] = request.user
        post['picture'] = picture
        request.POST = post

        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.picture = post['picture'][0]
            form.save()

            url = self.kwargs['slug']
            return redirect('/picture/' + url)


class PictureAdd(CreateView):
    form_class = AddPicture
    template_name = 'showroom/add-picture.html'

    def get_context_data(self, **kwargs):
        ctx = super(PictureAdd, self).get_context_data(**kwargs)
        ctx['title'] = 'Добавить картину'
        ctx['btn_text'] = 'Добавить картину'

        return ctx

def kontakty(request,**kwargs):
    dateToday = date.today().strftime('%d %m %Y')
    if request.method == 'POST':
        form = MessageFromUser(request.POST)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data.get('theme')
            plain_message = form.cleaned_data.get('text')
            from_email = f" от {form.cleaned_data.get('email')}"
            to = 'ducha2112@yandex.ru'
            send_mail(subject,plain_message, from_email,[to])
            messages.success(request, f'Сообщение успешно отправлено')
            return redirect('home')
    else:
        form=MessageFromUser()


    return render(request,'showroom/kontakty.html',{
            'date': dateToday,
            'title': 'Страница контакты',
            'form': form
        })

class DeletePictureView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Pictures
    success_url = '/'
    template_name = 'showroom/delete_picture.html'
    def test_func(self,*args,**kwargs):
        picture = self.get_object()
        print(self.request)
        url = self.kwargs['slug']
        return redirect('/picture/' + url)

class UpdatePictureView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Pictures
    template_name = 'showroom/add-picture.html'

    fields = ['slug','title','desc','image']

    def get_context_data(self, **kwards):
        ctx = super(UpdatePictureView, self).get_context_data(**kwards)

        ctx['title'] = 'Обновление рисунка'
        ctx['btn_text'] = 'Обновить'
        return ctx

    def test_func(self,*args,**kwargs):
        url = self.kwargs['slug']
        return redirect('/picture/' + url)

    def form_valid(self, form):

        return super().form_valid(form)