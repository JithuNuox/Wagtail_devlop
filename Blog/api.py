from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from wagtail.models import Locale
from django.utils.translation import get_language_from_request
from .models import BlogPage
from .serializers import BlogPageSerializer,BlogPageDetailSerializer

class BlogPageSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = BlogPageSerializer
    def get_serializer_class(self):
        group_serializer = {
            'list': BlogPageSerializer,
            'retrieve': BlogPageDetailSerializer,
        }
        serializer_class = group_serializer.get(self.action,None)
        
        if serializer_class is None:
            raise ValueError(f"No serializer found for action: {self.action}")
        
        return serializer_class
    def list(self,request,*args, **kwargs):
        response={}
        try:
            lang = get_language_from_request(request)
        
            locale = get_object_or_404(Locale, language_code=lang)
            
            queryset = BlogPage.objects.all().filter(locale=locale)
            # print("------queryset-----------------",queryset)
            serializer = BlogPageSerializer(queryset, many=True)
            # print("--------serializer---------",serializer)
            
            response['data'] = serializer.data
            # print("--------serializer---------",serializer.data)
        except Exception as e:
            response['error'] = 'api Failed'
            response['message'] = str(e)
            print("error :",e)
        
        return Response(response, status=status.HTTP_200_OK)
    def retrieve(self,request,*args, **kwargs):
        response ={}
        try:
            lang = get_language_from_request(request)
            locale = get_object_or_404(Locale, language_code=lang)
            slug=kwargs.get('slug')
            queryset = BlogPage.objects.live().filter(locale=locale)
            page = get_object_or_404(queryset,slug=slug)
            serializer =self.get_serializer(page,context={'request':request,'locale':locale})
            response['data'] = serializer.data
            response['status']="successful"
        except Exception as e:
            response['error']='failed'
            response['message']=str(e)
        return Response(response, status=status.HTTP_200_OK)
            
