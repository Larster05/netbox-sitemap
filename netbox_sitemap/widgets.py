from django import forms
from django.template.loader import render_to_string
from extras.dashboard.utils import register_widget
from extras.dashboard.widgets import DashboardWidget, WidgetConfigForm
from .models import Sitemap

def get_sitemap_choices():
    return [
        (sitemap.id, sitemap.name)
        for sitemap in Sitemap.objects.all()
    ]

@register_widget
class SitemapWidget(DashboardWidget):
    default_title = 'Sitemap'
    description = 'Display your sites on a map.'
    template_name = 'netbox_sitemap/sitemapwidget.html'

    class ConfigForm(WidgetConfigForm):
        sitemap = forms.ChoiceField(
            choices=get_sitemap_choices()
        )

    def render(self, request):
        sitemap_id = self.config.get('sitemap')
        return render_to_string(self.template_name, {'object_id': sitemap_id})