from django.db import models

# Create your models here.
from django.db import models
# from django.db import models
from wagtail.blocks import StructBlock, CharBlock, ChoiceBlock, ListBlock, PageChooserBlock, URLBlock
from django.core.exceptions import ValidationError
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from django.utils.translation import gettext_lazy as _
from wagtail.models import TranslatableMixin
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from wagtail.models import Page


NAV_TYPE = [
	    ('header', _('Header Navigation'),),
        ('footer', _('Footer Navigation'),),
        ('footer_links', _('Footer Links'),),
    ]

MENU_TYPE = [
	    ('text', _('Text Menu'),),
        ('bordered_button', _('Bordered Button Menu'),),
        ('filled_button', _('Filled Button Menu'),),
    ]

# Create your models here.
class MenuItemBlock(StructBlock):
    title = CharBlock(required=True)    
    link_type = ChoiceBlock(choices=[
        ('internal', 'Internal Page'),
        ('external', 'External URL'),
    ])

    external_url = URLBlock(required=False)
    internal_page_model_name = CharBlock(required=False, max_length=150, label="Page name(internal)", help_text="This field can be avoided and will be set automatically.", editable=False)

    class Meta:
        icon = "list-ul"
        label = "Menu Item"


class TabBlock(StructBlock):
    title = CharBlock(required=False, help_text=_("Please enter tab name"))
    slug = CharBlock(required=False, help_text=_("Please provide unique slug name for url"))
    menu_items = ListBlock(MenuItemBlock())

 
    class Meta:
        icon = "list-ul"
        label = "Multiple Menu Items"

class SingleMenuBlock(StructBlock):
    title = CharBlock(required=True, help_text=_("Please enter menu name"))    
    menu_type = ChoiceBlock(max_length=20, choices=MENU_TYPE,  null=True, blank=True, default="text", help_text=_("Menu type"))    
    menu_item = MenuItemBlock()
    class Meta:
        icon = "list-ul"
        label = "Single Menu"

class MultipleMenuBlock(StructBlock):
    title = CharBlock(required=True, help_text=_("Please enter menu name"))
    menu_type = ChoiceBlock(max_length=20, choices=MENU_TYPE,  null=True, blank=True, default="text", help_text=_("Menu type"))
    menu_items = ListBlock(MenuItemBlock())
    class Meta:
        icon = "list-ul"
        label = "Sub Menu"

class TabbedMenuBlock(StructBlock):
    title = CharBlock(required=True, help_text=_("Please enter tab name"))
    tabs = ListBlock(TabBlock())
    class Meta:
        icon = "list-ul"
        label = "Tabbed Menu"


# @register_snippet
class NavigationSnippet(TranslatableMixin, models.Model):
    name = models.CharField(max_length=255, help_text=_("Please enter name"))
    nav_type = models.CharField(
        max_length=20,
        choices=NAV_TYPE,
        null=True,
        blank=True,
        default="top",
        help_text=_("Navigation type")
    )
    menus = StreamField([
        ('single_menu', SingleMenuBlock()),
        ('multiple_menu', MultipleMenuBlock()),
        ('tabbed_menu', TabbedMenuBlock()),
    ], use_json_field=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('nav_type'),
        FieldPanel('menus'),
    ]

    def __str__(self):
        return self.name
    
