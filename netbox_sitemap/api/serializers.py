from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import Sitemap

class SitemapSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_sitemap-api:sitemap-detail'
    )

    class Meta:
        model = Sitemap
        fields = (
            'id', 'display', 'name', 'site_groups', 'sites', 'comments', 'tags', 'custom_fields', 'created',
            'last_updated',
        )
