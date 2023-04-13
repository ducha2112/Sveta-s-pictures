
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.HomePage.as_view(),name='home'),
    path('picture/<slug>',views.PictureDetailPage.as_view(),name='picture-detail'),
    path('picture-show/',views.PictureShow.as_view(), name='picture_show'),
    path('add-picture/',views.PictureAdd.as_view(), name='add-picture'),
    path('update-picture/<slug>',views.UpdatePictureView.as_view(), name='update-picture'),
    path('kontakty', views.kontakty, name='kontakty'),
    path('picture/<slug>/delete',views.DeletePictureView.as_view(),name='picture-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)