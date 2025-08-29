from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import NetBoxSitemap


class NetBoxSitemapForm(NetBoxModelForm):
    class Meta:
        model = NetBoxSitemap
        fields = ("name", "tags")
