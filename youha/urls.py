from rest_framework import routers
from .views import chatFlowView
from knox import views as knox_views
from django.urls import path, include
from . import views

router=routers.DefaultRouter()
#router.register('api/leads', LeadViewSet,'leads')
#router.register('api/users', userViewSet,'users')

urlpatterns=[
    path('api/chatFlow/<int:pk>',views.chatFlowDatailView.as_view()),
    path('api/chatFlow', views.chatFlowView.as_view()),
    path('api/audioFlow/<int:pk>', views.audioFlowDatailView.as_view())
]