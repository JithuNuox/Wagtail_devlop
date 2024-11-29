from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.ui.tables import UpdatedAtColumn
from wagtail.snippets.models import register_snippet
from wagtail import hooks
from django.core.cache import cache

from .models import FooterSnippet

class FooterSnippetViewSet(SnippetViewSet):
    model = FooterSnippet
    icon = "crosshairs"
    # table_class = CustomTable
    # ordering = ('-updated_at',)
    list_display = ('name','locale')
    menu_label = "Footer"
    menu_name = "footer"
    menu_order = 200
    add_to_admin_menu = True
    # search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('locale',)
    # inline_actions = ['edit', 'delete']
    
    
register_snippet(FooterSnippetViewSet)