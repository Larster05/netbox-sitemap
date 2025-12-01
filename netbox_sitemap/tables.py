import django_tables2 as tables
from netbox.tables import NetBoxTable, columns

from .models import Sitemap


class SitemapTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    site_groups = columns.ManyToManyColumn(
        linkify_item=True,
        verbose_name=('Site Groups')
    )
    sites = columns.ManyToManyColumn(
        linkify_item=True,
        verbose_name=('Sites')
    )
    regions = columns.ManyToManyColumn(
        linkify_item=True,
        verbose_name=('Regions')
    )
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = Sitemap
        fields = ("pk", "id", "name", "site_groups", "sites", "regions", "tags", "comments", "actions")
        default_columns = ("name", "site_groups", "sites", "regions")
