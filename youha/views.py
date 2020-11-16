from django.shortcuts import render
from .twitchCrawling import parser
from datetime import datetime, timedelta
from rest_framework import viewsets, permissions, generics, serializers, status
from rest_framework.response import Response
from .models import *
from django.shortcuts import get_object_or_404
from .serializers import downloadSerializer,OriginalVidSerializer,highlightVidSerializer, TwitchChapterSerializer,chatFlowSerializer,audioFlowSerializer,topWordsSerializer,sentimentSerializer,UserSerializer,CreateUserSerializer,LoginUserSerializer
from selenium.common.exceptions import NoSuchElementException
from knox.models import AuthToken
from django.contrib import auth
from rest_framework.views import APIView 
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from .downloader import download
from .highlight import findhighlight
from .sentiment import sentiment_analysis
from .topword import keywords
import time

class chatFlowView(generics.ListAPIView):
    serializer_class = chatFlowSerializer

    queryset =chatFlow.objects.all()

    def get(self,request):
        queryset =self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset,many=True)


        return Response(serializer.data)

class chatFlowDetailView(generics.ListAPIView):
    serializer_class = chatFlowSerializer

    def get_queryset(self):
        video_id=self.kwargs['pk']

        queryset =chatFlow.objects.all().filter(video=video_id).order_by('time')

        return queryset
    

class audioFlowDetailView(generics.ListAPIView):
    serializer_class = audioFlowSerializer

    def get_queryset(self):
        video_id=self.kwargs['pk']
        queryset =audioFlow.objects.all().filter(video=video_id)
        
        return queryset

class topWordsDetailView(generics.ListAPIView):
    serializer_class = topWordsSerializer

    def get_queryset(self):
        video_id=self.kwargs['pk']

        if(topWords.objects.all().filter(video=video_id).first() ==None):
            key = keywords.topwords_list(video_id)
            queryset =topWords.objects.all().filter(video=video_id).order_by('rank')
        else:
            queryset =topWords.objects.all().filter(video=video_id).order_by('rank')
        

        return queryset

class sentimentDetailView(generics.ListAPIView):
    serializer_class = sentimentSerializer

    def get_queryset(self):
        video_id=self.kwargs['pk']
        if(sentiment.objects.all().filter(video=video_id).first() ==None):
            sen = sentiment_analysis.extract(video_id,20)
            queryset =sentiment.objects.all().filter(video=video_id).order_by('time')
        else:
            queryset =sentiment.objects.all().filter(video=video_id).order_by('time')


        return queryset



class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.request.user.youha.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.User)

    def list(self,request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)

class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["email"]) < 6 or len(request.data["password"]) < 4:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user),
            }
        )


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user),
            }
        )


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class OriginalVidView(generics.ListAPIView):
    serializer_class = OriginalVidSerializer
    def get_queryset(self):
        video_id=self.kwargs['pk']
        
        if(originalVid.objects.all().filter(video_url=video_id).first() == None):
            crawling = parser.parse_twitch(video_id)
            queryset =originalVid.objects.all().filter(video_url=video_id)
        else:
            queryset =originalVid.objects.all().filter(video_url=video_id)
        return queryset

class TwitchChapterView(generics.ListAPIView):
    serializer_class = TwitchChapterSerializer
    def get_queryset(self):
        video_id=self.kwargs['pk']

        try:
            state = originalVid.objects.get(video_url=video_id)
        except originalVid.DoesNotExist :
                time.sleep(20)
 
        queryset =TwitchChapter.objects.all().filter(video=video_id)

        return queryset



# def crawling(request, *args, **kwargs):
#     print(kwargs['pk'])
#     url = str(kwargs['pk'])
#     options = webdriver.ChromeOptions()
#     options.add_argument('headless')
#     options.add_argument('window-size=1920x1080')
#     options.add_argument("disable-gpu")
#     driver = webdriver.Chrome('chromedriver.exe', options=options)
#     driver.maximize_window()
#     driver.get('https://www.twitch.tv/videos/'+url)
#     driver.implicitly_wait(5)

#     crawling = parser.parse_twitch(url,driver)
#     state=True
#     return state
        
# class downloadView(generics.ListAPIView):
#     serializer_class=downloadSerializer
#     def get_queryset(self):
#         url = self.kwargs['pk']
#         # while(True):

#         queryset =originalVid.objects.get(video_url=url)
#         if(queryset.downloadState == 0):
#             downloading=download.downloader(url)

#         return queryset


def downloading(request, *args, **kwargs):
    print(kwargs['pk'])
    url = str(kwargs['pk'])
    while(True):
        try:
            queryset =originalVid.objects.get(video_url=url)
            if(queryset.downloadState == 0):
                downloading=download.downloader(url)
            else:
                return
        except:
            continue

    return 


class highlightVidView(generics.ListAPIView):
    serializer_class = highlightVidSerializer
    def get_queryset(self):
        video_id=self.kwargs['pk']

        chapter_name=self.kwargs['chapter']

        if(highlightVid.objects.all().filter(video=video_id,chapter=chapter_name).first() ==None):
            h=findhighlight.extract(video_id,chapter_name,20)
            queryset =highlightVid.objects.all().filter(video=video_id,chapter=chapter_name).order_by('start_time')
        else:
            queryset =highlightVid.objects.all().filter(video=video_id,chapter=chapter_name).order_by('start_time')

        return queryset
