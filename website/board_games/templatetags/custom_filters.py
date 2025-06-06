from django import template

register = template.Library()

@register.filter
def get_range(value_min, value_max,step=1):

    return range(value_min, value_max, step)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def hash(h, key):
    if key in h.keys():
        return h[key]
    else:
        return 'images/board_games/point_interro.webp'
