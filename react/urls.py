from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.index),
    path('search',views.index),
    path('login',views.index),
    path('signup',views.index),
    path('selectchapter',views.index),
    path('mypage',views.index),
    path('highlightresult',views.index),
    path('statistics',views.index),

]
