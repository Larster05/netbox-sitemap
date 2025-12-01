from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import Sitemap

class SitemapSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_sitemap-api:sitemap-detail'
    )
    markers = serializers.ListField(child=serializers.JSONField(), read_only=True, source='get_markers')

    class Meta:
        model = Sitemap
        fields = (
            'id', 'url', 'display', 'name', 'site_groups', 'sites', 'regions', 'markers', 'comments', 'tags', 'custom_fields', 'created',
            'last_updated'
        )
        brief_fields =(
            'id', 'url', 'display', 'name', 'site_groups', 'sites', 'regions'
        )
