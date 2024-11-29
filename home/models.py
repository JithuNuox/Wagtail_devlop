from django.db import models

from wagtail.models import Page
from django.utils.translation import gettext_lazy as _
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from .blocks import ImageSliderBlock
from Devlop.utils import get_image_rendition


class HomePage(Page):
    main_title = models.CharField(max_length=100)
    content = StreamField(
        [('image_slider', ImageSliderBlock())], 
        use_json_field=True, 
        blank=True,
        min_num=1,
    )   
    
    # content = StreamField([
        #home page blocks
        # ('text_with_card_block', TextBoxWithCardBlock(group="Card Blocks")),
        # ('home_noor_block', HomeNoorBlock(group="Card Blocks")),
        # ('round_image_card_block', RoundImageCardBlock(group="Card Blocks")),
        # ('text_block', BaseTextBlock(group="Base Blocks")),
        # ('home_page_shares_list_block', HomePageSharesListBlock(group="Base Blocks")),
        # ('circle_swiper_block',CircleSwiperBlock(group="Swiper Blocks")),
        # ('gradient_box_swiper_block',GradientBoxSwiperBlock(group="Swiper Blocks")),
        # ('gradient_image_card_block', GradientImageCardBlock(group="Card Blocks")),
        # ('featured_article', FeaturedArticleBlock(group="Card Blocks")),

        #other page blocks
        # ('two_column_text_block', TwoColumnTextBlock(group="Base Blocks")),
        # ('form_text_block', FormTextBlock(group="Base Blocks")),
        # ('base_image_block', BaseImageTextBlock(group="Base Blocks")),
        # ('golden_swiper_block', GoldenSwiperBlock(group="Swiper Blocks")),
        # ('gradient_text_card_block', GradientTextCardBlock(group="Card Blocks")),
        # ('borderless_image_block', BorderlessImageCardBlock(group="Card Blocks")),
        # ('point_tab_block', PointTabBlock(group="Card Blocks")),
        # ('trade_block', TradeBlock(group="Base Blocks")),
        # ('faq_block', FAQBlock(group="Base Blocks")),
        # ('sandwich_image_block', SandwichImageBlock(group="Base Blocks")),
        # ('content_block', ContentBlock(group="Base Blocks")),
        # ('text_overlay_image_block', TextOverlayImageCardBlock(group="Card Blocks")),
        # ('team_members_swiper_block', TeamMembersSwiperBlock(group="Swiper Blocks")), 
        # ('chairmans_message_block', ChairmansMessageBlock(group="Base Blocks")), 
        # ('marquee_block', MarqueeBlock(group="Swiper Blocks")),
        # ('shares_list_block', SharesListBlock(group="Base Blocks")),
        # ('social_sharing_block', SocialSharingBlock(group="Base Blocks")),  
        # ('multi_list_text_block', ImageMultiListTextBlock(group="Base Blocks")), 
        # ('contact_address_block', ContactAddressBlock(group="Card Blocks")), 
        # ('contact_form_block', ContactFormBlock(group="Base Blocks")), 
        # ('contact_image_card_block', ContactGradientImageCardBlock(group="Card Blocks")), 
        # ('glossary_block', GlossaryBlock(group="Base Blocks")), 
        # ('document_block', DocumentBlock(group="Base Blocks")), 
        # ('multiple_document_block', MultipleDocumentBlock(group="Base Blocks")), 
        # ('table_content_block', TableContentBlock(group="Base Blocks")), 
        
    # ],use_json_field=True, blank=True)

    # max_count = 1  # Only one page is allowed
    
    content_panels = Page.content_panels + [
        FieldPanel('content'),
        # FieldPanel('content'),        
    ]
    template ="home/home_page.html"

    class Meta:
        verbose_name = _("Home Page")
        verbose_name_plural = _("Home Pages")

    def get_locale_display(self):
        return str(self.locale)

