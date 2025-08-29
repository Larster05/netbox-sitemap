from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("netbox-sitemaps/", views.NetBoxSitemapListView.as_view(), name="netboxsitemap_list"),
    path("netbox-sitemaps/add/", views.NetBoxSitemapEditView.as_view(), name="netboxsitemap_add"),
    path("netbox-sitemaps/<int:pk>/", views.NetBoxSitemapView.as_view(), name="netboxsitemap"),
    path("netbox-sitemaps/<int:pk>/edit/", views.NetBoxSitemapEditView.as_view(), name="netboxsitemap_edit"),
    path("netbox-sitemaps/<int:pk>/delete/", views.NetBoxSitemapDeleteView.as_view(), name="netboxsitemap_delete"),
    path(
        "netbox-sitemaps/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="netboxsitemap_changelog",
        kwargs={"model": models.NetBoxSitemap},
    ),
)
