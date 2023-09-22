from django import template

register=template.Library()
@register.filter
def capital_letter(value):
    if value=='admin':
        return value.upper()
    else:
        return value.capitalize()    