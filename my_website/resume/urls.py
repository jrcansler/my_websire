from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from resume import views

app_name = 'resume'

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^resume/', views.show_resume, name='show_resume'),

]
