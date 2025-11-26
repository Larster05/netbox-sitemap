from netbox.filtersets import NetBoxModelFilterSet
from .models import Sitemap


class SitemapFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = Sitemap
        fields = ('id', 'name', 'site_groups', 'sites', 'regions')
    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)