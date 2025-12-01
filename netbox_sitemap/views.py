from netbox.views import generic
from utilities.views import ViewTab, register_model_view

# Plugin specific imports
from .models import Sitemap
from .filtersets import SitemapFilterSet
from .forms import SitemapFilterForm, SitemapForm
from .tables import SitemapTable


@register_model_view(model=Sitemap)
class SitemapView(generic.ObjectView):
    queryset = Sitemap.objects.all()
    template_name = 'netbox_sitemap/sitemap.html'


@register_model_view(model=Sitemap, name='map', path='map')
class SitemapMapView(generic.ObjectView):
    queryset = Sitemap.objects.all()
    template_name = 'netbox_sitemap/sitemapmap.html'
    tab = ViewTab(
        label='Map',
    )


class SitemapListView(generic.ObjectListView):
    queryset = Sitemap.objects.all()
    table = SitemapTable
    filterset = SitemapFilterSet
    filterset_form = SitemapFilterForm


class SitemapEditView(generic.ObjectEditView):
    queryset = Sitemap.objects.all()
    form = SitemapForm


class SitemapDeleteView(generic.ObjectDeleteView):
    queryset = Sitemap.objects.all()
