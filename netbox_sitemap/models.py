from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel


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
    comments = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_sitemap:sitemap", args=[self.pk])
