from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.ui.tables import UpdatedAtColumn
from wagtail.snippets.models import register_snippet
from wagtail import hooks
from django.core.cache import cache

from .models import  NavigationSnippet


class NavigationViewSet(SnippetViewSet):
    model = NavigationSnippet
    icon = "crosshairs"
    menu_label = "Navigation"
    menu_name = "navigation"
    menu_order = 215
    add_to_admin_menu = True
    list_display = ('name',  'nav_type', 'locale')
    list_filter = ('locale',)
    ordering = ['name']
register_snippet(NavigationViewSet)