from django import template

register = template.Library()


def get_key(data_obj, key):
    try:
        return data_obj.get(key, "")
    except (TypeError, AttributeError):
        return ""


register.filter("get_key", get_key)
