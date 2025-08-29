"""Top-level package for NetBox Sitemap."""

__author__ = """Lars"""
__email__ = "mail@ldaeschner.de"
__version__ = "0.1.0"


from netbox.plugins import PluginConfig


class NetBoxSitemapConfig(PluginConfig):
    name = "netbox_sitemap"
    verbose_name = "NetBox Sitemap"
    description = "NetBox plugin to display sites on a map."
    version = "version"
    base_url = "netbox_sitemap"


config = NetBoxSitemapConfig
