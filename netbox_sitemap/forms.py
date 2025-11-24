from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelMultipleChoiceField
from utilities.forms.rendering import FieldSet
from dcim.models import SiteGroup, Site

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
    comments = CommentField()

    fieldsets = (
        FieldSet(
            'name', 'site_groups', 'sites', 'tags', name=('SiteMap')),
    )

    class Meta:
        model = Sitemap
        fields = ('name', 'site_groups', 'sites', 'tags', 'comments')

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