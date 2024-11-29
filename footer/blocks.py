from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.utils.translation import gettext_lazy as _
     
SOCIAL_MEDIA_CHOICE=[
    ('facebook', 'Facebook'),
    ('twitter', 'Twitter'),
    ('instagram', 'Instagram'),
    ('linkedin', 'LinkedIn'),
    ('youtube', 'YouTube'),
    ('google_plus', 'GooglePlus'),
]
class SocialMediaLinkBlock(blocks.StructBlock):
    # platform = blocks.CharBlock(required=True, help_text="Enter the social media platform name")
    platform = blocks.ChoiceBlock(choices=SOCIAL_MEDIA_CHOICE)
    icon = blocks.CharBlock(
        
        
    )
    url = blocks.URLBlock()
    class Meta:
        icon = 'tag'
        label = "Social Media"
    

class ContactBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    locations = blocks.CharBlock()
    phone_number = blocks.CharBlock()
    email = blocks.EmailBlock()

    class Meta:
        icon = 'tag'
        label = "Contact Information"

class NewLetterBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    description = blocks.RichTextBlock()
    class Meta:
        icon = 'tag'
        label = "News Letter"
    
#    ValueError: Error while serializing block definition: 'ContactBlockMeta' object has no attribute 'default' ---this error due to the initialize (blocks.Block) that changed into    
# t !!!!important---- (blocks.StructBlock)