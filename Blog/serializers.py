from rest_framework import serializers
from Blog.blocks import JobCardBlock
from .models import *
from wagtail.fields import StreamField, StreamValue
from wagtail.rich_text import RichText
from taggit.models import Tag

from Devlop.helper import local_timezone


class JobCardBlockSerializers(serializers.Serializer):
    job_title = serializers.CharField(required=True)
    company_name = serializers.CharField(required=True)
    job_description = serializers.SerializerMethodField()
    company_logo = serializers.SerializerMethodField()
    apply_button_text = serializers.CharField(required=True)
    
    def get_company_logo(self, obj):
        # import pdb; pdb.set_trace()
        # image = obj.value['main_image']
        image = obj.get('company_logo')
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
    def get_job_description(self, instance):
        content = instance.get('job_description')
        if not content:
            return None

        if isinstance(content, RichText):
            content = str(content)

        request = self.context.get('request')
        if not request:
            return content 
    
class BannerMixinSerializers(serializers.Serializer):
    banner_heading = serializers.CharField()
    banner_subheading = serializers.CharField()
    banner_description  = serializers.SerializerMethodField()
    banner_header_image = serializers.SerializerMethodField()
    def get_banner_header_image(self, obj):
        if obj.banner_header_image:
            return {
                "url": obj.banner_header_image.file.url,
            }
        return None
    def get_banner_description(self, instance):
        content = instance.get('banner_description')
        if not content:
            return None

        # Ensure content is a string
        if isinstance(content, RichText):
            content = str(content)

        request = self.context.get('request')
        if not request:
            return content  

class BlogIndexPageSerializers(serializers.Serializer):
    intro = serializers.SerializerMethodField()
    body = serializers.SerializerMethodField()
    banner = BannerMixinSerializers(source='*')
    def get_intro(self, instance):
        content = instance.get('intro')
        if not content:
            return None

        if isinstance(content, RichText):
            content = str(content)

        request = self.context.get('request')
        if not request:
            return content 
    def get_body(self, instance):
        content = instance.get('body')
        if not content:
            return None

        if isinstance(content, RichText):
            content = str(content)

        request = self.context.get('request')
        if not request:
            return content  

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class BlogPageSerializer(serializers.Serializer):
    slug = serializers.CharField(read_only=True)
    date = serializers.DateField() 
    author = serializers.SerializerMethodField()
    reading_time = serializers.CharField()  
    intro = serializers.SerializerMethodField()
    banner_image = serializers.SerializerMethodField()
    thumbnail_image = serializers.SerializerMethodField()
    # content = BannerMixinSerializers()
    tags = serializers.SerializerMethodField()
    def get_banner_image(self, obj):
        # import pdb; pdb.set_trace()
        if obj.banner_image:
            return {
                "url": obj.banner_image.file.url,
            }
        return None

    def get_thumbnail_image(self, obj):
        # import pdb; pdb.set_trace()

        if obj.thumbnail_image:
            return {
                "url": obj.thumbnail_image.file.url,
            }
        return None
    def get_author(self, obj):
        # import pdb; pdb.set_trace()

        if isinstance(obj.author, StreamValue):
            return [
                JobCardBlockSerializers(block.value).data for block in obj.author
            ]
        return None
    def get_tags(self, obj):
        return TagSerializer(obj.tags.all(), many=True).data
    def get_intro(self, obj):
        # import pdb; pdb.set_trace()
        # content = obj.get('intro')
        content = obj.intro
        if not content:
            return None

        if isinstance(content, RichText):
            content = str(content)

        request = self.context.get('request')
        if not request:
            return content 
        return content
    def get_published_at(self,obj):
        request = self.context['request']
        return local_timezone(request,obj.first_published_at,"%b %d %Y, %I:%M %p")

        


class BlogPageDetailSerializer(BlogPageSerializer):
    date = serializers.DateField() 
    author = serializers.SerializerMethodField()
    reading_time = serializers.CharField()  
    intro = serializers.SerializerMethodField()
    banner_image = serializers.SerializerMethodField()
    thumbnail_image = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    def get_banner_image(self, obj):
        if obj.header_image:
            return {
                "url": obj.banner_image.file.url,
            }
        return None
    
    
    def get_thumbnail_image(self, obj):
        if obj.header_image:
            return {
                "url": obj.thumbnail_image.file.url,
            }
        return None
    def get_author(self, obj):
        if isinstance(obj.author, StreamValue):
            return [
                JobCardBlockSerializers(block.value).data for block in obj.author
            ]
        return None
    def get_tags(self,instance):
        if instance(instance.tags, StreamValue):
            return[
                BlogPageTagSerializers(block.value).data for block in instance.tags
            ]

    
    
    

    