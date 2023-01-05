from django import template
from django.template.defaultfilters import safe
from menus.models import Menu

register = template.Library()


@register.simple_tag
def draw_menu(menu_name, request_path):
    menu_items = Menu.objects.filter(name=menu_name).order_by("order")

    def draw_menu_recursive(items, indent=0):
        menu_html = []
        for item in items:
            if item.url:
                urls = [item.get_absolute_url(), item.get_absolute_url() + '/']
                menu_html.append(f"{' ' * indent}<li class='nav-item p-1 "
                                 f"{'active' if request_path in urls else ''}'>"
                                 f"<a class='nav-link {'dropdown-toggle' if item.has_children() else ''}'"
                                 f"href='{item.get_absolute_url()}'>{item.name}</a>")
            if item.has_children():
                menu_html.append(f"{' ' * (indent + 1)}<ul class='dropdown-menu' aria-labelledby='navbarDropdown'>")
                menu_html.append(draw_menu_recursive(item.children.all(), indent + 2))
                menu_html.append(f"{' ' * (indent + 1)}</ul>")
            menu_html.append(f"{' ' * indent}</li>")

        return safe("\n".join(menu_html))

    return draw_menu_recursive(menu_items)
