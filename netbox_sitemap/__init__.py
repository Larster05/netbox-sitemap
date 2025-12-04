"""Top-level package for NetBox Sitemap Plugin."""

__author__ = """Lars Däschner"""
__email__ = "contact@ldaeschner.de"
__version__ = "0.3.0"


from netbox.plugins import PluginConfig


class SitemapConfig(PluginConfig):
    name = "netbox_sitemap"
    verbose_name = "NetBox Sitemap Plugin"
    description = "NetBox plugin for displaying sites on a map."
    version = __version__
    author = __author__
    base_url = "netbox-sitemap"

    def ready(self):
        super().ready()
        from . import widgets


config = SitemapConfig
