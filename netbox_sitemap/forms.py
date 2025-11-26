from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelMultipleChoiceField
from utilities.forms.rendering import FieldSet
from dcim.models import SiteGroup, Site, Region

from .models import Sitemap


class SitemapForm(NetBoxModelForm):
    site_groups = DynamicModelMultipleChoiceField(
        label=('Site Groups'),
        queryset=SiteGroup.objects.all(),
        required=False,
        quick_add=True
    )
    sites = DynamicModelMultipleChoiceField(
        label=('Sites'),
        queryset=Site.objects.all(),
        required=False,
        quick_add=True
    )
    regions = DynamicModelMultipleChoiceField(
        label=('Regions'),
        queryset=Region.objects.all(),
        required=False,
        quick_add=True
    )
    comments = CommentField()

    fieldsets = (
        FieldSet(
            'name', 'site_groups', 'sites', 'regions', 'tags', name=('SiteMap')),
    )

    class Meta:
        model = Sitemap
        fields = ('name', 'site_groups', 'sites', 'regions', 'tags', 'comments')

class SitemapFilterForm(NetBoxModelFilterSetForm):
    model = Sitemap

    site_groups = forms.ModelMultipleChoiceField(
        label=('Site Groups'),
        queryset=SiteGroup.objects.all(),
        required=False
    )
    sites = forms.ModelMultipleChoiceField(
        label=('Sites'),
        queryset=Site.objects.all(),
        required=False
    )
    regions = forms.ModelMultipleChoiceField(
        label=('Regions'),
        queryset=Region.objects.all(),
        required=False
    )