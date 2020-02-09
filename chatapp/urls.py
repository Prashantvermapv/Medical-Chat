from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
app_name='chatapp'
urlpatterns = [
    path('', views.Home, name='home'),
    path('post/', views.Post, name='post'),
    #path('api/',views.convoList.as_view(),name='api'),
    #path('try/',views.P,name='p'),
    path('index/',views.Index,name='index'),
    path('new/',views.new,name='new')
]
#urlpatterns=format_suffix_patterns(urlpatterns)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
