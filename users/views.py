from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm
from  django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Пользователь {username} был успешно создан, электронная почта {email}')
            return redirect('home')
    else:
        form = UserRegisterForm()

    # form = UserCreationForm()
    return render(
        request,
        'users/registration.html',
        {
            'title':'Здесь вы можете пройти регистрацию на сайте',
            'form':form
        }
    )

# проверка авторизации
@login_required
def profile(request):
    if request.method == 'POST':
        profileForm = ProfileImageForm(request.POST,request.FILES,  instance=request.user.profile)
        updateUserForm = UserUpdateForm(request.POST,  instance=request.user)



        if profileForm.is_valid() and updateUserForm.is_valid() :
            updateUserForm.save()
            profileForm.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен!')
            return redirect('profile')
    else:
        profileForm = ProfileImageForm(instance=request.user.profile)
        updateUserForm = UserUpdateForm(instance=request.user)



    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm,
        'title':'Профайл'



    }
    return render(
        request,
        'users/profile.html', data)


