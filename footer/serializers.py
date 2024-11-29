from rest_framework import serializers
from .blocks import *
from .models import *
from wagtail.fields import StreamField,StreamValue
from wagtail.rich_text import RichText

SOCIAL_MEDIA_CHOICE=[
    ('facebook', 'Facebook'),
    ('twitter', 'Twitter'),
    ('instagram', 'Instagram'),
    ('linkedin', 'LinkedIn'),
    ('youtube', 'YouTube'),
    ('google_plus', 'GooglePlus'),
]

class SocialMediaSerializers(serializers.Serializer):
    platform = serializers.ChoiceField(choices=SOCIAL_MEDIA_CHOICE, read_only=True)
    icon = serializers.CharField(read_only=True)
    url = serializers.URLField(read_only=True)
    
class ContactBlockSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    locations = serializers.CharField(read_only=True)
    phone_number = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)


class NewLetterBlock(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    description = serializers.SerializerMethodField()
    def get_description(self, instance):
        content = instance.get('description')
        if not content:
            return None

        # Ensure content is a string
        if isinstance(content, RichText):
            content = str(content)

        request = self.context.get('request')
        if not request:
            return content  

    
    
class FooterSnippetSerializer(serializers.Serializer):
    name = serializers.CharField(read_only = True)
    disclaimer = serializers.SerializerMethodField()   
    copyright = serializers.SerializerMethodField() 
    social_media = serializers.SerializerMethodField(read_only=True)
    contact_content = serializers.SerializerMethodField(read_only=True)
    new_letter_content = serializers.SerializerMethodField(read_only=True)
    
    def get_disclaimer(self, instance):
        # import pdb; pdb.set_trace()
        content = getattr(instance, 'disclaimer', None)
        if not content:
            return None

        if isinstance(content, RichText):
            content = str(content)

        request = self.context.get('request')
        if not request:
            return content

        return content
    def get_copyright(self, instance):
        # import pdb; pdb.set_trace()
        dt = getattr(instance, 'copyright', None)
        if not dt:
            return None

        if isinstance(dt, RichText):
            dt = str(dt)

        request = self.context.get('request')
        if not request:
            return dt 
        return dt   
    def get_social_media(self, obj):
        if isinstance(obj.social_media, StreamValue):
            return [
                SocialMediaSerializers(block.value).data for block in obj.social_media
            ]
        return None
    def get_contact_content(self,obj):
        if isinstance(obj.contact_content, StreamValue):
            return [
                ContactBlockSerializer(block.value).data for block in obj.contact_content
            ]
        return None
    def get_new_letter_content(self,obj):
        if isinstance(obj.new_letter_content, StreamValue):
            return [
                    NewLetterBlock(block.value).data for block in obj.new_letter_content
                ]
        return None
            
class FooterSnippetDetailSerializer(FooterSnippetSerializer):
    name = serializers.CharField(read_only = True)
    disclaimer = RichTextField()  
    copyright = RichTextField()
    social_media = serializers.SerializerMethodField(read_only=True)
    
    def get_social_media(self,obj):
        import pdb; pdb.set_trace()
        social_media =[]
        for link in obj.social_media:
            social_media.append({
                'platform': link.platform,
                'icon': link.icon,
                'url': link.url,
            })
            
    