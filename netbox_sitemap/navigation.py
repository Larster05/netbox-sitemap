from netbox.plugins import PluginMenuButton, PluginMenuItem


plugin_buttons = [
    PluginMenuButton(
        link="plugins:netbox_sitemap:netboxsitemap_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
    )
]

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_sitemap:netboxsitemap_list",
        link_text="NetBox Sitemap",
        buttons=plugin_buttons,
    ),
)
