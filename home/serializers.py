from rest_framework import serializers
from wagtail.fields import StreamValue
from .models import HomePage
from wagtail import blocks
from django.utils.translation import gettext_lazy as _
# from Movie.utils import get_image_rendition  # Import this to get the image rendition
from wagtail.images.blocks import ImageChooserBlock
from Devlop.utils import get_image_rendition
from wagtail.images.models import Image
from wagtail.rich_text import RichText
from bs4 import BeautifulSoup
from wagtail.models import Page
import base64

class PageSerializer(serializers.Serializer):
    page_type = serializers.SerializerMethodField()
    class Meta:
        model = Page
        fields = ['slug','page_type']
    def get_page_type(self, obj):
        # import pdb; pdb.set_trace()
        return obj.specific._meta.model_name
        
class LinkBlockSerializer(serializers.Serializer):
    label = serializers.CharField(read_only=True)
    link_type = serializers.CharField(read_only=True)
    internal_page = PageSerializer(required=False)
    external_url = serializers.URLField(required=False)
    
    def to_representation(self, instance):
        # import pdb; pdb.set_trace()
        data = super().to_representation(instance)
        if instance.get('internal_page'):
            if isinstance(instance['internal_page'], Page):
                data['internal_page'] = PageSerializer(instance['internal_page']).data
            else:
                try:
                    page = Page.objects.get(id=instance['internal_page'])
                    data['internal_page'] = PageSerializer(page).data
                except Page.DoesNotExist:
                    data['internal_page'] = None
        return data
        
class ImageSliderBlockSerializer(serializers.Serializer):
    main_title = serializers.CharField(read_only=True)
    sub_image = serializers.SerializerMethodField(source='main_image',read_only=True)
    description = serializers.CharField(read_only=True)
    links = LinkBlockSerializer(many=True, read_only=True)
    def get_sub_image(self, obj):
        # import pdb; pdb.set_trace()
        # image = obj.value['main_image']
        image = obj.get('main_image')
        # print('image')
        if image:
            rendition = get_image_rendition(image, 'original')
            if rendition:
                return {
                    "url": rendition['url'],
                    "full_url": rendition['full_url'],
                    "width": rendition['width'],
                    "height": rendition['height'],
                    "alt": rendition['alt']
                }
        return None
    

    
    
class HomePageSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    slug = serializers.CharField(read_only=True)
    content = serializers.SerializerMethodField()
    
    def get_content(self, obj):
        image_sliders = []
        request = self.context.get('request')
        for block in obj.content:
            if block.block_type == 'image_slider':
                image_slider_data = block.value
                image_sliders.append({
                    'type': 'image_slider',
                    'value': ImageSliderBlockSerializer(image_slider_data, context={'parent': self,'request': request}).data
                })
        return image_sliders
class HomePageDetailSerializer(HomePageSerializer):
    titles = serializers.CharField(read_only=True)
    slug = serializers.CharField(read_only=True)
    image_slider = ImageSliderBlockSerializer(source='*')
    def get_image_sliders(self, obj):
        image_sliders = []
        request = self.context.get('request')
        for block in obj.image_slider:
            if block.block_type == 'image_slider':
                image_sliders.append({
                    'type': 'image_slider',
                    'value': ImageSliderBlockSerializer(block.value, context={'parent': self,'request': request}).data
                })
        return image_sliders
    
    

