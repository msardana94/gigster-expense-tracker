from django import template
import os

register = template.Library()


@register.filter('fieldtype')
def fieldtype(field):
    return field.field.widget.__class__.__name__
