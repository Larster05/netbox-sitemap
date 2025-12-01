from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("sitemaps/", views.SitemapListView.as_view(), name="sitemap_list"),
    path("sitemaps/add/", views.SitemapEditView.as_view(), name="sitemap_add"),
    path("sitemaps/<int:pk>/", views.SitemapView.as_view(), name="sitemap"),
    path("sitemaps/<int:pk>/map/", views.SitemapMapView.as_view(), name="sitemap_map"),
    path("sitemaps/<int:pk>/edit/", views.SitemapEditView.as_view(), name="sitemap_edit"),
    path("sitemaps/<int:pk>/delete/", views.SitemapDeleteView.as_view(), name="sitemap_delete"),
    path(
        "sitemaps/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="sitemap_changelog",
        kwargs={"model": models.Sitemap},
    ),
)
