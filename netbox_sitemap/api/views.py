from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import SitemapSerializer

class SitemapViewSet(NetBoxModelViewSet):
    queryset = models.Sitemap.objects.prefetch_related('site_groups', 'sites', 'regions', 'tags')
    serializer_class = SitemapSerializer
    filterset_class = filtersets.SitemapFilterSet
