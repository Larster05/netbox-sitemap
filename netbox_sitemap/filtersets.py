from netbox.filtersets import NetBoxModelFilterSet
from .models import Sitemap


# class SitemapFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = Sitemap
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
