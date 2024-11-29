from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from wagtail.models import Locale
from django.utils.translation import get_language_from_request
from .models import FooterSnippet
from .serializers import *

class FooterSnippetSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = FooterSnippetSerializer
    def get_serializer_class(self):
        group_serializer = {
            'list': FooterSnippetSerializer,
            'retrieve': FooterSnippetDetailSerializer,
        }
        serializer_class = group_serializer.get(self.action,None)
        
        if serializer_class is None:
            raise ValueError(f"No serializer found for action: {self.action}")
        
        return serializer_class
    def list(self,request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        response = {}
        try:
            lang = get_language_from_request(request)
            locale = get_object_or_404(Locale, language_code=lang)
            querysets = FooterSnippet.objects.all().filter(locale=locale).first()
            # print("---querysets-----------------",querysets)
            serializer = self.get_serializer(querysets, context={'request': request,"locale":locale,})
            # print("------serializer--------------",serializer)
            response['result'] = 'success'
            # print("----------response----------",response)
            response['records'] = serializer.data
            # print("---------serializer.data-----------",serializer.data)
        except Exception as e:
            response['result'] = 'Failed'
            response['message'] = str(e)
            print("error--------------------",e)
            
        return Response(response, status=status.HTTP_200_OK)
    
    #single page data
    
    def retrieve(self,request,*args, **kwargs):
        response = {}
        try:
            lang = get_language_from_request(request)
            locale = get_object_or_404(Locale, language_code=lang)
            
            slug = kwargs.get('slug')
            queryset = FooterSnippet.objects.live().filter(locale=locale)
            
            page = get_object_or_404(queryset,slug=slug)
            serializer = self.get_serializer(page, context={'request': request,"locale":locale,})
            
            response['result']='success'
            response['records']=serializer.data 
            
        except Exception as e:
            
            response['result']='failed'
            response['message']=str(e)
        return Response(response, status=status.HTTP_200_OK)
            