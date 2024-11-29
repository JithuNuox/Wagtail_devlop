from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from wagtail.search import index
from taggit.models import TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager
from Devlop.utils import get_image_rendition
from .blocks import JobCardBlock


class BannerMixin(models.Model):
    banner_heading = models.CharField(max_length=250)
    banner_subheading = models.CharField(max_length=250, null=True, blank=True)
    banner_description  = RichTextField(blank=True, editor='default')
    banner_header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Banner image"),
        verbose_name=_('Banner Image')
    )

    banner_panels = [
        FieldPanel('banner_heading'),
        FieldPanel('banner_subheading'),
        FieldPanel('banner_description'),
        FieldPanel("banner_header_image"),
    ]

    class Meta:
        abstract = True
    
    
class BlogIndexPage(Page, BannerMixin):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + BannerMixin.banner_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    max_count = 1  
    parent_page_types = ['home.HomePage']  
    subpage_types = ['Blog.BlogPage'] 

    class Meta:
        verbose_name = _("Blog Index Page") 
        verbose_name_plural = _("Blog Index Pages")


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class BlogPage(Page, BannerMixin):
    date = models.DateField(_("Post date"), null=False, blank=False) 
    author = StreamField([
        ('job_card_block', JobCardBlock())  
    ], use_json_field=True, max_num=1, min_num=1)  

    reading_time = models.CharField(_("Read Time"), null=False, blank=False, max_length=50)  
    intro = RichTextField(blank=True) 
    banner_image = models.ForeignKey(
        "wagtailimages.Image",  
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Banner image"),
    )
    thumbnail_image = models.ForeignKey(
        "wagtailimages.Image",  
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Thumbnail Image (238x170px recommended)")
    )
    
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        # index.SearchField('content'),
    ]

    content_panels =  Page.content_panels + BannerMixin.banner_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('author'),
            FieldPanel('reading_time'),
            FieldPanel("banner_image"),
            FieldPanel('intro'),
            FieldPanel("thumbnail_image"),
            FieldPanel('tags'),
        ], heading="Blog information"),
        # FieldPanel('content'),
    ]

    subpage_types = []  
    parent_page_types = ['Blog.BlogIndexPage'] 

    def increment_view_count(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])
    def __str__(self):
        return self.intro

    class Meta:
        verbose_name = _("Blog Page") 
        verbose_name_plural = _("Blog Pages")


