from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_sitemap'

router = NetBoxRouter()
router.register('sitemaps', views.SitemapViewSet)

urlpatterns = router.urls