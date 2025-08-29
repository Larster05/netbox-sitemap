from netbox.filtersets import NetBoxModelFilterSet
from .models import NetBoxSitemap


# class NetBoxSitemapFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = NetBoxSitemap
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
