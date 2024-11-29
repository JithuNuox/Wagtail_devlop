from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.utils.translation import gettext_lazy as _

class JobCardBlock(blocks.StructBlock):
    job_title = blocks.CharBlock(required=True)
    company_name = blocks.CharBlock(required=True)
    job_description = blocks.RichTextBlock(required=True)
    company_logo = ImageChooserBlock(required=True, help_text="Company logo")
    apply_button_text = blocks.CharBlock(required=True)
    
    class Meta:
        icon = 'tag'
        label = "Job Card"
    