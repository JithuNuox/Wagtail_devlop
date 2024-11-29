from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.utils.translation import gettext_lazy as _



class LinkBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=False, help_text=_("Enter the label of the link"))
    link_type = blocks.ChoiceBlock(
        choices = [
            ('internal', _('Internal Page')),
            ('external', _('External URL')),
        ],
        default='internal',
        help_text=_("Select the type of link"),
    )
    internal_page = blocks.PageChooserBlock(
        required=False, 
        help_text=_("Select an internal page"),
        # target_model = PAGE_TARGETS
    )
    external_url = blocks.URLBlock(
        required=False, 
        help_text=_("Enter an external URL"),
    )

class ImageSliderBlock(blocks.StructBlock):
    main_title = blocks.CharBlock(required=True)
    main_image = ImageChooserBlock(required=True, help_text="Main image of the slider")  
    description = blocks.CharBlock(required=True)
    links = blocks.ListBlock(
        LinkBlock(),
        min_num=0,  # No minimum requirement
        max_num=2,  # Maximum of two links
        help_text=_("Add button section"),
        label="Add link details"
    )

    class Meta:
        icon = 'image'
        label = "Image Slider"
