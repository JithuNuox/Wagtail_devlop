from django.db import models

# Create your models here.
from django.db import models

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.models import TranslatableMixin
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from django.core.cache import cache
from .blocks import SocialMediaLinkBlock,ContactBlock,NewLetterBlock
from Navigation.models import NavigationSnippet

class FooterSnippet(TranslatableMixin, models.Model):
    name = models.CharField(max_length=250,help_text=_("Please enter name"))
    disclaimer = RichTextField(blank=True,  editor='default' ,help_text=_("Please enter disclaimer"),)  
    copyright = RichTextField(blank=True, editor='default' , help_text=_("Please enter copyright")) 
    # footer_link =models.ForeignKey(on_delete=models.SET_NULL)

    social_media = StreamField(
        [('social_media', SocialMediaLinkBlock())], 
        use_json_field=True, 
        blank=False,
    )
    contact_content = StreamField(
        [('contact_block', ContactBlock())],
        blank=True,
    )
    new_letter_content = StreamField(
        [('new_letter_block', NewLetterBlock())],
        blank=True,
    )

    panels = [
        FieldPanel('disclaimer'),
        FieldPanel('copyright'),
        FieldPanel('name'),
        FieldPanel('social_media'),
        FieldPanel('contact_content'),
        FieldPanel('new_letter_content'),

    ]

    def __str__(self):
        return self.name
