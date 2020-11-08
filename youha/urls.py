from rest_framework import routers
from .views import userViewSet,RegistrationAPI, LoginAPI, UserAPI
from knox import views as knox_views
from django.urls import path, include


router=routers.DefaultRouter()
#router.register('api/leads', LeadViewSet,'leads')
router.register('api/users', userViewSet,'users')

urlpatterns=router.urls