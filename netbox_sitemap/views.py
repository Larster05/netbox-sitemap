from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


class NetBoxSitemapView(generic.ObjectView):
    queryset = models.NetBoxSitemap.objects.all()


class NetBoxSitemapListView(generic.ObjectListView):
    queryset = models.NetBoxSitemap.objects.all()
    table = tables.NetBoxSitemapTable


class NetBoxSitemapEditView(generic.ObjectEditView):
    queryset = models.NetBoxSitemap.objects.all()
    form = forms.NetBoxSitemapForm


class NetBoxSitemapDeleteView(generic.ObjectDeleteView):
    queryset = models.NetBoxSitemap.objects.all()
