from dcim.api.serializers import SiteGroupSerializer, SiteSerializer

from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import Sitemap

class SitemapSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_sitemap-api:sitemap-detail'
    )
    site_groups = SiteGroupSerializer(nested=True, required=False, allow_null=True)
    sites = SiteSerializer(nested=True, required=False, allow_null=True)

    class Meta:
        model = Sitemap
        fields = (
            'id', 'url', 'display', 'name', 'site_groups', 'sites', 'comments', 'tags', 'custom_fields', 'created',
            'last_updated'
        )
        brief_fields =(
            'id', 'url', 'display', 'name', 'site_groups', 'sites'
        )