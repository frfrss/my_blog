from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'myblog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.article_comment, name='detail'),
    path('<int:article_id>/vote/', views.vote, name='vote'),
]