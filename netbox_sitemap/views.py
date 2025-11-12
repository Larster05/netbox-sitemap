from netbox.views import generic
from . import filtersets, forms, models, tables


class SitemapView(generic.ObjectView):
    queryset = models.Sitemap.objects.all()


class SitemapListView(generic.ObjectListView):
    queryset = models.Sitemap.objects.all()
    table = tables.SitemapTable


class SitemapEditView(generic.ObjectEditView):
    queryset = models.Sitemap.objects.all()
    form = forms.SitemapForm


class SitemapDeleteView(generic.ObjectDeleteView):
    queryset = models.Sitemap.objects.all()
