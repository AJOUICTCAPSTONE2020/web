from rest_framework import routers
from .views import chatFlowView, chatFlowDetailView,audioFlowDetailView,topWordsDetailView,sentimentDetailView
from knox import views as knox_views
from django.urls import path, include
from . import views

router=routers.DefaultRouter()
#router.register('api/leads', LeadViewSet,'leads')
#router.register('api/users', userViewSet,'users')

urlpatterns=[
    path('api/chatFlow/<int:pk>',views.chatFlowDetailView.as_view()),
    path('api/chatFlow', views.chatFlowView.as_view()),
    path('api/audioFlow/<int:pk>', views.audioFlowDetailView.as_view()),
    path('api/sentiment/<int:pk>', views.sentimentDetailView.as_view()),
    path('api/topWords/<int:pk>', views.topWordsDetailView.as_view()),
    path('api/sentiment/<int:pk>', views.sentimentDetailView.as_view())
]