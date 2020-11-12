from rest_framework import routers
from .views import chatFlowView, chatFlowDetailView,audioFlowDetailView,topWordsDetailView,sentimentDetailView,TwitchChapterView,TwitchDataView
from knox import views as knox_views
from django.urls import path, include
from . import views

router=routers.DefaultRouter()
#router.register('api/leads', LeadViewSet,'leads')
#router.register('api/users', userViewSet,'users')

urlpatterns=[
    path('api/chatFlow/<int:pk>',views.chatFlowDetailView.as_view()),
    path('api/audioFlow/<int:pk>', views.audioFlowDetailView.as_view()),
    path('api/sentiment/<int:pk>', views.sentimentDetailView.as_view()),
    path('api/topWords/<int:pk>', views.topWordsDetailView.as_view()),
    path('api/sentiment/<int:pk>', views.sentimentDetailView.as_view()),
    path('api/TwitchData/<int:pk>', views.TwitchDataView.as_view()),
    path('api/TwitchChapter/<int:pk>', views.TwitchChapterView.as_view()),
]