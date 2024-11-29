from wagtail.admin.viewsets.pages import PageListingViewSet
from wagtail.admin.views.pages.create import CreateView
from wagtail.admin.views.pages.edit import EditView
from django.urls import path
from wagtail import hooks
from wagtail.admin.viewsets.base import ViewSetGroup
from django.utils.translation import gettext_lazy as _
from wagtail.admin.ui.tables import Column
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet

# Importing models used in different ViewSets
from .models import BlogPage

class BlogPageCreateView(CreateView):
    model = BlogPage
class BlogPageEditView(EditView):
    model = BlogPage

class BlogPageViewSet(PageListingViewSet):
    model = BlogPage
    name = "blog_page"
    icon = 'tag'  
    menu_label = 'Blogs'
    menu_order = 207  
    add_to_settings_menu = False
    exclude_from_explorer = False
    add_to_admin_menu = True 
    list_display = ('name')  
    search_fields = ('name')

    columns = PageListingViewSet.columns + [
        Column("category", label="Category", sort_key="category"), 
        Column("locale", label="Locale", sort_key="locale"), 
    ]

    create_view_class = BlogPageCreateView
    edit_view_class = BlogPageEditView

    def get_urlpatterns(self):
        urlpatterns = super().get_urlpatterns()
        return urlpatterns + [
            path('create/', self.create_view_class.as_view(), name='create'),  
            path('<int:page_id>/edit/', self.edit_view_class.as_view(), name='edit'),  
        ]
    
class BlogViewSetGroup(ViewSetGroup):
    menu_label = 'Blogs' # Label in the admin menu
    menu_icon = 'folder-open-inverse' # Icon for the menu
    menu_order = 210 # Order in the admin menu
    items = [
        BlogPageViewSet,
    ]

# Register the ViewSetGroup
@hooks.register("register_admin_viewset")
def register_viewset():
    return BlogViewSetGroup()