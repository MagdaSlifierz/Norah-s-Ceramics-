from django import template

register = template.Library()


def currency(pence):
    try:
        pounds = int(pence) / 100
    except ValueError:
        pounds = 0
    return "{0:.2f}".format(pounds)


register.filter("currency", currency)
