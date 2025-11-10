"""Top-level package for NetBox Sitemap Plugin."""

__author__ = """Lars Däschner"""
__email__ = "contact@ldaeschner.de"
__version__ = "0.1.0-alpha7"


from netbox.plugins import PluginConfig


class SitemapConfig(PluginConfig):
    name = "netbox_sitemap"
    verbose_name = "NetBox Sitemap Plugin"
    description = "NetBox plugin for displaying sites on a map."
    version = "version"
    base_url = "netbox_sitemap"


config = SitemapConfig
