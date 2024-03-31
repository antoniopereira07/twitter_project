from django import template

register = template.Library()

@register.filter(name='add_placeholder')
def add_placeholder(field, placeholder):
    field.field.widget.attrs['placeholder'] = placeholder
    return field
