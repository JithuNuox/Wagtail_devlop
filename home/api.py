from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from wagtail.models import Locale
from django.utils.translation import get_language_from_request
from .models import HomePage
from .serializers import HomePageSerializer,HomePageDetailSerializer
# Create your views here.
class HomePageViewSet(viewsets.ModelViewSet):
    serializer_class = HomePageSerializer
    def get_serializer_class(self):
        group_serializer = {
            'list': HomePageSerializer,
            'retrieve': HomePageDetailSerializer,
            # 'related': BlogPageSerializer,
        }
        serializer_class = group_serializer.get(self.action, None)
        
        if serializer_class is None:
            raise ValueError(f"No serializer found for action: {self.action}")
        
        return serializer_class
        
    def list(self, request, *args, **kwargs):
        response = {}
        try:
            lang = get_language_from_request(self.request)
            
            locale = get_object_or_404(Locale, language_code=lang)
            querysets = HomePage.objects.live().filter(locale=locale).first()
            serializer = self.get_serializer(querysets, context={'request': request,"locale":locale,})
            
            response['result'] = 'success'
            response['records'] = serializer.data
            # print("records------------------------",serializer.data)
        except Exception as e:
            print("Error:", e)
            response['result'] = 'failure'
            response['message'] = str(e)    
        return Response(response, status=status.HTTP_200_OK)
    
    #related pages selections
    def related(self, request, *args, **kwargs):
        response = {}
        try:
            slug = kwargs.get('slug')
            lang = get_language_from_request(request)
            locale = get_object_or_404(Locale, language_code=lang)
            
            page = get_object_or_404(HomePage.objects.live(), locale=locale, slug=slug)            
            # querysets = HomePage.objects.live().filter(locale=locale).select_related('image_slider').prefetch_related('tags').exclude(id=page.id).distinct()[:10]
            querysets = HomePage.objects.live().filter(locale=locale).first()

            serializer = self.get_serializer(querysets, many=True, context={'request': request})
            response['result'] = 'success'
            response['records'] = serializer.data
        except Exception as e:
            response['result'] = 'failure'
            response['message'] = str(e)
            
        return Response(response, status=status.HTTP_200_OK)
    
    #single page data
    def retrieve(self, request, *args, **kwargs):
        response = {}
        try:
        
            slug = kwargs.get('slug')
            
            lang = get_language_from_request(request)
            locale = get_object_or_404(Locale, language_code=lang)
            
            queryset = HomePage.objects.live().filter(locale=locale)
            
            home_page = get_object_or_404(queryset, slug=slug)
            
            if isinstance(home_page):
                home_page.increment_view_count()

            serializer = self.get_serializer(home_page, context={'request': request})
            
            response['result'] = 'success'
            response['records'] = serializer.data
        except Exception as e:
            response['result'] = 'failure'
            response['message'] = str(e)
        return Response(response, status=status.HTTP_200_OK)
