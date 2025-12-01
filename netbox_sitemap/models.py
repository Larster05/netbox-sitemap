from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from dcim.models import Site


class Sitemap(NetBoxModel):
    name = models.CharField(
        max_length=100
    )
    site_groups = models.ManyToManyField(
        to='dcim.SiteGroup',
        related_name='sitemaps',
        blank=True
    )
    sites = models.ManyToManyField(
        to='dcim.Site',
        related_name='sitemaps',
        blank=True
    )
    regions = models.ManyToManyField(
        to='dcim.Region',
        related_name='sitemaps',
        blank=True
    )
    comments = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_sitemap:sitemap", args=[self.pk])

    def get_markers(self):
        markers = []
        site_ids = []
        # requesting site_ids from sites
        for site in self.sites.all():
            if site.longitude != None and site.latitude != None and site.id not in site_ids:
                site_ids.append(site.id)
        # requesting site_ids from site-groups
        for group in self.site_groups.all():
            for site in Site.objects.filter(group=group):
                if site.longitude != None and site.latitude != None and site.id not in site_ids:
                    site_ids.append(site.id)
        # requesting site_ids from regions
        for region in self.regions.all():
            for site in Site.objects.filter(region=region):
                if site.longitude != None and site.latitude != None and site.id not in site_ids:
                    site_ids.append(site.id)
        # populating markers with site information
        for site_id in site_ids:
            site = Site.objects.get(id=site_id)
            markers.append({
                'type': 'Feature',
                'properties': {
                    'url': site.get_absolute_url(),
                    'name': site.name,
                    'iconSize': [40, 40]
                },
                'geometry': {
                    'type': 'Point',
                    'coordinates': [
                        site.longitude,
                        site.latitude
                    ]
                }
            })
        return markers