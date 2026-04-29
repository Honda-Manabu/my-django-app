from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    # http://localhost:8000/ で ms_index.html を表示
    #path('', views.index, name='index'),
    # http://localhost:8000/spage1/ などを表示
    path('spage<int:num>/', views.spage, name='spage'),
]