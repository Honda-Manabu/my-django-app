from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    # http://localhost:8000/ で ms_index.html を表示
    path('', views.index, name='ms_index'),
    path('communities/', views.ms_cmtys, name='ms_cmtys'),
    path('contact/', views.ms_contact, name='ms_contact'),
    path('links/', views.ms_link, name='ms_link'),
    path('taste/', views.ms_tastcho, name='ms_tastcho'),
    # 旧メニュー入り口
    path('about/', views.spage, {'num': 0}, name='ms_spage0'),
    # http://localhost:8000/spage1/ などを表示
    path('spage<int:num>/', views.spage, name='spage'),
]