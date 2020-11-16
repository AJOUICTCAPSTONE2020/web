from rest_framework import routers
from .views import highlightVidView,downloading,chatFlowView,chatFlowDetailView,audioFlowDetailView,topWordsDetailView,sentimentDetailView,TwitchChapterView,OriginalVidView
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
    path('api/topChart/<int:pk>', views.topWordsDetailView.as_view()),
    path('api/sentiment/<int:pk>', views.sentimentDetailView.as_view()),
    path('api/selectchapter/<int:pk>', views.OriginalVidView.as_view()),
    path('api/chapter/selectchapter/<int:pk>', views.TwitchChapterView.as_view()),
    # path('api/crawling/<int:pk>',crawling),
    path('api/downloading/selectchapter/<int:pk>',downloading),
    path('api/highlight/<int:pk>/<str:chapter>',views.highlightVidView.as_view()),
]

